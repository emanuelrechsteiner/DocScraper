---
url: https://supabase.com/docs/guides/local-development/seeding-your-database
scraped_at: 2025-05-25T09:25:42.334717
title: Seeding your database | Supabase Docs
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
[Local Dev / CLI](https://supabase.com/docs/guides/local-development)
  * [Overview](https://supabase.com/docs/guides/local-development)
CLI
  * [Getting started](https://supabase.com/docs/guides/local-development/cli/getting-started)
  * [Configuration](https://supabase.com/docs/guides/local-development/cli/config)
  * [CLI commands](https://supabase.com/docs/reference/cli)
Local development
  * [Getting started](https://supabase.com/docs/guides/local-development/overview)
  * [Declarative database schemas](https://supabase.com/docs/guides/local-development/declarative-database-schemas)
  * [Seeding your database](https://supabase.com/docs/guides/local-development/seeding-your-database)
  * [Managing config and secrets](https://supabase.com/docs/guides/local-development/managing-config)
  * [Restoring downloaded backup](https://supabase.com/docs/guides/local-development/restoring-downloaded-backup)
  * [Customizing email templates](https://supabase.com/docs/guides/local-development/customizing-email-templates)
Testing
  * [Getting started](https://supabase.com/docs/guides/local-development/testing/overview)
  * [pgTAP advanced guide](https://supabase.com/docs/guides/local-development/testing/pgtap-extended)
  * [Database testing](https://supabase.com/docs/guides/database/testing)
  * [RLS policies testing](https://supabase.com/docs/guides/database/extensions/pgtap#testing-rls-policies)


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
Local Development
  1. [Local Dev / CLI](https://supabase.com/docs/guides/local-development)
  2. Local development
  3. [Seeding your database](https://supabase.com/docs/guides/local-development/seeding-your-database)


Seeding your database
Populate your database with initial data for reproducible environments across local and testing.
## What is seed data?[#](https://supabase.com/docs/guides/local-development/seeding-your-database#what-is-seed-data)
Seeding is the process of populating a database with initial data, typically used to provide sample or default records for testing and development purposes. You can use this to create "reproducible environments" for local development, staging, and production.
## Using seed files[#](https://supabase.com/docs/guides/local-development/seeding-your-database#using-seed-files)
Seed files are executed every time you run `supabase start` or `supabase db reset`. Seeding occurs _after_ all database migrations have been completed. As a best practice, only include data insertions in your seed files, and avoid adding schema statements.
By default, if no specific configuration is provided, the system will look for a seed file matching the pattern `supabase/seed.sql`. This maintains backward compatibility with earlier versions, where the seed file was placed in the `supabase` folder.
You can add any SQL statements to this file. For example:
```

1
2
3
4
5
6
insert into countries (name, code)values ('United States', 'US'), ('Canada', 'CA'), ('Mexico', 'MX');

```

If you want to manage multiple seed files or organize them across different folders, you can configure additional paths or glob patterns in your `config.toml` (see the [next section](https://supabase.com/docs/guides/local-development/seeding-your-database#splitting-up-your-seed-file) for details).
### Splitting up your seed file[#](https://supabase.com/docs/guides/local-development/seeding-your-database#splitting-up-your-seed-file)
For better modularity and maintainability, you can split your seed data into multiple files. For example, you can organize your seeds by table and include files such as `countries.sql` and `cities.sql`. Configure them in `config.toml` like so:
```

1
2
3
[db.seed]enabled=truesql_paths=['./countries.sql','./cities.sql']

```

Or to include all `.sql` files under a specific folder you can do:
```

1
2
3
[db.seed]enabled=truesql_paths=['./seeds/*.sql']

```

The CLI processes seed files in the order they are declared in the `sql_paths` array. If a glob pattern is used and matches multiple files, those files are sorted in lexicographic order to ensure consistent execution. Additionally:
  * The base folder for the pattern matching is `supabase` so `./countries.sql` will search for `supabase/countries.sql`
  * Files matched by multiple patterns will be deduplicated to prevent redundant seeding.
  * If a pattern does not match any files, a warning will be logged to help you troubleshoot potential configuration issues.


## Generating seed data[#](https://supabase.com/docs/guides/local-development/seeding-your-database#generating-seed-data)
You can generate seed data for local development using [Snaplet](https://github.com/snaplet/seed).
To use Snaplet, you need to have Node.js and npm installed. You can add Node.js to your project by running `npm init -y` in your project directory.
If this is your first time using Snaplet to seed your project, you'll need to set up Snaplet with the following command:
```

1
npx@snaplet/seedinit

```

This command will analyze your database and its structure, and then generate a JavaScript client which can be used to define exactly how your data should be generated using code. The `init` command generates a configuration file, `seed.config.ts` and an example script, `seed.ts`, as a starting point.
During `init` if you are not using an Object Relational Mapper (ORM) or your ORM is not in the supported list, choose `node-postgres`.
In most cases you only want to generate data for specific schemas or tables. This is defined with `select`. Here is an example `seed.config.ts` configuration file:
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
exportdefaultdefineConfig({adapter:async()=>{constclient=newClient({connectionString:'postgresql://postgres:postgres@localhost:54322/postgres',})awaitclient.connect()returnnewSeedPg(client)},// We only want to generate data for the public schemaselect:['!*','public.*'],})

```

Suppose you have a database with the following schema:
![An example schema](https://supabase.com/docs/img/guides/cli/snaplet-example-schema.png)
You can use the seed script example generated by Snaplet `seed.ts` to define the values you want to generate. For example:
  * A `Post` with the title `"There is a lot of snow around here!"`
  * The `Post.createdBy` user with an email address ending in `"@acme.org"`
  * Three `Post.comments` from three different users.


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
import{createSeedClient}from'@snaplet/seed'import{copycat}from'@snaplet/copycat'asyncfunctionmain(){constseed=awaitcreateSeedClient({dryRun:true})awaitseed.Post([{title:'There is a lot of snow around here!',createdBy:{email:(ctx)=>copycat.email(ctx.seed,{domain:'acme.org',}),},Comment:(x)=>x(3),},])process.exit()}main()

```

Running `npx tsx seed.ts > supabase/seed.sql` generates the relevant SQL statements inside your `supabase/seed.sql` file:
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
-- The `Post.createdBy` user with an email address ending in `"@acme.org"`INSERT INTO"User" (name, email) VALUES ("John Snow", "snow@acme.org")--- A `Post` with the title `"There is a lot of snow around here!"`INSERT INTO"Post" (title, content, createdBy) VALUES ("There is a lot of snow around here!","Lorem ipsum dolar",1)--- Three `Post.Comment` from three different users.INSERT INTO"User" (name, email) VALUES ("Stephanie Shadow", "shadow@domain.com")INSERT INTO"Comment" (text, userId, postId) VALUES ("I love cheese", 2, 1)INSERT INTO"User" (name, email) VALUES ("John Rambo", "rambo@trymore.dev")INSERT INTO"Comment" (text, userId, postId) VALUES ("Lorem ipsum dolar sit", 3, 1)INSERT INTO"User" (name, email) VALUES ("Steven Plank", "s@plank.org")INSERT INTO"Comment" (text, userId, postId) VALUES ("Actually, that's not correct...", 4, 1)

```

Whenever your database structure changes, you will need to regenerate `@snaplet/seed` to keep it in sync with the new structure. You can do this by running:
```

1
npx@snaplet/seedsync

```

You can further enhance your seed script by using Large Language Models to generate more realistic data. To enable this feature, set one of the following environment variables in your `.env` file:
```

1
2
OPENAI_API_KEY=<your_openai_api_key>GROQ_API_KEY=<your_groq_api_key>

```

After setting the environment variables, run the following commands to sync and generate the seed data:
```

1
2
npx@snaplet/seedsyncnpxtsxseed.ts>supabase/seed.sql

```

For more information, check out Snaplet's [seed documentation](https://snaplet-seed.netlify.app/seed/integrations/supabase)
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/local-development/seeding-your-database.mdx)
### Is this helpful?
No Yes
### On this page
[What is seed data?](https://supabase.com/docs/guides/local-development/seeding-your-database#what-is-seed-data)[Using seed files](https://supabase.com/docs/guides/local-development/seeding-your-database#using-seed-files)[Splitting up your seed file](https://supabase.com/docs/guides/local-development/seeding-your-database#splitting-up-your-seed-file)[Generating seed data](https://supabase.com/docs/guides/local-development/seeding-your-database#generating-seed-data)
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



