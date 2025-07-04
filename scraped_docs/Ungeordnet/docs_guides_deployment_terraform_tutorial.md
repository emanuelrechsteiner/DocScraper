---
url: https://supabase.com/docs/guides/deployment/terraform/tutorial
scraped_at: 2025-05-25T09:26:29.518261
title: Using the Supabase Terraform Provider | Supabase Docs
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
  2. Terraform
  3. [Terraform tutorial](https://supabase.com/docs/guides/deployment/terraform/tutorial)


Using the Supabase Terraform Provider
## Setting up a TF module[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#setting-up-a-tf-module)
  1. Create a Personal Access Token from Supabase Dashboard.
  2. Save your access token locally to `access-token` file or a secure credentials store.
  3. Create `module/provider.tf` with the following contents:


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
terraform{required_providers{supabase ={source="supabase/supabase"version="~> 1.0"}}}provider"supabase"{access_token =file("${path.cwd}/access-token")}

```

Run the command `terraform -chdir=module apply` which should succeed in finding the provider.
## Creating a project[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#creating-a-project)
Supabase projects are represented as a TF resource called `supabase_project`.
Create a `module/resource.tf` file with the following contents.
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
# Create a project resourceresource"supabase_project""production"{organization_id  ="<your-org-id>"name       ="tf-example"database_password ="<your-password>"region      ="ap-southeast-1"lifecycle{ignore_changes =[database_password]}}

```

Remember to substitue placeholder values with your own. For sensitive fields like password, you may consider retrieving it from a secure credentials store.
Next, run `terraform -chdir=module apply` and confirm creating the new project resource.
### Importing a project[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#importing-a-project)
If you have an existing project hosted on Supabase, you may import it into your local terraform state for tracking and management.
Edit `module/resource.tf` with the following changes.
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
# Define a linked project variable as user inputvariable"linked_project"{type =string}import{to =supabase_project.productionid = var.linked_project}# Create a project resourceresource"supabase_project""production"{organization_id  ="<your-org-id>"name       ="tf-example"database_password ="<your-password>"region      ="ap-southeast-1"lifecycle{ignore_changes =[database_password]}}

```

Run `terraform -chdir=module apply` and you will be prompted to enter the reference ID of an existing Supabase project. If your local TF state is empty, your project will be imported from remote rather than recreated.
Alternatively, you may use the `terraform import ...` command without editing the resource file.
## Configuring a project[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#configuring-a-project)
Keeping your project settings in-sync is easy with the `supabase_settings` resource.
Create `module/settings.tf` with the following contents.
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
# Configure api settings for the linked projectresource"supabase_settings""production"{project_ref = var.linked_projectapi =jsonencode({db_schema="public,storage,graphql_public"db_extra_search_path="public,extensions"max_rows=1000})}

```

Project settings don't exist on their own. They are created and destroyed together with their corresponding project resource referenced by the `project_ref` field. This means there is no difference between creating and updating `supabase_settings` resource while deletion is always a no-op.
You may declare any subset of fields to be managed by your TF module. The Supabase provider always performs a partial update when you run `terraform -chdir=module apply`. The underlying API call is also idempotent so it's safe to apply again if the local state is lost.
To see the full list of settings available, try importing the `supabase_settings` resource instead.
### Configuring branches[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#configuring-branches)
One of the most powerful features of TF is the ability to fan out configs to multiple resources. You can easily mirror the configurations of your production project to your branch databases using the `for_each` meta-argument.
Create a `module/branches.tf` file.
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
# Fetch all branches of a linked projectdata"supabase_branch""all"{parent_project_ref = var.linked_project}# Override settings for each preview branchresource"supabase_settings""branch"{for_each ={forbindata.supabase_branch.all.branches:b.project_ref=>b}project_ref =each.keyapi =supabase_settings.production.apiauth =jsonencode({site_url="http://localhost:3001"})}

```

When you run `terraform -chdir=module apply`, the provider will configure all branches associated with your `linked_project` to mirror the `api` settings of your production project.
In addition, the `auth.site_url` settings of your branches will be customised to a localhost URL for all branches. This allows your users to login via a separate domain for testing.
## Committing your changes[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#committing-your-changes)
Finally, you may commit the entire `module` directory to git for version control. This allows your CI runner to run `terraform apply` automatically on new config changes. Any command line variables can be passed to CI via `TF_VAR_*` environment variables instead.
## Resolving config drift[#](https://supabase.com/docs/guides/deployment/terraform/tutorial#resolving-config-drift)
Tracking your configs in TF module does not mean that you lose the ability to change configs through the dashboard. However, doing so could introduce config drift that you need to resolve manually by adding them to your `*.tf` files.
[Edit this page on GitHub ](https://github.com/supabase/terraform-provider-supabase/blob/v1.1.3/docs/tutorial.md)
### Is this helpful?
No Yes
### On this page
[Setting up a TF module](https://supabase.com/docs/guides/deployment/terraform/tutorial#setting-up-a-tf-module)[Creating a project](https://supabase.com/docs/guides/deployment/terraform/tutorial#creating-a-project)[Importing a project](https://supabase.com/docs/guides/deployment/terraform/tutorial#importing-a-project)[Configuring a project](https://supabase.com/docs/guides/deployment/terraform/tutorial#configuring-a-project)[Configuring branches](https://supabase.com/docs/guides/deployment/terraform/tutorial#configuring-branches)[Committing your changes](https://supabase.com/docs/guides/deployment/terraform/tutorial#committing-your-changes)[Resolving config drift](https://supabase.com/docs/guides/deployment/terraform/tutorial#resolving-config-drift)
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



