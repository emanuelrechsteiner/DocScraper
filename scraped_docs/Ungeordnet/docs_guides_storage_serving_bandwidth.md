---
url: https://supabase.com/docs/guides/storage/serving/bandwidth
scraped_at: 2025-05-25T09:30:19.312060
title: Bandwidth & Storage Egress | Supabase Docs
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
[Storage](https://supabase.com/docs/guides/storage)
  * [Overview](https://supabase.com/docs/guides/storage)
  * [Quickstart](https://supabase.com/docs/guides/storage/quickstart)
Buckets
  * [Fundamentals](https://supabase.com/docs/guides/storage/buckets/fundamentals)
  * [Creating Buckets](https://supabase.com/docs/guides/storage/buckets/creating-buckets)
Security
  * [Ownership](https://supabase.com/docs/guides/storage/security/ownership)
  * [Access Control](https://supabase.com/docs/guides/storage/security/access-control)
Uploads
  * [Standard Uploads](https://supabase.com/docs/guides/storage/uploads/standard-uploads)
  * [Resumable Uploads](https://supabase.com/docs/guides/storage/uploads/resumable-uploads)
  * [S3 Uploads](https://supabase.com/docs/guides/storage/uploads/s3-uploads)
  * [Limits](https://supabase.com/docs/guides/storage/uploads/file-limits)
Serving
  * [Serving assets](https://supabase.com/docs/guides/storage/serving/downloads)
  * [Image Transformations](https://supabase.com/docs/guides/storage/serving/image-transformations)
  * [Bandwidth & Storage Egress](https://supabase.com/docs/guides/storage/serving/bandwidth)
Management
  * [Copy / Move Objects](https://supabase.com/docs/guides/storage/management/copy-move-objects)
  * [Delete Objects](https://supabase.com/docs/guides/storage/management/delete-objects)
  * [Pricing](https://supabase.com/docs/guides/storage/management/pricing)
S3
  * [Authentication](https://supabase.com/docs/guides/storage/s3/authentication)
  * [API Compatibility](https://supabase.com/docs/guides/storage/s3/compatibility)
CDN
  * [Fundamentals](https://supabase.com/docs/guides/storage/cdn/fundamentals)
  * [Smart CDN](https://supabase.com/docs/guides/storage/cdn/smart-cdn)
  * [Metrics](https://supabase.com/docs/guides/storage/cdn/metrics)
Debugging
  * [Logs](https://supabase.com/docs/guides/storage/debugging/logs)
  * [Error Codes](https://supabase.com/docs/guides/storage/debugging/error-codes)
Schema
  * [Database Design](https://supabase.com/docs/guides/storage/schema/design)
  * [Helper Functions](https://supabase.com/docs/guides/storage/schema/helper-functions)
  * [Custom Roles](https://supabase.com/docs/guides/storage/schema/custom-roles)
Going to production
  * [Scaling](https://supabase.com/docs/guides/storage/production/scaling)


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
Storage
  1. [Storage](https://supabase.com/docs/guides/storage)
  2. Serving
  3. [Bandwidth & Storage Egress](https://supabase.com/docs/guides/storage/serving/bandwidth)


Bandwidth & Storage Egress
Bandwidth & Storage Egress
## Bandwidth & Storage egress[#](https://supabase.com/docs/guides/storage/serving/bandwidth#bandwidth--storage-egress)
Free Plan Organizations in Supabase have a limit of 5 GB of bandwidth. This limit is calculated by the sum of all the data transferred from the Supabase servers to the client. This includes all the data transferred from the database, storage, and functions.
### Checking Storage egress requests in Logs Explorer:[#](https://supabase.com/docs/guides/storage/serving/bandwidth#checking-storage-egress-requests-in-logs-explorer)
We have a template query that you can use to get the number of requests for each object in [Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer/templates).
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
selectr.methodas http_verb,r.pathas filepath,count(*) as num_requestsfrom edge_logscross join unnest(metadata) as mcross join unnest(m.request) as rcross join unnest(r.headers) as hwhere (pathlike'%storage/v1/object/%'orpathlike'%storage/v1/render/%') andr.method='GET'group byr.path, r.methodorder by num_requests desclimit100;

```

Example of the output:
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
[  {"filepath":"/storage/v1/object/sign/large%20bucket/20230902_200037.gif",  "http_verb":"GET",  "num_requests":100  },  {"filepath":"/storage/v1/object/public/demob/Sports/volleyball.png",  "http_verb":"GET",  "num_requests":168  }]

```

### Calculating egress:[#](https://supabase.com/docs/guides/storage/serving/bandwidth#calculating-egress)
If you already know the size of those files, you can calculate the egress by multiplying the number of requests by the size of the file. You can also get the size of the file with the following cURL:
```

1
curl-s-w"%{size_download}\n"-o/dev/null"https://my_project.supabase.co/storage/v1/object/large%20bucket/20230902_200037.gif"

```

This will return the size of the file in bytes. For this example, let's say that `20230902_200037.gif` has a file size of 3 megabytes and `volleyball.png` has a file size of 570 kilobytes.
Now, we have to sum all the egress for all the files to get the total egress:
```

1
2
3
100 * 3MB = 300MB168 * 570KB = 95.76MBTotal Egress = 395.76MB

```

You can see that these values can get quite large, so it's important to keep track of the egress and optimize the files.
### Optimizing egress:[#](https://supabase.com/docs/guides/storage/serving/bandwidth#optimizing-egress)
If you are on the Pro Plan, you can use the [Supabase Image Transformations](https://supabase.com/docs/guides/storage/image-transformations) to optimize the images and reduce the egress.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/storage/serving/bandwidth.mdx)
### Is this helpful?
No Yes
### On this page
[Bandwidth & Storage egress](https://supabase.com/docs/guides/storage/serving/bandwidth#bandwidth--storage-egress)[Checking Storage egress requests in Logs Explorer:](https://supabase.com/docs/guides/storage/serving/bandwidth#checking-storage-egress-requests-in-logs-explorer)[Calculating egress:](https://supabase.com/docs/guides/storage/serving/bandwidth#calculating-egress)[Optimizing egress:](https://supabase.com/docs/guides/storage/serving/bandwidth#optimizing-egress)
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



