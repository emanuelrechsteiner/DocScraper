---
url: https://supabase.com/docs/guides/storage/production/scaling
scraped_at: 2025-05-25T08:57:01.538543
title: Storage Optimizations | Supabase Docs
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
  2. Going to production
  3. [Scaling](https://supabase.com/docs/guides/storage/production/scaling)


Storage Optimizations
Scaling Storage
Here are some optimizations that you can consider to improve performance and reduce costs as you start scaling Storage.
## Egress[#](https://supabase.com/docs/guides/storage/production/scaling#egress)
If your project has high egress, these optimizations can help reducing it.
#### Resize images[#](https://supabase.com/docs/guides/storage/production/scaling#resize-images)
Images typically make up most of your egress. By keeping them as small as possible, you can cut down on egress and boost your application's performance. You can take advantage of our [Image Transformation](https://supabase.com/docs/guides/storage/serving/image-transformations) service to optimize any image on the fly.
#### Set a high cache-control value[#](https://supabase.com/docs/guides/storage/production/scaling#set-a-high-cache-control-value)
Using the browser cache can effectively lower your egress since the asset remains stored in the user's browser after the initial download. Setting a high `cache-control` value ensures the asset stays in the user's browser for an extended period, decreasing the need to download it from the server repeatedly. Read more [here](https://supabase.com/docs/guides/storage/cdn/smart-cdn#cache-duration)
#### Limit the upload size[#](https://supabase.com/docs/guides/storage/production/scaling#limit-the-upload-size)
You have the option to set a maximum upload size for your bucket. Doing this can prevent users from uploading and then downloading excessively large files. You can control the maximum file size by configuring this option at the [bucket level](https://supabase.com/docs/guides/storage/buckets/creating-buckets).
## Optimize listing objects[#](https://supabase.com/docs/guides/storage/production/scaling#optimize-listing-objects)
Once you have a substantial number of objects, you might observe that the `supabase.storage.list()` method starts to slow down. This occurs because the endpoint is quite generic and attempts to retrieve both folders and objects in a single query. While this approach is very useful for building features like the Storage viewer on the Supabase dashboard, it can impact performance with a large number of objects.
If your application doesn't need the entire hierarchy computed you can speed up drastically the query execution for listing your objects by creating a Postgres function as following:
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
24
25
26
27
28
29
create or replacefunctionlist_objects(  bucketid text,  prefix text,  limits intdefault100,  offsets intdefault0) returnstable (nametext,  id uuid,  updated_at timestamptz,  created_at timestamptz,  last_accessed_at timestamptz,  metadata jsonb) as $$beginreturn query SELECTobjects.name,objects.id,objects.updated_at,objects.created_at,objects.last_accessed_at,objects.metadataFROMstorage.objectsWHEREobjects.namelike prefix ||'%'AND bucket_id = bucketidORDER BYnameASCLIMIT limits  OFFSET offsets;end;$$ language plpgsql stable;

```

You can then use the your Postgres function as following:
Using SQL:
```

1
select*from list_objects('bucket_id', '', 100, 0);

```

Using the SDK:
```

1
2
3
4
5
6
const{data,error}=awaitsupabase.rpc('list_objects',{bucketid:'yourbucket',prefix:'',limit:100,offset:0,})

```

## Optimizing RLS[#](https://supabase.com/docs/guides/storage/production/scaling#optimizing-rls)
When creating RLS policies against the storage tables you can add indexes to the interested columns to speed up the lookup
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/storage/production/scaling.mdx)
### Is this helpful?
No Yes
### On this page
[Egress](https://supabase.com/docs/guides/storage/production/scaling#egress)[Optimize listing objects](https://supabase.com/docs/guides/storage/production/scaling#optimize-listing-objects)[Optimizing RLS](https://supabase.com/docs/guides/storage/production/scaling#optimizing-rls)
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



