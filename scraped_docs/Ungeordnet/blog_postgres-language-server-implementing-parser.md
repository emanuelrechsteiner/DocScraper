---
url: https://supabase.com/blog/postgres-language-server-implementing-parser
scraped_at: 2025-05-25T09:45:45.618353
title: Postgres Language Server: implementing the Parser
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
# Postgres Language Server: implementing the Parser
08 Dec 2023
•
26 minute read
[![Philipp Steinrötter avatar](https://supabase.com/_next/image?url=%2Fimages%2Fphilipp-steinrotter.jpg&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Philipp SteinrötterGuest Author](https://twitter.com/psteinroe)
![Postgres Language Server: implementing the Parser](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-postgres-language-server%2Fpostgres-language-server-thumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
During our previous Launch Week we [announced](https://news.ycombinator.com/item?id=37020610) the development of a [Postgres Language Server](https://github.com/supabase/postgres_lsp). The response was more enthusiastic than we imagined and we received some excellent ideas.
This is an update on the Parser, which is the fundamental primitive of a Language Server. We’ve been through several iterations of the parser and we want to detail our explorations.
Want to learn some more acronyms?
There will be a few acronyms in this post. We don’t want this post to be “inside baseball” so here are a few concepts that you need to know:
  * _**LSP / Language Server Protocol:**_ Something that helps code editors understand code better. It provides functionality like linting and error detection.
  * **Postgres Language Server:** a server that will help with Postgres programming - writing SQL, type inference, etc.
  * **Parser** : A parser converts written code into a form that tools can work with. For example, it identifies variables in code. and then the tools can easily access those variables. We’ll describe this more below.


## Background: Why build a Language Server?[#](https://supabase.com/blog/postgres-language-server-implementing-parser#background-why-build-a-language-server)
Postgres is gaining popularity, and yet the tooling around it still needs a lot of work. Writing SQL in editors like VSCode is a pain. One of the unique features of Supabase is the ability to access your Postgres database from a browser or mobile app through our [Data APIs](https://supabase.com/docs/guides/api). This means that developers are writing more [PL/pgSQL](https://www.postgresql.org/docs/current/plpgsql.html).
While code editors have great support for most programming languages, SQL support is underwhelming. We want to make Postgres as simple as Python.
## Language Server's Core: The Role of the Parser[#](https://supabase.com/blog/postgres-language-server-implementing-parser#language-servers-core-the-role-of-the-parser)
On the highest level, a language server is a thing which
  1. accepts input source code from the client
  2. turns it into a semantic model of the code
  3. and provides language-specific smarts back to the client.


![Diagram explaining how a Language server works and the role of the parser](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-postgres-language-server%2Flanguage-server-diagram-dark-mode.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
The parser is the core of every language server. It takes the raw string, turns it into a stream of tokens, and builds a syntax tree. This syntax tree can then be used to extract structural information.
Usually, the parser builds a concrete [syntax tree](https://en.wikipedia.org/wiki/Parse_tree) (CST) before turning it into an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (AST). A CST preserves all syntax elements present in the source code with the goal of being able to re-create the exact original source, while an AST contains only the meaning of the source. For example, take a simple expression `2 * (7 + 3)`:
`
1
      CST          AST
2
     -----         -----
3
     expr           *
4
    /  |  \        /  \
5
 term   *  term       2   +
6
  |       |          / \
7
factor     factor        7  3   
8
  |     /  |  \
9
  2    (  expr  )  
10
       / | \
11
     term  + term
12
      |    |
13
     factor  factor
14
      |    |
15
      7    3 
`
## Implementing a Parser for Postgres[#](https://supabase.com/blog/postgres-language-server-implementing-parser#implementing-a-parser-for-postgres)
Implementing a parser for Postgres is challenging because of the ever-evolving and complex syntax of Postgres. Even `select` statements are very complex to parse. Then there are common table expressions, sub-queries and the like. This is one of the reasons why existing Postgres tooling is scarce, badly maintained, and often does not work well.
We decided to not create a custom parser. Instead, we leverage [libpg_query](https://github.com/pganalyze/libpg_query) to parse SQL code reliably. The pganalyze team has a published a great blog post on [why this approach is preferable](https://pganalyze.com/blog/parse-postgresql-queries-in-ruby).
However, libpg _query is designed to parse _executable_ SQL — not to provide language intelligence. Using it for a language server means adapting it to our specific use case. Let’s explore how we adapted it:
### Tokenization[#](https://supabase.com/blog/postgres-language-server-implementing-parser#tokenization)
Before any syntax tree can be built, the input string needs to be converted into a stream of tokens. libpg_query exposes a `scan` API that returns all non-whitespace tokens of the source, even for invalid SQL. For example, a simple statement `select '1';` returns
`
1
ScanToken {
2
    start: 0,
3
    end: 6,
4
    token: Select,
5
    keyword_kind: ReservedKeyword,
6
},
7
ScanToken {
8
		  start: 7,
9
		  end: 10,
10
    token: Sconst,
11
    keyword_kind: NoKeyword,
12
},
13
ScanToken {
14
    start: 10,
15
    end: 11,
16
    token: Ascii59,
17
    keyword_kind: NoKeyword,
18
}
`
Every `ScanToken` token contains its variant, a range, and a keyword kind. To simplify the implementation of the parser, we extract the text for each token using the range for now. We arrive at the following `Token` struct.
`
1
pub struct Token {
2
  /// The kind of the token
3
  pub kind: SyntaxKind,
4
  /// Text from the input
5
  pub text: String,
6
  /// Range within the input
7
  pub span: TextRange,
8
  /// Variants from `ScanToken.keyword_kind` + `Whitespace`
9
  pub token_type: TokenType,
10
}
`
To have a complete token stream, we merge the results of `scan` with a list of all whitespace tokens in the source, where the latter are extracted by a simple regular expression. For a simple statement `select '1';`, the following tokens are returned by the lexer.
`
1
[
2
  Token {
3
    kind: Select,
4
    text: "select",
5
    span: 0..6,
6
    token_type: ReservedKeyword,
7
  },
8
  Token {
9
    kind: Whitespace,
10
    text: " ",
11
    span: 6..7,
12
    token_type: Whitespace,
13
  },
14
  Token {
15
    kind: Sconst,
16
    text: "'1'",
17
    span: 7..10,
18
    token_type: NoKeyword,
19
  },
20
  Token {
21
    kind: Ascii59,
22
    text: ";",
23
    span: 10..11,
24
    token_type: NoKeyword,
25
  },
26
]
`
### Conversion to a Syntax Tree[#](https://supabase.com/blog/postgres-language-server-implementing-parser#conversion-to-a-syntax-tree)
To transform the stream of tokens into a syntax tree, we face the first challenges with `libpg_query`. In a language server, it's important to handle incomplete or improperly formatted input gracefully. When an error occurs you don’t want the parser to “stop”. You want it to check for _all_ errors in your code:
`
1
create table posts (
2
 id serial primary key # <- ERR: missing comma, Parser should continue
3
 content text
4
);
56
create table comments (
7
 id serial primary key,
8
 post_id int references posts # <- ERR: missing comma, second error returned
9
 comment text
10
);
`
Unfortunately, the `parse` api from `libpg_query` only parses the entire input — if any SQL statement contains a syntax error, an error is returned for the entire input.
To overcome this, we implemented a resilient `source` parser. This parser breaks the input into individual SQL statements and parses them one by one, allowing us to handle syntax errors within each statement independently. It is implemented as a top-down [LL parser](https://en.wikipedia.org/wiki/LL_parser). Specifically, the parser iterates the token stream left-to-right, and checks if the cursor currently is at the start of a new statement. Once a statement is entered, it walks the tokens until `;` or another statement start is encountered while skipping sub-statements.
Luckily, Postgres statements always start with distinct keywords. An update statement is identifiable with `update`, a delete statement with `delete from`. There are a few statements that need more than the first few tokens to be distinguishable, but we only care about whether there is a statement, and not what statement there is exactly, so ambiguity is very much acceptable.
For the implementation, we only need to provide the distinct keywords each statement starts with and compare it to the current tokens using a lookahead mechanism.
💡 Our LL parser is very simple. For more details check out [this blog post](https://matklad.github.io/2023/05/21/resilient-ll-parsing-tutorial.html).
### Reverse-Engineering the CST[#](https://supabase.com/blog/postgres-language-server-implementing-parser#reverse-engineering-the-cst)
The second limitation we encountered: `libpg_query` only exposes an API for the AST, not for the CST. To provide language intelligence on the source code, both are required. Since we do not want to implement our own parser, we need to work with what we have to build the CST: the AST and a stream of tokens. The goal is to reverse-engineer the AST into the CST. This involves re-using the AST nodes as CST nodes, and figuring out what token belongs beneath what node. The exemplary statement `select '1';` should be be parsed into
`
1
SelectStmt@0..11
2
  Select@0..6 "select"
3
  Whitespace@6..7 " "
4
  ResTarget@7..10
5
   AConst@7..10
6
    Sconst@7..10 "'1'"
7
  Ascii59@10..11 ";"
`
To do that, we need to know the range of every node that is within the AST.
We made _numerous_ iterations over the past few months to figure out how to accomplish this with minimal manual implementations. Before diving into details, lets take a closer look at the `parse` API of `libpg_query`. For the exemplary statement above, it returns (simplified for readability):
`
1
SelectStmt {
2
  target_list: [
3
	  ResTarget {
4
	    val: Some(
5
	      Node {
6
	        node: Some(
7
	         AConst {
8
	           location: 7,
9
	           val: Some(
10
	             Sval(
11
	               String {
12
	                 sval: "1",
13
	               },
14
	             ),
15
	           ),
16
	         },
17
	        ),
18
	      },
19
	    ),
20
	    location: 7,
21
	  },
22
  ],
23
}
`
There are a few limitations:
  1. Some nodes do have a `location` property that indicates where the node starts in the source, but not all.
  2. There is no information on the range of a node within the source.
  3. Some locations are not what you would expect. For example the location of the expression node is the location of the operator, not the start of the left expression.


To summarise: _we need a range for each node, and we only have a start position, but not always, and sometimes it is wrong._
Our first very iterations were naive. We explored what information we could extract from `scan` and `parse`, and if anything can help in reverse-engineering the CST.
It turns out, the most reliable way of determining the range of a node is by knowing all **properties** of that node, and its position in the tree.
A property is any text for which a Token can potentially be found in the source code. For example, a `SelectStmt` node has the `select` keyword as a property, and if there is a `from_clause`, a `from` keyword. For the exemplary statement above, the properties are
`
1
SelectStmt: [Select],
2
RangeVar: [],
3
AConst: ['1']
`
Note that we do not have an extra `String` node, and instead add its properties to the parent `AConst` node. This reason is that a `String` node does not bring any value to the CST, since we already know that `‘1'` is a string from the kind of the respective `Token`. The same is true for all nodes that just contain type information such as `Integer`, `Boolean` and `Float`.
The position of any node is the same in AST and CST, and thereby can be reflected from it.
### Implementation[#](https://supabase.com/blog/postgres-language-server-implementing-parser#implementation)
Before the actual parsing begins, the AST returned by `parse` is converted into an uniform tree structure where each node holds the kind of the node, a list of properties, the depth and, if available, the location.
For example, for `select '1';`:
`
1
edges: (0, 1), (1, 2),
2
nodes: {
3
  0: Node {
4
    kind: SelectStmt,
5
    depth: 1,
6
    properties: [
7
      TokenProperty {
8
        value: None,
9
        kind: Some(
10
          Select,
11
        ),
12
      },
13
    ],
14
    location: None,
15
  },
16
  1: Node {
17
    kind: ResTarget,
18
    depth: 2,
19
    properties: [],
20
    location: Some(
21
      7,
22
    ),
23
  },
24
  2: Node {
25
    kind: AConst,
26
    depth: 3,
27
    properties: [
28
      TokenProperty {
29
        value: Some(
30
          "1",
31
        ),
32
        kind: None,
33
      },
34
    ],
35
    location: Some(
36
      7,
37
    ),
38
  },
39
},
`
To implement such a conversion we need a way to
  * get an `Option<usize>` with the location for every node type, if any
  * compile a list of all properties that a node contains
  * walk down the AST until the leaves are reached


Due to the strict type system of Rust, a manual implementation would be a significant and repetitive effort. With languages such as JavaScript, getting the location of a node would be as simple as `node?.location`. In Rust, a large match statement covering all possible nodes is required to do the same. Luckily, `libpg_query` exports a protobuf definition containing all AST nodes and their fields. For example, an `AExpr` node is defined as
`
1
message A_Expr
2
{
3
 A_Expr_Kind kind = 1 [json_name="kind"];
4
 repeated Node name = 2 [json_name="name"];
5
 Node lexpr = 3 [json_name="lexpr"];
6
 Node rexpr = 4 [json_name="rexpr"];
7
 int32 location = 5 [json_name="location"];
8
}
`
We introspect that definition to generate code at build time using [procedural macros](https://doc.rust-lang.org/reference/procedural-macros.html).
Leveraging the powerful repetition feature of the [`quote`](https://github.com/dtolnay/quote) crate, the `match` statement of a `get_location` function can be implemented with just a few lines of code.
`
1
pub fn get_location_mod(_item: proc_macro2::TokenStream) -> proc_macro2::TokenStream {
2
		// Parse the proto file using a custom parser
3
		let parser = ProtoParser::new("libpg_query/protobuf/pg_query.proto");
4
  let proto_file = parser.parse();
56
		// get all node identifiers for the left side of the match arm
7
		let node_identifiers = node_identifiers(&proto_file.nodes);
8
		// get a TokenStream for each node that returns the location
9
		// if it is part of the node properties
10
  let location_idents = location_idents(&proto_file.nodes);
1112
  quote! {
13
    /// Returns the location of a node
14
    pub fn get_location(node: &NodeEnum) -> Option<usize> {
15
      match node {
16
        #(NodeEnum::#node_identifiers(n) => #location_idents),*
17
						}
18
    }
19
  }
20
}
`
The `location_idents` function iterates all nodes, searches for a `location` property in the protobuf definition for each node, and returns a `TokenStream` with either `Some(n.location)` or `None` for each.
`
1
fn location_idents(nodes: &[Node]) -> Vec<TokenStream> {
2
  nodes
3
    .iter()
4
    .map(|node| {
5
      if node
6
        .fields
7
        .iter()
8
								// has location property?
9
        .find(|n| n.name == "location" && n.field_type == FieldType::Int32)
10
        .is_some()
11
      {
12
        quote! { Some(n.location) }
13
      } else {
14
        quote! { None }
15
      }
16
    })
17
    .collect()
18
}
`
Similarly, we can generate code to recursively walk down the `FieldType == Node` and `FieldType == Vec<Node>` properties of the AST nodes. No manual work required.
Even the function that returns all properties for a node can be generated, at least partly. All AST fields of `FieldType == String` can always be added to the list of properties. In the example above, the `sval: “1”` of the `String` node makes up the properties of its parent, the `AConst` node. What is remaining are mostly just the keywords that need to be defined for every node. A `SelectStmt` node has the `select` keyword as a property, and if there is a `from_clause`, a `from` keyword.
`
1
fn custom_handlers(node: &Node) -> TokenStream {
2
  match node.name.as_str() {
3
			"SelectStmt" => quote! {
4
			  tokens.push(TokenProperty::from(Token::Select));
5
			  if n.from_clause.len() > 0 {
6
			    tokens.push(TokenProperty::from(Token::From));
7
			  }
8
					...
9
			},
10
		...
11
}
`
💡 Implementing this for every node is a time-consuming effort, and _**we would love to get help from the community**_ here. Check out [this issue](https://github.com/supabase/postgres_lsp/issues/51) if you like to support.
### Parsing a Statement[#](https://supabase.com/blog/postgres-language-server-implementing-parser#parsing-a-statement)
After the tree has been generated, the parser goes through the tokens and finds the node in whose properties the current token can be found. But not every node is a possible successor. Lets look how the parser builds the CST for the statement `select '1' from contact` at a high level.
We start with the full tree, and all tokens:
`
1
Remaining Tokens: ["select", "'1'", "from", "contact"]
23
Parse Tree:
45
 SelectStmt (0, [Select, From])
6
     /     \
7
1 (ResTarget, [])  2 (RangeVar, ['contact'])
8
    |       
9
 3 (AConst, ['1'])
`
Starting with the root node, the parser first searches the current node for the token. In this case, with success. `Select` is removed from `SelectStmt` .
In the next iteration, we search for `'1'`. Since its not in the current node, a breadth-first search is used to find the property within children nodes. We arrive at `AConst` , open all nodes we encountered along the way, and advance.
`
1
Remaining Tokens: ["from", "contact"]
23
Parse Tree:
45
 SelectStmt (0, [From])
6
     /     \
7
1 (ResTarget, [])  2 (RangeVar, ['contact'])
8
    |       
9
 3 (AConst, []) 
1011
CST:
12
SelectStmt
13
  Select@0..6 "select"
14
  Whitespace@6..7 " "
15
  ResTarget@7..10
16
   AConst@7..10
17
    Sconst@7..10 "'1'"
`
Since we arrived at a leaf node with no properties left, the next token can not be part of this node or any child. It can be closed immediately after advancing the token. We remove it from the tree and set the current node to its parent. The same now applies to `ResTarget`, so we arrive back at `SelectStmt`:
`
1
Remaining Tokens: ["from", "contact"]
23
Parse Tree:
45
 SelectStmt (0, [From])
6
          \
7
           2 (RangeVar, ['contact'])
89
CST:
10
SelectStmt
11
  Select@0..6 "select"
12
  Whitespace@6..7 " "
13
  ResTarget@7..10
14
   AConst@7..10
15
    Sconst@7..10 "'1'"
`
The `from` token can once again be found within the current node and we just advance the parser. Since `SelectStmt` is not a leaf node, we stay where we are.
`
1
Remaining Tokens: ["contact"]
23
Parse Tree:
45
 SelectStmt (0, [])
6
          \
7
           2 (RangeVar, ['contact'])
89
CST:
10
SelectStmt
11
  Select@0..6 "select"
12
  Whitespace@6..7 " "
13
  ResTarget@7..10
14
   AConst@7..10
15
    Sconst@7..10 "'1'"
16
  Whitespace@10..11 " "
17
  From@11..15 "from"
`
From here, it repeats itself: `contact` is found within `RangeVar` using a breadth-first search. It becomes a leaf node that is closed after applying the token. Since no tokens are left, we finish parsing by closing `SelectStmt`, resulting in:
`
1
SelectStmt@0..23
2
  Select@0..6 "select"
3
  Whitespace@6..7 " "
4
  ResTarget@7..10
5
   AConst@7..10
6
    Sconst@7..10 "'1'"
7
  Whitespace@10..11 " "
8
  From@11..15 "from"
9
  Whitespace@15..16 " "
10
  RangeVar@16..23
11
   Ident@16..23 "contact"
`
Keep in mind, this illustration shows you only an overview of the process.If you are interested in the details, take a look at the source code [here](https://github.com/supabase/postgres_lsp/blob/2bb50e7b0733bd4cf630aba453d5132d03dfc113/crates/parser/src/parse/libpg_query_node.rs).
You may have noticed that neither `location` nor `depth` were mentioned. Both are only used to improve performance and safeguard. Among other things, branches with nodes behind the current position of the parser are skipped. Further, the parser panics when a node is opened and either its position or its depth does not match the current state of the parser. This means that the returned CST is guaranteed to be correct.
### Limitations[#](https://supabase.com/blog/postgres-language-server-implementing-parser#limitations)
If the SQL is invalid and `parse` returns an error, the returned CST is just a flat list of tokens. Consequently, the statement parser is not resilient. This is not great, but we have intentionally implemented it so that custom and resilient implementations can be added statement by statement later.
Ultimately, we want the `libpg_query`-based parser to just serve as a fallback. For now however, our goal is to provide a usable language server as fast as possible. And even if some intelligence features will only work on valid statements, we believe it is still better than what we have today: no intelligence at all.
## Next Steps[#](https://supabase.com/blog/postgres-language-server-implementing-parser#next-steps)
There are some minor improvements remaining for the parser. But the largest part are the manual implementations missing in `get_node_properties` . Its a time-consuming effort, and **_we would love to get help from the community_** here. Check out [this issue](https://github.com/supabase/postgres_lsp/issues/51) if you like to support.
After that, we will move on to the semantic data model and the language server itself. Other parser features such as support for [PL/pgSQL](https://www.postgresql.org/docs/current/plpgsql.html) function body parsing will be added later. We want to get this project into a usable state as fast as possible.
[Launch Week ![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/launch-week)
11-15 Dec
Main Stage
[Day 1 -Supabase Studio: introducing an **AI Assistant** , **Postgres roles** , and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)[ Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)[Day 3 -Introducing Supabase **Branching** , a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)[Day 4 -Supabase Auth: **Identity Linking** , **Session Control** , **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)[ Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage
[01 -Supabase Album](https://supabase.productions/)[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)[05 -pg_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server-implementing-parser&text=Postgres%20Language%20Server%3A%20implementing%20the%20Parser)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server-implementing-parser&text=Postgres%20Language%20Server%3A%20implementing%20the%20Parser)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server-implementing-parser&t=Postgres%20Language%20Server%3A%20implementing%20the%20Parser)
[Last postHow design works at Supabase8 December 2023](https://supabase.com/blog/how-design-works-at-supabase)
[Next postSupabase Beta November 20235 December 2023](https://supabase.com/blog/beta-update-november-2023)
[launch-week](https://supabase.com/blog/tags/launch-week)[postgres](https://supabase.com/blog/tags/postgres)[planetpg](https://supabase.com/blog/tags/planetpg)
On this page
  * [Background: Why build a Language Server?](https://supabase.com/blog/postgres-language-server-implementing-parser#background-why-build-a-language-server)
  * [Language Server's Core: The Role of the Parser](https://supabase.com/blog/postgres-language-server-implementing-parser#language-servers-core-the-role-of-the-parser)
  * [Implementing a Parser for Postgres](https://supabase.com/blog/postgres-language-server-implementing-parser#implementing-a-parser-for-postgres)
    * [Tokenization](https://supabase.com/blog/postgres-language-server-implementing-parser#tokenization)
    * [Conversion to a Syntax Tree](https://supabase.com/blog/postgres-language-server-implementing-parser#conversion-to-a-syntax-tree)
    * [Reverse-Engineering the CST](https://supabase.com/blog/postgres-language-server-implementing-parser#reverse-engineering-the-cst)
    * [Implementation](https://supabase.com/blog/postgres-language-server-implementing-parser#implementation)
    * [Parsing a Statement](https://supabase.com/blog/postgres-language-server-implementing-parser#parsing-a-statement)
    * [Limitations](https://supabase.com/blog/postgres-language-server-implementing-parser#limitations)
  * [Next Steps](https://supabase.com/blog/postgres-language-server-implementing-parser#next-steps)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server-implementing-parser&text=Postgres%20Language%20Server%3A%20implementing%20the%20Parser)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server-implementing-parser&text=Postgres%20Language%20Server%3A%20implementing%20the%20Parser)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-language-server-implementing-parser&t=Postgres%20Language%20Server%3A%20implementing%20the%20Parser)
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
![Diagram explaining how a Language server works and the role of the parser](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-postgres-language-server%2Flanguage-server-diagram-dark-mode.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

