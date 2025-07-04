---
url: https://supabase.com/docs/guides/local-development/testing/pgtap-extended
scraped_at: 2025-05-25T09:29:54.880481
title: Advanced pgTAP Testing | Supabase Docs
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
  2. Testing
  3. [pgTAP advanced guide](https://supabase.com/docs/guides/local-development/testing/pgtap-extended)


Advanced pgTAP Testing
While basic pgTAP provides excellent testing capabilities, you can enhance the testing workflow using database development tools and helper packages. This guide covers advanced testing techniques using database.dev and community-maintained test helpers.
## Using database.dev[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#using-databasedev)
[Database.dev](https://database.dev) is a package manager for Postgres that allows installation and use of community-maintained packages, including testing utilities.
### Setting up dbdev[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#setting-up-dbdev)
To use database development tools and packages, install some prerequisites:
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
create extension ifnotexistshttpwithschema extensions;create extension ifnotexists pg_tle;drop extension ifexists"supabase-dbdev";selectpgtle.uninstall_extension_if_exists('supabase-dbdev');selectpgtle.install_extension('supabase-dbdev',resp.contents->>'version','PostgreSQL package manager',resp.contents->>'sql'  )fromhttp(  ('GET','https://api.database.dev/rest/v1/'||'package_versions?select=sql,version'||'&package_name=eq.supabase-dbdev'||'&order=version.desc'||'&limit=1',array[      ('apiKey', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtdXB0cHBsZnZpaWZyYndtbXR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAxMDczNzIsImV4cCI6MTk5NTY4MzM3Mn0.z2CN0mvO2No8wSi46Gw59DFGCTJrzM0AQKsu_5k134s')::http_header    ],null,null  )) x,lateral (select    ((row_to_json(x) ->'content') #>>'{}')::json->0) resp(contents);create extension "supabase-dbdev";selectdbdev.install('supabase-dbdev');-- Drop and recreate the extension to ensure a clean installationdrop extension ifexists"supabase-dbdev";create extension "supabase-dbdev";

```

### Installing test helpers[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#installing-test-helpers)
The Test Helpers package provides utilities that simplify testing Supabase-specific features:
```

1
2
selectdbdev.install('basejump-supabase_test_helpers');create extension ifnotexists"basejump-supabase_test_helpers"version'0.0.6';

```

## Test helper benefits[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#test-helper-benefits)
The test helpers package provides several advantages over writing raw pgTAP tests:
  1. **Simplified User Management**
     * Create test users with `tests.create_supabase_user()`
     * Switch contexts with `tests.authenticate_as()`
     * Retrieve user IDs using `tests.get_supabase_uid()`
  2. **Row Level Security (RLS) Testing Utilities**
     * Verify RLS status with `tests.rls_enabled()`
     * Test policy enforcement
     * Simulate different user contexts
  3. **Reduced Boilerplate**
     * No need to manually insert auth.users
     * Simplified JWT claim management
     * Clean test setup and cleanup


## Schema-wide Row Level Security testing[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#schema-wide-row-level-security-testing)
When working with Row Level Security, it's crucial to ensure that RLS is enabled on all tables that need it. Create a simple test to verify RLS is enabled across an entire schema:
```

1
2
3
4
5
6
7
8
begin;select plan(1);-- Verify RLS is enabled on all tables in the public schemaselecttests.rls_enabled('public');select*from finish();rollback;

```

## Test file organization[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#test-file-organization)
When working with multiple test files that share common setup requirements, it's beneficial to create a single "pre-test" file that handles the global environment setup. This approach reduces duplication and ensures consistent test environments.
### Creating a pre-test hook[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#creating-a-pre-test-hook)
Since pgTAP test files are executed in alphabetical order, create a setup file that runs first by using a naming convention like `000-setup-tests-hooks.sql`:
```

1
supabasetestnew000-setup-tests-hooks

```

This setup file should contain:
  1. All shared extensions and dependencies
  2. Common test utilities
  3. A simple always green test to verify the setup


Here's an example setup file:
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
-- install tests utilities-- install pgtap extension for testingcreate extension ifnotexists pgtap withschema extensions;/*------------------------- install dbdev --------------------------Requires: - pg_tle: https://github.com/aws/pg_tle - pgsql-http: https://github.com/pramsey/pgsql-http*/create extension ifnotexistshttpwithschema extensions;create extension ifnotexists pg_tle;drop extension ifexists"supabase-dbdev";selectpgtle.uninstall_extension_if_exists('supabase-dbdev');selectpgtle.install_extension('supabase-dbdev',resp.contents->>'version','PostgreSQL package manager',resp.contents->>'sql'  )fromhttp(  ('GET','https://api.database.dev/rest/v1/'||'package_versions?select=sql,version'||'&package_name=eq.supabase-dbdev'||'&order=version.desc'||'&limit=1',array[      ('apiKey', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtdXB0cHBsZnZpaWZyYndtbXR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAxMDczNzIsImV4cCI6MTk5NTY4MzM3Mn0.z2CN0mvO2No8wSi46Gw59DFGCTJrzM0AQKsu_5k134s')::http_header    ],null,null  )) x,lateral (select    ((row_to_json(x) ->'content') #>>'{}')::json->0) resp(contents);create extension "supabase-dbdev";selectdbdev.install('supabase-dbdev');drop extension ifexists"supabase-dbdev";create extension "supabase-dbdev";-- Install test helpersselectdbdev.install('basejump-supabase_test_helpers');create extension ifnotexists"basejump-supabase_test_helpers"version'0.0.6';-- Verify setup with a no-op testbegin;select plan(1);select ok(true, 'Pre-test hook completed successfully');select*from finish();rollback;

```

### Benefits[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#benefits)
This approach provides several advantages:
  * Reduces code duplication across test files
  * Ensures consistent test environment setup
  * Makes it easier to maintain and update shared dependencies
  * Provides immediate feedback if the setup process fails


Your subsequent test files (`001-auth-tests.sql`, `002-rls-tests.sql`) can focus solely on their specific test cases, knowing that the environment is properly configured.
## Example: Advanced RLS testing[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#example-advanced-rls-testing)
Here's a complete example using test helpers to verify RLS policies putting it all together:
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
begin;-- Assuming 000-setup-tests-hooks.sql file is present to use tests helpersselect plan(4);-- Set up test data-- Create test supabase usersselecttests.create_supabase_user('user1@test.com');selecttests.create_supabase_user('user2@test.com');-- Create test datainsert intopublic.todos (task, user_id) values ('User 1 Task 1', tests.get_supabase_uid('user1@test.com')), ('User 1 Task 2', tests.get_supabase_uid('user1@test.com')), ('User 2 Task 1', tests.get_supabase_uid('user2@test.com'));-- Test as User 1selecttests.authenticate_as('user1@test.com');-- Test 1: User 1 should only see their own todosselect results_eq('select count(*) from todos',ARRAY[2::bigint],'User 1 should only see their 2 todos');-- Test 2: User 1 can create their own todoselect lives_ok( $$insert into todos (task, user_id) values ('New Task', tests.get_supabase_uid('user1@test.com'))$$,'User 1 can create their own todo');-- Test as User 2selecttests.authenticate_as('user2@test.com');-- Test 3: User 2 should only see their own todosselect results_eq('select count(*) from todos',ARRAY[1::bigint],'User 2 should only see their 1 todo');-- Test 4: User 2 cannot modify User 1's todoSELECT results_ne(  $$ update todos set task ='Hacked!'where user_id =tests.get_supabase_uid('user1@test.com') returning 1 $$,  $$ values(1) $$,'User 2 cannot modify User 1 todos');select*from finish();rollback;

```

## Not another todo app: Testing complex organizations[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#not-another-todo-app-testing-complex-organizations)
Todo apps are great for learning, but this section explores testing a more realistic scenario: a multi-tenant content publishing platform. This example demonstrates testing complex permissions, plan restrictions, and content management.
### System overview[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#system-overview)
This demo app implements:
  * Organizations with tiered plans (free/pro/enterprise)
  * Role-based access (owner/admin/editor/viewer)
  * Content management (posts/comments)
  * Premium content restrictions
  * Plan-based limitations


### What makes this complex?[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#what-makes-this-complex)
  1. **Layered Permissions**
     * Role hierarchies affect access rights
     * Plan types influence user capabilities
     * Content state (draft/published) affects permissions
  2. **Business Rules**
     * Free plan post limits
     * Premium content visibility
     * Cross-organization security


### Testing focus areas[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#testing-focus-areas)
When writing tests, verify:
  * Organization member access control
  * Content visibility across roles
  * Plan limitation enforcement
  * Cross-organization data isolation


#### 1. App schema definitions[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#1-app-schema-definitions)
The app schema tables are defined like this:
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
createtablepublic.profiles ( id uuid referencesauth.users(id) primary key, username textuniquenot null, full_name text, bio text, created_at timestamptzdefaultnow(), updated_at timestamptzdefaultnow());createtablepublic.organizations ( id bigintprimary keygeneratedalwaysasidentity,nametextnot null, slug textuniquenot null, plan_type textnot nullcheck (plan_type in ('free', 'pro', 'enterprise')), max_posts intnot nulldefault5, created_at timestamptzdefaultnow());createtablepublic.org_members ( org_id bigintreferencespublic.organizations(id) on delete cascade, user_id uuid referencesauth.users(id) on delete cascade,roletextnot nullcheck (rolein ('owner', 'admin', 'editor', 'viewer')), created_at timestamptzdefaultnow(),primary key (org_id, user_id));createtablepublic.posts ( id bigintprimary keygeneratedalwaysasidentity, title textnot null, content textnot null, author_id uuid referencespublic.profiles(id) not null, org_id bigintreferencespublic.organizations(id),statustextnot nullcheck (statusin ('draft', 'published', 'archived')), is_premium booleandefault false, scheduled_for timestamptz, category text, view_count intdefault0, published_at timestamptz, created_at timestamptzdefaultnow(), updated_at timestamptzdefaultnow());createtablepublic.comments ( id bigintprimary keygeneratedalwaysasidentity, post_id bigintreferencespublic.posts(id) on delete cascade, author_id uuid referencespublic.profiles(id), content textnot null, is_deleted booleandefault false, created_at timestamptzdefaultnow(), updated_at timestamptzdefaultnow());

```

#### 2. RLS policies declaration[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#2-rls-policies-declaration)
Now to setup the RLS policies for each tables:
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
-- Create a private schema to store all security definer functions utils-- As such functions should never be in a API exposed schemacreateschemaifnotexistsprivate;-- Helper function for role checkscreate or replacefunctionprivate.get_user_org_role(org_id bigint, user_id uuid)returnstextset search_path =''as $$selectrolefrompublic.org_memberswhere org_id = $1and user_id = $2;-- Note the use of security definer to avoid RLS checking recursion issue-- see: https://supabase.com/docs/guides/database/postgres/row-level-security#use-security-definer-functions$$ languagesqlsecurity definer;-- Helper utils to check if an org is below the max post limitcreate or replacefunctionprivate.can_add_post(org_id bigint)returnsbooleanset search_path =''as $$select (selectcount(*)frompublic.posts pwherep.org_id= $1) <o.max_postsfrompublic.organizations owhereo.id= $1$$ languagesqlsecurity definer;-- Enable RLS for all tablesaltertablepublic.profilesenablerowlevelsecurity;altertablepublic.organizationsenablerowlevelsecurity;altertablepublic.org_membersenablerowlevelsecurity;altertablepublic.postsenablerowlevelsecurity;altertablepublic.commentsenablerowlevelsecurity;-- Profiles policiescreatepolicy"Public profiles are viewable by everyone"onpublic.profilesforselectusing (true);createpolicy"Users can insert their own profile"onpublic.profilesforinsertwithcheck ((selectauth.uid()) = id);createpolicy"Users can update their own profile"onpublic.profilesforupdateusing ((selectauth.uid()) = id)withcheck ((selectauth.uid()) = id);-- Organizations policiescreatepolicy"Public org info visible to all"onpublic.organizationsforselectusing (true);createpolicy"Org management restricted to owners"onpublic.organizationsfor all using (private.get_user_org_role(id, (selectauth.uid())) ='owner' );-- Org Members policiescreatepolicy"Members visible to org members"onpublic.org_membersforselectusing (private.get_user_org_role(org_id, (selectauth.uid())) is not null );createpolicy"Member management restricted to admins and owners"onpublic.org_membersfor all using (private.get_user_org_role(org_id, (selectauth.uid())) in ('owner', 'admin') );-- Posts policiescreatepolicy"Complex post visibility"onpublic.postsforselectusing (-- Published non-premium posts are visible to all  (status='published'andnot is_premium)or-- Premium posts visible to org members only  (status='published'and is_premium andprivate.get_user_org_role(org_id, (selectauth.uid())) is not null)or-- All posts visible to editors and aboveprivate.get_user_org_role(org_id, (selectauth.uid())) in ('owner', 'admin', 'editor') );createpolicy"Post creation rules"onpublic.postsforinsertwithcheck (-- Must be org member with appropriate roleprivate.get_user_org_role(org_id, (selectauth.uid())) in ('owner', 'admin', 'editor')and-- Check org post limits for free plans  (   (selecto.plan_type!='free'from organizations owhereo.id= org_id)or   (selectprivate.can_add_post(org_id))  ) );createpolicy"Post update rules"onpublic.postsforupdateusing (exists (select1where-- Editors can update non-published posts    (private.get_user_org_role(org_id, (selectauth.uid())) ='editor'andstatus!='published')or-- Admins and owners can update any postprivate.get_user_org_role(org_id, (selectauth.uid())) in ('owner', 'admin')  ) );-- Comments policiescreatepolicy"Comments on published posts are viewable by everyone"onpublic.commentsforselectusing (exists (select1frompublic.postswhere id = post_idandstatus='published'  )andnot is_deleted );createpolicy"Authenticated users can create comments"onpublic.commentsforinsertwithcheck ((selectauth.uid()) = author_id);createpolicy"Users can update their own comments"onpublic.commentsforupdateusing (author_id = (selectauth.uid()));

```

#### 3. Test cases:[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#3-test-cases)
Now everything is setup, let's write RLS test cases, note that each section could be in its own test:
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
-- Assuming we already have: 000-setup-tests-hooks.sql file we can use tests helpersbegin;-- Declare total number of testsselect plan(10);-- Create test usersselecttests.create_supabase_user('org_owner', 'owner@test.com');selecttests.create_supabase_user('org_admin', 'admin@test.com');selecttests.create_supabase_user('org_editor', 'editor@test.com');selecttests.create_supabase_user('premium_user', 'premium@test.com');selecttests.create_supabase_user('free_user', 'free@test.com');selecttests.create_supabase_user('scheduler', 'scheduler@test.com');selecttests.create_supabase_user('free_author', 'free_author@test.com');-- Create profiles for test usersinsert into profiles (id, username, full_name)values (tests.get_supabase_uid('org_owner'), 'org_owner', 'Organization Owner'), (tests.get_supabase_uid('org_admin'), 'org_admin', 'Organization Admin'), (tests.get_supabase_uid('org_editor'), 'org_editor', 'Organization Editor'), (tests.get_supabase_uid('premium_user'), 'premium_user', 'Premium User'), (tests.get_supabase_uid('free_user'), 'free_user', 'Free User'), (tests.get_supabase_uid('scheduler'), 'scheduler', 'Scheduler User'), (tests.get_supabase_uid('free_author'), 'free_author', 'Free Author');-- First authenticate as service role to bypass RLS for initial setupselecttests.authenticate_as_service_role();-- Create test organizations and setup datawith new_org as (insert into organizations (name, slug, plan_type, max_posts)values  ('Test Org', 'test-org', 'pro', 100),  ('Premium Org', 'premium-org', 'enterprise', 1000),  ('Schedule Org', 'schedule-org', 'pro', 100),  ('Free Org', 'free-org', 'free', 2) returning id, slug),-- Setup members and postsmember_setup as (insert into org_members (org_id, user_id, role)selectorg.id,  user_id,rolefrom new_org org cross join (values   (tests.get_supabase_uid('org_owner'), 'owner'),   (tests.get_supabase_uid('org_admin'), 'admin'),   (tests.get_supabase_uid('org_editor'), 'editor'),   (tests.get_supabase_uid('premium_user'), 'viewer'),   (tests.get_supabase_uid('scheduler'), 'editor'),   (tests.get_supabase_uid('free_author'), 'editor') ) as members(user_id, role)whereorg.slug='test-org'or (org.slug='premium-org'androle='viewer')or (org.slug='schedule-org'androle='editor')or (org.slug='free-org'androle='editor'))-- Setup initial postsinsert into posts (title, content, org_id, author_id, status, is_premium, scheduled_for)select title, content,org.id, author_id,status, is_premium, scheduled_forfrom new_org org cross join (values  ('Premium Post', 'Premium content', tests.get_supabase_uid('premium_user'), 'published', true, null),  ('Free Post', 'Free content', tests.get_supabase_uid('premium_user'), 'published', false, null),  ('Future Post', 'Future content', tests.get_supabase_uid('scheduler'), 'published', false, '2024-01-02 12:00:00+00'::timestamptz)) as posts(title, content, author_id, status, is_premium, scheduled_for)whereorg.slugin ('premium-org', 'schedule-org');-- Test owner privilegesselecttests.authenticate_as('org_owner');select lives_ok( $$update organizationssetname='Updated Org'where id = (select id from organizations limit1) $$,'Owner can update organization');-- Test admin privilegesselecttests.authenticate_as('org_admin');select results_eq(  $$selectcount(*) from org_members$$,ARRAY[6::bigint],'Admin can view all members');-- Test editor restrictionsselecttests.authenticate_as('org_editor');select throws_ok( $$insert into org_members (org_id, user_id, role)values (   (select id from organizations limit1),   (selecttests.get_supabase_uid('org_editor')),'viewer'  ) $$,'42501','new row violates row-level security policy for table "org_members"','Editor cannot manage members');-- Premium Content Access Testsselecttests.authenticate_as('premium_user');select results_eq(  $$selectcount(*) from posts where org_id = (select id from organizations where slug ='premium-org')$$,ARRAY[3::bigint],'Premium user can see all posts');selecttests.clear_authentication();select results_eq(  $$selectcount(*) from posts where org_id = (select id from organizations where slug ='premium-org')$$,ARRAY[2::bigint],'Anonymous users can only see free posts');-- Time-Based Publishing Testsselecttests.authenticate_as('scheduler');selecttests.freeze_time('2024-01-01 12:00:00+00'::timestamptz);select results_eq(  $$selectcount(*) from posts where scheduled_for >now()and org_id = (select id from organizations where slug ='schedule-org')$$,ARRAY[1::bigint],'Can see scheduled posts');selecttests.freeze_time('2024-01-02 13:00:00+00'::timestamptz);select results_eq(  $$selectcount(*) from posts where scheduled_for <now()and org_id = (select id from organizations where slug ='schedule-org')$$,ARRAY[1::bigint],'Can see posts after schedule time');selecttests.unfreeze_time();-- Plan Limit Testsselecttests.authenticate_as('free_author');select lives_ok( $$insert into posts (title, content, org_id, author_id, status)select'Post 1', 'Content 1', id, auth.uid(), 'draft'from organizations where slug ='free-org'limit1 $$,'First post creates successfully');select lives_ok( $$insert into posts (title, content, org_id, author_id, status)select'Post 2', 'Content 2', id, auth.uid(), 'draft'from organizations where slug ='free-org'limit1 $$,'Second post creates successfully');select throws_ok( $$insert into posts (title, content, org_id, author_id, status)select'Post 3', 'Content 3', id, auth.uid(), 'draft'from organizations where slug ='free-org'limit1 $$,'42501','new row violates row-level security policy for table "posts"','Cannot exceed free plan post limit');select*from finish();rollback;

```

## Additional resources[#](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#additional-resources)
  * [Test Helpers Documentation](https://database.dev/basejump/supabase_test_helpers)
  * [Test Helpers Reference](https://github.com/usebasejump/supabase-test-helpers)
  * [Row Level Security Writing Guide](https://usebasejump.com/blog/testing-on-supabase-with-pgtap)
  * [Database.dev Package Registry](https://database.dev)
  * [Row Level Security Performance and Best Practices](https://github.com/orgs/supabase/discussions/14576)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/local-development/testing/pgtap-extended.mdx)
### Is this helpful?
No Yes
### On this page
[Using database.dev](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#using-databasedev)[Setting up dbdev](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#setting-up-dbdev)[Installing test helpers](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#installing-test-helpers)[Test helper benefits](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#test-helper-benefits)[Schema-wide Row Level Security testing](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#schema-wide-row-level-security-testing)[Test file organization](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#test-file-organization)[Creating a pre-test hook](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#creating-a-pre-test-hook)[Benefits](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#benefits)[Example: Advanced RLS testing](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#example-advanced-rls-testing)[Not another todo app: Testing complex organizations](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#not-another-todo-app-testing-complex-organizations)[System overview](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#system-overview)[What makes this complex?](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#what-makes-this-complex)[Testing focus areas](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#testing-focus-areas)[Additional resources](https://supabase.com/docs/guides/local-development/testing/pgtap-extended#additional-resources)
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



