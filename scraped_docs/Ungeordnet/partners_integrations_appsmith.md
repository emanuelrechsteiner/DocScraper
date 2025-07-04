---
url: https://supabase.com/partners/integrations/appsmith
scraped_at: 2025-05-25T09:15:36.535223
title: Appsmith | Works With Supabase
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
![Appsmith](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fappsmith%2Fappsmith-logo.png&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Appsmith
![Appsmith](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fappsmith%2Fappsmith-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Appsmith](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fappsmith%2Fappsmith-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Appsmith](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fappsmith%2Fappsmith-3.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
Appsmith is an open-source framework for building internal tools. It lets you drag-and-drop UI components to build pages, connect to any API, database or GraphQL source and write logic with JavaScript objects.
## Documentation
This guide explains how to quickly build a Support Dashboard by connecting a Supabase back-end to an Appsmith front-end.
[Appsmith](https://www.appsmith.com/) is an open-source framework for building internal tools. It lets you drag-and-drop UI components to build pages, connect to any API, database or GraphQL source and write logic with JavaScript objects.
If you don’t have an Appsmith account, create one [here](https://app.appsmith.com/user/signup).
Let’s get started!
## Step 1: Set up your Backend on Supabase
  * On the [Supabase dashboard](https://supabase.com/dashboard), click `New project` and set the name to **Support Dashboard**


![create-project-for-appsmith](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/new-project.png)
  * Create a new table by clicking on the Create Table option on the side navigation.
  * Supabase provides many ways to add data to the tables, from writing queries to creating schemas using UI to simply uploading CSV files. For our support dashboard, we will be creating the **tickets** table by uploading the [CSV file](https://raw.githubusercontent.com/vihar/datasets/master/tickets.csv) on Supabase.


![create-table-for-appsmith](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/create-table.png)
The database is now set up.
## Step 2: Connect the database to Appsmith
  * Note down the database connection information under Project Settings in Supabase.


![connection-parameters-for-appsmith](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/connection-parameters.png)
  * On Appsmith, create a new application under the dashboard under your preferred organization.
  * Click on the `+` icon next to Datasources on the left navigation bar under Page1
  * Next, click on Create New tab and choose PostgreSQL datasource, you’ll see the following screenshot:


![create-datasource-appsmith-04](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/documentation/create-datasource-appsmith-04.png)
  * Fill out the form to connect to your Supabase instance. Click **Test** to test connection and then **Save** to save the datasource


![connect-supabase-datasource-05](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/documentation/connect-supabase-datasource-05.png)
## Step 3: Build UI on Appsmith
  * Click on the + icon next to widgets and drag and drop a Tab widget. We can configure using the property pane by clicking on the cog icon on the top-right corner.
  * As seen in the below screenshot, we have added four tabs to support the dashboard.


![property-pane-appsmith-06](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/documentation/property-pane-appsmith-06.png)
  * Add widgets to the **Home** tab to create the dashboard as shown in the screenshot below. For eg: **Critical Open Issues** is a **Text** widget and below it is an **Input** widget which we will bind later to display the number of open tickets.
  * Set up the **New** button to open a modal which will have a form to raise a new ticket.


![bind-query-appsmith-07](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/documentation/bind-query-appsmith-07.png)
  * In the modal widget, add a few widgets to accept input when creating a new ticket. Please refer to the screenshot below.


![modal-appsmith-08](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/documentation/modal-appsmith-08.png)
## Step 4: Writing Queries in Appsmith and binding data to widgets
  * Click on the + icon next to Datasources on the navigation bar and click New Query next to the Supabase connection here to create a new query.


![create-query-appsmith-09](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/appsmith/documentation/create-query-appsmith-09.png)
  * Rename the query to create_new_ticket under the query pane; here we can write SQL that can collect the data from the widgets using mustache templates.


`
1
INSERT INTO PUBLIC."tickets"("id","createdAt","user","updatedAt","description",
2
"status","priority","category","assignedTo")
3
VALUES('{{appsmith.store.ticket.id}}','{{moment().format('yyyy-mm-ddHH:MM:ss')}}','{{c_user.text}}',
4
'{{moment().format('yyyy-mm-ddHH:MM:ss')}}','{{c_description.text}}','{{c_status.selectedOptionValue}}',
5
'{{c_property.selectedOptionValue}}',
6
'{{c_category.selectedOptionValue}}','{{c_assignee.selectedOptionValue}}');
`
  * Click the **Confirm** button on the modal and under **Events** , set the **onClick** property to execute the create_new_ticket query.
  * Create a second query named **get_tickets** that will list all the tickets.


`
1
SELECT * FROM public."tickets";
`
  * Drag and drop a table widget under the **Assigned To Me** tab. Open the property pane and add the following snippet under **Table Data** to bind the query results.


`
1
{
2
 {
3
  get_tickets.data.filter(
4
   (t) => t.assignedTo === 'confidence@appsmith.com' && t.status !== 'closed'
5
  )
6
 }
7
}
`
  * Drag and drop a table widget under the **Resolved** tab. Open the property pane and add the following snippet under **Table Data** to bind the query results.


`
1
{
2
 {
3
  get_tickets.data.filter((t) => t.status === 'open')
4
 }
5
}
`
  * Drag and drop a table widget under the **Closed** tab. Open the property pane and add the following snippet under **Table Data** to bind the query results.


`
1
{
2
 {
3
  get_tickets.data.filter((t) => t.status === 'closed')
4
 }
5
}
`
## Step 5: Creating Charts in Appsmith
  * On the **Home** tab, click on the first Chart widget. Add Title **Open Issues By Category**. Change the **Chart Type** property to **Column Chart**.
  * Update the x-axis and y-axis Labels under **Axis** on the property pane.
  * Add the following code snippet under the **Series Data** property to bind the data to be displayed on the x and y axes.


`
1
[
2
 {
3
  "x": "Hardware",
4
  "y": {{get_tickets.data.filter(t => t.status==='open' && t.category==='hardware').length}}
5
 },
6
 {
7
  "x": "Software",
8
  "y": {{get_tickets.data.filter(t => t.status==='open' && t.category==='software').length}}
9
 },
10
 {
11
  "x": "Other",
12
  "y": {{get_tickets.data.filter(t => t.status==='open' && t.category==='other').length}}
13
 }
14
]
`
  * The second chart will be a pie chart. Add the title, axes labels as mentioned above,
  * Add the following code snippet under the **Series Data** property of the pie chart.


`
1
[
2
 {
3
  "x": "High",
4
  "y": {{get_tickets.data.filter(t => t.status==='open' && t.priority==='high').length}}
5
 },
6
 {
7
  "x": "Medium",
8
  "y": {{get_tickets.data.filter(t => t.status==='open' && t.priority==='medium').length}}
9
 },
10
 {
11
  "x": "Low",
12
  "y": {{get_tickets.data.filter(t => t.status==='open' && t.priority==='low').length}}
13
 }
14
]
`
## Resources
  * [Appsmith](https://www.appsmith.com/) official website.
  * [Appsmith GitHub](https://github.com/appsmithorg).
  * [Appsmith](https://docs.appsmith.com/) documentation.


## Details
Watch an introductory video
![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
DeveloperAppsmith
Category[Low-Code](https://supabase.com/partners/integrations#low-code)
Website[www.appsmith.com](https://www.appsmith.com/)
Documentation[Learn](https://www.appsmith.com/)
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

