---
url: https://supabase.com/docs/guides/platform/terraform
scraped_at: 2025-05-25T09:33:52.516617
title: Terraform Provider | Supabase Docs
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
  3. [Terraform provider](https://supabase.com/docs/guides/deployment/terraform)


Terraform Provider
The [Supabase Provider](https://registry.terraform.io/providers/supabase/supabase/latest/docs) allows Terraform to manage resources hosted on [Supabase](https://supabase.com/) platform.
You may use this provider to version control your project settings or setup CI/CD pipelines for automatically provisioning projects and branches.
  * [CI/CD example](https://github.com/supabase/supabase-action-example/tree/main/supabase/remotes)
  * [Step-by-step tutorials](https://supabase.com/docs/guides/deployment/terraform/tutorial)
  * [Contributing guide](https://github.com/supabase/terraform-provider-supabase/blob/v1.1.3/CONTRIBUTING.md)


## Using the provider[#](https://supabase.com/docs/guides/deployment/terraform#using-the-provider)
This simple example imports an existing Supabase project and synchronises its API settings.
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
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
terraform{required_providers{supabase ={source="supabase/supabase"version="~> 1.0"}}}provider"supabase"{access_token =file("${path.module}/access-token")}# Define a linked project variable as user inputvariable"linked_project"{type =string}# Import the linked project resourceimport{to =supabase_project.productionid =var.linked_project}resource"supabase_project""production"{organization_id  ="nknnyrtlhxudbsbuazsu"name       ="tf-project"database_password ="tf-example"region      ="ap-southeast-1"lifecycle{ignore_changes =[database_password]}}# Configure api settings for the linked projectresource"supabase_settings""production"{project_ref =var.linked_projectapi =jsonencode({db_schema="public,storage,graphql_public"db_extra_search_path="public,extensions"max_rows=1000})}

```

[Edit this page on GitHub ](https://github.com/supabase/terraform-provider-supabase/blob/v1.1.3/README.md)
### Is this helpful?
No Yes
### On this page
[Using the provider](https://supabase.com/docs/guides/deployment/terraform#using-the-provider)
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



