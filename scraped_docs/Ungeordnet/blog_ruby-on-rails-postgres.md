---
url: https://supabase.com/blog/ruby-on-rails-postgres
scraped_at: 2025-05-25T08:52:21.687991
title: Getting started with Ruby on Rails and Postgres on Supabase
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
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Getting started with Ruby on Rails and Postgres on Supabase
29 Jan 2024
•
5 minute read
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Getting started with Ruby on Rails and Postgres on Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fgetting-started%2Frails%2Frails.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Every Supabase project comes with a full [Postgres](https://www.postgresql.org/) database, a free and open source database which is considered one of the world's most stable and advanced databases.
Postgres is an ideal choice for your Ruby on Rails applications as Rails ships with a built-in Postgres adapter!
In this post we'll start from scratch, creating a new Rails project, connecting it to our Supabase Postgres database, and interacting with the database using the Rails Console.
##### Need help migrating?
Supabase is one of the best [free alternatives to Heroku Postgres](https://supabase.com/alternatives/supabase-vs-heroku-postgres). See [this guide](https://supabase.com/docs/guides/resources/migrating-to-supabase/heroku) to learn how to migrate from Heroku to Supabase.
There's also a [Heroku to Supabase migration tool](https://migrate.supabase.com/) available to migrate in just a few clicks.
If you prefer video guide, you can follow along below. And make sure to subscribe to the [Supabase YouTube channel](https://www.youtube.com/channel/UCNTVzV1InxHV-YR0fSajqPQ?view_as=subscriber&sub_confirmation=1)!
## Create a Rails Project[#](https://supabase.com/blog/ruby-on-rails-postgres#create-a-rails-project)
Make sure your Ruby and Rails versions are up to date, then use `rails new` to scaffold a new Rails project. Use the `-d=postgresql` flag to set it up for Postgres.
Go to the [Rails docs](https://guides.rubyonrails.org/getting_started.html) for more details.
Terminal
`
1
rails new blog -d=postgresql
`
## Set up the Postgres connection details[#](https://supabase.com/blog/ruby-on-rails-postgres#set-up-the-postgres-connection-details)
Go to [database.new](https://database.new) and create a new Supabase project. Save your database password securely.
When your project is up and running, navigate to the [project connect page](https://supabase.com/dashboard/project/_?showConnect=true) to find the URI connection string.
Rails ships with a Postgres adapter included, you can simply configure it via the environment variables. You can find the database URL in your [Supabase Dashboard](https://supabase.com/dashboard/project/_/settings/database).
Terminal
`
1
export DATABASE_URL=postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
`
## Create and run a database migration[#](https://supabase.com/blog/ruby-on-rails-postgres#create-and-run-a-database-migration)
Rails includes Active Record as the ORM as well as database migration tooling which generates the SQL migration files for you.
Create an example `Article` model and generate the migration files.
Terminal
`
1
bin/rails generate scaffold Article title:string body:text
2
bin/rails db:migrate
`
## Use the Model to interact with the database[#](https://supabase.com/blog/ruby-on-rails-postgres#use-the-model-to-interact-with-the-database)
You can use the included Rails console to interact with the database. For example, you can create new entries or list all entries in a Model's table.
Terminal
`
1
bin/rails console
`
irb
`
1
article = Article.new(title: "Hello Rails", body: "I am on Rails!")
2
article.save # Saves the entry to the database
34
Article.all
`
## Start the app[#](https://supabase.com/blog/ruby-on-rails-postgres#start-the-app)
Terminal
`
1
bin/rails server
`
Run the development server. Go to <http://127.0.0.1:3000> in a browser to see your application running.
## Update the app to show articles[#](https://supabase.com/blog/ruby-on-rails-postgres#update-the-app-to-show-articles)
Currently the app shows a nice development splash screen, let's update this to show our articles from the database:
config/routes.rb
`
1
Rails.application.routes.draw do
2
 # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
34
 # Defines the root path route ("/")
5
 root "articles#index"
6
end
`
## Deploy to Fly.io[#](https://supabase.com/blog/ruby-on-rails-postgres#deploy-to-flyio)
In order to start working with Fly.io, you will need `flyctl`, our CLI app for managing apps. If you've already installed it, carry on. If not, hop over to the [installation guide](https://fly.io/docs/hands-on/install-flyctl/). Once that's installed you'll want to [log in to Fly](https://fly.io/docs/getting-started/log-in-to-fly/).
### Provision Rails with Fly.io[#](https://supabase.com/blog/ruby-on-rails-postgres#provision-rails-with-flyio)
To configure and launch the app, you can use `fly launch` and follow the wizard.
When asked "Do you want to tweak these settings before proceeding?" select `y` and set Postgres to `none` as we will be providing the Supabase database URL as a secret.
### Set the connection string as secret[#](https://supabase.com/blog/ruby-on-rails-postgres#set-the-connection-string-as-secret)
Use the Fly.io CLI to set the Supabase database connection URI from above as a sevret which is exposed as an environment variable to the Rails app.
Terminal
`
1
fly secrets set DATABASE_URL=$DATABASE_URL
`
### Deploy the app[#](https://supabase.com/blog/ruby-on-rails-postgres#deploy-the-app)
Deploying your application is done with the following command:
Terminal
`
1
fly deploy
`
This will take a few seconds as it uploads your application, builds a machine image, deploys the images, and then monitors to ensure it starts successfully. Once complete visit your app with the following command:
Terminal
`
1
fly apps open
`
That's it! You're Rails app is up and running with Supabase Postgres and Fly.io!
## Conclusion[#](https://supabase.com/blog/ruby-on-rails-postgres#conclusion)
Supabase is the ideal platform for powering your Postgres database for your Ruby on Rails applications! Every Supabase project comes with a full Postgres database and a good number of [useful extensions](https://supabase.com/docs/guides/database/extensions)!
Try it out now at [database.new](https://database.new)!
## More Supabase[#](https://supabase.com/blog/ruby-on-rails-postgres#more-supabase)
  * [Migration guides](https://supabase.com/docs/guides/resources#migrate-to-supabase)
  * [Options for connecting to your Postgres database](https://supabase.com/docs/guides/database/connecting-to-postgres)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fruby-on-rails-postgres&text=Getting%20started%20with%20Ruby%20on%20Rails%20and%20Postgres%20on%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fruby-on-rails-postgres&text=Getting%20started%20with%20Ruby%20on%20Rails%20and%20Postgres%20on%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fruby-on-rails-postgres&t=Getting%20started%20with%20Ruby%20on%20Rails%20and%20Postgres%20on%20Supabase)
[Last postpgvector 0.6.0: 30x faster with parallel index builds30 January 2024](https://supabase.com/blog/pgvector-fast-builds)
[Next postCreate a Figma Clone app with Flutter and Supabase Realtime26 January 2024](https://supabase.com/blog/flutter-figma-clone)
[postgres](https://supabase.com/blog/tags/postgres)[developers](https://supabase.com/blog/tags/developers)[ruby](https://supabase.com/blog/tags/ruby)
On this page
  * [Create a Rails Project](https://supabase.com/blog/ruby-on-rails-postgres#create-a-rails-project)
  * [Set up the Postgres connection details](https://supabase.com/blog/ruby-on-rails-postgres#set-up-the-postgres-connection-details)
  * [Create and run a database migration](https://supabase.com/blog/ruby-on-rails-postgres#create-and-run-a-database-migration)
  * [Use the Model to interact with the database](https://supabase.com/blog/ruby-on-rails-postgres#use-the-model-to-interact-with-the-database)
  * [Start the app](https://supabase.com/blog/ruby-on-rails-postgres#start-the-app)
  * [Update the app to show articles](https://supabase.com/blog/ruby-on-rails-postgres#update-the-app-to-show-articles)
  * [Deploy to Fly.io](https://supabase.com/blog/ruby-on-rails-postgres#deploy-to-flyio)
    * [Provision Rails with Fly.io](https://supabase.com/blog/ruby-on-rails-postgres#provision-rails-with-flyio)
    * [Set the connection string as secret](https://supabase.com/blog/ruby-on-rails-postgres#set-the-connection-string-as-secret)
    * [Deploy the app](https://supabase.com/blog/ruby-on-rails-postgres#deploy-the-app)
  * [Conclusion](https://supabase.com/blog/ruby-on-rails-postgres#conclusion)
  * [More Supabase](https://supabase.com/blog/ruby-on-rails-postgres#more-supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fruby-on-rails-postgres&text=Getting%20started%20with%20Ruby%20on%20Rails%20and%20Postgres%20on%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fruby-on-rails-postgres&text=Getting%20started%20with%20Ruby%20on%20Rails%20and%20Postgres%20on%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fruby-on-rails-postgres&t=Getting%20started%20with%20Ruby%20on%20Rails%20and%20Postgres%20on%20Supabase)
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

