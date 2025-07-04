---
url: http://supabase.com/docs/guides/storage/security/ownership
scraped_at: 2025-05-25T09:33:26.897605
title: Ownership | Supabase Docs
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
  2. Security
  3. [Ownership](https://supabase.com/docs/guides/storage/security/ownership)


Ownership
When creating new buckets or objects in Supabase Storage, an owner is automatically assigned to the bucket or object. The owner is the user who created the resource and the value is derived from the `sub` claim in the JWT. We store the `owner` in the `owner_id` column.
When using the `service_key` to create a resource, the owner will not be set and the resource will be owned by anyone. This is also the case when you are creating Storage resources via the Dashboard.
The Storage schema has 2 fields to represent ownership: `owner` and `owner_id`. `owner` is deprecated and will be removed. Use `owner_id` instead.
## Access control[#](https://supabase.com/docs/guides/storage/security/ownership#access-control)
By itself, the ownership of a resource does not provide any access control. However, you can enforce the ownership by implementing access control against storage resources scoped to their owner.
For example, you can implement a policy where only the owner of an object can delete it. To do this, check the `owner_id` field of the object and compare it with the `sub` claim of the JWT:
```

1
2
3
4
5
6
7
createpolicy"User can delete their own objects"onstorage.objectsfordeleteto authenticatedusing (  owner_id = (selectauth.uid()));

```

The use of RLS policies is just one way to enforce access control. You can also implement access control in your server code by following the same pattern.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/storage/security/ownership.mdx)
### Is this helpful?
No Yes
### On this page
[Access control](https://supabase.com/docs/guides/storage/security/ownership#access-control)
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



