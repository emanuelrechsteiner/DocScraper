---
url: https://supabase.com/blog/postgis-generate-vector-tiles
scraped_at: 2025-05-25T09:27:48.635858
title: Generate Vector Tiles with PostGIS
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
# Generate Vector Tiles with PostGIS
26 Jun 2024
•
12 minute read
[![Brandon Liu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fbdon.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Brandon LiuGuest Author](https://github.com/bdon)
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Generate Vector Tiles with PostGIS](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpostgis_vector_tiles%2Foverture_postgis_mvt.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Do you prefer audio-visual learning? Watch the video guide!](https://supabase.link/supa-gis-yt-docs)
[Or jump straight into the code](https://github.com/bdon/supabase-vector-tile)
[Overture Maps Foundation](https://overturemaps.org/) is a [Joint Development Foundation Project](https://jointdevelopment.org/) initiated by Amazon, Meta, Microsoft, and tomtom, aiming to create reliable, easy-to-use, and interoperable open map data.
Overture Maps allows us to download open map data, like places of interest, as [GeoJSON](https://geojson.org/) which we can transform into SQL and ingest into our Postgres database on Supabase.
Using PostGIS we can then programmatically generate vector tiles and serve them to our MapLibre GL client using supabase-js.
Vector tiles are packets of geographic data, packaged into pre-defined roughly-square shaped "tiles" for transfer over the web. Map data is requested by a client as a set of "tiles" corresponding to square areas of land of a pre-defined size and location.
Especially for large datasets, this has the benefit that the data transfer is greatly reduced because only data within the current viewport, and at the current zoom level needs to be transferred.
In this tutorial, you will learn to
  * Use Overture Maps to download open map places data in GeoJSON format.
  * Use GDAL ogr2ogr to transform GeoJSON into SQL statements.
  * Import location data and JSON metadata into your Supabase Postgres database using psql.
  * Use PostGIS' `ST_AsMVT` to aggregate a set of rows corresponding to a tile layer into a binary vector tile representation.
  * Use MapLibre's `addProtocol` to visualize large PostGIS tables by making remote procedure calls with supabase-js.
  * Use supabase-js to fetch additional JSON metadata on demand


## Download open map data with Overture Maps[#](https://supabase.com/blog/postgis-generate-vector-tiles#download-open-map-data-with-overture-maps)
Overture Maps provides a [python command-line tool](https://docs.overturemaps.org/getting-data/overturemaps-py/) to download data within a region of interest and converts it to several common geospatial file formats.
We can download places in Singapore into a GeoJSON file with this command:
`
1
overturemaps download --bbox=103.570233,1.125077,104.115855,1.490957 -f geojson --type=place -o places.geojson
`
Depending on the size of the bounding box this can take quite some time!
## Transform GeoJSON into SQL[#](https://supabase.com/blog/postgis-generate-vector-tiles#transform-geojson-into-sql)
In the next step, we can use [GDAL ogr2ogr](https://gdal.org/programs/ogr2ogr.html) to transform the GeoJSON file into a PostGIS compatible SQL file.
You can install `GDAL` via `homebrew brew install gdal` or follow the [download instructions](https://gdal.org/download.html).
`
1
PG_USE_COPY=true ogr2ogr -f pgdump places.sql places.geojson
`
## Import location data into Supabase[#](https://supabase.com/blog/postgis-generate-vector-tiles#import-location-data-into-supabase)
Enable the PostGIS extension on your Supabase Database on a dedicated separate `gis` schema. To do so you can navigate to the [SQL Editor](https://supabase.com/dashboard/project/_/sql/new) and run the following SQL, or you can enable the extension from the [Database Extensions Settings](https://supabase.com/dashboard/project/_/database/extensions).
As PostGIS can be quite compute heavy, we recommend enabling it on a dedicated separate schema, for example, named `gis`!
`
1
CREATE SCHEMA IF NOT EXISTS "gis";
2
CREATE EXTENSION IF NOT EXISTS "postgis" WITH SCHEMA "gis";
`
Import the open map data into a `places` table in Supabase:
`
1
psql -h aws-0-us-west-1.pooler.supabase.com -p 5432 -d postgres -U postgres.project-ref < places.sql
`
You can find the credentials in the [project connect page](https://supabase.com/dashboard/project/_?showConnect=true) of your Supabase Dashboard.
### Enable RLS and create a public read policy[#](https://supabase.com/blog/postgis-generate-vector-tiles#enable-rls-and-create-a-public-read-policy)
We want the places data to be available publicly, so we can create a row level security policy that enables public read access.
In your Supabase Dashboard, navigate to the [SQL Editor](https://supabase.com/dashboard/project/_/sql/new) and run the following:
`
1
ALTER TABLE "public"."places" ENABLE ROW LEVEL SECURITY;
23
CREATE POLICY "Enable read access for all users" ON "public"."places" FOR SELECT USING (true);
`
## Generate vector tiles with PostGIS[#](https://supabase.com/blog/postgis-generate-vector-tiles#generate-vector-tiles-with-postgis)
To programmatically generate vector tiles on client-side request, we need to create a Postgres function that we can invoke via a [remote procedure call](https://supabase.com/docs/reference/javascript/rpc). In your SQL Editor, run:
`
1
CREATE OR REPLACE FUNCTION mvt(z integer, x integer, y integer)
2
RETURNS text
3
LANGUAGE plpgsql
4
AS $$
5
DECLARE
6
  mvt_output text;
7
BEGIN
8
  WITH
9
  -- Define the bounds of the tile using the provided Z, X, Y coordinates
10
  bounds AS (
11
    SELECT ST_TileEnvelope(z, x, y) AS geom
12
  ),
13
  -- Transform the geometries from EPSG:4326 to EPSG:3857 and clip them to the tile bounds
14
  mvtgeom AS (
15
    SELECT
16
      -- include the name and id only at zoom 13 to make low-zoom tiles smaller
17
      CASE
18
      WHEN z > 13 THEN id
19
      ELSE NULL
20
      END AS id,
21
      CASE
22
      WHEN z > 13 THEN names::json->>'primary'
23
      ELSE NULL
24
      END AS primary_name,
25
      categories::json->>'main' as main_category,
26
      ST_AsMVTGeom(
27
        ST_Transform(wkb_geometry, 3857), -- Transform the geometry to Web Mercator
28
        bounds.geom,
29
        4096, -- The extent of the tile in pixels (commonly 256 or 4096)
30
        0,  -- Buffer around the tile in pixels
31
        true -- Clip geometries to the tile extent
32
      ) AS geom
33
    FROM
34
      places, bounds
35
    WHERE
36
      ST_Intersects(ST_Transform(wkb_geometry, 3857), bounds.geom)
37
  )
38
  -- Generate the MVT from the clipped geometries
39
  SELECT INTO mvt_output encode(ST_AsMVT(mvtgeom, 'places', 4096, 'geom'),'base64')
40
  FROM mvtgeom;
4142
  RETURN mvt_output;
43
END;
44
$$;
`
To limit the amount of data sent over the wire, we limit the amount of metadata to include in the vector tile. For example we add a condition for the zoom level, and only return the place name when the user has zoomed in beyond level 13.
## Use supabase-js to fetch vector tiles from MapLibre GL client[#](https://supabase.com/blog/postgis-generate-vector-tiles#use-supabase-js-to-fetch-vector-tiles-from-maplibre-gl-client)
You can find the full `index.html` code on [GitHub](https://github.com/bdon/supabase-vector-tile/blob/main/index.html). Here we'll highlight how to add a new protocol to MapLibreGL to fetch the bas64 encoded binary vector tile data via supabase-js so that MapLibre GL can fetch and render the data as your users interact with the map:
index.html
`
1
const client = supabase.createClient('your-supabase-api-url', 'your-supabase-anon-key')
23
function base64ToArrayBuffer(base64) {
4
 var binaryString = atob(base64)
5
 var bytes = new Uint8Array(binaryString.length)
6
 for (var i = 0; i < binaryString.length; i++) {
7
  bytes[i] = binaryString.charCodeAt(i)
8
 }
9
 return bytes
10
}
1112
maplibregl.addProtocol('supabase', async (params, abortController) => {
13
 const re = new RegExp(/supabase:\/\/(.+)\/(\d+)\/(\d+)\/(\d+)/)
14
 const result = params.url.match(re)
15
 const { data, error } = await client.rpc('mvt', {
16
  z: result[2],
17
  x: result[3],
18
  y: result[4],
19
 })
20
 const encoded = base64ToArrayBuffer(data)
21
 if (!error) {
22
  return { data: encoded }
23
 } else {
24
  throw new Error(`Tile fetch error:`)
25
 }
26
})
`
With the supabase protocol registered, we can now add it to our MapLibre GL sources on top of a basemap like [Protomaps](https://protomaps.com/) for example:
index.html
`
1
// ...
2
const map = new maplibregl.Map({
3
 hash: true,
4
 container: 'map',
5
 style: {
6
  version: 8,
7
  glyphs: 'https://cdn.protomaps.com/fonts/pbf/{fontstack}/{range}.pbf',
8
  sources: {
9
   supabase: {
10
    type: 'vector',
11
    tiles: ['supabase://boston/{z}/{x}/{y}'],
12
    attribution: '© <a href="https://overturemaps.org">Overture Maps Foundation</a>',
13
   },
14
   protomaps: {
15
    type: 'vector',
16
    url: 'https://api.protomaps.com/tiles/v3.json?key=your-protomaps-api-key',
17
    attribution: 'Basemap © <a href="https://openstreetmap.org">OpenStreetMap</a>',
18
   },
19
  },
20
 },
21
})
22
// ...
`
## On demand fetch additional JSON metadata[#](https://supabase.com/blog/postgis-generate-vector-tiles#on-demand-fetch-additional-json-metadata)
To limit the amount of data sent over the wire, we don't encode all the metadata in the vector tile itself, but rather set up an onclick handler to fetch the additional metadata on demand within the MapLibre GL popup:
index.html
`
1
// ..
2
const popup = new maplibregl.Popup({
3
 closeButton: true,
4
 closeOnClick: false,
5
 maxWidth: 'none',
6
})
78
function loadDetails(element, id) {
9
 element.innerHTML = 'loading...'
10
 client
11
  .from('places')
12
  .select(
13
   `
14
     websites,
15
     socials,
16
     phones,
17
     addresses,
18
     source: sources->0->dataset
19
    `
20
  )
21
  .eq('id', id)
22
  .single()
23
  .then(({ data, error }) => {
24
   if (error) return console.error(error)
25
   element.parentElement.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`
26
  })
27
}
2829
map.on('click', 'overture-pois-text', async (e) => {
30
 if (e.features.length > 0) {
31
  const feature = e.features[0]
32
  console.log(feature)
33
  popup.setHTML(
34
   `
35
    <table style="font-size:12px">
36
      <tr>
37
        <td>id:</td>
38
        <td>${feature.properties.id}</td>
39
      </tr>
40
      <tr>
41
        <td>name:</td>
42
        <td>${feature.properties.primary_name}</td>
43
      </tr>
44
      <tr>
45
        <td>main_category:</td>
46
        <td>${feature.properties.main_category}</td>
47
      </tr>
48
      <tr>
49
        <td>details:</td>
50
        <td>
51
         <span onclick="loadDetails(this, '${feature.properties.id}')">
52
          load details
53
         </span>
54
        </td>
55
      </tr>
56
    </table>
57
   `
58
  )
59
  popup.setLngLat(e.lngLat)
60
  popup.addTo(map)
61
 }
62
})
63
// ...
`
## Conclusion[#](https://supabase.com/blog/postgis-generate-vector-tiles#conclusion)
PostGIS is incredibly powerful, allowing you to programmatically generate vector tiles from table rows stored in Postgres. Paired with Supabase's auto generated REST API and supabase-js client library you're able to build interactive geospatial applications with ease!
Want to learn more about Maps and PostGIS? Make sure to follow our [Twitter](https://x.com/supabase) and [YouTube](https://www.youtube.com/@Supabase) channels to not miss out! See you then!
## More Supabase[#](https://supabase.com/blog/postgis-generate-vector-tiles#more-supabase)
  * [Watch the video guide](https://supabase.link/supa-gis-yt-docs)
  * [Find the code](https://github.com/bdon/supabase-vector-tile)
  * [Self-host Maps on Supabase Storage with Protomaps](https://supabase.link/protomaps-storage-yt)
  * [Getting started with PostGIS](https://supabase.link/postgis-quickstart-yt)
  * [PostGIS docs guide](https://supabase.com/docs/guides/database/extensions/postgis)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&t=Generate%20Vector%20Tiles%20with%20PostGIS)
[Last postPostgres Realtime location sharing with MapLibre4 July 2024](https://supabase.com/blog/postgres-realtime-location-sharing-with-maplibre)
[Next postSelf-host Maps with Protomaps and Supabase Storage19 June 2024](https://supabase.com/blog/self-host-maps-storage-protomaps)
[postgres](https://supabase.com/blog/tags/postgres)[postgis](https://supabase.com/blog/tags/postgis)[maps](https://supabase.com/blog/tags/maps)
On this page
  * [Download open map data with Overture Maps](https://supabase.com/blog/postgis-generate-vector-tiles#download-open-map-data-with-overture-maps)
  * [Transform GeoJSON into SQL](https://supabase.com/blog/postgis-generate-vector-tiles#transform-geojson-into-sql)
  * [Import location data into Supabase](https://supabase.com/blog/postgis-generate-vector-tiles#import-location-data-into-supabase)
    * [Enable RLS and create a public read policy](https://supabase.com/blog/postgis-generate-vector-tiles#enable-rls-and-create-a-public-read-policy)
  * [Generate vector tiles with PostGIS](https://supabase.com/blog/postgis-generate-vector-tiles#generate-vector-tiles-with-postgis)
  * [Use supabase-js to fetch vector tiles from MapLibre GL client](https://supabase.com/blog/postgis-generate-vector-tiles#use-supabase-js-to-fetch-vector-tiles-from-maplibre-gl-client)
  * [On demand fetch additional JSON metadata](https://supabase.com/blog/postgis-generate-vector-tiles#on-demand-fetch-additional-json-metadata)
  * [Conclusion](https://supabase.com/blog/postgis-generate-vector-tiles#conclusion)
  * [More Supabase](https://supabase.com/blog/postgis-generate-vector-tiles#more-supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&text=Generate%20Vector%20Tiles%20with%20PostGIS)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgis-generate-vector-tiles&t=Generate%20Vector%20Tiles%20with%20PostGIS)
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

