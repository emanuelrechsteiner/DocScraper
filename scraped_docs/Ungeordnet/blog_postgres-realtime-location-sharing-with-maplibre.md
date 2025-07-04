---
url: https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre
scraped_at: 2025-05-25T09:46:01.511501
title: Postgres Realtime location sharing with MapLibre
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Postgres Realtime location sharing with MapLibre
04 Jul 2024
•
8 minute read
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Postgres Realtime location sharing with MapLibre](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgres_realtime_maplibre%2Fpostgres_realtime_maplibre.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Do you prefer audio-visual learning? Watch the video guide!](https://supabase.link/realtime-maps-yt)
[Or jump straight into the code](https://supabase.link/realtime-maps-gh)
This tutorial is building upon the previous learnings on Postgis and Supabase and adding Supabase Realtime on top. If you're new to this topic, we recommend you review the following first:
  * Getting started with PostGIS and Supabase [[video]](https://supabase.link/postgis-quickstart-yt) [[docs]](https://supabase.com/docs/guides/database/extensions/postgis)
  * Self-host Maps with Protomaps and Supabase Storage [[video]](https://supabase.link/protomaps-storage-yt) [[blog]](https://supabase.com/blog/self-host-maps-storage-protomaps)
  * Generate Vector Tiles with PostGIS [[video]](https://supabase.link/supa-gis-yt) [[blog]](https://supabase.com/blog/postgis-generate-vector-tiles)


In this tutorial, you will learn to
  * Use a Supabase Edge Function to build a Telegram Bot that captures live location data.
  * Use an RPC (remote procedure call) to insert location data into Postgres from an Edge Function.
  * Use Supabase Realtime to listen to changes in the database.
  * Use MapLibre GL JS in React to draw live location data onto the map.


## Use an Edge Functions to write location data to Supabase[#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-an-edge-functions-to-write-location-data-to-supabase)
In this section, you will create an Edge Function that will capture live location data from a Telegram Bot. The Telegram Bot will send location data to the Edge Function, which will then insert the data into Supabase.
For a detailed guide on how to create a Telegram Bot, please refer to our docs [here](https://supabase.com/docs/guides/functions/examples/telegram-bot).
You can find the production ready code for the Telegram Bot Supabase Edge Function on [GitHub](https://github.com/thorwebdev/location-tRacer/blob/main/supabase/functions/telegram-bot/index.ts). This is the relevant code that listens to the live location updates and writes them to the database:
/supabase/functions/telegram-bot/index.ts
`
1
import { Bot, webhookCallback } from 'https://deno.land/x/grammy@v1.20.3/mod.ts'
2
import { createClient } from 'jsr:@supabase/supabase-js@2.39.7'
3
import { Database } from '../_shared/database.types.ts'
45
const token = Deno.env.get('BOT_TOKEN')
6
if (!token) throw new Error('BOT_TOKEN is unset')
78
const supabase = createClient<Database>(
9
 Deno.env.get('SUPABASE_URL')!,
10
 Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
11
)
1213
const bot = new Bot(token)
14
// ...
1516
bot.on('edit:location', async (ctx) => {
17
 const {
18
  location,
19
  from: { id: user_id },
20
  edit_date,
21
 } = ctx.update.edited_message!
22
 if (location) {
23
  // Insert into db
24
  const { error } = await supabase.rpc('location_insert', {
25
   _user_id: user_id,
26
   _lat: location.latitude,
27
   _long: location.longitude,
28
   _timestamp: edit_date,
29
  })
30
  if (
31
   error &&
32
   error.message !==
33
    'null value in column "event_id" of relation "locations" violates not-null constraint' &&
34
   error.message !== 'duplicate key value violates unique constraint "locations_pkey"'
35
  ) {
36
   return console.log(`edit:location:insert:error:user:${user_id}: ${error.message}`)
37
  }
38
 }
39
 return
40
})
4142
const handleUpdate = webhookCallback(bot, 'std/http')
4344
Deno.serve(async (req) => {
45
 const headers = req.headers
46
 try {
47
  const url = new URL(req.url)
48
  if (url.searchParams.get('secret') !== Deno.env.get('FUNCTION_SECRET')) {
49
   return new Response('not allowed', { status: 405 })
50
  }
5152
  return await handleUpdate(req)
53
 } catch (err) {
54
  console.log(headers)
55
  console.error(err)
56
 }
57
 return new Response()
58
})
`
## Use an RPC to insert location data into Postgres[#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-an-rpc-to-insert-location-data-into-postgres)
The edge function above uses an RPC (remote procedure call) to insert the location data into the database. The RPC is defined in our [Supabase Migrations](https://github.com/thorwebdev/location-tRacer/blob/main/supabase/migrations/20240227024905_init.sql#L80). The RPC first validates that the user has an active session and then inserts the location data into the `locations` table:
`
1
CREATE OR REPLACE FUNCTION public.location_insert(_timestamp bigint, _lat double precision, _long double precision, _user_id bigint)
2
RETURNS void AS $$
3
declare active_event_id uuid;
4
begin
5
 select event_id into active_event_id from public.sessions where user_id = _user_id and status = 'ACTIVE'::session_status;
67
 INSERT INTO public.locations(event_id, user_id, created_at, lat, long, location)
8
 VALUES (active_event_id, _user_id, to_timestamp(_timestamp), _lat, _long, st_point(_long, _lat));
9
end;
10
$$ LANGUAGE plpgsql VOLATILE;
`
## Use Supabase Realtime to listen to changes in the database[#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-supabase-realtime-to-listen-to-changes-in-the-database)
In this section, you will use Supabase Realtime to listen to changes in the database. The Realtime API is a powerful tool that allows you to broadcast changes in the database to multiple clients.
The full client-side code for listening to the realtime changes and drawing the marker onto the map is available on [GitHub](https://github.com/thorwebdev/location-tRacer/blob/main/app/app/realtimemap/%5Bevent%5D/page.tsx).
We're going to brake it down into a couple of steps:
Since we're working in React, we will set up the Realtime subscription in the `useEffect` hook. If you're using Next.js, it's important to mark this with `use client` as we will need client-side JavaScript to make this happen:
/app/app/realtimemap/%5Bevent%5D/page.tsx
`
1
// ...
2
export default function Page({ params }: { params: { event: string } }) {
3
 const supabase = createClient<Database>()
4
 const [locations, setLocations] = useState<{
5
  [key: string]: Tables<'locations'>
6
 } | null>(null)
7
 const locationsRef = useRef<{
8
  [key: string]: Tables<'locations'>
9
 } | null>()
10
 locationsRef.current = locations
1112
 useEffect(() => {
13
  // Listen to realtime updates
14
  const subs = supabase
15
   .channel('schema-db-changes')
16
   .on(
17
    'postgres_changes',
18
    {
19
     event: 'INSERT', // Listen only to INSERTs
20
     schema: 'public',
21
     table: 'locations',
22
     filter: `event_id=eq.${params.event}`,
23
    },
24
    (payload) => {
25
     const loc = payload.new as Tables<'locations'>
26
     const updated = {
27
      ...locationsRef.current,
28
      [loc.user_id.toString()]: loc,
29
     }
3031
     setLocations(updated)
32
    }
33
   )
34
   .subscribe()
35
  console.log('Subscribed')
3637
  return () => {
38
   subs.unsubscribe()
39
  }
40
 }, [])
41
// ...
`
## Use MapLibre GL JS in React to draw live location data onto the map[#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-maplibre-gl-js-in-react-to-draw-live-location-data-onto-the-map)
The realtime subscription listener above updates the state of the `locations` object with the new location data, anytime it is inserted into the table. We can now use `react-map-gl` to easily draw the location markers onto the map:
/app/app/realtimemap/%5Bevent%5D/page.tsx
`
1
// ...
2
<Map
3
 className="map"
4
 cooperativeGestures={true}
5
 initialViewState={{
6
  longitude: 103.852713,
7
  latitude: 1.285727,
8
  zoom: 13,
9
 }}
10
 mapStyle={{
11
  version: 8,
12
  glyphs: 'https://cdn.protomaps.com/fonts/pbf/{fontstack}/{range}.pbf',
13
  sources: {
14
   protomaps: {
15
    attribution:
16
     '<a href="https://github.com/protomaps/basemaps">Protomaps</a> © <a href="https://openstreetmap.org">OpenStreetMap</a>',
17
    type: 'vector',
18
    url: 'pmtiles://https://<project_ref>.supabase.co/functions/v1/maps-private/my_area.pmtiles',
19
   },
20
  },
21
  transition: {
22
   duration: 0,
23
  },
24
  // @ts-ignore
25
  layers: layers('protomaps', 'light'),
26
 }}
27
 // @ts-ignore
28
 mapLib={maplibregl}
29
>
30
 {Object.entries(locations).map(([key, value]) => (
31
  <Marker key={key} longitude={value.long} latitude={value.lat} color="red" />
32
 ))}
33
</Map>
`
Note that we're using [Protomaps](https://protomaps.com/) hosted on Supabase Storage here for the base map. To learn about this read our [previous tutorial here](https://supabase.com/blog/self-host-maps-storage-protomaps).
That's it, this is how easy it is to add realtime location data to your applications using Supabase! We can't wait to see what you will build!
## Conclusion[#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#conclusion)
Supabase Realtime is ideal for broadcasting location data to multiple clients. Combined with the power of PostGIS and the broader Postgres extension ecosystem, its's a powerful solution for all your geospatial needs!
Want to learn more about Maps and PostGIS? Make sure to follow our [Twitter](https://x.com/supabase) and [YouTube](https://www.youtube.com/@Supabase) channels to not miss out! See you then!
## More Supabase[#](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#more-supabase)
  * [Watch the video guide](https://supabase.link/realtime-maps-yt)
  * [Find the code](https://supabase.link/realtime-maps-gh)
  * [Build your own open source Google Maps API alternative](https://supabase.link/supa-gis-yt)
  * [Self-host Maps on Supabase Storage with Protomaps](https://supabase.link/protomaps-storage-yt)
  * [Getting started with PostGIS](https://supabase.link/postgis-quickstart-yt)
  * [PostGIS docs guide](https://supabase.com/docs/guides/database/extensions/postgis)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&t=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)
[Last postSimplifying Time-Based Queries with Range Columns11 July 2024](https://supabase.com/blog/range-columns)
[Next postGenerate Vector Tiles with PostGIS26 June 2024](https://supabase.com/blog/postgis-generate-vector-tiles)
[postgres](https://supabase.com/blog/tags/postgres)[realtime](https://supabase.com/blog/tags/realtime)[maps](https://supabase.com/blog/tags/maps)
On this page
  * [Use an Edge Functions to write location data to Supabase](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-an-edge-functions-to-write-location-data-to-supabase)
  * [Use an RPC to insert location data into Postgres](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-an-rpc-to-insert-location-data-into-postgres)
  * [Use Supabase Realtime to listen to changes in the database](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-supabase-realtime-to-listen-to-changes-in-the-database)
  * [Use MapLibre GL JS in React to draw live location data onto the map](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#use-maplibre-gl-js-in-react-to-draw-live-location-data-onto-the-map)
  * [Conclusion](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#conclusion)
  * [More Supabase](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre#more-supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&text=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-realtime-location-sharing-with-maplibre&t=Postgres%20Realtime%20location%20sharing%20with%20MapLibre)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

