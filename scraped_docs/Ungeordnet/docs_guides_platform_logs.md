---
url: https://supabase.com/docs/guides/platform/logs
scraped_at: 2025-05-25T09:19:16.320889
title: Logging | Supabase Docs
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
[Telemetry](https://supabase.com/docs/guides/telemetry)
  * [Overview](https://supabase.com/docs/guides/telemetry)
Logging & observability
  * [Logging](https://supabase.com/docs/guides/telemetry/logs)
  * [Advanced log filtering](https://supabase.com/docs/guides/telemetry/advanced-log-filtering)
  * [Log drains](https://supabase.com/docs/guides/telemetry/log-drains)
  * [Metrics](https://supabase.com/docs/guides/telemetry/metrics)
  * [Sentry integration](https://supabase.com/docs/guides/telemetry/sentry-monitoring)


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
Telemetry
  1. [Telemetry](https://supabase.com/docs/guides/telemetry)
  2. Logging & observability
  3. [Logging](https://supabase.com/docs/guides/telemetry/logs)


Logging
The Supabase Platform includes a Logs Explorer that allows log tracing and debugging. Log retention is based on your [project's pricing plan](https://supabase.com/pricing).
## Product logs[#](https://supabase.com/docs/guides/telemetry/logs#product-logs)
Supabase provides a logging interface specific to each product. You can use simple regular expressions for keywords and patterns to search log event messages. You can also export and download the log events matching your query as a spreadsheet.
APIPostgresAuthStorageRealtimeEdge Functions
[API logs](https://supabase.com/dashboard/project/_/logs/edge-logs) show all network requests and response for the REST and GraphQL [APIs](https://supabase.com/docs/guides/database/api). If [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas) are enabled, logs are automatically filtered between databases as well as the [API Load Balancer](https://supabase.com/docs/guides/platform/read-replicas#api-load-balancer) endpoint. Logs for a specific endpoint can be toggled with the `Source` button on the upper-right section of the dashboard.
When viewing logs originating from the API Load Balancer endpoint, the upstream database or the one that eventually handles the request can be found under the `Redirect Identifier` field. This is equivalent to `metadata.load_balancer_redirect_identifier` when querying the underlying logs.
![API Logs](https://supabase.com/docs/img/guides/platform/logs/logs-api.png)
## Working with API logs[#](https://supabase.com/docs/guides/telemetry/logs#working-with-api-logs)
[API logs](https://supabase.com/dashboard/project/_/logs/edge-logs) run through the Cloudflare edge servers and will have attached Cloudflare metadata under the `metadata.request.cf.*` fields.
### Allowed headers[#](https://supabase.com/docs/guides/telemetry/logs#allowed-headers)
A strict list of request and response headers are permitted in the API logs. Request and response headers will still be received by the server(s) and client(s), but will not be attached to the API logs generated.
Request headers:
  * `accept`
  * `cf-connecting-ip`
  * `cf-ipcountry`
  * `host`
  * `user-agent`
  * `x-forwarded-proto`
  * `referer`
  * `content-length`
  * `x-real-ip`
  * `x-client-info`
  * `x-forwarded-user-agent`
  * `range`
  * `prefer`


Response headers:
  * `cf-cache-status`
  * `cf-ray`
  * `content-location`
  * `content-range`
  * `content-type`
  * `content-length`
  * `date`
  * `transfer-encoding`
  * `x-kong-proxy-latency`
  * `x-kong-upstream-latency`
  * `sb-gateway-mode`
  * `sb-gateway-version`


### Additional request metadata[#](https://supabase.com/docs/guides/telemetry/logs#additional-request-metadata)
To attach additional metadata to a request, it is recommended to use the `User-Agent` header for purposes such as device or version identification.
For example:
```

1
2
node MyApp/1.2.3 (device-id:abc123)Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 MyApp/1.2.3 (Foo v1.3.2; Bar v2.2.2)

```

Do not log Personal Identifiable Information (PII) within the `User-Agent` header, to avoid infringing data protection privacy laws. Overly fine-grained and detailed user agents may allow fingerprinting and identification of the end user through PII.
## Logging Postgres queries[#](https://supabase.com/docs/guides/telemetry/logs#logging-postgres-queries)
To enable query logs for other categories of statements:
  1. [Enable the pgAudit extension](https://supabase.com/dashboard/project/_/database/extensions).
  2. Configure `pgaudit.log` (see below). Perform a fast reboot if needed.
  3. View your query logs under [Logs > Postgres Logs](https://supabase.com/dashboard/project/_/logs/postgres-logs).


### Configuring `pgaudit.log`[#](https://supabase.com/docs/guides/telemetry/logs#configuring-pgauditlog)
The stored value under `pgaudit.log` determines the classes of statements that are logged by [pgAudit extension](https://www.pgaudit.org/). Refer to the pgAudit documentation for the [full list of values](https://github.com/pgaudit/pgaudit/blob/master/README.md#pgauditlog).
To enable logging for function calls/do blocks, writes, and DDL statements for a single session, execute the following within the session:
```

1
2
-- temporary single-session config updatesetpgaudit.log='function, write, ddl';

```

To _permanently_ set a logging configuration (beyond a single session), execute the following, then perform a fast reboot:
```

1
2
-- equivalent permanent config update.alterrole postgres setpgaudit.logto'function, write, ddl';

```

To help with debugging, we recommend adjusting the log scope to only relevant statements as having too wide of a scope would result in a lot of noise in your Postgres logs.
Note that in the above example, the role is set to `postgres`. To log user-traffic flowing through the [HTTP APIs](https://supabase.com/docs/guides/database/api#rest-api-overview) powered by PostgREST, set your configuration values for the `authenticator`.
```

1
2
-- for API-related logsalterrole authenticator setpgaudit.logto'write';

```

By default, the log level will be set to `log`. To view other levels, run the following:
```

1
2
3
-- adjust log levelalterrole postgres setpgaudit.log_levelto'info';alterrole postgres setpgaudit.log_levelto'debug5';

```

Note that as per the pgAudit [log_level documentation](https://github.com/pgaudit/pgaudit/blob/master/README.md#pgauditlog_level), `error`, `fatal`, and `panic` are not allowed.
To reset system-wide settings, execute the following, then perform a fast reboot:
```

1
2
-- resets stored config.alterrole postgres resetpgaudit.log

```

If any permission errors are encountered when executing `alter role postgres ...`, it is likely that your project has yet to receive the patch to the latest version of [supautils](https://github.com/supabase/supautils), which is currently being rolled out.
### `RAISE`d log messages in Postgres[#](https://supabase.com/docs/guides/telemetry/logs#raise-d-log-messages-in-postgres)
Messages that are manually logged via `RAISE INFO`, `RAISE NOTICE`, `RAISE WARNING`, and `RAISE LOG` are shown in Postgres Logs. Note that only messages at or above your logging level are shown. Syncing of messages to Postgres Logs may take a few minutes.
If your logs aren't showing, check your logging level by running:
```

1
show log_min_messages;

```

Note that `LOG` is a higher level than `WARNING` and `ERROR`, so if your level is set to `LOG`, you will not see `WARNING` and `ERROR` messages.
## Logging realtime connections[#](https://supabase.com/docs/guides/telemetry/logs#logging-realtime-connections)
Realtime doesn't log new WebSocket connections or Channel joins by default. Enable connection logging per client by including an `info` `log_level` parameter when instantiating the Supabase client.
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
import{createClient}from'@supabase/supabase-js'constoptions={realtime:{params:{log_level:'info',},},}constsupabase=createClient('https://xyzcompany.supabase.co','public-anon-key',options)

```

## Logs Explorer[#](https://supabase.com/docs/guides/telemetry/logs#logs-explorer)
The [Logs Explorer](https://supabase.com/dashboard/project/_/logs-explorer) exposes logs from each part of the Supabase stack as a separate table that can be queried and joined using SQL.
![Logs Explorer](https://supabase.com/docs/img/guides/platform/logs/logs-explorer.png)
You can access the following logs from the **Sources** drop-down:
  * `auth_logs`: GoTrue server logs, containing authentication/authorization activity.
  * `edge_logs`: Edge network logs, containing request and response metadata retrieved from Cloudflare.
  * `function_edge_logs`: Edge network logs for only edge functions, containing network requests and response metadata for each execution.
  * `function_logs`: Function internal logs, containing any `console` logging from within the edge function.
  * `postgres_logs`: Postgres database logs, containing statements executed by connected applications.
  * `realtime_logs`: Realtime server logs, containing client connection information.
  * `storage_logs`: Storage server logs, containing object upload and retrieval information.


## Querying with the Logs Explorer[#](https://supabase.com/docs/guides/telemetry/logs#querying-with-the-logs-explorer)
The Logs Explorer uses BigQuery and supports all [available SQL functions and operators](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators).
### Timestamp display and behavior[#](https://supabase.com/docs/guides/telemetry/logs#timestamp-display-and-behavior)
Each log entry is stored with a `timestamp` as a `TIMESTAMP` data type. Use the appropriate [timestamp function](https://cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp) to utilize the `timestamp` field in a query.
Raw top-level timestamp values are rendered as unix microsecond. To render the timestamps in a human-readable format, use the `DATETIME()` function to convert the unix timestamp display into an ISO-8601 timestamp.
```

1
2
3
4
5
6
7
-- timestamp column without datetime()selecttimestampfrom ....-- 1664270180000-- timestamp column with datetime()selectdatetime(timestamp) from ....-- 2022-09-27T09:17:10.439Z

```

### Unnesting arrays[#](https://supabase.com/docs/guides/telemetry/logs#unnesting-arrays)
Each log event stores metadata an array of objects with multiple levels, and can be seen by selecting single log events in the Logs Explorer. To query arrays, use `unnest()` on each array field and add it to the query as a join. This allows you to reference the nested objects with an alias and select their individual fields.
For example, to query the edge logs without any joins:
```

1
selecttimestamp, metadata from edge_logs as t;

```

The resulting `metadata` key is rendered as an array of objects in the Logs Explorer. In the following diagram, each box represents a nested array of objects:
![Without Unnesting](https://supabase.com/docs/img/unnesting-none.png)
Perform a `cross join unnest()` to work with the keys nested in the `metadata` key.
To query for a nested value, add a join for each array level:
```

1
2
3
4
5
6
selecttimestamp, request.method, header.cf_ipcountryfrom edge_logs as tcross join unnest(t.metadata) as metadatacross join unnest(metadata.request) as requestcross join unnest(request.headers) as header;

```

This surfaces the following columns available for selection: ![With Two Level Unnesting](https://supabase.com/docs/img/unnesting-2.png)
This allows you to select the `method` and `cf_ipcountry` columns. In JS dot notation, the full paths for each selected column are:
  * `metadata[].request[].method`
  * `metadata[].request[].headers[].cf_ipcountry`


### LIMIT and result row limitations[#](https://supabase.com/docs/guides/telemetry/logs#limit-and-result-row-limitations)
The Logs Explorer has a maximum of 1000 rows per run. Use `LIMIT` to optimize your queries by reducing the number of rows returned further.
### Best practices[#](https://supabase.com/docs/guides/telemetry/logs#best-practices)
  1. Include a filter over **timestamp**


Querying your entire log history might seem appealing. For **Enterprise** customers that have a large retention range, you run the risk of timeouts due additional time required to scan the larger dataset.
  1. Avoid selecting large nested objects. Select individual values instead.


When querying large objects, the columnar storage engine selects each column associated with each nested key, resulting in a large number of columns being selected. This inadvertently impacts the query speed and may result in timeouts or memory errors, especially for projects with a lot of logs.
Instead, select only the values required.
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
-- ❌ Avoid doing thisselectdatetime(timestamp), m as metadata -- <- metadata contains many nested keysfrom edge_logs as tcross join unnest(t.metadata) as m;-- ✅ Do thisselectdatetime(timestamp),r.method-- <- select only the required valuesfrom edge_logs as tcross join unnest(t.metadata) as mcross join unnest(m.request) as r;

```

### Examples and templates[#](https://supabase.com/docs/guides/telemetry/logs#examples-and-templates)
The Logs Explorer includes **Templates** (available in the Templates tab or the dropdown in the Query tab) to help you get started.
For example, you can enter the following query in the SQL Editor to retrieve each user's IP address:
```

1
2
3
4
5
6
7
selectdatetime(timestamp), h.x_real_ipfrom edge_logscross join unnest(metadata) as mcross join unnest(m.request) as rcross join unnest(r.headers) as hwhereh.x_real_ipis not nullandr.method="GET";

```

### Logs field reference[#](https://supabase.com/docs/guides/telemetry/logs#logs-field-reference)
Refer to the full field reference for each available source below. Do note that in order to access each nested key, you would need to perform the [necessary unnesting joins](https://supabase.com/docs/guides/telemetry/logs#unnesting-arrays)
API GatewayAuthStorageFunction EdgeFunction RuntimePostgresRealtimePostgRESTSupavisor (Shared Pooler)PgBouncer (Dedicated Pooler)Database Version Upgrade
Path| Type  
---|---  
id| string  
timestamp| datetime  
event_message| string  
identifier| string  
metadata.load_balancer_redirect_identifier| string  
metadata.request.cf.asOrganization| string  
metadata.request.cf.asn| number  
metadata.request.cf.botManagement.corporateProxy| boolean  
metadata.request.cf.botManagement.detectionIds| number[]  
metadata.request.cf.botManagement.ja3Hash| string  
metadata.request.cf.botManagement.score| number  
metadata.request.cf.botManagement.staticResource| boolean  
metadata.request.cf.botManagement.verifiedBot| boolean  
metadata.request.cf.city| string  
metadata.request.cf.clientTcpRtt| number  
metadata.request.cf.clientTrustScore| number  
metadata.request.cf.colo| string  
metadata.request.cf.continent| string  
metadata.request.cf.country| string  
metadata.request.cf.edgeRequestKeepAliveStatus| number  
metadata.request.cf.httpProtocol| string  
metadata.request.cf.latitude| string  
metadata.request.cf.longitude| string  
metadata.request.cf.metroCode| string  
metadata.request.cf.postalCode| string  
metadata.request.cf.region| string  
metadata.request.cf.timezone| string  
metadata.request.cf.tlsCipher| string  
metadata.request.cf.tlsClientAuth.certPresented| string  
metadata.request.cf.tlsClientAuth.certRevoked| string  
metadata.request.cf.tlsClientAuth.certVerified| string  
metadata.request.cf.tlsExportedAuthenticator.clientFinished| string  
metadata.request.cf.tlsExportedAuthenticator.clientHandshake| string  
metadata.request.cf.tlsExportedAuthenticator.serverFinished| string  
metadata.request.cf.tlsExportedAuthenticator.serverHandshake| string  
metadata.request.cf.tlsVersion| string  
metadata.request.headers.cf_connecting_ip| string  
metadata.request.headers.cf_ipcountry| string  
metadata.request.headers.cf_ray| string  
metadata.request.headers.host| string  
metadata.request.headers.referer| string  
metadata.request.headers.x_client_info| string  
metadata.request.headers.x_forwarded_proto| string  
metadata.request.headers.x_real_ip| string  
metadata.request.host| string  
metadata.request.method| string  
metadata.request.path| string  
metadata.request.protocol| string  
metadata.request.search| string  
metadata.request.url| string  
metadata.response.headers.cf_cache_status| string  
metadata.response.headers.cf_ray| string  
metadata.response.headers.content_location| string  
metadata.response.headers.content_range| string  
metadata.response.headers.content_type| string  
metadata.response.headers.date| string  
metadata.response.headers.sb_gateway_version| string  
metadata.response.headers.transfer_encoding| string  
metadata.response.headers.x_kong_proxy_latency| string  
metadata.response.origin_time| number  
metadata.response.status_code| number  
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/telemetry/logs.mdx)
### Is this helpful?
No Yes
### On this page
[Product logs](https://supabase.com/docs/guides/telemetry/logs#product-logs)[Working with API logs](https://supabase.com/docs/guides/telemetry/logs#working-with-api-logs)[Allowed headers](https://supabase.com/docs/guides/telemetry/logs#allowed-headers)[Additional request metadata](https://supabase.com/docs/guides/telemetry/logs#additional-request-metadata)[Logging Postgres queries](https://supabase.com/docs/guides/telemetry/logs#logging-postgres-queries)[Configuring pgaudit.log](https://supabase.com/docs/guides/telemetry/logs#configuring-pgauditlog)[RAISEd log messages in Postgres](https://supabase.com/docs/guides/telemetry/logs#raise-d-log-messages-in-postgres)[Logging realtime connections](https://supabase.com/docs/guides/telemetry/logs#logging-realtime-connections)[Logs Explorer](https://supabase.com/docs/guides/telemetry/logs#logs-explorer)[Querying with the Logs Explorer](https://supabase.com/docs/guides/telemetry/logs#querying-with-the-logs-explorer)[Timestamp display and behavior](https://supabase.com/docs/guides/telemetry/logs#timestamp-display-and-behavior)[Unnesting arrays](https://supabase.com/docs/guides/telemetry/logs#unnesting-arrays)[LIMIT and result row limitations](https://supabase.com/docs/guides/telemetry/logs#limit-and-result-row-limitations)[Best practices](https://supabase.com/docs/guides/telemetry/logs#best-practices)[Examples and templates](https://supabase.com/docs/guides/telemetry/logs#examples-and-templates)[Logs field reference](https://supabase.com/docs/guides/telemetry/logs#logs-field-reference)
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



