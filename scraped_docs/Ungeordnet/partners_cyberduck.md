---
url: https://supabase.com/partners/cyberduck
scraped_at: 2025-05-25T09:11:56.794312
title: Cyberduck | Works With Supabase
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
[Back](https://supabase.com/partners/integrations)
![Cyberduck](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fcyberduck%2Fcyberduck-icon-384.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Cyberduck
## Overview
Cyberduck is a free and open-source file manager for Windows and macOS that can be used to connect to Supabase Storage S3. In this guide, you'll learn how to connect to Supabase Storage S3 with Cyberduck.
![Supabase Cyberduck](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cyberduck/cyberduck-files.png?t=2024-04-18T08%3A39%3A48.575Z)
## Prerequisites
You'll need valid credentials to connect to Supabase Storage S3. You can generate these credentials from the [Supabase Dashboard](https://supabase.com/dashboard/project/_/settings/storage).
## Download Cyberduck
You can download Cyberduck from the [Download Page](https://cyberduck.io/download/).
## Configure Cyberduck Profile
To configure cyberduck to connect to Supabase Storage S3 you need to create a custom profile.
Copy the following profile into a file called `supabase.cyberduckprofile`
`
1
<?xml version="1.0" encoding="UTF-8"?>
2
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
3
<plist version="1.0">
4
  <dict>
5
    <key>Protocol</key>
6
    <string>s3</string>
7
    <key>Vendor</key>
8
    <string>Supabase Storage S3</string>
9
    <key>Scheme</key>
10
    <string>https</string>
11
    <key>Description</key>
12
    <string>Supabase Storage (S3)</string>
13
    <key>Default Hostname</key>
14
    <string>YOUR_PROJECT_REF.supabase.co</string>
15
    <key>Default Port</key>
16
    <string>443</string>
17
    <key>Region</key>
18
    <string>YOUR_REGION</string>
19
    <key>Properties</key>
20
    <array>
21
      <string>s3.storage.class.options=STANDARD</string>
22
      <string>s3.bucket.virtualhost.disable=true</string>
23
    </array>
24
    <key>Context</key>
25
    <string>/storage/v1/s3</string>
26
    <key>Help</key>
27
    <string>https://supabase.com/docs/guides/storage</string>
28
  </dict>
29
</plist>
`
Change the following values in the profile:
  * `YOUR_PROJECT_REF` with your Supabase project reference.
  * `YOUR_REGION` with your Supabase region.


Save the profile and double click on the file to open it with Cyberduck.
## Connect to Supabase Storage S3
You'll be presented with the following screen, fill in the `Access Key ID` and the `Secret Access Key` with your credentials.
![credentials](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cyberduck/credentials.png)
Close the window, and double click on the profile to connect to Supabase Storage S3.
## Details
DeveloperSupabase
Category[Storage](https://supabase.com/partners/integrations#storage)
Website[cyberduck.io](https://cyberduck.io/)
Documentation[Learn](https://cyberduck.io/)
Third-party integrations and docs are managed by Supabase partners.
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

