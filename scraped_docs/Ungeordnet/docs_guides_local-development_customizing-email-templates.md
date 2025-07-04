---
url: https://supabase.com/docs/guides/local-development/customizing-email-templates
scraped_at: 2025-05-25T09:11:20.514827
title: Customizing email templates | Supabase Docs
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
  3. [Customizing email templates](https://supabase.com/docs/guides/local-development/customizing-email-templates)


Customizing email templates
Customizing local email templates using config.toml.
You can customize the email templates for local development [using the `config.toml` settings](https://supabase.com/docs/guides/cli/config#auth-config).
## Configuring templates[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#configuring-templates)
You should provide a relative URL to the `content_path` parameter, pointing to an HTML file which contains the template. For example
supabase/config.tomlsupabase/templates/invite.html
```

1
2
3
[auth.email.template.invite]subject="You are invited to Acme Inc"content_path="./supabase/templates/invite.html"

```

## Available email templates[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#available-email-templates)
There are several Auth email templates which can be configured:
  * `auth.email.template.invite`
  * `auth.email.template.confirmation`
  * `auth.email.template.recovery`
  * `auth.email.template.magic_link`
  * `auth.email.template.email_change`


## Template variables[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#template-variables)
The templating system provides the following variables for use:
### `ConfirmationURL`[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#confirmationurl)
Contains the confirmation URL. For example, a signup confirmation URL would look like:
```

1
https://project-ref.supabase.co/auth/v1/verify?token={{ .TokenHash }}&type=email&redirect_to=https://example.com/path

```

**Usage**
```

1
<p>Click here to confirm: {{ .ConfirmationURL }}</p>

```

### `Token`[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#token)
Contains a 6-digit One-Time-Password (OTP) that can be used instead of the `ConfirmationURL`.
**Usage**
```

1
<p>Here is your one time password: {{ .Token }}</p>

```

### `TokenHash`[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#tokenhash)
Contains a hashed version of the `Token`. This is useful for constructing your own email link in the email template.
**Usage**
```

1
2
3
4
5
6
<p>Follow this link to confirm your user:</p><p><a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Confirm your email</a></p>

```

### `SiteURL`[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#siteurl)
Contains your application's Site URL. This can be configured in your project's [authentication settings](https://supabase.com/dashboard/project/_/auth/url-configuration).
**Usage**
```

1
<p>Visit <a href="{{ .SiteURL }}">here</a> to log in.</p>

```

### `Email`[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#email)
Contains the user's email address.
**Usage**
```

1
<p>A recovery request was sent to {{ .Email }}.</p>

```

### `NewEmail`[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#newemail)
Contains the new user's email address. This is only available in the `email_change` email template.
**Usage**
```

1
<p>You are requesting to update your email address to {{ .NewEmail }}.</p>

```

## Deploying email templates[#](https://supabase.com/docs/guides/local-development/customizing-email-templates#deploying-email-templates)
These settings are for local development. To apply the changes locally, stop and restart the Supabase containers:
```

1
supabasestop&&supabasestart

```

For hosted projects managed by Supabase, copy the templates into the [Email Templates](https://supabase.com/dashboard/project/_/auth/templates) section of the Dashboard.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/local-development/customizing-email-templates.mdx)
### Is this helpful?
No Yes
### On this page
[Configuring templates](https://supabase.com/docs/guides/local-development/customizing-email-templates#configuring-templates)[Available email templates](https://supabase.com/docs/guides/local-development/customizing-email-templates#available-email-templates)[Template variables](https://supabase.com/docs/guides/local-development/customizing-email-templates#template-variables)[ConfirmationURL](https://supabase.com/docs/guides/local-development/customizing-email-templates#confirmationurl)[Token](https://supabase.com/docs/guides/local-development/customizing-email-templates#token)[TokenHash](https://supabase.com/docs/guides/local-development/customizing-email-templates#tokenhash)[SiteURL](https://supabase.com/docs/guides/local-development/customizing-email-templates#siteurl)[Email](https://supabase.com/docs/guides/local-development/customizing-email-templates#email)[NewEmail](https://supabase.com/docs/guides/local-development/customizing-email-templates#newemail)[Deploying email templates](https://supabase.com/docs/guides/local-development/customizing-email-templates#deploying-email-templates)
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



