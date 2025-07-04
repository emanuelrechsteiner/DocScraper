---
url: https://supabase.com/blog/how-pg-graphql-works
scraped_at: 2025-05-25T08:58:57.150836
title: How pg_graphql works
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# How pg_graphql works
24 Jan 2024
•
14 minute read
[![Raminder Singh avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fimor.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Raminder SinghEngineering](https://github.com/imor)
![How pg_graphql works](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fhow-pg-graphql-works%2Fthumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Supabase’s GraphQL API is powered by `pg_graphql`. In this post, we will look at the internal workings of `pg_graphql`. Since it is an extension written in the Rust programming language, familiar with Rust will help - although it’s not a requirement to understand this post.
This article will give you a deeper understanding of `pg_graphql` , helping you to:
  * Make design decisions about how to use GraphQL in your application.
  * Understand how a GraphQL query is processed internally by `pg_graphql`.
  * Understand, or even fix, simple bugs and implement beginner-friendly features in `pg_graphql`.


## What is pg_graphql?[#](https://supabase.com/blog/how-pg-graphql-works#what-is-pg_graphql)
`pg_graphql` is a [Postgres extension](https://supabase.com/docs/guides/database/extensions/pg_graphql) that reads the SQL schema in a database and exposes it as a [GraphQL](https://spec.graphql.org/October2021/) schema. The GraphQL interface is made available through a SQL function `graphql.resolve(...)` which allows any programming language to use GraphQL without any additional servers, processes, or libraries. It is also possible to call the `graphql.resolve(...)` function from [PostgREST](https://postgrest.org/en/stable/), or any other HTTP proxy, to safely expose the GraphQL API via HTTP/S.
## GraphQL request[#](https://supabase.com/blog/how-pg-graphql-works#graphql-request)
When a client sends a GraphQL request to `pg_graphql` it gets a response back. But do you know what happens inside `pg_graphql` to serve that request? Let’s take a look at the life of a GraphQL request.
The entry point of a request is the [`graphql.resolve(query, ..)`](https://github.com/supabase/pg_graphql/blob/master/sql/resolve.sql) function. This function calls the [`graphql._internal_resolve(query)`](https://github.com/supabase/pg_graphql/blob/941c7c7ae1d8e06dd4891d75fb1615a863d0c0e6/src/lib.rs#L25) function which is written in Rust and where the real magic starts. The [first line](https://github.com/supabase/pg_graphql/blob/941c7c7ae1d8e06dd4891d75fb1615a863d0c0e6/src/lib.rs#L33) in that function uses the [`graphql-parser` crate](https://github.com/graphql-rust/graphql-parser) to parse the GraphQL query into a tree structure. Let’s see how that works.
## Parsing GraphQL[#](https://supabase.com/blog/how-pg-graphql-works#parsing-graphql)
Parsing converts a query string into an abstract syntax tree (AST). This is a two-step process, first, a tokenizer converts the input string into tokens, and then a parser organizes the tokens into nodes of the AST.
### Tokenizer[#](https://supabase.com/blog/how-pg-graphql-works#tokenizer)
A tokenizer (aka a lexer) reads the query string and spits out tokens in the language. For example, take a look at the following query:
`
1
query {
2
 bookCollection {
3
  edges {
4
   node {
5
    id
6
   }
7
  }
8
 }
9
}
`
It will be turned into the following tokens by the tokenizer: `query`, `{`, `bookCollection`, `{`, `edges`, `{`, `node`, `{`, `id`, `}`, `}`, `}` and `}`. How does the tokenizer know where a token starts and ends? The tokenizer relies on [lexical grammar](https://spec.graphql.org/October2021/#sec-Appendix-Grammar-Summary) to figure out token boundaries. It looks at the next character in the text to first find the kind of token to expect and then uses the grammar rules for that token to find where it ends. For example, the first character in our example is `q` which means it must be a [`Name`](https://spec.graphql.org/October2021/#Name) because its grammar looks like this:
![lexical grammar](https://supabase.com/_next/image?url=images%2Fblog%2Fhow-pg-graphql-works%2Flexical-grammar.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The grammar tells the tokenizer that if the next character is a [`Letter`](https://spec.graphql.org/October2021/#Letter) or an underscore then it is the start of a `Name`. And when the tokenizer finds a character that is not a [`NameContinue`](https://spec.graphql.org/October2021/#NameContinue) it ends the token. In our example, the `Name` token ends before the first whitespace after `query`.
Note that the tokenizer’s job is to just produce valid lexical tokens, even if those tokens do not make a valid GraphQL query. For example, the tokenizer will happily produce the tokens `}`, `query`, and `{` for an input string `} query {`. It is the parser’s job to reject these sequences of tokens as invalid.
There are also tokens that the tokenizer ignores. There’s good reason, for example, to ignore whitespace because it allows you to format your code as you please. But a quirk of the lexical structure of GraphQL is that it also ignores commas. This means, you can stick a comma just about anywhere and the query would still be valid. E.g. the last example can also be rewritten as:
`
1
query, {,
2
 bookCollection, {,
3
  edges, {,
4
   node, {,
5
    id,
6
   },
7
  },
8
 },
9
},
`
It’s possible you haven’t heard that before. We suggest not abusing the comma; use it thoughtfully to write queries that are easy to read.
### Parser[#](https://supabase.com/blog/how-pg-graphql-works#parser)
The list of tokens produced by the tokenizer are consumed by the parser to generate the AST. The [parsing grammar](https://spec.graphql.org/October2021/#sec-Document-Syntax) dictates how the parser makes sense of the tokens. Since `pg_graphql` needs to execute the query, it expects an [`ExecutableDocument`](https://spec.graphql.org/October2021/#ExecutableDocument). So the parser tries to parse an `ExecutableDocument` which is defined in the grammar like this:
![executable document](https://supabase.com/_next/image?url=images%2Fblog%2Fhow-pg-graphql-works%2Fexecutable-document.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
An `ExecutableDocument` contains a list of [`ExecutableDefinitions`](https://spec.graphql.org/October2021/#ExecutableDefinition) which is defined like this:
![executable definitions](https://supabase.com/_next/image?url=images%2Fblog%2Fhow-pg-graphql-works%2Fexecutable-definitions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
An `ExecutableDefinition` can be either an [`OperationDefinition`](https://spec.graphql.org/October2021/#OperationDefinition) or a [`FragmentDefinition`](https://spec.graphql.org/October2021/#FragmentDefinition). Which one should the parser try to parse? Similar to how the tokenizer looks at the next character, the parser can look at the next token to know which definition lies next. The next token in our example is `query`. Can `query` appear at the beginning of `OperationDefinition`? Let’s check its definition:
![operation definition](https://supabase.com/_next/image?url=images%2Fblog%2Fhow-pg-graphql-works%2Foperation-definition.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The parser again has two choices since `OperationDefinition` can either be an `OperationType Name(opt) VariableDefinitions(opt) Directives(opt) SelectionSet` or a [`SelectionSet`](https://spec.graphql.org/October2021/#SelectionSet). So which of those two can start with `query?` The first one starts with [`OperationType`](https://spec.graphql.org/October2021/#OperationType) which is defined like this:
![operation definition](https://supabase.com/_next/image?url=images%2Fblog%2Fhow-pg-graphql-works%2Foperation-type.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Et voilà! The `query` token can start an `OperationType`, which means the parser now knows that it has to parse the first arm of the `OperationDefinition`. Which in turn means that it is going to parse an `OperationDefinition` arm of the `ExecutableDefinition`. Can’t the other arm of the definition also start with `query`? No, the language designers designed the grammar to avoid such ambiguities.
💡 This technique of looking at the next token (or the next few tokens) to find what to parse is called lookahead. The fewer the lookahead, the faster the parser. Fortunately, GraphQL has at most a few tokens of lookahead.
Now that the parser knows it will parse `OperationType Name(opt) VariableDefinitions(opt) Directives(opt) SelectionSet`, it skips the `query` token and looks at the next token, which is `{`. A `{` It can’t appear in the beginning of `Name(opt)`, `VariableDefinitions(opt)` or `Directives(opt)`, but it can start a `SelectionSet`:
![operation definition](https://supabase.com/_next/image?url=images%2Fblog%2Fhow-pg-graphql-works%2Fselection-set.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
So the parser skips past the `{` token and then tries to parse a list of `Selection`s. The parser parses the rest of the input string using the same process. It rejects an invalid list of tokens like `}`, `query` and `{` because no grammar rule starts with an `}`. For our example query, the parser generates the following AST:
`
1
Document {
2
 definitions: [Operation(Query(Query {
3
  name: None,
4
  variable_definitions: [],
5
  directives: [],
6
  selection_set: SelectionSet {
7
   items: [Field(Field {
8
    alias: None,
9
    name: "bookCollection",
10
    arguments: [],
11
    directives: [],
12
    selection_set: SelectionSet {
13
     items: [Field(Field {
14
      alias: None,
15
      name: "edges",
16
      arguments: [],
17
      directives: [],
18
      selection_set: SelectionSet {
19
       items: [Field(Field {
20
        alias: None,
21
        name: "node",
22
        arguments: [],
23
        directives: [],
24
        selection_set: SelectionSet {
25
         items: [Field(Field {
26
          alias: None,
27
          name: "id",
28
          arguments: [],
29
          directives: [],
30
          selection_set: SelectionSet { items: [] },
31
         })],
32
        },
33
       })],
34
      },
35
     })],
36
    },
37
   })],
38
  },
39
 }))],
40
}
`
An AST in `graphql-parser` is just Rust structs and enums. For example, the `Document` is a struct:
`
1
#[derive(Debug, Clone, PartialEq)]
2
pub struct Document<'a, T: Text<'a>> {
3
  pub definitions: Vec<Definition<'a, T>>,
4
}
`
A `Definition` is an enum:
`
1
#[derive(Debug, Clone, PartialEq)]
2
pub enum Definition<'a, T: Text<'a>> {
3
  Operation(OperationDefinition<'a, T>),
4
  Fragment(FragmentDefinition<'a, T>),
5
}
`
However, it is not enough to parse the query into an AST. Why? Similar to how a valid list of tokens produced by the tokenizer doesn’t mean it will produce a valid AST, a valid AST doesn’t mean that the AST can be executed by `pg_graphql`. So before execution, `pg_graphql` validates the AST.
## Validation[#](https://supabase.com/blog/how-pg-graphql-works#validation)
To understand why a valid AST doesn’t mean that the query can be executed take the following example. Here the query produced a valid AST but it is still invalid because there [can't be a named operation together with an anonymous operation](https://spec.graphql.org/October2021/#sec-Lone-Anonymous-Operation) in a GraphQL query:
`
1
{
2
 bookCollection {
3
  edges {
4
   node {
5
    id
6
   }
7
  }
8
 }
9
}
1011
query getBookNames {
12
 bookCollection {
13
  edges {
14
   node {
15
    name
16
   }
17
  }
18
 }
19
}
`
The above was just one example of the kind of validations performed. The GraphQL spec defines many other types of validations like:
  * [Operation names must be unique](https://spec.graphql.org/October2021/#sec-Operation-Name-Uniqueness).
  * [Field on a selection set must be defined](https://spec.graphql.org/October2021/#sec-Field-Selections) on the target type.
  * Literal [values in the query must be coercible to the expected type](https://spec.graphql.org/October2021/#sec-Values-of-Correct-Type).
  * Only [defined argument names are accepted](https://spec.graphql.org/October2021/#sec-Argument-Names).
  * And many more.


`pg_graphql` performs these validations and returns errors if they fail. For example:
  * Operation name uniqueness is tested in [`resolve_inner` function in `resolve.rs`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/resolve.rs#L65-L72).
  * Existence of fields in a selection set is tested in [`resolve_selection_set` function in `resolve.rs`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/resolve.rs#L179-L187).
  * Types of literal values are tested in [`validate_arg_from_type` function in `parser_util.rs`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/parser_util.rs#L276-L480).
  * Allowed arguments are tested in [`restrict_allowed_arguments` function in `builder.rs`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/builder.rs#L999-L1017).


💡 If you are familiar with compiler theory, you can think of the validation step as the semantic analysis phase of a compiler.
Some of the validations need to know the types in the reflected GraphQL schema. For example, for the [field selection](https://spec.graphql.org/October2021/#sec-Field-Selections) validation, the validation code must know which fields are defined on a GraphQL object. This information is contained in the reflected GraphQL schema.
## Schema Reflection[#](https://supabase.com/blog/how-pg-graphql-works#schema-reflection)
`pg_graphql` builds GraphQL schema by reading information from many [system catalogs](https://www.postgresql.org/docs/current/catalogs.html). The [`load_sql_context` function](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/sql_types.rs#L771-L886) reads this information into a [`Context` object](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/sql_types.rs#L573-L583) by running the query in the [`load_sql_context.sql` file](https://github.com/supabase/pg_graphql/blob/master/sql/load_sql_context.sql). `load_sql_context.sql` loads information about [enums](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L26), [composite](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L101) and [non-composite](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L67) types, [foreign keys](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L121), [schemas](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L178), [tables](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L204) and [functions](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/load_sql_context.sql#L369).
It might [look like](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/lib.rs#L49) the context is loaded for each GraphQL query, but this function is memoized for performance by the [`cached` attribute.](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/sql_types.rs#L771-L776) This means it will only be called again if its input argument `_config` of type [`Config`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/sql_types.rs#L566-L571) changes from the last time it was called.`Config` has three parts:
  1. Current search path. It is a list of schemas that are searched in order when looking up a database object.
  2. Current role. It is the role under which any SQL statements will be executed.
  3. Current schema version. It is the current version of the database’s schema. The version is updated by a couple of [triggers that detect changes in schema](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/sql/schema_version.sql#L23-L29).


It makes sense to reload the schema if any `Config` fields change because they can potentially alter the results of running transpiled SQL statements.
The `Context` object is wrapped in a [`__Schema`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/graphql.rs#L3827-L3830) object which is used to not only serve [introspection](https://spec.graphql.org/October2021/#sec-Introspection) queries but also provide information to run validations and for transpilation to SQL. For example, take a look at [how tables are converted into`<table_name>Collection`s](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/graphql.rs#L1184-L1216). This code adds `Collection` objects to the [`QueryType`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/graphql.rs#L936-L939) object by iterating over tables and adding a `<table_name>Collection`field. Notice how`QueryType`'s `schema` field is used extensively throughout this code snippet.
## Transpilation and Query Execution[#](https://supabase.com/blog/how-pg-graphql-works#transpilation-and-query-execution)
Transpilation is a two-step process. First, builder objects are constructed from the AST and `__Schema`, and then the builder objects are converted into SQL. A builder object contains all the information needed to produce a SQL query.
For example, when a table is added as a collection object to the `QueryType` object, [its `type_` field is set to `__Type::Connection(_)`](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/graphql.rs#L1204). This type is then [checked in the `resolve_selection_set` function](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/resolve.rs#L188) and [converted to an appropriate builder type](https://github.com/supabase/pg_graphql/blob/3cb00f7b778a027375896f7b29ebed8a73ea7dbf/src/resolve.rs#L190-L197). A builder implements the [`QueryEntrypoint` trait](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L69-L98). `QueryEntrypoint` has only one required method named `to_sql_entrypoint` which the [`ConnectionBuilder` implements](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L1071-L1075) by calling [its `to_sql` method](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L908-L1068). The `to_sql` method contains the meat of the logic to generate SQL.
💡 There’s also a [`MutationEntrypoint` trait](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L35) for mutation queries with a similar [`execute` method](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L38-L66).
An important aspect of the SQL generation code is how it calls [`quote_ident`](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L14-L16) and [`quote_literal`](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L18-L20) functions to avoid SQL injection. Without them, a caller could potentially send a specially crafted input to execute arbitrary SQL code.
The generated SQL code is then run in the [`execute` method of `QueryEntrypoint` trait](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L72-L98). The transpiled queries return a [`jsonb` object](https://www.postgresql.org/docs/current/datatype-json.html) which is deserialized into a [`pgrx::JsonB` object](https://github.com/pgcentralfoundation/pgrx/blob/e7112edb6686519d22ae5a5101692d6ea1e8b9b5/pgrx/src/datum/json.rs#L20-L22). Since `pgrx::JsonB` is a wrapper over a [`serde_json::Value` object](https://github.com/serde-rs/json/blob/f88bf1fccb05aa4de129675de44eb6aaf3fec0a0/src/value/mod.rs#L116-L176), it is trivial for the [code to unwrap it](https://github.com/supabase/pg_graphql/blob/490214d1713b1e30b07fa7f53f210ee952a65f34/src/transpile.rs#L93) and return this as a `JSON` response to the client.
## Conclusion[#](https://supabase.com/blog/how-pg-graphql-works#conclusion)
In this post, we looked at how `pg_graphql` processes a GraphQL request. A request goes through the steps of tokenization, parsing, validation, transpilation, and execution. We looked in detail at the actions `pg_graphql` performs in each step. This knowledge should equip you to understand how `pg_graphql` works internally and help you make more informed decisions about how you can better use GraphQL APIs. If you feel ambitious, you can also start contributing to `pg_graphql` which we always welcome.
## More pg_graphql[#](https://supabase.com/blog/how-pg-graphql-works#more-pg_graphql)
  * [pg_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)
  * [What's New in pg_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)
  * [Supabase GraphQL docs](https://supabase.com/docs/guides/graphql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-pg-graphql-works&text=How%20pg_graphql%20works)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-pg-graphql-works&text=How%20pg_graphql%20works)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-pg-graphql-works&t=How%20pg_graphql%20works)
[Last postCreate a Figma Clone app with Flutter and Supabase Realtime26 January 2024](https://supabase.com/blog/flutter-figma-clone)
[Next postGetting started with Laravel and Postgres22 January 2024](https://supabase.com/blog/laravel-postgres)
[pg-graphql](https://supabase.com/blog/tags/pg-graphql)[supabase-engineering](https://supabase.com/blog/tags/supabase-engineering)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [What is pg_graphql?](https://supabase.com/blog/how-pg-graphql-works#what-is-pg_graphql)
  * [GraphQL request](https://supabase.com/blog/how-pg-graphql-works#graphql-request)
  * [Parsing GraphQL](https://supabase.com/blog/how-pg-graphql-works#parsing-graphql)
    * [Tokenizer](https://supabase.com/blog/how-pg-graphql-works#tokenizer)
    * [Parser](https://supabase.com/blog/how-pg-graphql-works#parser)
  * [Validation](https://supabase.com/blog/how-pg-graphql-works#validation)
  * [Schema Reflection](https://supabase.com/blog/how-pg-graphql-works#schema-reflection)
  * [Transpilation and Query Execution](https://supabase.com/blog/how-pg-graphql-works#transpilation-and-query-execution)
  * [Conclusion](https://supabase.com/blog/how-pg-graphql-works#conclusion)
  * [More pg_graphql](https://supabase.com/blog/how-pg-graphql-works#more-pg_graphql)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-pg-graphql-works&text=How%20pg_graphql%20works)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-pg-graphql-works&text=How%20pg_graphql%20works)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fhow-pg-graphql-works&t=How%20pg_graphql%20works)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

