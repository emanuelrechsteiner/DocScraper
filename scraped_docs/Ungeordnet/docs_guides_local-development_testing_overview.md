---
url: https://supabase.com/docs/guides/local-development/testing/overview
scraped_at: 2025-05-25T09:23:28.289210
title: Testing Overview | Supabase Docs
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
  3. [Getting started](https://supabase.com/docs/guides/local-development/testing/overview)


Testing Overview
Testing is a critical part of database development, especially when working with features like Row Level Security (RLS) policies. This guide provides a comprehensive approach to testing your Supabase database.
## Testing approaches[#](https://supabase.com/docs/guides/local-development/testing/overview#testing-approaches)
### Database unit testing with pgTAP[#](https://supabase.com/docs/guides/local-development/testing/overview#database-unit-testing-with-pgtap)
[pgTAP](https://pgtap.org) is a unit testing framework for Postgres that allows testing:
  * Database structure: tables, columns, constraints
  * Row Level Security (RLS) policies
  * Functions and procedures
  * Data integrity


This example demonstrates setting up and testing RLS policies for a simple todo application:
  1. Create a test table with RLS enabled:
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
-- Create a simple todos tablecreatetabletodos (id uuid primary keydefault gen_random_uuid(),task textnot null,user_id uuid referencesauth.usersnot null,completed booleandefault false);-- Enable RLSaltertable todos enablerowlevelsecurity;-- Create a policycreatepolicy"Users can only access their own todos"on todos for all -- this policy applies to all operationsto authenticatedusing ((selectauth.uid()) = user_id);

```

  2. Set up your testing environment:
```

1
2
# Create a new test for our policies using supabase clisupabasetestnewtodos_rls.test

```

  3. Write your RLS tests:
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
begin;-- install tests utilities-- install pgtap extension for testingcreate extension ifnotexists pgtap withschema extensions;-- Start declare we'll have 4 test cases in our test suiteselect plan(4);-- Setup our testing data-- Set up auth.users entriesinsert intoauth.users (id, email) values	('123e4567-e89b-12d3-a456-426614174000', 'user1@test.com'),	('987fcdeb-51a2-43d7-9012-345678901234', 'user2@test.com');-- Create test todosinsert intopublic.todos (task, user_id) values	('User 1 Task 1', '123e4567-e89b-12d3-a456-426614174000'),	('User 1 Task 2', '123e4567-e89b-12d3-a456-426614174000'),	('User 2 Task 1', '987fcdeb-51a2-43d7-9012-345678901234');-- as User 1setlocalrole authenticated;setlocalrequest.jwt.claim.sub='123e4567-e89b-12d3-a456-426614174000';-- Test 1: User 1 should only see their own todosselect results_eq('select count(*) from todos',ARRAY[2::bigint],'User 1 should only see their 2 todos');-- Test 2: User 1 can create their own todoselect lives_ok(	$$insert into todos (task, user_id) values ('New Task', '123e4567-e89b-12d3-a456-426614174000'::uuid)$$,'User 1 can create their own todo');-- as User 2setlocalrequest.jwt.claim.sub='987fcdeb-51a2-43d7-9012-345678901234';-- Test 3: User 2 should only see their own todosselect results_eq('select count(*) from todos',ARRAY[1::bigint],'User 2 should only see their 1 todo');-- Test 4: User 2 cannot modify User 1's todoSELECT results_ne(	$$ update todos set task ='Hacked!'where user_id ='123e4567-e89b-12d3-a456-426614174000'::uuid returning 1 $$,	$$ values(1) $$,'User 2 cannot modify User 1 todos');select*from finish();rollback;

```

  4. Run the tests:
```

1
2
3
4
5
6
supabasetestdbpsql:todos_rls.test.sql:4:NOTICE:extension"pgtap"alreadyexists,skipping./todos_rls.test.sql..okAlltestssuccessful.Files=1,Tests=6,0wallclocksecs ( 0.01usr+0.00sys=0.01CPU)Result:PASS

```



### Application-Level testing[#](https://supabase.com/docs/guides/local-development/testing/overview#application-level-testing)
Testing through application code provides end-to-end verification. Unlike database-level testing with pgTAP, application-level tests cannot use transactions for isolation.
Application-level tests should not rely on a clean database state, as resetting the database before each test can be slow and makes tests difficult to parallelize. Instead, design your tests to be independent by using unique user IDs for each test case.
Here's an example using TypeScript that mirrors the pgTAP tests above:
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
import{createClient}from'@supabase/supabase-js'import{beforeAll,describe,expect,it}from'vitest'importcryptofrom'crypto'describe('Todos RLS',()=>{// Generate unique IDs for this test suite to avoid conflicts with other testsconstUSER_1_ID=crypto.randomUUID()constUSER_2_ID=crypto.randomUUID()constsupabase=createClient(process.env.SUPABASE_URL!,process.env.SUPABASE_ANON_KEY!)beforeAll(async()=>{// Setup test data specific to this test suiteconstadminSupabase=createClient(process.env.SUPABASE_URL!,process.env.SERVICE_ROLE_KEY!)// Create test users with unique IDsawaitadminSupabase.auth.admin.createUser({id:USER_1_ID,email:`user1-${USER_1_ID}@test.com`,password:'password123',// We want the user to be usable right away without email confirmationemail_confirm:true,})awaitadminSupabase.auth.admin.createUser({id:USER_2_ID,email:`user2-${USER_2_ID}@test.com`,password:'password123',email_confirm:true,})// Create initial todosawaitadminSupabase.from('todos').insert([{task:'User 1 Task 1',user_id:USER_1_ID},{task:'User 1 Task 2',user_id:USER_1_ID},{task:'User 2 Task 1',user_id:USER_2_ID},])})it('should allow User 1 to only see their own todos',async()=>{// Sign in as User 1awaitsupabase.auth.signInWithPassword({email:`user1-${USER_1_ID}@test.com`,password:'password123',})const{data:todos}=awaitsupabase.from('todos').select('*')expect(todos).toHaveLength(2)todos?.forEach((todo)=>{expect(todo.user_id).toBe(USER_1_ID)})})it('should allow User 1 to create their own todo',async()=>{awaitsupabase.auth.signInWithPassword({email:`user1-${USER_1_ID}@test.com`,password:'password123',})const{error}=awaitsupabase.from('todos').insert({task:'New Task',user_id:USER_1_ID})expect(error).toBeNull()})it('should allow User 2 to only see their own todos',async()=>{// Sign in as User 2awaitsupabase.auth.signInWithPassword({email:`user2-${USER_2_ID}@test.com`,password:'password123',})const{data:todos}=awaitsupabase.from('todos').select('*')expect(todos).toHaveLength(1)todos?.forEach((todo)=>{expect(todo.user_id).toBe(USER_2_ID)})})it('should prevent User 2 from modifying User 1 todos',async()=>{awaitsupabase.auth.signInWithPassword({email:`user2-${USER_2_ID}@test.com`,password:'password123',})// Attempt to update the todos we shouldn't have access to// result will be a no-opawaitsupabase.from('todos').update({task:'Hacked!'}).eq('user_id',USER_1_ID)// Log back in as User 1 to verify their todos weren't changedawaitsupabase.auth.signInWithPassword({email:`user1-${USER_1_ID}@test.com`,password:'password123',})// Fetch User 1's todosconst{data:todos}=awaitsupabase.from('todos').select('*')// Verify that none of the todos were changed to "Hacked!"expect(todos).toBeDefined()todos?.forEach((todo)=>{expect(todo.task).not.toBe('Hacked!')})})})

```

#### Test isolation strategies[#](https://supabase.com/docs/guides/local-development/testing/overview#test-isolation-strategies)
For application-level testing, consider these approaches for test isolation:
  1. **Unique Identifiers** : Generate unique IDs for each test suite to prevent data conflicts
  2. **Cleanup After Tests** : If necessary, clean up created data in an `afterAll` or `afterEach` hook
  3. **Isolated Data Sets** : Use prefixes or namespaces in data to separate test cases


### Continuous integration testing[#](https://supabase.com/docs/guides/local-development/testing/overview#continuous-integration-testing)
Set up automated database testing in your CI pipeline:
  1. Create a GitHub Actions workflow `.github/workflows/db-tests.yml`:


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
name:Database Testson:push:branches:[main]pull_request:branches:[main]jobs:test:runs-on:ubuntu-lateststeps:-uses:actions/checkout@v4-name:Setup Supabase CLIuses:supabase/setup-cli@v1-name:Start Supabaserun:supabase start-name:Run Testsrun:supabase test db

```

## Best practices[#](https://supabase.com/docs/guides/local-development/testing/overview#best-practices)
  1. **Test Data Setup**
     * Use begin and rollback to ensure test isolation
     * Create realistic test data that covers edge cases
     * Use different user roles and permissions in tests
  2. **RLS Policy Testing**
     * Test Create, Read, Update, Delete operations
     * Test with different user roles: anonymous and authenticated
     * Test edge cases and potential security bypasses
     * Always test negative cases: what users should not be able to do
  3. **CI/CD Integration**
     * Run tests automatically on every pull request
     * Include database tests in deployment pipeline
     * Keep test runs fast using transactions


## Real-World examples[#](https://supabase.com/docs/guides/local-development/testing/overview#real-world-examples)
For more complex, real-world examples of database testing, check out:
  * [Database Tests Example Repository](https://github.com/usebasejump/basejump/tree/main/supabase/tests/database) - A production-grade example of testing RLS policies
  * [RLS Guide and Best Practices](https://github.com/orgs/supabase/discussions/14576)


## Troubleshooting[#](https://supabase.com/docs/guides/local-development/testing/overview#troubleshooting)
Common issues and solutions:
  1. **Test Failures Due to RLS**
     * Ensure you've set the correct role `set local role authenticated;`
     * Verify JWT claims are set `set local "request.jwt.claims"`
     * Check policy definitions match your test assumptions
  2. **CI Pipeline Issues**
     * Verify Supabase CLI is properly installed
     * Ensure database migrations are run before tests
     * Check for proper test isolation using transactions


## Additional resources[#](https://supabase.com/docs/guides/local-development/testing/overview#additional-resources)
  * [pgTAP Documentation](https://pgtap.org)
  * [Supabase CLI Reference](https://supabase.com/docs/reference/cli/supabase-test)
  * [pgTAP Supabase reference](https://supabase.com/docs/guides/database/extensions/pgtap?queryGroups=database-method&database-method=sql#testing-rls-policies)
  * [Database testing reference](https://supabase.com/docs/guides/database/testing)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/local-development/testing/overview.mdx)
### Is this helpful?
No Yes
### On this page
[Testing approaches](https://supabase.com/docs/guides/local-development/testing/overview#testing-approaches)[Database unit testing with pgTAP](https://supabase.com/docs/guides/local-development/testing/overview#database-unit-testing-with-pgtap)[Application-Level testing](https://supabase.com/docs/guides/local-development/testing/overview#application-level-testing)[Continuous integration testing](https://supabase.com/docs/guides/local-development/testing/overview#continuous-integration-testing)[Best practices](https://supabase.com/docs/guides/local-development/testing/overview#best-practices)[Real-World examples](https://supabase.com/docs/guides/local-development/testing/overview#real-world-examples)[Troubleshooting](https://supabase.com/docs/guides/local-development/testing/overview#troubleshooting)[Additional resources](https://supabase.com/docs/guides/local-development/testing/overview#additional-resources)
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



