---
url: https://supabase.com/docs/guides/database/extensions/postgis
scraped_at: 2025-05-25T09:34:50.304664
title: PostGIS: Geo queries | Supabase Docs
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
[Database](https://supabase.com/docs/guides/database/overview)
  * [Overview](https://supabase.com/docs/guides/database/overview)
Fundamentals
  * [Connecting to your database](https://supabase.com/docs/guides/database/connecting-to-postgres)
  * [Importing data](https://supabase.com/docs/guides/database/import-data)
  * [Securing your data](https://supabase.com/docs/guides/database/secure-data)
Working with your database (basics)
  * [Managing tables, views, and data](https://supabase.com/docs/guides/database/tables)
  * [Working with arrays](https://supabase.com/docs/guides/database/arrays)
  * [Managing indexes](https://supabase.com/docs/guides/database/postgres/indexes)
  * [Querying joins and nested tables](https://supabase.com/docs/guides/database/joins-and-nesting)
  * [JSON and unstructured data](https://supabase.com/docs/guides/database/json)
Working with your database (intermediate)
  * [Implementing cascade deletes](https://supabase.com/docs/guides/database/postgres/cascade-deletes)
  * [Managing enums](https://supabase.com/docs/guides/database/postgres/enums)
  * [Managing database functions](https://supabase.com/docs/guides/database/functions)
  * [Managing database triggers](https://supabase.com/docs/guides/database/postgres/triggers)
  * [Managing database webhooks](https://supabase.com/docs/guides/database/webhooks)
  * [Using Full Text Search](https://supabase.com/docs/guides/database/full-text-search)
  * [Partitioning your tables](https://supabase.com/docs/guides/database/partitions)
  * [Managing connections](https://supabase.com/docs/guides/database/connection-management)
OrioleDB
  * [Overview](https://supabase.com/docs/guides/database/orioledb)
Access and security
  * [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
  * [Column Level Security](https://supabase.com/docs/guides/database/postgres/column-level-security)
  * [Hardening the Data API](https://supabase.com/docs/guides/database/hardening-data-api)
  * [Custom Claims & RBAC](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac)
  * [Managing Postgres Roles](https://supabase.com/docs/guides/database/postgres/roles)
  * [Using Custom Postgres Roles](https://supabase.com/docs/guides/storage/schema/custom-roles)
  * [Managing secrets with Vault](https://supabase.com/docs/guides/database/vault)
  * [Superuser Access and Unsupported Operations](https://supabase.com/docs/guides/database/postgres/roles-superuser)
Configuration, optimization, and testing
  * [Database configuration](https://supabase.com/docs/guides/database/postgres/configuration)
  * [Managing database replication](https://supabase.com/docs/guides/database/replication)
  * [Query optimization](https://supabase.com/docs/guides/database/query-optimization)
  * [Database Advisors](https://supabase.com/docs/guides/database/database-advisors)
  * [Testing your database](https://supabase.com/docs/guides/database/testing)
  * [Customizing Postgres config](https://supabase.com/docs/guides/database/custom-postgres-config)
Debugging
  * [Timeouts](https://supabase.com/docs/guides/database/postgres/timeouts)
  * [Debugging and monitoring](https://supabase.com/docs/guides/database/inspect)
  * [Debugging performance issues](https://supabase.com/docs/guides/database/debugging-performance)
  * [Supavisor](https://supabase.com/docs/guides/database/supavisor)
ORM Quickstarts
  * [Prisma](https://supabase.com/docs/guides/database/prisma)
  * [Drizzle](https://supabase.com/docs/guides/database/drizzle)
  * [Postgres.js](https://supabase.com/docs/guides/database/postgres-js)
GUI quickstarts
  * [pgAdmin](https://supabase.com/docs/guides/database/pgadmin)
  * [PSQL](https://supabase.com/docs/guides/database/psql)
  * [DBeaver](https://supabase.com/docs/guides/database/dbeaver)
  * [Metabase](https://supabase.com/docs/guides/database/metabase)
  * [Beekeeper Studio](https://supabase.com/docs/guides/database/beekeeper-studio)
Extensions
  * [Overview](https://supabase.com/docs/guides/database/extensions)
  * [HypoPG: Hypothetical indexes](https://supabase.com/docs/guides/database/extensions/hypopg)
  * [plv8: Javascript Language](https://supabase.com/docs/guides/database/extensions/plv8)
  * [http: RESTful Client](https://supabase.com/docs/guides/database/extensions/http)
  * [index_advisor: Query optimization](https://supabase.com/docs/guides/database/extensions/index_advisor)
  * [PGAudit: Postgres Auditing](https://supabase.com/docs/guides/database/extensions/pgaudit)
  * [pgjwt: JSON Web Tokens](https://supabase.com/docs/guides/database/extensions/pgjwt)
  * [PGroonga: Multilingual Full Text Search](https://supabase.com/docs/guides/database/extensions/pgroonga)
  * [pgRouting: Geospatial Routing](https://supabase.com/docs/guides/database/extensions/pgrouting)
  * [pg_cron: Schedule Recurring Jobs](https://supabase.com/docs/guides/database/extensions/pg_cron)
  * [pg_graphql: GraphQL Support](https://supabase.com/docs/guides/database/extensions/pg_graphql)
  * [pg_hashids: Short UIDs](https://supabase.com/docs/guides/database/extensions/pg_hashids)
  * [pg_jsonschema: JSON Schema Validation](https://supabase.com/docs/guides/database/extensions/pg_jsonschema)
  * [pg_net: Async Networking](https://supabase.com/docs/guides/database/extensions/pg_net)
  * [pg_plan_filter: Restrict Total Cost](https://supabase.com/docs/guides/database/extensions/pg_plan_filter)
  * [postgres_fdw: query data from an external Postgres server](https://supabase.com/docs/guides/database/extensions/postgres_fdw)
  * [pgvector: Embeddings and vector similarity](https://supabase.com/docs/guides/database/extensions/pgvector)
  * [pg_stat_statements: SQL Planning and Execution Statistics](https://supabase.com/docs/guides/database/extensions/pg_stat_statements)
  * [pg_repack: Storage Optimization](https://supabase.com/docs/guides/database/extensions/pg_repack)
  * [PostGIS: Geo queries](https://supabase.com/docs/guides/database/extensions/postgis)
  * [pgmq: Queues](https://supabase.com/docs/guides/database/extensions/pgmq)
  * [pgsodium (pending deprecation): Encryption Features](https://supabase.com/docs/guides/database/extensions/pgsodium)
  * [pgTAP: Unit Testing](https://supabase.com/docs/guides/database/extensions/pgtap)
  * [plpgsql_check: PL/pgSQL Linter](https://supabase.com/docs/guides/database/extensions/plpgsql_check)
  * [timescaledb: Time-series data](https://supabase.com/docs/guides/database/extensions/timescaledb)
  * [uuid-ossp: Unique Identifiers](https://supabase.com/docs/guides/database/extensions/uuid-ossp)
  * [RUM: inverted index for full-text search](https://supabase.com/docs/guides/database/extensions/rum)
Foreign Data Wrappers
  * [Overview](https://supabase.com/docs/guides/database/extensions/wrappers/overview)
  * [Connecting to Auth0](https://supabase.com/docs/guides/database/extensions/wrappers/auth0)
  * [Connecting to Airtable](https://supabase.com/docs/guides/database/extensions/wrappers/airtable)
  * [Connecting to AWS Cognito](https://supabase.com/docs/guides/database/extensions/wrappers/cognito)
  * [Connecting to AWS S3](https://supabase.com/docs/guides/database/extensions/wrappers/s3)
  * [Connecting to BigQuery](https://supabase.com/docs/guides/database/extensions/wrappers/bigquery)
  * [Connecting to Clerk](https://supabase.com/docs/guides/database/extensions/wrappers/clerk)
  * [Connecting to ClickHouse](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse)
  * [Connecting to Firebase](https://supabase.com/docs/guides/database/extensions/wrappers/firebase)
  * [Connecting to Logflare](https://supabase.com/docs/guides/database/extensions/wrappers/logflare)
  * [Connecting to MSSQL](https://supabase.com/docs/guides/database/extensions/wrappers/mssql)
  * [Connecting to Notion](https://supabase.com/docs/guides/database/extensions/wrappers/notion)
  * [Connecting to Paddle](https://supabase.com/docs/guides/database/extensions/wrappers/paddle)
  * [Connecting to Redis](https://supabase.com/docs/guides/database/extensions/wrappers/redis)
  * [Connecting to Snowflake](https://supabase.com/docs/guides/database/extensions/wrappers/snowflake)
  * [Connecting to Stripe](https://supabase.com/docs/guides/database/extensions/wrappers/stripe)
Examples
  * [Drop All Tables in Schema](https://supabase.com/docs/guides/database/postgres/dropping-all-tables-in-schema)
  * [Select First Row per Group](https://supabase.com/docs/guides/database/postgres/first-row-in-group)
  * [Print PostgreSQL Version](https://supabase.com/docs/guides/database/postgres/which-version-of-postgres)
  * [Replicating from Supabase to External Postgres](https://supabase.com/docs/guides/database/postgres/setup-replication-external)


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
Database
  1. [Database](https://supabase.com/docs/guides/database/overview)
  2. Extensions
  3. [PostGIS: Geo queries](https://supabase.com/docs/guides/database/extensions/postgis)


PostGIS: Geo queries
[PostGIS](https://postgis.net/) is a Postgres extension that allows you to interact with Geo data within Postgres. You can sort your data by geographic location, get data within certain geographic boundaries, and do much more with it.
## Overview[#](https://supabase.com/docs/guides/database/extensions/postgis#overview)
While you may be able to store simple lat/long geographic coordinates as a set of decimals, it does not scale very well when you try to query through a large data set. PostGIS comes with special data types that are efficient, and indexable for high scalability.
The additional data types that PostGIS provides include [Point](https://postgis.net/docs/using_postgis_dbmanagement.html#Point), [Polygon](https://postgis.net/docs/using_postgis_dbmanagement.html#Polygon), [LineString](https://postgis.net/docs/using_postgis_dbmanagement.html#LineString), and many more to represent different types of geographical data. In this guide, we will mainly focus on how to interact with `Point` type, which represents a single set of latitude and longitude. If you are interested in digging deeper, you can learn more about different data types on the [data management section of PostGIS docs](https://postgis.net/docs/using_postgis_dbmanagement.html).
## Enable the extension[#](https://supabase.com/docs/guides/database/extensions/postgis#enable-the-extension)
You can get started with PostGIS by enabling the PostGIS extension in your Supabase dashboard.
DashboardSQL
```

1
2
3
4
5
6
7
8
-- Create a dedicated separate schemacreateschemaifnotexists"gis";-- Example: enable the "postgis" extensioncreate extension postgis withschema"gis";-- Example: disable the "postgis" extensiondrop extension ifexists postgis;

```

## Examples[#](https://supabase.com/docs/guides/database/extensions/postgis#examples)
Now that we are ready to get started with PostGIS, let’s create a table and see how we can utilize PostGIS for some typical use cases. Let’s imagine we are creating a simple restaurant-searching app.
Let’s create our table. Each row represents a restaurant with its location stored in `location` column as a `Point` type.
```

1
2
3
4
5
createtableifnotexistspublic.restaurants (	id intgeneratedbydefaultasidentityprimary key,nametextnot null,locationgis.geography(POINT) not null);

```

We can then set a [spatial index](https://postgis.net/docs/using_postgis_dbmanagement.html#build-indexes) on the `location` column of this table.
```

1
2
3
createindexrestaurants_geo_indexonpublic.restaurantsusing GIST (location);

```

### Inserting data[#](https://supabase.com/docs/guides/database/extensions/postgis#inserting-data)
You can insert geographical data through SQL or through our API.
DataSQLJavaScriptDartSwiftKotlin
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
const{error}=awaitsupabase.from('restaurants').insert([{name:'Supa Burger',location:'POINT(-73.946823 40.807416)',},{name:'Supa Pizza',location:'POINT(-73.94581 40.807475)',},{name:'Supa Taco',location:'POINT(-73.945826 40.80629)',},])

```

Notice the order in which you pass the latitude and longitude. Longitude comes first, and is because longitude represents the x-axis of the location. Another thing to watch for is when inserting data from the client library, there is no comma between the two values, just a single space.
At this point, if you go into your Supabase dashboard and look at the data, you will notice that the value of the `location` column looks something like this.
```

1
0101000020E6100000A4DFBE0E9C91614044FAEDEBC0494240

```

We can query the `restaurants` table directly, but it will return the `location` column in the format you see above. We will create [database functions](https://supabase.com/docs/guides/database/functions) so that we can use the [st_y()](https://postgis.net/docs/ST_Y.html) and [st_x()](https://postgis.net/docs/ST_X.html) function to convert it back to lat and long floating values.
### Order by distance[#](https://supabase.com/docs/guides/database/extensions/postgis#order-by-distance)
Sorting datasets from closest to farthest, sometimes called nearest-neighbor sort, is a very common use case in Geo-queries. PostGIS can handle it with the use of the [`<->`](https://postgis.net/docs/geometry_distance_knn.html) operator. `<->` operator returns the two-dimensional distance between two geometries and will utilize the spatial index when used within `order by` clause. You can create the following database function to sort the restaurants from closest to farthest by passing the current locations as parameters.
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
create or replacefunctionnearby_restaurants(lat float, long float)returnstable (id public.restaurants.id%TYPE, namepublic.restaurants.name%TYPE, lat float, long float, dist_meters float)set search_path =''languagesqlas $$select id, name, gis.st_y(location::gis.geometry) as lat, gis.st_x(location::gis.geometry) as long, gis.st_distance(location, gis.st_point(long, lat)::gis.geography) as dist_metersfrompublic.restaurantsorder bylocation operator(gis.<->) gis.st_point(long, lat)::gis.geography;$$;

```

Before being able to call this function from our client we need to grant access to our `gis` schema:
```

1
grant usage onschema gis to anon, authenticated;

```

Now you can call this function from your client using `rpc()` like this:
JavaScriptDartSwiftKotlinResult
```

1
2
3
4
const{data,error}=awaitsupabase.rpc('nearby_restaurants',{lat:40.807313,long:-73.946713,})

```

### Finding all data points within a bounding box[#](https://supabase.com/docs/guides/database/extensions/postgis#finding-all-data-points-within-a-bounding-box)
![Searching within a bounding box of a map](https://supabase.com/docs/img/guides/database/extensions/postgis/map.png)
When you are working on a map-based application where the user scrolls through your map, you might want to load the data that lies within the bounding box of the map every time your users scroll. PostGIS can return the rows that are within the bounding box just by supplying the bottom left and the top right coordinates. Let’s look at what the function would look like:
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
create or replacefunctionrestaurants_in_view(min_lat float, min_long float, max_lat float, max_long float)returnstable (id public.restaurants.id%TYPE, namepublic.restaurants.name%TYPE, lat float, long float)set search_path to''languagesqlas $$select id, name, gis.st_y(location::gis.geometry) as lat, gis.st_x(location::gis.geometry) as longfrompublic.restaurantswherelocation operator(gis.&&) gis.ST_SetSRID(gis.ST_MakeBox2D(gis.ST_Point(min_long, min_lat), gis.ST_Point(max_long, max_lat)), 4326)$$;

```

The [`&&`](https://postgis.net/docs/geometry_overlaps.html) operator used in the `where` statement here returns a boolean of whether the bounding box of the two geometries intersect or not. We are basically creating a bounding box from the two points and finding those points that fall under the bounding box. We are also utilizing a few different PostGIS functions:
  * [ST_MakeBox2D](https://postgis.net/docs/ST_MakeBox2D.html): Creates a 2-dimensional box from two points.
  * [ST_SetSRID](https://postgis.net/docs/ST_SetSRID.html): Sets the [SRID](https://postgis.net/docs/manual-dev/using_postgis_dbmanagement.html#spatial_ref_sys), which is an identifier of what coordinate system to use for the geometry. 4326 is the standard longitude and latitude coordinate system.


You can call this function from your client using `rpc()` like this:
JavaScriptDartSwiftKotlinResult
```

1
2
3
4
5
6
const{data,error}=awaitsupabase.rpc('restaurants_in_view',{min_lat:40.807,min_long:-73.946,max_lat:40.808,max_long:-73.945,})

```

## Troubleshooting[#](https://supabase.com/docs/guides/database/extensions/postgis#troubleshooting)
The [official PostGIS documentation](https://postgis.net/documentation/tips/tip-move-postgis-schema/) for relocating the schema will cause issues for Supabase projects. These issues might not be apparent immediately but will eventually surface. To relocate your schema, use the following steps instead.
As of PostGIS 2.3 or newer, the PostGIS extension is no longer relocatable from one schema to another. If you need to move it from one schema to another for any reason (e.g. from the public schema to the extensions schema for security reasons), you would normally run a ALTER EXTENSION to relocate the schema. However, you will now to do the following steps:
  1. Backup your Database to prevent data loss - You can do this through the [CLI](https://supabase.com/docs/reference/cli/supabase-db-dump) or Postgres backup tools such as [pg_dumpall](https://www.postgresql.org/docs/current/backup-dump.html#BACKUP-DUMP-ALL)
  2. Drop all dependencies you created and the PostGIS extension - `DROP EXTENSION postgis CASCADE;`
  3. Enable PostGIS extension in the new schema - `CREATE EXTENSION postgis SCHEMA extensions;`
  4. Restore dropped data via the Backup if necessary from step 1 with your tool of choice.


## Resources[#](https://supabase.com/docs/guides/database/extensions/postgis#resources)
  * [Official PostGIS documentation](https://postgis.net/documentation/)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/database/extensions/postgis.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FagFsGDJxjwA%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Overview](https://supabase.com/docs/guides/database/extensions/postgis#overview)[Enable the extension](https://supabase.com/docs/guides/database/extensions/postgis#enable-the-extension)[Examples](https://supabase.com/docs/guides/database/extensions/postgis#examples)[Inserting data](https://supabase.com/docs/guides/database/extensions/postgis#inserting-data)[Order by distance](https://supabase.com/docs/guides/database/extensions/postgis#order-by-distance)[Finding all data points within a bounding box](https://supabase.com/docs/guides/database/extensions/postgis#finding-all-data-points-within-a-bounding-box)[Troubleshooting](https://supabase.com/docs/guides/database/extensions/postgis#troubleshooting)[Resources](https://supabase.com/docs/guides/database/extensions/postgis#resources)
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



