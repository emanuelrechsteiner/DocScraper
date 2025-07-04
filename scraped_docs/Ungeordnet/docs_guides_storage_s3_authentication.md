---
url: http://supabase.com/docs/guides/storage/s3/authentication
scraped_at: 2025-05-25T09:34:46.770193
title: S3 Authentication | Supabase Docs
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
  2. S3
  3. [Authentication](https://supabase.com/docs/guides/storage/s3/authentication)


S3 Authentication
Learn about authenticating with Supabase Storage S3.
You have two options to authenticate with Supabase Storage S3:
  * Using the generated S3 access keys from your [project settings](https://supabase.com/dashboard/project/_/settings/storage) (Intended exclusively for server-side use)
  * Using a Session Token, which will allow you to authenticate with a user JWT token and provide limited access via Row Level Security (RLS).


## S3 access keys[#](https://supabase.com/docs/guides/storage/s3/authentication#s3-access-keys)
##### Keep these credentials secure
S3 access keys provide full access to all S3 operations across all buckets and bypass RLS policies. These are meant to be used only on the server.
To authenticate with S3, generate a pair of credentials (Access Key ID and Secret Access Key), copy the endpoint and region from the [project settings page](https://supabase.com/dashboard/project/_/settings/storage).
This is all the information you need to connect to Supabase Storage using any S3-compatible service.
![Storage S3 Access keys](https://supabase.com/docs/img/storage/s3-credentials.png)
aws-sdk-jsAWS Credentials
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
import{S3Client}from'@aws-sdk/client-s3';constclient=newS3Client({forcePathStyle:true,region:'project_region',endpoint:'https://project_ref.supabase.co/storage/v1/s3',credentials:{accessKeyId:'your_access_key_id',secretAccessKey:'your_secret_access_key',}})

```

## Session token[#](https://supabase.com/docs/guides/storage/s3/authentication#session-token)
You can authenticate to Supabase S3 with a user JWT token to provide limited access via RLS to all S3 operations. This is useful when you want initialize the S3 client on the server scoped to a specific user, or use the S3 client directly from the client side.
All S3 operations performed with the Session Token are scoped to the authenticated user. RLS policies on the Storage Schema are respected.
To authenticate with S3 using a Session Token, use the following credentials:
  * access_key_id: `project_ref`
  * secret_access_key: `anonKey`
  * session_token: `valid jwt token`


For example, using the `aws-sdk` library:
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
import{S3Client}from'@aws-sdk/client-s3'const{data:{session},}=awaitsupabase.auth.getSession()constclient=newS3Client({forcePathStyle:true,region:'project_region',endpoint:'https://project_ref.supabase.co/storage/v1/s3',credentials:{accessKeyId:'project_ref',secretAccessKey:'anonKey',sessionToken:session.access_token,},})

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/storage/s3/authentication.mdx)
### Is this helpful?
No Yes
### On this page
[S3 access keys](https://supabase.com/docs/guides/storage/s3/authentication#s3-access-keys)[Session token](https://supabase.com/docs/guides/storage/s3/authentication#session-token)
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



