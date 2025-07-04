---
url: https://supabase.com/docs/guides/storage/serving/downloads
scraped_at: 2025-05-25T09:45:38.504718
title: Serving assets from Storage | Supabase Docs
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
  3. [Serving assets](https://supabase.com/docs/guides/storage/serving/downloads)


Serving assets from Storage
Serving assets from Storage
## Public buckets[#](https://supabase.com/docs/guides/storage/serving/downloads#public-buckets)
As mentioned in the [Buckets Fundamentals](https://supabase.com/docs/guides/storage/buckets/fundamentals) all files uploaded in a public bucket are publicly accessible and benefit a high CDN cache HIT ratio.
You can access them by using this conventional URL:
```

1
https://[project_id].supabase.co/storage/v1/object/public/[bucket]/[asset-name]

```

You can also use the Supabase SDK `getPublicUrl` to generate this URL for you
```

1
2
3
const{data}=supabase.storage.from('bucket').getPublicUrl('filePath.jpg')console.log(data.publicUrl)

```

### Downloading[#](https://supabase.com/docs/guides/storage/serving/downloads#downloading)
If you want the browser to start an automatic download of the asset instead of trying serving it, you can add the `?download` query string parameter.
By default it will use the asset name to save the file on disk. You can optionally pass a custom name to the `download` parameter as following: `?download=customname.jpg`
## Private buckets[#](https://supabase.com/docs/guides/storage/serving/downloads#private-buckets)
Assets stored in a non-public bucket are considered private and are not accessible via a public URL like the public buckets.
You can access them only by:
  * Signing a time limited URL on the Server, for example with Edge Functions.
  * with a GET request the URL `https://[project_id].supabase.co/storage/v1/object/authenticated/[bucket]/[asset-name]` and the user Authorization header


### Signing URLs[#](https://supabase.com/docs/guides/storage/serving/downloads#signing-urls)
You can sign a time-limited URL that you can share to your users by invoking the `createSignedUrl` method on the SDK.
```

1
2
3
4
5
6
7
const{data,error}=awaitsupabase.storage.from('bucket').createSignedUrl('private-document.pdf',3600)if (data) {console.log(data.signedUrl)}

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/storage/serving/downloads.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FdLqSmxX3r7I%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Public buckets](https://supabase.com/docs/guides/storage/serving/downloads#public-buckets)[Downloading](https://supabase.com/docs/guides/storage/serving/downloads#downloading)[Private buckets](https://supabase.com/docs/guides/storage/serving/downloads#private-buckets)[Signing URLs](https://supabase.com/docs/guides/storage/serving/downloads#signing-urls)
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



