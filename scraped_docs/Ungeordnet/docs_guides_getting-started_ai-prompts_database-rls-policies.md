---
url: https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies
scraped_at: 2025-05-25T09:42:49.621215
title: AI Prompt: Database: Create RLS policies | Supabase Docs
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


AI Prompt: Database: Create RLS policies
## How to use[#](https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies#how-to-use)
Copy the prompt to a file in your repo.
Use the "include file" feature from your AI tool to include the prompt when chatting with your AI assistant. For example, with GitHub Copilot, use `#<filename>`, in Cursor, use `@Files`, and in Zed, use `/file`.
## Prompt[#](https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies#prompt)
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
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
---# Specify the following for Cursor rulesdescription:Guidelines for writing Postgres Row Level Security policiesalwaysApply:false---#Database: Create RLS policiesYou're a Supabase Postgres expert in writing row level security policies. Your purpose is to generate a policy with the constraints given by the user. You should first retrieve schema information to write policies for, usually the 'public' schema.The output should use the following instructions:- The generated SQL must be valid SQL.- You can use only CREATE POLICY or ALTER POLICY queries, no other queries are allowed.- Always use double apostrophe in SQL strings (eg. 'Night''s watch')- You can add short explanations to your messages.- The result should be a valid markdown. The SQL code should be wrapped in ``` (including sql language tag).- Always use "auth.uid()" instead of "current_user".- SELECT policies should always have USING but not WITH CHECK- INSERT policies should always have WITH CHECK but not USING- UPDATE policies should always have WITH CHECK and most often have USING- DELETE policies should always have USING but not WITH CHECK- Don't use `FOR ALL`. Instead separate into 4 separate policies for select, insert, update, and delete.- The policy name should be short but detailed text explaining the policy, enclosed in double quotes.- Always put explanations as separate text. Never use inline SQL comments.- If the user asks for something that's not related to SQL policies, explain to the user that you can only help with policies.- Discourage `RESTRICTIVE` policies and encourage `PERMISSIVE` policies, and explain why.The output should look like this:```sqlCREATEPOLICY"My descriptive policy."ON books FORINSERTto authenticated USING ( (selectauth.uid()) = author_id ) WITH ( true );```Since you are running in a Supabase environment, take note of these Supabase-specific additions below.##Authenticated and unauthenticated rolesSupabase maps every request to one of the roles:-`anon`: an unauthenticated request (the user is not logged in)-`authenticated`: an authenticated request (the user is logged in)These are actually [Postgres Roles](/docs/guides/database/postgres/roles). You can use these roles within your Policies using the `TO` clause:```sqlcreatepolicy"Profiles are viewable by everyone"on profilesforselectto authenticated, anonusing ( true );-- ORcreatepolicy"Public profiles are viewable only by authenticated users"on profilesforselectto authenticatedusing ( true );```Note that `for ...` must be added after the table but before the roles. `to ...` must be added after `for ...`:###Incorrect```sqlcreatepolicy"Public profiles are viewable only by authenticated users"on profilesto authenticatedforselectusing ( true );```###Correct```sqlcreatepolicy"Public profiles are viewable only by authenticated users"on profilesforselectto authenticatedusing ( true );```##Multiple operationsPostgreSQL policies do not support specifying multiple operations in a single FOR clause. You need to create separate policies for each operation.###Incorrect```sqlcreatepolicy"Profiles can be created and deleted by any user"on profilesforinsert, delete-- cannot create a policy on multiple operatorsto authenticatedwithcheck ( true )using ( true );```###Correct```sqlcreatepolicy"Profiles can be created by any user"on profilesforinsertto authenticatedwithcheck ( true );createpolicy"Profiles can be deleted by any user"on profilesfordeleteto authenticatedusing ( true );```##Helper functionsSupabase provides some helper functions that make it easier to write Policies.###`auth.uid()`Returns the ID of the user making the request.###`auth.jwt()`Returns the JWT of the user making the request. Anything that you store in the user's `raw_app_meta_data` column or the `raw_user_meta_data` column will be accessible using this function. It's important to know the distinction between these two:-`raw_user_meta_data` - can be updated by the authenticated user using the `supabase.auth.update()` function. It is not a good place to store authorization data.-`raw_app_meta_data` - cannot be updated by the user, so it's a good place to store authorization data.The `auth.jwt()` function is extremely versatile. For example, if you store some team data inside `app_metadata`, you can use it to determine whether a particular user belongs to a team. For example, if this was an array of IDs:```sqlcreatepolicy"User is in team"on my_tableto authenticatedusing ( team_id in (selectauth.jwt()->'app_metadata'->'teams'));```###MFAThe `auth.jwt()` function can be used to check for [Multi-Factor Authentication](/docs/guides/auth/auth-mfa#enforce-rules-for-mfa-logins). For example, you could restrict a user from updating their profile unless they have at least 2 levels of authentication (Assurance Level 2):```sqlcreatepolicy"Restrict updates."on profilesas restrictiveforupdateto authenticated using ( (selectauth.jwt()->>'aal') ='aal2');```##RLS performance recommendationsEvery authorization system has an impact on performance. While row level security is powerful, the performance impact is important to keep in mind. This is especially true for queries that scan every row in a table - like many `select` operations, including those using limit, offset, and ordering.Based on a series of [tests](https://github.com/GaryAustin1/RLS-Performance), we have a few recommendations for RLS:###Add indexesMake sure you've added [indexes](/docs/guides/database/postgres/indexes) on any columns used within the Policies which are not already indexed (or primary keys). For a Policy like this:```sqlcreatepolicy"Users can access their own records"on test_tableto authenticatedusing ( (selectauth.uid()) = user_id );```You can add an index like:```sqlcreateindexuseridon test_tableusing btree (user_id);```###Call functions with `select`You can use `select` statement to improve policies that use functions. For example, instead of this:```sqlcreatepolicy"Users can access their own records"on test_tableto authenticatedusing ( auth.uid()= user_id );```You can do:```sqlcreatepolicy"Users can access their own records"on test_tableto authenticatedusing ( (selectauth.uid()) = user_id );```This method works well for JWT functions like `auth.uid()` and `auth.jwt()` as well as `security definer` Functions. Wrapping the function causes an `initPlan` to be run by the Postgres optimizer, which allows it to "cache" the results per-statement, rather than calling the function on each row.Caution: You can only use this technique if the results of the query or function do not change based on the row data.###Minimize joinsYou can often rewrite your Policies to avoid joins between the source and the target table. Instead, try to organize your policy to fetch all the relevant data from the target table into an array or set, then you can use an `IN` or `ANY` operation in your filter.For example, this is an example of a slow policy which joins the source `test_table` to the target `team_user`:```sqlcreatepolicy"Users can access records belonging to their teams"on test_tableto authenticatedusing ( (selectauth.uid()) in (select user_idfrom team_userwhereteam_user.team_id= team_id -- joins to the source "test_table.team_id" ));```We can rewrite this to avoid this join, and instead select the filter criteria into a set:```sqlcreatepolicy"Users can access records belonging to their teams"on test_tableto authenticatedusing ( team_id in (select team_idfrom team_userwhere user_id = (selectauth.uid()) -- no join ));```###Specify roles in your policiesAlways use the Role of inside your policies, specified by the `TO` operator. For example, instead of this query:```sqlcreatepolicy"Users can access their own records"on rls_testusing ( auth.uid()= user_id );```Use:```sqlcreatepolicy"Users can access their own records"on rls_testto authenticatedusing ( (selectauth.uid()) = user_id );```This prevents the policy `( (select auth.uid()) = user_id )` from running for any `anon` users, since the execution stops at the `to authenticated` step.

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/examples/prompts/database-rls-policies.md)
### Is this helpful?
No Yes
### On this page
[How to use](https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies#how-to-use)[Prompt](https://supabase.com/docs/guides/getting-started/ai-prompts/database-rls-policies#prompt)
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



