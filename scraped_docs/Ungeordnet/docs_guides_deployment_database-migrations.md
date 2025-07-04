---
url: https://supabase.com/docs/guides/deployment/database-migrations
scraped_at: 2025-05-25T09:14:44.953575
title: Database Migrations | Supabase Docs
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
[Deployment](https://supabase.com/docs/guides/deployment)
  * [Overview](https://supabase.com/docs/guides/deployment)
Environments
  * [Managing environments](https://supabase.com/docs/guides/deployment/managing-environments)
  * [Database migrations](https://supabase.com/docs/guides/deployment/database-migrations)
  * [Branching](https://supabase.com/docs/guides/deployment/branching)
Terraform
  * [Terraform provider](https://supabase.com/docs/guides/deployment/terraform)
  * [Terraform tutorial](https://supabase.com/docs/guides/deployment/terraform/tutorial)
  * [Terraform reference](https://supabase.com/docs/guides/deployment/terraform/reference)
Production readiness
  * [Shared responsibility model](https://supabase.com/docs/guides/deployment/shared-responsibility-model)
  * [Maturity model](https://supabase.com/docs/guides/deployment/maturity-model)
  * [Production checklist](https://supabase.com/docs/guides/deployment/going-into-prod)
  * [SOC 2 compliance](https://supabase.com/docs/guides/security/soc-2-compliance)
CI/CD
  * [Generate types from your database](https://supabase.com/docs/guides/deployment/ci/generating-types)
  * [Automated testing](https://supabase.com/docs/guides/deployment/ci/testing)
  * [Back up your database](https://supabase.com/docs/guides/deployment/ci/backups)


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
Home
  1. [Deployment](https://supabase.com/docs/guides/deployment)
  2. Environments
  3. [Database migrations](https://supabase.com/docs/guides/deployment/database-migrations)


Database Migrations
How to manage schema migrations for your Supabase project.
Database migrations are SQL statements that create, update, or delete your existing database schemas. They are a common way of tracking changes to your database over time.
## Schema migrations[#](https://supabase.com/docs/guides/deployment/database-migrations#schema-migrations)
For this guide, we'll create a table called `employees` and see how we can make changes to it.
You will need to [install](https://supabase.com/docs/guides/local-development#quickstart) the Supabase CLI and start the local development stack.
1
### Create your first migration file
To get started, generate a [new migration](https://supabase.com/docs/reference/cli/supabase-migration-new) to store the SQL needed to create our `employees` table.
###### Terminal
```

1
supabasemigrationnewcreate_employees_table

```

2
### Add the SQL to your migration file
This creates a new migration file in supabase/migrations directory.
To that file, add the SQL to create this `employees` table.
###### supabase/migrations/<timestamp>_create_employees_table.sql
```

1
2
3
4
5
6
createtableifnotexists employees ( id bigintprimary keygeneratedalwaysasidentity,nametextnot null, email text, created_at timestamptzdefaultnow());

```

3
### Apply your first migration
Run this migration to create the `employees` table.
Now you can visit your new `employees` table in the local Dashboard.
###### Terminal
```

1
supabasemigrationup

```

4
### Modify your employees table
Next, modify your `employees` table by adding a column for `department`.
###### Terminal
```

1
supabasemigrationnewadd_department_column

```

5
### Add a new column to your table
To that new migration file, add the SQL to create a new `department` column.
###### supabase/migrations/<timestamp>_add_department_column.sql
```

1
2
altertableifexistspublic.employeesadd department textdefault'Hooli';

```

6
### Apply your second migration
Run this migration to update your existing `employees` table.
###### Terminal
```

1
supabasemigrationup

```

Finally, you should see the `department` column added to your `employees` table in the local Dashboard.
View the [complete code](https://github.com/supabase/supabase/tree/master/examples/database/employees) for this example on GitHub.
### Seeding data[#](https://supabase.com/docs/guides/deployment/database-migrations#seeding-data)
Now that you are managing your database with migrations scripts, it would be great have some seed data to use every time you reset the database.
1
### Populate your table
Create a seed script in supabase/seed.sql.
To that file, add the SQL to insert data into your `employees` table.
###### supabase/seed.sql
```

1
2
3
4
5
6
insert intopublic.employees (name)values ('Erlich Bachman'), ('Richard Hendricks'), ('Monica Hall');

```

2
### Reset your database
Reset your database to reapply migrations and populate with seed data.
###### Terminal
```

1
supabasedbreset

```

You should now see the `employees` table, along with your seed data in the Dashboard! All of your database changes are captured in code, and you can reset to a known state at any time, complete with seed data.
### Diffing changes[#](https://supabase.com/docs/guides/deployment/database-migrations#diffing-changes)
This workflow is great if you know SQL and are comfortable creating tables and columns. If not, you can still use the Dashboard to create tables and columns, and then use the CLI to diff your changes and create migrations.
1
### Create your table from the Dashboard
Create a new table called `cities`, with columns `id`, `name` and `population`.
Then generate a [schema diff](https://supabase.com/docs/reference/cli/supabase-db-diff).
###### Terminal
```

1
supabasedbdiff-fcreate_cities_table

```

2
### Add schema diff as a migration
A new migration file is created for you.
Alternately, you can copy the table definitions directly from the Table Editor.
###### supabase/migrations/<timestamp>_create_cities_table.sql
```

1
2
3
4
5
createtable "public"."cities" ("id"bigintprimary keygeneratedalwaysasidentity,"name"text,"population"bigint);

```

3
### Test your migration
Test your new migration file by resetting your local database.
###### Terminal
```

1
supabasedbreset

```

The last step is deploying these changes to a live Supabase project.
## Deploy your project[#](https://supabase.com/docs/guides/deployment/database-migrations#deploy-your-project)
You've been developing your project locally, making changes to your tables via migrations. It's time to deploy your project to the Supabase Platform and start scaling up to millions of users!
Head over to [Supabase](https://supabase.com/dashboard) and create a new project to deploy to.
1
### Log in to the Supabase CLI
[Login](https://supabase.com/docs/reference/cli/supabase-login) to the Supabase CLI using an auto-generated Personal Access Token.
###### Terminal
```

1
supabaselogin

```

2
### Link your project
[Link](https://supabase.com/docs/reference/cli/supabase-link) to your remote project by selecting from the on-screen prompt.
###### Terminal
```

1
supabaselink

```

3
### Deploy database migrations
[Push](https://supabase.com/docs/reference/cli/supabase-db-push) your migrations to the remote database.
###### Terminal
```

1
supabasedbpush

```

4
### Deploy database seed data (optional)
[Push](https://supabase.com/docs/reference/cli/supabase-db-push) your migrations and seed the remote database.
###### Terminal
```

1
supabasedbpush--include-seed

```

Visiting your live project on [Supabase](https://supabase.com/dashboard/project/_), you'll see a new `employees` table, complete with the `department` column you added in the second migration above.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/deployment/database-migrations.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FKx5nHBmIxyQ%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Schema migrations](https://supabase.com/docs/guides/deployment/database-migrations#schema-migrations)[Seeding data](https://supabase.com/docs/guides/deployment/database-migrations#seeding-data)[Diffing changes](https://supabase.com/docs/guides/deployment/database-migrations#diffing-changes)[Deploy your project](https://supabase.com/docs/guides/deployment/database-migrations#deploy-your-project)
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



