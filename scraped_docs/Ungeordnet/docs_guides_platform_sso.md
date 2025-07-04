---
url: https://supabase.com/docs/guides/platform/sso
scraped_at: 2025-05-25T09:06:11.072716
title: Enable SSO for Your Organization | Supabase Docs
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
[Platform](https://supabase.com/docs/guides/platform)
Add-ons
  * [Custom Domains](https://supabase.com/docs/guides/platform/custom-domains)
  * [Database Backups](https://supabase.com/docs/guides/platform/backups)
  * [IPv4 Address](https://supabase.com/docs/guides/platform/ipv4-address)
  * [Read Replicas](https://supabase.com/docs/guides/platform/read-replicas)
Upgrades & Migrations
  * [Upgrading](https://supabase.com/docs/guides/platform/upgrading)
  * [Migrating within Supabase](https://supabase.com/docs/guides/platform/migrating-within-supabase)
  * [Migrating to Supabase](https://supabase.com/docs/guides/platform/migrating-to-supabase)
Project & Account Management
  * [Access Control](https://supabase.com/docs/guides/platform/access-control)
  * [Multi-factor Authentication](https://supabase.com/docs/guides/platform/multi-factor-authentication)
  * [Transfer Project](https://supabase.com/docs/guides/platform/project-transfer)
  * [Single Sign-On](https://supabase.com/docs/guides/platform/sso)
  * [SSO with Azure AD](https://supabase.com/docs/guides/platform/sso/azure)
  * [SSO with Google Workspace](https://supabase.com/docs/guides/platform/sso/gsuite)
  * [SSO with Okta](https://supabase.com/docs/guides/platform/sso/okta)
Platform Configuration
  * [Regions](https://supabase.com/docs/guides/platform/regions)
  * [Compute and Disk](https://supabase.com/docs/guides/platform/compute-and-disk)
  * [Database Size](https://supabase.com/docs/guides/platform/database-size)
  * [HIPAA Projects](https://supabase.com/docs/guides/platform/hipaa-projects)
  * [Network Restrictions](https://supabase.com/docs/guides/platform/network-restrictions)
  * [Performance Tuning](https://supabase.com/docs/guides/platform/performance)
  * [SSL Enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement)
  * [Default Platform Permissions](https://supabase.com/docs/guides/platform/permissions)
Billing
  * [About billing on Supabase](https://supabase.com/docs/guides/platform/billing-on-supabase)
  * [Get set up for billing](https://supabase.com/docs/guides/platform/get-set-up-for-billing)
  * [Manage your subscription](https://supabase.com/docs/guides/platform/manage-your-subscription)
  * [Manage your usage](https://supabase.com/docs/guides/platform/manage-your-usage)
  * [Your monthly invoice](https://supabase.com/docs/guides/platform/your-monthly-invoice)
  * [Control your costs](https://supabase.com/docs/guides/platform/cost-control)
  * [Credits](https://supabase.com/docs/guides/platform/credits)
  * [Billing FAQ](https://supabase.com/docs/guides/platform/billing-faq)


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
Platform
  1. [Platform](https://supabase.com/docs/guides/platform)
  2. Project & Account Management
  3. [Single Sign-On](https://supabase.com/docs/guides/platform/sso)


Enable SSO for Your Organization
Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml).
Supabase offers single sign-on (SSO) as a login option to provide additional account security for your team. This allows company administrators to enforce the use of an identity provider when logging into Supabase. SSO improves the onboarding and offboarding experience of the company as the employee only needs a single set of credentials to access third-party applications or tools which can also be revoked by an administrator.
Supabase currently provides SAML SSO for [Team and Enterprise Plan customers](https://supabase.com/pricing). If you are an existing Team or Enterprise Plan customer, continue with the setup below. Once completed, [contact us](https://supabase.com/dashboard/support/new?category=Login_issues&subject=Enquiry%20about%20setting%20up%20SSO&message=I%20would%20like%20to%20set%20up%20SAML%20SSO%20for%20my%20team%20and%20have%20followed%20https://supabase.com/docs/guides/platform/sso%20and%20configured%20my%20provider%20%0A%0APlease%20attach%20the%20IDP%20metadata%20in%20the%20attachments%20below) to enable SSO for your team.
## Setup and limitations[#](https://supabase.com/docs/guides/platform/sso#setup-and-limitations)
Supabase supports practically all identity providers that support the SAML 2.0 SSO protocol. We've prepared these guides for commonly used identity providers to help you get started. If you use a different provider, our support stands ready to support you.
  * [Google Workspaces (formerly G Suite)](https://supabase.com/docs/guides/platform/sso/gsuite)
  * [Azure Active Directory](https://supabase.com/docs/guides/platform/sso/azure)
  * [Okta](https://supabase.com/docs/guides/platform/sso/okta)


Accounts signing in with SSO have certain limitations. The following sections outline the limitations when SSO is enabled or disabled for your team.
### Enable SSO for your team [#](https://supabase.com/docs/guides/platform/sso#enable-sso)
  * Organization invites are restricted to company members belonging to the same identity provider.
  * Every user has an organization created by default. They can create as many projects as they want.
  * An SSO user will not be able to update or reset their password since the company administrator manages their access via the identity provider.
  * If an SSO user with the following email of `alice@foocorp.com` attempts to sign in with a GitHub account that uses the same email, a separate Supabase account is created and will not be linked to the SSO user's account.
  * An SSO user will not be able to see all organizations/projects created under the same identity provider. They will need to be invited to the Supabase organization first. Refer to [access control](https://supabase.com/docs/guides/platform/access-control) for more information.


### Disable SSO for your team [#](https://supabase.com/docs/guides/platform/sso#disable-sso)
  * You can prevent a user's account from further access to Supabase by removing or disabling their account in your identity provider.
  * You should also remove or downgrade their permissions from any organizations inside Supabase.

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/platform/sso.mdx)
### Is this helpful?
No Yes
### On this page
[Setup and limitations](https://supabase.com/docs/guides/platform/sso#setup-and-limitations)[Enable SSO for your team ](https://supabase.com/docs/guides/platform/sso#enable-sso)[Disable SSO for your team ](https://supabase.com/docs/guides/platform/sso#disable-sso)
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



