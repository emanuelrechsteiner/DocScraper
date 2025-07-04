---
url: https://supabase.com/docs/guides/getting-started/ai-prompts/database-functions
scraped_at: 2025-05-25T08:53:27.909300
title: AI Prompt: Database: Create functions | Supabase Docs
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
[Start with Supabase](https://supabase.com/docs/guides/getting-started)
  * [Features](https://supabase.com/docs/guides/getting-started/features)
  * [Architecture](https://supabase.com/docs/guides/getting-started/architecture)
Framework Quickstarts
  * [Next.js](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
  * [React](https://supabase.com/docs/guides/getting-started/quickstarts/reactjs)
  * [Nuxt](https://supabase.com/docs/guides/getting-started/quickstarts/nuxtjs)
  * [Vue](https://supabase.com/docs/guides/getting-started/quickstarts/vue)
  * [Hono](https://supabase.com/docs/guides/getting-started/quickstarts/hono)
  * [Flutter](https://supabase.com/docs/guides/getting-started/quickstarts/flutter)
  * [iOS SwiftUI](https://supabase.com/docs/guides/getting-started/quickstarts/ios-swiftui)
  * [Android Kotlin](https://supabase.com/docs/guides/getting-started/quickstarts/kotlin)
  * [SvelteKit](https://supabase.com/docs/guides/getting-started/quickstarts/sveltekit)
  * [Laravel PHP](https://supabase.com/docs/guides/getting-started/quickstarts/laravel)
  * [Ruby on Rails](https://supabase.com/docs/guides/getting-started/quickstarts/ruby-on-rails)
  * [SolidJS](https://supabase.com/docs/guides/getting-started/quickstarts/solidjs)
  * [RedwoodJS](https://supabase.com/docs/guides/getting-started/quickstarts/redwoodjs)
  * [refine](https://supabase.com/docs/guides/getting-started/quickstarts/refine)
Web app demos
  * [Next.js](https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs)
  * [React](https://supabase.com/docs/guides/getting-started/tutorials/with-react)
  * [Vue 3](https://supabase.com/docs/guides/getting-started/tutorials/with-vue-3)
  * [Nuxt 3](https://supabase.com/docs/guides/getting-started/tutorials/with-nuxt-3)
  * [Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-angular)
  * [RedwoodJS](https://supabase.com/docs/guides/getting-started/tutorials/with-redwoodjs)
  * [SolidJS](https://supabase.com/docs/guides/getting-started/tutorials/with-solidjs)
  * [Svelte](https://supabase.com/docs/guides/getting-started/tutorials/with-svelte)
  * [SvelteKit](https://supabase.com/docs/guides/getting-started/tutorials/with-sveltekit)
  * [refine](https://supabase.com/docs/guides/getting-started/tutorials/with-refine)
Mobile tutorials
  * [Flutter](https://supabase.com/docs/guides/getting-started/tutorials/with-flutter)
  * [Expo React Native](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native)
  * [Android Kotlin](https://supabase.com/docs/guides/getting-started/tutorials/with-kotlin)
  * [Ionic React](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-react)
  * [Ionic Vue](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-vue)
  * [Ionic Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular)
  * [Swift](https://supabase.com/docs/guides/getting-started/tutorials/with-swift)
AI Tools
  * [Prompts](https://supabase.com/docs/guides/getting-started/ai-prompts)
  * [Bootstrap Next.js app with Supabase Auth](https://supabase.com/docs/guides/getting-started/ai-prompts/nextjs-supabase-auth)
  * [Writing Supabase Edge Functions](https://supabase.com/docs/guides/getting-started/ai-prompts/edge-functions)
  * [Database: Declarative Database Schema](https://supabase.com/docs/guides/getting-started/ai-prompts/declarative-database-schema)
  * [Database: Create RLS policies](https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies)
  * [Database: Create functions](https://supabase.com/docs/guides/getting-started/ai-prompts/database-functions)
  * [Database: Create migration](https://supabase.com/docs/guides/getting-started/ai-prompts/database-create-migration)
  * [Postgres SQL Style Guide](https://supabase.com/docs/guides/getting-started/ai-prompts/code-format-sql)
  * [Model context protocol (MCP)](https://supabase.com/docs/guides/getting-started/mcp)


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
Getting Started
  1. [Getting started](https://supabase.com/docs/guides/getting-started)
  2. AI Tools
  3. [Prompts](https://supabase.com/docs/guides/getting-started/ai-prompts)


AI Prompt: Database: Create functions
## How to use[#](https://supabase.com/docs/guides/getting-started/ai-prompts/database-functions#how-to-use)
Copy the prompt to a file in your repo.
Use the "include file" feature from your AI tool to include the prompt when chatting with your AI assistant. For example, with GitHub Copilot, use `#<filename>`, in Cursor, use `@Files`, and in Zed, use `/file`.
## Prompt[#](https://supabase.com/docs/guides/getting-started/ai-prompts/database-functions#prompt)
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
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
---# Specify the following for Cursor rulesdescription:Guidelines for writing Supabase database functionsalwaysApply:false---#Database: Create functionsYou're a Supabase Postgres expert in writing database functions. Generate **high-quality PostgreSQL functions** that adhere to the following best practices:##General Guidelines1.**Default to `SECURITY INVOKER`:**- Functions should run with the permissions of the user invoking the function, ensuring safer access control.- Use `SECURITY DEFINER` only when explicitly required and explain the rationale.2.**Set the `search_path` Configuration Parameter:**- Always set `search_path` to an empty string (`set search_path = '';`).- This avoids unexpected behavior and security risks caused by resolving object references in untrusted or unintended schemas.- Use fully qualified names (e.g., `schema_name.table_name`) for all database objects referenced within the function.3.**Adhere to SQL Standards and Validation:**- Ensure all queries within the function are valid PostgreSQL SQL queries and compatible with the specified context (ie. Supabase).##Best Practices1.**Minimize Side Effects:**- Prefer functions that return results over those that modify data unless they serve a specific purpose (e.g., triggers).2.**Use Explicit Typing:**- Clearly specify input and output types, avoiding ambiguous or loosely typed parameters.3.**Default to Immutable or Stable Functions:**- Where possible, declare functions as `IMMUTABLE` or `STABLE` to allow better optimization by PostgreSQL. Use `VOLATILE` only if the function modifies data or has side effects.4.**Triggers (if Applicable):**- If the function is used as a trigger, include a valid `CREATE TRIGGER` statement that attaches the function to the desired table and event (e.g., `BEFORE INSERT`).##Example Templates###Simple Function with `SECURITY INVOKER````sqlcreate or replacefunctionmy_schema.hello_world()returnstextlanguage plpgsqlsecurity invokerset search_path =''as $$beginreturn'hello world';end;$$;```###Function with Parameters and Fully Qualified Object Names```sqlcreate or replacefunctionpublic.calculate_total_price(order_id bigint)returnsnumericlanguage plpgsqlsecurity invokerset search_path =''as $$declare total numeric;beginselectsum(price * quantity)into totalfrompublic.order_itemswhere order_id =calculate_total_price.order_id;return total;end;$$;```###Function as a Trigger```sqlcreate or replacefunctionmy_schema.update_updated_at()returns triggerlanguage plpgsqlsecurity invokerset search_path =''as $$begin-- Update the "updated_at" column on row modificationnew.updated_at :=now();return new;end;$$;createtriggerupdate_updated_at_triggerbeforeupdateonmy_schema.my_tablefor each rowexecutefunctionmy_schema.update_updated_at();```###Function with Error Handling```sqlcreate or replacefunctionmy_schema.safe_divide(numerator numeric, denominator numeric)returnsnumericlanguage plpgsqlsecurity invokerset search_path =''as $$beginif denominator =0then  raise exception 'Division by zero is not allowed';endif;return numerator / denominator;end;$$;```###Immutable Function for Better Optimization```sqlcreate or replacefunctionmy_schema.full_name(first_name text, last_name text)returnstextlanguagesqlsecurity invokerset search_path =''immutableas $$select first_name ||''|| last_name;$$;```

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/examples/prompts/database-functions.md)
### Is this helpful?
No Yes
### On this page
[How to use](https://supabase.com/docs/guides/getting-started/ai-prompts/database-functions#how-to-use)[Prompt](https://supabase.com/docs/guides/getting-started/ai-prompts/database-functions#prompt)
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



