---
url: https://supabase.com/docs/guides/local-development/declarative-database-schemas
scraped_at: 2025-05-25T09:46:15.337509
title: Declarative database schemas | Supabase Docs
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
  3. [Declarative database schemas](https://supabase.com/docs/guides/local-development/declarative-database-schemas)


Declarative database schemas
Manage your database schemas in one place and generate versioned migrations.
## Overview[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#overview)
Declarative schemas provide a developer-friendly way to maintain schema migrations.
[Migrations](https://supabase.com/docs/guides/deployment/database-migrations) are traditionally managed imperatively (you provide the instructions on how exactly to change the database). This can lead to related information being scattered over multiple migration files. With declarative schemas, you instead declare the state you want your database to be in, and the instructions are generated for you.
## Schema migrations[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#schema-migrations)
Schema migrations are SQL statements written in Data Definition Language. They are versioned in your `supabase/migrations` directory to ensure schema consistency between local and remote environments.
### Declaring your schema[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#declaring-your-schema)
1
### Create your first schema file
Create a SQL file in `supabase/schemas` directory that defines an `employees` table.
supabase/schemas/employees.sql
```

1
2
3
4
createtable "employees" ("id"integernot null,"name"text);

```

Make sure your local database is stopped before diffing your schema.
2
### Generate a migration file
Generate a migration file by diffing against your declared schema.
Terminal
```

1
supabasedbdiff-fcreate_employees_table

```

3
### Start the local database and apply migrations
Start the local database and then apply the migration file to see your schema changes in the local Dashboard.
Terminal
```

1
supabasestart&&supabasemigrationup

```

### Updating your schema[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#updating-your-schema)
1
### Stop the local database
Before updating your schema files, stop the local development environment.
Terminal
```

1
supabasestop

```

2
### Add a new column
Edit `supabase/schemas/employees.sql` file to add a new column to `employees` table.
supabase/schemas/employees.sql
```

1
2
3
4
5
createtable "employees" ("id"integernot null,"name"text,"age"smallintnot null);

```

Some entities like views and enums expect columns to be declared in a specific order. To avoid messy diffs, always append new columns to the end of the table.
3
### Generate a new migration
Diff existing migrations against your declared schema.
Terminal
```

1
supabasedbdiff-fadd_age

```

4
### Review the generated migration
Verify that the generated migration contain a single incremental change.
supabase/migrations/<timestamp>_add_age.sql
```

1
altertable"public"."employees"add column "age"smallintnot null;

```

5
### Apply the pending migration
Start the database locally and apply the pending migration.
Terminal
```

1
supabasestart&&supabasemigrationup

```

### Deploying your schema changes[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#deploying-your-schema-changes)
1
### Log in to the Supabase CLI
[Log in](https://supabase.com/docs/reference/cli/supabase-login) via the Supabase CLI.
Terminal
```

1
supabaselogin

```

2
### Link your remote project
Follow the on-screen prompts to [link](https://supabase.com/docs/reference/cli/supabase-link) your remote project.
Terminal
```

1
supabaselink

```

3
### Deploy database changes
[Push](https://supabase.com/docs/reference/cli/supabase-db-push) your changes to the remote database.
Terminal
```

1
supabasedbpush

```

### Managing dependencies[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#managing-dependencies)
As your database schema evolves, you will probably start using more advanced entities like views and functions. These entities are notoriously verbose to manage using plain migrations because the entire body must be recreated whenever there is a change. Using declarative schema, you can now edit them in-place so it’s much easier to review.
supabase/schemas/employees.sql
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
createtable "employees" ("id"integernot null,"name"text,"age"smallintnot null);createview "profiles" asselect id, namefrom"employees";createfunction "get_age"(employee_id integer) RETURNSsmallintLANGUAGE"sql"AS $$select agefrom employeeswhere id = employee_id;$$;

```

Your schema files are run in lexicographic order by default. The order is important when you have foreign keys between multiple tables as the parent table must be created first. For example, your `supabase` directory may end up with the following structure.
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
.└──supabase/├──schemas/│├──employees.sql│└──managers.sql└──migrations/├──20241004112233_create_employees_table.sql├──20241005112233_add_employee_age.sql└──20241006112233_add_managers_table.sql

```

For small projects with only a few tables, the default schema order may be sufficient. However, as your project grows, you might need more control over the order in which schemas are applied. To specify a custom order for applying the schemas, you can declare them explicitly in `config.toml`. Any glob patterns will evaluated, deduplicated, and sorted in lexicographic order. For example, the following pattern ensures `employees.sql` is always executed first.
supabase/config.toml
```

1
2
3
4
5
[db.migrations]schema_paths=["./schemas/employees.sql","./schemas/*.sql",]

```

### Pulling in your production schema[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#pulling-in-your-production-schema)
To set up declarative schemas on a existing project, you can pull in your production schema by running:
Terminal
```

1
supabasedbdump>supabase/schemas/prod.sql

```

From there, you can start breaking down your schema into smaller files and generate migrations. You can do this all at once, or incrementally as you make changes to your schema.
### Rolling back a schema change[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#rolling-back-a-schema-change)
During development, you may want to rollback a migration to keep your new schema changes in a single migration file. This can be done by resetting your local database to a previous version.
Terminal
```

1
supabasedbreset--version20241005112233

```

After a reset, you can [edit the schema](https://supabase.com/docs/guides/local-development/declarative-database-schemas#updating-your-schema) and regenerate a new migration file. Note that you should not reset a version that's already deployed to production.
If you need to rollback a migration that's already deployed, you should first revert changes to the schema files. Then you can generate a new migration file containing the down migration. This ensures your production migrations are always rolling forward.
SQL statements generated in a down migration are usually destructive. You must review them carefully to avoid unintentional data loss.
## Known caveats[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#known-caveats)
The `migra` diff tool used for generating schema diff is capable of tracking most database changes. However, there are edge cases where it can fail.
If you need to use any of the entities below, remember to add them through [versioned migrations](https://supabase.com/docs/guides/deployment/database-migrations) instead.
### Data manipulation language[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#data-manipulation-language)
  * DML statements such as `insert`, `update`, `delete`, etc., are not captured by schema diff


### View ownership[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#view-ownership)
  * [view owner and grants](https://github.com/djrobstep/migra/issues/160#issuecomment-1702983833)
  * [security invoker on views](https://github.com/djrobstep/migra/issues/234)
  * [materialized views](https://github.com/djrobstep/migra/issues/194)
  * doesn’t recreate views when altering column type


### RLS policies[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#rls-policies)
  * [alter policy statements](https://github.com/djrobstep/schemainspect/blob/master/schemainspect/pg/obj.py#L228)
  * [column privileges](https://github.com/djrobstep/schemainspect/pull/67)


### Other entities[#](https://supabase.com/docs/guides/local-development/declarative-database-schemas#other-entities)
  * schema privileges are not tracked because each schema is diffed separately
  * [comments are not tracked](https://github.com/djrobstep/migra/issues/69)
  * [partitions are not tracked](https://github.com/djrobstep/migra/issues/186)
  * [`alter publication ... add table ...`](https://github.com/supabase/cli/issues/883)
  * [create domain statements are ignored](https://github.com/supabase/cli/issues/2137)
  * [grant statements are duplicated from default privileges](https://github.com/supabase/cli/issues/1864)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/local-development/declarative-database-schemas.mdx)
### Is this helpful?
No Yes
### On this page
[Overview](https://supabase.com/docs/guides/local-development/declarative-database-schemas#overview)[Schema migrations](https://supabase.com/docs/guides/local-development/declarative-database-schemas#schema-migrations)[Declaring your schema](https://supabase.com/docs/guides/local-development/declarative-database-schemas#declaring-your-schema)[Updating your schema](https://supabase.com/docs/guides/local-development/declarative-database-schemas#updating-your-schema)[Deploying your schema changes](https://supabase.com/docs/guides/local-development/declarative-database-schemas#deploying-your-schema-changes)[Managing dependencies](https://supabase.com/docs/guides/local-development/declarative-database-schemas#managing-dependencies)[Pulling in your production schema](https://supabase.com/docs/guides/local-development/declarative-database-schemas#pulling-in-your-production-schema)[Rolling back a schema change](https://supabase.com/docs/guides/local-development/declarative-database-schemas#rolling-back-a-schema-change)[Known caveats](https://supabase.com/docs/guides/local-development/declarative-database-schemas#known-caveats)[Data manipulation language](https://supabase.com/docs/guides/local-development/declarative-database-schemas#data-manipulation-language)[View ownership](https://supabase.com/docs/guides/local-development/declarative-database-schemas#view-ownership)[RLS policies](https://supabase.com/docs/guides/local-development/declarative-database-schemas#rls-policies)[Other entities](https://supabase.com/docs/guides/local-development/declarative-database-schemas#other-entities)
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



