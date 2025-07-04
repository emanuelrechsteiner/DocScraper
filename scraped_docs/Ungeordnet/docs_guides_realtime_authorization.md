---
url: https://supabase.com/docs/guides/realtime/authorization
scraped_at: 2025-05-25T09:42:46.079537
title: Realtime Authorization | Supabase Docs
---

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Main menu
[Realtime](https://supabase.com/docs/guides/realtime)
  * [Overview](https://supabase.com/docs/guides/realtime)
  * [Concepts](https://supabase.com/docs/guides/realtime/concepts)
Usage
  * [Broadcast](https://supabase.com/docs/guides/realtime/broadcast)
  * [Presence](https://supabase.com/docs/guides/realtime/presence)
  * [Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes)
Security
  * [Authorization](https://supabase.com/docs/guides/realtime/authorization)
Guides
  * [Subscribing to Database Changes](https://supabase.com/docs/guides/realtime/subscribing-to-database-changes)
  * [Using Realtime with Next.js](https://supabase.com/docs/guides/realtime/realtime-with-nextjs)
  * [Using Realtime Presence with Flutter](https://supabase.com/docs/guides/realtime/realtime-user-presence)
  * [Listening to Postgres Changes with Flutter](https://supabase.com/docs/guides/realtime/realtime-listening-flutter)
Deep dive
  * [Quotas](https://supabase.com/docs/guides/realtime/quotas)
  * [Pricing](https://supabase.com/docs/guides/realtime/pricing)
  * [Architecture](https://supabase.com/docs/guides/realtime/architecture)
  * [Message Protocol](https://supabase.com/docs/guides/realtime/protocol)
  * [Benchmarks](https://supabase.com/docs/guides/realtime/benchmarks)
Debugging
  * [Operational Error Codes](https://supabase.com/docs/guides/realtime/error_codes)


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Realtime
  1. [Realtime](https://supabase.com/docs/guides/realtime)
  2. Security
  3. [Authorization](https://supabase.com/docs/guides/realtime/authorization)


Realtime Authorization
You can control client access to Realtime [Broadcast](https://supabase.com/docs/guides/realtime/broadcast) and [Presence](https://supabase.com/docs/guides/realtime/presence) by adding Row Level Security policies to the `realtime.messages` table. Each RLS policy can map to a specific action a client can take:
  * Control which clients can broadcast to a Channel
  * Control which clients can receive broadcasts from a Channel
  * Control which clients can publish their presence to a Channel
  * Control which clients can receive messages about the presence of other clients


Realtime Authorization is in Public Beta. To use Authorization for your Realtime Channels, use `supabase-js` version `v2.44.0` or later.
## How it works[#](https://supabase.com/docs/guides/realtime/authorization#how-it-works)
Realtime uses the `messages` table in your database's `realtime` schema to generate access policies for your clients when they connect to a Channel topic.
By creating RLS polices on the `realtime.messages` table you can control the access users have to a Channel topic, and features within a Channel topic.
The validation is done when the user connects. When their WebSocket connection is established and a Channel topic is joined, their permissions are calculated based on:
  * The RLS policies on the `realtime.messages` table
  * The user information sent as part of their [Auth JWT](https://supabase.com/docs/guides/auth/jwts)
  * The request headers
  * The Channel topic the user is trying to connect to


When Realtime generates a policy for a client it performs a query on the `realtime.messages` table and then rolls it back. Realtime does not store any messages in your `realtime.messages` table.
Using Realtime Authorization involves two steps:
  * In your database, create RLS policies on the `realtime.messages`
  * In your client, instantiate the Realtime Channel with the `config` option `private: true`


Increased RLS complexity can impact database performance and connection time, leading to higher connection latency and decreased join rates.
## Helper functions[#](https://supabase.com/docs/guides/realtime/authorization#helper-functions)
You can use the following helper functions when writing RLS policies:
### `realtime.topic`[#](https://supabase.com/docs/guides/realtime/authorization#realtimetopic)
Returns the Channel topic the user is attempting to connect to.
```

1
2
3
4
5
6
7
createpolicy"authenticated can read all messages on topic"on"realtime"."messages"forselectto authenticatedusing ( (selectrealtime.topic()) ='room-1');

```

## Examples[#](https://supabase.com/docs/guides/realtime/authorization#examples)
The following examples use this schema:
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
createtablepublic.rooms (  id bigintgeneratedbydefaultasidentityprimary key,  topic textnot nullunique);altertablepublic.roomsenablerowlevelsecurity;createtablepublic.profiles ( id uuid not nullreferencesauth.userson delete cascade, email textNOT NULL,primary key (id));altertablepublic.profilesenablerowlevelsecurity;createtablepublic.rooms_users ( user_id uuid referencesauth.users (id), room_topic textreferencespublic.rooms (topic), created_at timestamptzdefault current_timestamp);altertablepublic.rooms_usersenablerowlevelsecurity;

```

### Broadcast[#](https://supabase.com/docs/guides/realtime/authorization#broadcast)
The `extension` field on the `realtime.messages` table records the message type. For Broadcast messages, the value of `realtime.messages.extension` is `broadcast`. You can check for this in your RLS policies.
#### Allow a user to join (and read) a Broadcast topic[#](https://supabase.com/docs/guides/realtime/authorization#allow-a-user-to-join-and-read-a-broadcast-topic)
To join a Broadcast Channel, a user must have at least one read or write permission on the Channel topic.
Here, we allow reads (`select`s) for users who are linked to the requested topic within the relationship table `public.room_users`:
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
createpolicy"authenticated can receive broadcast"on"realtime"."messages"forselectto authenticatedusing (exists (select   user_idfrom   rooms_userswhere   user_id = (selectauth.uid())and topic = (selectrealtime.topic())andrealtime.messages.extension in ('broadcast') ));

```

Then, to join a topic with RLS enabled, instantiate the Channel with the `private` option set to `true`.
JavaScriptDartSwiftKotlinPython
```

1
2
3
4
5
6
7
8
9
10
11
12
13
constchannel=supabase.channel('room-1',{config:{private:true},})channel.on('broadcast',{event:'test'},(payload)=>console.log(payload)).subscribe((status,err)=>{if (status==='SUBSCRIBED') {console.log('Connected!')}else{console.error(err)}})

```

#### Allow a user to send a Broadcast message[#](https://supabase.com/docs/guides/realtime/authorization#allow-a-user-to-send-a-broadcast-message)
To authorize sending Broadcast messages, create a policy for `insert` where the value of `realtime.messages.extension` is `broadcast`.
Here, we allow writes (sends) for users who are linked to the requested topic within the relationship table `public.room_users`:
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
createpolicy"authenticated can send broadcast on topic"on"realtime"."messages"forinsertto authenticatedwithcheck (exists (select   user_idfrom   rooms_userswhere   user_id = (selectauth.uid())and topic = (selectrealtime.topic())andrealtime.messages.extension in ('broadcast') ));

```

### Presence[#](https://supabase.com/docs/guides/realtime/authorization#presence)
The `extension` field on the `realtime.messages` table records the message type. For Presence messages, the value of `realtime.messages.extension` is `presence`. You can check for this in your RLS policies.
#### Allow users to listen to Presence messages on a Channel[#](https://supabase.com/docs/guides/realtime/authorization#allow-users-to-listen-to-presence-messages-on-a-channel)
Create a policy for `select` on `realtime.messages` where `realtime.messages.extension` is `presence`.
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
createpolicy"authenticated can listen to presence in topic"on"realtime"."messages"forselectto authenticatedusing (exists (select   user_idfrom   rooms_userswhere   user_id = (selectauth.uid())and topic = (selectrealtime.topic())andrealtime.messages.extension in ('presence') ));

```

#### Allow users to send Presence messages on a channel[#](https://supabase.com/docs/guides/realtime/authorization#allow-users-to-send-presence-messages-on-a-channel)
To update the Presence status for a user create a policy for `insert` on `realtime.messages` where the value of `realtime.messages.extension` is `presence`.
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
createpolicy"authenticated can track presence on topic"on"realtime"."messages"forinsertto authenticatedwithcheck (exists (select   user_idfrom   rooms_userswhere   user_id = (selectauth.uid())andname= (selectrealtime.topic())andrealtime.messages.extension in ('presence') ));

```

### Presence and Broadcast[#](https://supabase.com/docs/guides/realtime/authorization#presence-and-broadcast)
Authorize both Presence and Broadcast by including both extensions in the `where` filter.
#### Broadcast and Presence read[#](https://supabase.com/docs/guides/realtime/authorization#broadcast-and-presence-read)
Authorize Presence and Broadcast read in one RLS policy.
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
createpolicy"authenticated can listen to broadcast and presence on topic"on"realtime"."messages"forselectto authenticatedusing (exists (select   user_idfrom   rooms_userswhere   user_id = (selectauth.uid())and topic = (selectrealtime.topic())andrealtime.messages.extension in ('broadcast', 'presence') ));

```

#### Broadcast and Presence write[#](https://supabase.com/docs/guides/realtime/authorization#broadcast-and-presence-write)
Authorize Presence and Broadcast write in one RLS policy.
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
createpolicy"authenticated can send broadcast and presence on topic"on"realtime"."messages"forinsertto authenticatedwithcheck (exists (select   user_idfrom   rooms_userswhere   user_id = (selectauth.uid())andname= (selectrealtime.topic())andrealtime.messages.extension in ('broadcast', 'presence') ));

```

## Interaction with Postgres Changes[#](https://supabase.com/docs/guides/realtime/authorization#interaction-with-postgres-changes)
Realtime Postgres Changes are separate from Channel authorization. The `private` Channel option does not apply to Postgres Changes.
When using Postgres Changes with RLS, database records are sent only to clients who are allowed to read them based on your RLS policies.
## Updating RLS policies[#](https://supabase.com/docs/guides/realtime/authorization#updating-rls-policies)
Client access polices are cached for the duration of the connection. Your database is not queried for every Channel message.
Realtime updates the access policy cache for a client based on your RLS polices when:
  * A client connects to Realtime and subscribes to a Channel
  * A new JWT is sent to Realtime from a client via the [`access_token` message](https://supabase.com/docs/guides/realtime/protocol#access-token)


If a new JWT is never received on the Channel, the client will be disconnected when the JWT expires.
Make sure to keep the JWT expiration window short.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/realtime/authorization.mdx)
### Is this helpful?
No Yes
### On this page
[How it works](https://supabase.com/docs/guides/realtime/authorization#how-it-works)[Helper functions](https://supabase.com/docs/guides/realtime/authorization#helper-functions)[realtime.topic](https://supabase.com/docs/guides/realtime/authorization#realtimetopic)[Examples](https://supabase.com/docs/guides/realtime/authorization#examples)[Broadcast](https://supabase.com/docs/guides/realtime/authorization#broadcast)[Presence](https://supabase.com/docs/guides/realtime/authorization#presence)[Presence and Broadcast](https://supabase.com/docs/guides/realtime/authorization#presence-and-broadcast)[Interaction with Postgres Changes](https://supabase.com/docs/guides/realtime/authorization#interaction-with-postgres-changes)[Updating RLS policies](https://supabase.com/docs/guides/realtime/authorization#updating-rls-policies)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings



