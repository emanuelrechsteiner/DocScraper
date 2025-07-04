---
url: https://supabase.com/partners/flutterflow
scraped_at: 2025-05-25T09:30:29.870111
title: FlutterFlow | Works With Supabase
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
![FlutterFlow](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fflutterflow%2Fflutterflow-logo.jpeg&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# FlutterFlow
![FlutterFlow](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fflutterflow%2Fflutterflow-1.jpeg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![FlutterFlow](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fflutterflow%2Fflutterflow-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
FlutterFlow is a low-code builder for developing native mobile applications using Flutter. You can use the simple drag-and-drop interface to build your app faster than traditional development.
## Documentation
FlutterFlow and Supabase integration is currently in alpha, and supported features may be limited.
[FlutterFlow](https://flutterflow.io/) is a low-code builder for developing native mobile applications using Flutter. You can use the simple drag-and-drop interface to build your app faster than traditional development.
This guide gives you a quick overview of implementing basic CRUD operations using FlutterFlow and Supabase. You can find the full docs on FlutterFlow and Supabase [here](https://docs.flutterflow.io/actions/actions/backend-database/supabase).
## Step 1: Connect FlutterFlow to Supabase
Before we dive into the code, this guide assumes that you have the following ready:
  * [Supabase](https://database.new/) project created
  * Have setup tables in your Supabase project
  * [FlutterFlow](https://app.flutterflow.io/) project created


You can then connect your Supabase project to your FlutterFlow project with the following steps:
  1. In your Supabase project, navigate to Project Settings > API. Copy the Project URL.
  2. Return to FlutterFlow, navigate to Settings and Integrations > Integrations > Supabase. Turn on the toggle (i.e., enable Supabase) and paste the API URL.
  3. Similarly, from the Supabase API section, copy the anon key (under Project API keys) and paste it inside the FlutterFlow > Settings and Integrations > Integrations > Supabase > Anon Key.
  4. Click on the Get Schema button. This will show the list of all tables with their schema (structure) created in Supabase.
  5. (Optional) If you have defined an Array for any Column Data Type in Supabase, you must set its type here. To do so, tap the "Click to set Array type" and choose the right one.


## Step 2: Inserting rows
Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.
  1. Select the Widget (e.g., Button) on which you want to define the action.
  2. Select Actions from the Properties panel (the right menu), and click Open. This will open an Action flow Editor in a new popup window. 
    1. Click on + Add Action.
    2. On the right side, search and select the Supabase > Insert Row action.
    3. Set the Table to your table name (e.g., assignments).
    4. Under the Set Fields section, click on the + Add Field button.
    5. Click on the Field name and scroll down to find the Value Source dropdown and change it to From Variable.
    6. Click on UNSET and select Widget State > Name of the TextField.
    7. Similarly, add the field for the other UI elements.


## Step 3: Selecting and displaying rows
To query a Supabase table on a ListView:
  1. Select the ListView widget. Make sure you choose the ListView widget, not the ListTile.
  2. Select Backend Query from the properties panel (the right menu), and click Add Backend Query.
  3. Set the Query Type to Supabase Query.
  4. Select your Table from the dropdown list
  5. Set the Query Type to List of Rows.
  6. Optional: If you want to display the limited result, say, for example, you have thousands of entries, but you want to display only 100, you can specify the limit.
  7. Click Confirm.


## Step 4: Updating rows
Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.
  1. Select the Widget (e.g., Button) on which you want to define the action.
  2. Select Actions from the Properties panel (the right menu), and click Open. This will open an Action flow Editor in a new popup window. 
    1. Click on + Add Action.
    2. On the right side, search and select the Supabase > Update Row action.
    3. Set the Table to your table name (e.g., assignments).
    4. Optional: If you want to get the rows after the update is finished, enable the Return Matching Rows option.
    5. Now, you must set the row you want to update. Usually, this is done by finding a row in a table that matches the current row ID. To do so, click + Add Filter button inside the Matching Rows section. 
      1. Set the Field Name to the field that contains the IDs. Typically, this is the id column.
      2. Set the Relation to Equal To because you want to find a row with the exact id.
      3. Into the Value Source, you can select the From Variable and provide the id of the row for which you just updated values in the UI.
    6. Under the Set Fields section, click on the + Add Field button.
    7. Click on the field name.
    8. Scroll down to find the Value Source dropdown and change it to From Variable.
    9. Click on UNSET and select Widget State > Name of the TextField.
    10. Similarly, add the field for the other UI elements.


## Step 5: Deleting rows
Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.
  1. Select the Widget (e.g., Button) on which you want to define the action.
  2. Select Actions from the Properties panel (the right menu), and click Open. This will open an Action flow Editor in a new popup window. 
    1. Click on + Add Action.
    2. On the right side, search and select the Supabase -> Delete Row action.
    3. Set the Table to your table name (e.g., assignments).
    4. Optional: Later, if you want to know which rows were deleted from a table, enable the Return Matching Rows option.
    5. Now, you must set the row you want to delete. Usually, this is done by finding a row in a table that matches the current row ID. To do so, click + Add Filter button inside the Matching Rows section. 
      1. Set the Field Name to the field that contains the IDs. Typically, this is the id column.
      2. Set the Relation to Equal To because you want to find a row with the exact id.
      3. Into the Value Source, you can select the From Variable and provide the id of the row you want to delete.


## Resources
You can find more detailed guides on FlutterFlow’s docs.
  * [FlutterFlow Supabase available actions](https://docs.flutterflow.io/actions/actions/backend-database/supabase)
  * [Retrieving Data from Supabase on FlutterFlow](https://docs.flutterflow.io/data-and-backend/supabase/supabase-database/retrieving-data)
  * [Adding data to Supabase DB from FlutterFlow](https://docs.flutterflow.io/data-and-backend/supabase/supabase-database/adding-data)


## Details
Watch an introductory video
![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
DeveloperFlutterFlow
Category[Low-Code](https://supabase.com/partners/integrations#low-code)
Website[flutterflow.io](https://flutterflow.io/)
Documentation[Learn](https://docs.flutterflow.io/)
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

