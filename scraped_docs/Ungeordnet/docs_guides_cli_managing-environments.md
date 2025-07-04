---
url: https://supabase.com/docs/guides/cli/managing-environments
scraped_at: 2025-05-25T08:41:36.560926
title: Managing Environments | Supabase Docs
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
  3. [Managing environments](https://supabase.com/docs/guides/deployment/managing-environments)


Managing Environments
Manage multiple environments using Database Migrations and GitHub Actions.
This guide shows you how to set up your local Supabase development environment that integrates with GitHub Actions to automatically test and release schema changes to staging and production Supabase projects.
![Diagram showing a possible environment setup for Supabase development. There are 3 branches and 3 corresponding databases: feature branch and local database, develop branch and staging database, and main branch and production database.](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Flocal-dev-environment--light.svg&w=3840&q=75)
## Set up a local environment[#](https://supabase.com/docs/guides/deployment/managing-environments#set-up-a-local-environment)
The first step is to set up your local repository with the Supabase CLI:
```

1
supabaseinit

```

You should see a new `supabase` directory. Then you need to link your local repository with your Supabase project:
```

1
2
supabaseloginsupabaselink--project-ref$PROJECT_ID

```

You can get your `$PROJECT_ID` from your project's dashboard URL:
```

1
https://supabase.com/dashboard/project/<project-id>

```

If you're using an existing Supabase project, you might have made schema changes through the Dashboard. Run the following command to pull these changes before making local schema changes from the CLI:
```

1
supabase db pull

```

This command creates a new migration in `supabase/migrations/<timestamp>_remote_schema.sql` which reflects the schema changes you have made previously.
Now commit your local changes to Git and run the local development setup:
```

1
2
3
gitadd.gitcommit-m"init supabase"supabasestart

```

You are now ready to develop schema changes locally and create your first migration.
## Create a new migration[#](https://supabase.com/docs/guides/deployment/managing-environments#create-a-new-migration)
There are two ways to make schema changes:
  1. Manual migration: Write DDL statements manually into a migration file
  2. Auto schema diff: Make changes through Studio UI and auto generate a schema diff


### Manual migration[#](https://supabase.com/docs/guides/deployment/managing-environments#manual-migration)
Create a new migration script by running:
```

1
supabasemigrationnewnew_employee

```

You should see a new file created: `supabase/migrations/<timestamp>_new_employee.sql`. You can then write SQL statements in this script using a text editor:
```

1
2
3
4
createtablepublic.employees ( id integerprimary keygeneratedalwaysasidentity,nametext);

```

Apply the new migration to your local database:
```

1
supabasedbreset

```

This command recreates your local database from scratch and applies all migration scripts under `supabase/migrations` directory. Now your local database is up to date.
The new migration command also supports stdin as input. This allows you to pipe in an existing script from another file or stdout:
`supabase migration new new_employee < create_employees_table.sql`
### Auto schema diff[#](https://supabase.com/docs/guides/deployment/managing-environments#auto-schema-diff)
Unlike manual migrations, auto schema diff creates a new migration script from changes **already** applied to your local database.
Create an `employees` table under the `public` schema using Studio UI, accessible at [localhost:54323](http://localhost:54323/) by default.
Next, generate a schema diff by running the following command:
```

1
supabasedbdiff-fnew_employee

```

You should see that a new file `supabase/migrations/<timestamp>_new_employee.sql` is created. Open the file and verify that the generated DDL statements are the same as below.
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
24
-- This script was generated by the Schema Diff utility in pgAdmin 4-- For the circular dependencies, the order in which Schema Diff writes the objects is not very sophisticated-- and may require manual changes to the script to ensure changes are applied in the correct order.-- Please report an issue for any failure with the reproduction steps.CREATETABLEIFNOTEXISTSpublic.employees(  id integerNOT NULLGENERATEDALWAYSASIDENTITY ( INCREMENT 1START1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),nametextCOLLATE pg_catalog."default",CONSTRAINT employees_pkey PRIMARY KEY (id))TABLESPACE pg_default;ALTERTABLEIFEXISTSpublic.employeesOWNERto postgres;GRANT ALL ONTABLEpublic.employeesTO anon;GRANT ALL ONTABLEpublic.employeesTO authenticated;GRANT ALL ONTABLEpublic.employeesTO postgres;GRANT ALL ONTABLEpublic.employeesTO service_role;

```

You may notice that the auto-generated migration script is more verbose than the manually written one. This is because the default schema diff tool does not account for default privileges added by the initial schema.
Commit the new migration script to git and you are ready to deploy.
Alternatively, you may pass in the `--use-migra` experimental flag to generate a more concise migration using [`migra`](https://github.com/djrobstep/migra).
Without the `-f` file flag, the output is written to stdout by default.
`supabase db diff --use-migra`
## Deploy a migration[#](https://supabase.com/docs/guides/deployment/managing-environments#deploy-a-migration)
In a production environment, we recommend using a CI/CD pipeline to deploy new migrations with GitHub Actions rather than deploying from your local machine.
![Diagram showing a possible environment setup for Supabase development. There are 3 branches and 3 corresponding databases: feature branch and local database, develop branch and staging database, and main branch and production database.](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Flocal-dev-environment--light.svg&w=3840&q=75)
This example uses two Supabase projects, one for production and one for staging.
Prepare your environments by:
  * Creating separate Supabase projects for staging and production
  * Pushing your git repository to GitHub and enabling GitHub Actions


You need a _new_ project for staging. A project which has already been modified to reflect the production project's schema can't be used because the CLI would reapply these changes.
### Configure GitHub Actions[#](https://supabase.com/docs/guides/deployment/managing-environments#configure-github-actions)
The Supabase CLI requires a few environment variables to run in non-interactive mode.
  * `SUPABASE_ACCESS_TOKEN` is your personal access token
  * `SUPABASE_DB_PASSWORD` is your project specific database password
  * `SUPABASE_PROJECT_ID` is your project specific reference string


We recommend adding these as [encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to your GitHub Actions runners.
Create the following files inside the `.github/workflows` directory:
ci.yamlstaging.yamlproduction.yaml
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
24
25
26
27
28
name:CIon:pull_request:workflow_dispatch:jobs:test:runs-on:ubuntu-lateststeps:-uses:actions/checkout@v4-uses:supabase/setup-cli@v1with:version:latest-name:Start Supabase local development setuprun:supabase db start-name:Verify generated types are checked inrun:|     supabase gen types typescript --local > types.gen.ts     if ! git diff --ignore-space-at-eol --exit-code --quiet types.gen.ts; then      echo "Detected uncommitted changes after build. See status below:"      git diff      exit 1     fi

```

The full example code is available in the [demo repository](https://github.com/supabase/supabase-action-example).
Commit these files to git and push to your `main` branch on GitHub. Update these environment variables to match your Supabase projects:
  * `SUPABASE_ACCESS_TOKEN`
  * `PRODUCTION_PROJECT_ID`
  * `PRODUCTION_DB_PASSWORD`
  * `STAGING_PROJECT_ID`
  * `STAGING_DB_PASSWORD`


When configured correctly, your repository will have CI and Release workflows that trigger on new commits pushed to `main` and `develop` branches.
![Correctly configured repo](https://supabase.com/docs/img/guides/cli/ci-main.png)
### Open a PR with new migration[#](https://supabase.com/docs/guides/deployment/managing-environments#open-a-pr-with-new-migration)
Follow the [migration steps](https://supabase.com/docs/guides/deployment/managing-environments#create-a-new-migration) to create a `supabase/migrations/<timestamp>_new_employee.sql` file.
Checkout a new branch `feat/employee` from `develop` , commit the migration file, and push to GitHub.
```

1
2
3
4
gitcheckout-bfeat/employeegitaddsupabase/migrations/<timestamp>_new_employee.sqlgitcommit-m"Add employee table"gitpush--set-upstreamoriginfeat/employee

```

Open a PR from `feat/employee` to the `develop` branch to see that the CI workflow has been triggered.
Once the test error is resolved, merge this PR and watch the deployment in action.
### Release to production[#](https://supabase.com/docs/guides/deployment/managing-environments#release-to-production)
After verifying your staging project has successfully migrated, create another PR from `develop` to `main` and merge it to deploy the migration to the production project.
The `release` job applies all new migration scripts merged in `supabase/migrations` directory to a linked Supabase project. You can control which project the job links to via `PROJECT_ID` environment variable.
## Troubleshooting[#](https://supabase.com/docs/guides/deployment/managing-environments#troubleshooting)
### Sync production project to staging[#](https://supabase.com/docs/guides/deployment/managing-environments#sync-production-project-to-staging)
When setting up a new staging project, you might need to sync the initial schema with migrations previously applied to the production project.
One way is to leverage the Release workflow:
  * Create a new branch `develop` and choose `main` as the branch source
  * Push the `develop` branch to GitHub


The GitHub Actions runner will deploy your existing migrations to the staging project.
Alternatively, you can also apply migrations through your local CLI to a linked remote database.
```

1
supabase db push

```

Once pushed, check that the migration version is up to date for both local and remote databases.
```

1
supabase migration list

```

### Permission denied on `db pull`[#](https://supabase.com/docs/guides/deployment/managing-environments#permission-denied-on-db-pull)
If you have been using Supabase hosted projects for a long time, you might encounter the following permission error when executing `db pull`.
```

1
2
3
Error:Errorrunningpg_dumponremotedatabase:pg_dump:error:queryfailed:ERROR:permissiondeniedfortable_typepg_dump:error:querywas:LOCKTABLE"graphql"."_type"INACCESSSHAREMODE

```

To resolve this error, you need to grant `postgres` role permissions to `graphql` schema. You can do that by running the following query from Supabase dashboard's SQL Editor.
```

1
2
3
grant all on all tables inschema graphql to postgres, anon, authenticated, service_role;grant all on all functions inschema graphql to postgres, anon, authenticated, service_role;grant all on all sequences inschema graphql to postgres, anon, authenticated, service_role;

```

### Permission denied on `db push`[#](https://supabase.com/docs/guides/deployment/managing-environments#permission-denied-on-db-push)
If you created a table through Supabase dashboard, and your new migration script contains `ALTER TABLE` statements, you might run into permission error when applying them on staging or production databases.
```

1
ERROR:mustbeowneroftableemployees (SQLSTATE 42501);whileexecutingmigration<timestamp>

```

This is because tables created through Supabase dashboard are owned by `supabase_admin` role while the migration scripts executed through CLI are under `postgres` role.
One way to solve this is to reassign the owner of those tables to `postgres` role. For example, if your table is named `users` in the public schema, you can run the following command to reassign owner.
```

1
ALTERTABLE users OWNERTO postgres;

```

Apart from tables, you also need to reassign owner of other entities using their respective commands, including [types](https://www.postgresql.org/docs/current/sql-altertype.html), [functions](https://www.postgresql.org/docs/current/sql-alterroutine.html), and [schemas](https://www.postgresql.org/docs/current/sql-alterschema.html).
### Rebasing new migrations[#](https://supabase.com/docs/guides/deployment/managing-environments#rebasing-new-migrations)
Sometimes your teammate may merge a new migration file to git main branch, and now you need to rebase your local schema changes on top.
We can handle this scenario gracefully by renaming your old migration file with a new timestamp.
```

1
2
3
4
5
gitpullsupabasemigrationnewdev_A# Assume the new file is: supabase/migrations/<t+2>_dev_A.sqlmv<time>_dev_A.sql<t+2>_dev_A.sqlsupabasedbreset

```

In case [`reset`](https://supabase.com/docs/reference/cli/usage#supabase-db-reset) fails, you can manually resolve conflicts by editing `<t+2>_dev_A.sql` file.
Once validated locally, commit your changes to Git and push to GitHub.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/deployment/managing-environments.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FrOLyOsBR1Uc%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Set up a local environment](https://supabase.com/docs/guides/deployment/managing-environments#set-up-a-local-environment)[Create a new migration](https://supabase.com/docs/guides/deployment/managing-environments#create-a-new-migration)[Manual migration](https://supabase.com/docs/guides/deployment/managing-environments#manual-migration)[Auto schema diff](https://supabase.com/docs/guides/deployment/managing-environments#auto-schema-diff)[Deploy a migration](https://supabase.com/docs/guides/deployment/managing-environments#deploy-a-migration)[Configure GitHub Actions](https://supabase.com/docs/guides/deployment/managing-environments#configure-github-actions)[Open a PR with new migration](https://supabase.com/docs/guides/deployment/managing-environments#open-a-pr-with-new-migration)[Release to production](https://supabase.com/docs/guides/deployment/managing-environments#release-to-production)[Troubleshooting](https://supabase.com/docs/guides/deployment/managing-environments#troubleshooting)[Sync production project to staging](https://supabase.com/docs/guides/deployment/managing-environments#sync-production-project-to-staging)[Permission denied on db pull](https://supabase.com/docs/guides/deployment/managing-environments#permission-denied-on-db-pull)[Permission denied on db push](https://supabase.com/docs/guides/deployment/managing-environments#permission-denied-on-db-push)[Rebasing new migrations](https://supabase.com/docs/guides/deployment/managing-environments#rebasing-new-migrations)
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


![Diagram showing a possible environment setup for Supabase development. There are 3 branches and 3 corresponding databases: feature branch and local database, develop branch and staging database, and main branch and production database.](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fimg%2Flocal-dev-environment--light.svg&w=1920&q=75)

