---
url: https://supabase.com/docs/guides/deployment/terraform/reference
scraped_at: 2025-05-25T09:07:38.322047
title: Terraform Provider reference | Supabase Docs
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
  3. [Terraform reference](https://supabase.com/docs/guides/deployment/terraform/reference)


Terraform Provider reference
Resources and data sources available through the Terraform Provider
The Terraform Provider provices access to [resources](https://developer.hashicorp.com/terraform/language/resources) and [data sources](https://developer.hashicorp.com/terraform/language/data-sources). Resources are infrastructure objects, such as a Supabase project, that you can declaratively configure. Data sources are sources of information about your Supabase instances.
## Provider settings[#](https://supabase.com/docs/guides/deployment/terraform/reference#provider-settings)
Use these settings to configure your Supabase provider and authenticate to your Supabase project.
### Example usage[#](https://supabase.com/docs/guides/deployment/terraform/reference#example-usage)
```
1provider "supabase" {
2  access_token = ""3  endpoint = ""4}
```

### Details[#](https://supabase.com/docs/guides/deployment/terraform/reference#details)
Attribute| Description| Type| Optional| Sensitive  
---|---|---|---|---  
access_token| Supabase access token| string| true| true  
endpoint| Supabase API endpoint| string| true|   
## Resources[#](https://supabase.com/docs/guides/deployment/terraform/reference#resources)
You can configure these resources using the Supabase Terraform provider:
supabase_branchsupabase_projectsupabase_settings
#### Example usage[#](https://supabase.com/docs/guides/deployment/terraform/reference#example-usage)
```
1resource "supabase_branch""<label>" {
2  git_branch = ""3  parent_project_ref = ""4  region = ""5}
```

#### Details[#](https://supabase.com/docs/guides/deployment/terraform/reference#details)
Attribute| Description| Type| Required| Optional| Read-only  
---|---|---|---|---|---  
`database`| Database connection details| Nested type| | | true  
`git_branch`| Git branch| string| true| |   
`id`| Branch identifier| string| | | true  
`parent_project_ref`| Parent project ref| string| true| |   
`region`| Database region| string| | true|   
## Data sources[#](https://supabase.com/docs/guides/deployment/terraform/reference#data-sources)
You can read these resources using the Supabase Terraform provider:
supabase_branch
#### Example usage[#](https://supabase.com/docs/guides/deployment/terraform/reference#example-usage)
```
1resource "supabase_branch""all" {
2  parent_project_ref = ""3}
```

#### Details[#](https://supabase.com/docs/guides/deployment/terraform/reference#details)
Attribute| Description| Type| Required| Optional| Read-only  
---|---|---|---|---|---  
`branches`| Branch databases| Nested type| | | true  
`parent_project_ref`| Parent project ref| string| true| |   
[Edit this page on GitHub ](https://github.com/supabase/terraform-provider-supabase)
### Is this helpful?
No Yes
### On this page
[Provider settings](https://supabase.com/docs/guides/deployment/terraform/reference#provider-settings)[Example usage](https://supabase.com/docs/guides/deployment/terraform/reference#example-usage)[Details](https://supabase.com/docs/guides/deployment/terraform/reference#details)[Resources](https://supabase.com/docs/guides/deployment/terraform/reference#resources)[Data sources](https://supabase.com/docs/guides/deployment/terraform/reference#data-sources)
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



