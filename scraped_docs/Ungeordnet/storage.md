---
url: http://supabase.com/storage
scraped_at: 2025-05-25T09:16:49.318168
title: Storage | Store any digital content
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
[Database](https://supabase.com/database)[Auth](https://supabase.com/auth)[Storage](https://supabase.com/storage)[Edge Functions](https://supabase.com/edge-functions)[Realtime](https://supabase.com/realtime)
Storage
# Store and serve any type of digital content
An open source **S3 Compatible** Object Store, with unlimited scalability, for any file type.
With custom policies and permissions that are familiar and easy to implement.
[Start a project](https://supabase.com/dashboard)[See documentation](https://supabase.com/docs/guides/storage)
![storage header](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fstorage%2Fheader--dark.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
#### Interoperable
Integrates well with the rest of Supabase ecosystem, including Auth and Postgres.
#### Lightning fast
Thin API server layer that leverages Postgres' permissions and performance.
#### Multiple Protocol Support
S3, Resumable Uploads and Standard Uploads. Enterprise-level scalability.
## Sleek dashboard for managing your media
A complete Object Explorer so that any of your team can use.
Drag and drop uploading, moving objects, and multiple object selection. As easy as working on your desktop.
File previewsColumn viewList viewMulti select actionsPath navigator
![File previews](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fstorage%2Fdashboard-view%2Ffile-previews.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Column view](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fstorage%2Fdashboard-view%2Fcolumn-view.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![List view](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fstorage%2Fdashboard-view%2Flist-view.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Multi select actions](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fstorage%2Fdashboard-view%2Fmulti-column-selection.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Path navigator](https://supabase.com/_next/image?url=%2Fimages%2Fproduct%2Fstorage%2Fdashboard-view%2Fpath-setting.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
File previewsColumn viewList viewMulti select actionsPath navigator
#### File previews
Preview any media type, including video and audio.
#### Column view
Slick Miller-column navigation for rapid folder exploration.
#### List view
List View to find detailed File metadata at a glance.
#### Multi select actions
Multi-import and multi-export. Select multiple files from multiple folders.
#### Path navigator
If you know the exact path of your file, type it in and navigate directly.
Check out our example app#### [Profile management exampleUpdate a user account with public profile information, including uploading a profile image. View Template ](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management)
## Simple and convenient APIs
Built from the ground up for interoperable authentication.
Fast and easy to implement using our powerful library clients.
#### CDN
Serve from over 285 cities globally to reduce latency.
[Explore docs](https://supabase.com/docs/guides/storage/cdn/fundamentals)
#### Image Optimizations and Transformations
Resize and compress your media files on the fly.
[Explore docs](https://supabase.com/docs/guides/storage/serving/image-transformations)
Upload a fileDownload a fileList filesMove and rename filesDelete files
```
// Upload an image to the "avatars" bucketconst spaceCat = event.target.files[0]
const { data, error } = await supabase
 .storage
 .from('avatars')
 .upload('space-cat.png', spaceCat)
 
 
 

 
```

```
// Download the "space-cat.png" image from the "avatars" bucketconst { data, error } = await supabase
  .storage
  .from('avatars')
  .download('space-cat.png')



    
 
```

```
// List all the files in the "avatars" bucketconst { data, error } = await supabase
  .storage
  .from('avatars')
  .list()


    
 
```

```
// Move and rename filesconst { data, error } = await supabase
 .storage
 .from('avatars')
 .move('public/space-cat.png', 'private/space-cat.png')



    
 
```

```
// Delete a list of filesconst { data, error } = await supabase
 .storage
 .from('avatars')
 .remove([ 'avatar1.png', 'avatar2.png' ])




    
 
```

## Integrates natively with Supabase Auth
Using Postgres Row Level Security to create Object access rules.
Storage Authorization is built around Postgres so that you can use any combination of SQL, Postgres functions, and even your own metadata to write policies.
[Explore documentation](https://supabase.com/docs/reference/javascript/storage-createbucket)
Public access to a bucketPublic access to a folderAuthenticated access to a bucketIndividual access to a file
```
create policy "Public Access" 
on storage.objects forallusing ( bucket_id ='avatars' );
  
```

```
create policy "Public access to a folder" 
on storage.objects forallusing (
 bucket_id ='avatars'and (storage.foldername(name))[1] ='public');
  
```

```
create policy "Logged in access" 
on storage.objects 
forallusing (
 bucket_id ='avatars'and auth.role() ='authenticated'and (storage.foldername(name))[1] ='authenticated');
```

```
create policy "Individual access" 
on storage.objects forallusing (
 bucket_id ='avatars'and name ='folder/only_uid.jpg'and (select auth.uid()) ='d8c7bce9-cfeb-497b-bd61-e66ce2cbdaa2');
```

Allow public CRUD access to a bucket
This will allow any user access to the bucket named 'avatars'
Allow public CRUD access to a folder in a bucket
This will allow any user access to the folder named 'public' in the bucket 'avatars'
Allow any authenticated user access to a folder
This will allow any authenticated user access to the folder named 'authenticated' in the bucket 'avatars'
Allow a specific user access to a file
This will allow a specific user based on the user's UID access to a file named 'only_uid.jpg'
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

