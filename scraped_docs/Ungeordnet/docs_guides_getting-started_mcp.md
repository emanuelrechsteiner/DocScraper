---
url: http://supabase.com/docs/guides/getting-started/mcp
scraped_at: 2025-05-25T09:42:20.130874
title: Model context protocol (MCP) | Supabase Docs
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
  1. [Start with Supabase](https://supabase.com/docs/guides/getting-started)
  2. AI Tools
  3. [Model context protocol (MCP)](https://supabase.com/docs/guides/getting-started/mcp)


Model context protocol (MCP)
Connect your AI tools to Supabase using MCP
The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is a standard for connecting Large Language Models (LLMs) to platforms like Supabase. This guide covers how to connect Supabase to the following AI tools using MCP:
  * [Cursor](https://supabase.com/docs/guides/getting-started/mcp#cursor)
  * [Windsurf](https://supabase.com/docs/guides/getting-started/mcp#windsurf) (Codium)
  * [Visual Studio Code](https://supabase.com/docs/guides/getting-started/mcp#visual-studio-code-copilot) (Copilot)
  * [Cline](https://supabase.com/docs/guides/getting-started/mcp#cline) (VS Code extension)
  * [Claude desktop](https://supabase.com/docs/guides/getting-started/mcp#claude-desktop)
  * [Claude code](https://supabase.com/docs/guides/getting-started/mcp#claude-code)


Once connected, your AI assistants can interact with and query your Supabase projects on your behalf.
## Step 1: Create a personal access token (PAT)[#](https://supabase.com/docs/guides/getting-started/mcp#step-1-create-a-personal-access-token-pat)
First, go to your [Supabase settings](https://supabase.com/dashboard/account/tokens) and create a personal access token. Give it a name that describes its purpose, like "Cursor MCP Server". This will be used to authenticate the MCP server with your Supabase account.
## Step 2: Configure in your AI tool[#](https://supabase.com/docs/guides/getting-started/mcp#step-2-configure-in-your-ai-tool)
MCP compatible tools can connect to Supabase using the [Supabase MCP server](https://github.com/supabase-community/supabase-mcp). Below are instructions for connecting to this server using popular AI tools:
### Cursor[#](https://supabase.com/docs/guides/getting-started/mcp#cursor)
  1. Open [Cursor](https://www.cursor.com/) and create a `.cursor` directory in your project root if it doesn't exist.
  2. Create a `.cursor/mcp.json` file if it doesn't exist and open it.
  3. Add the following configuration:
macOSWindowsWindows (WSL)Linux
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
{"mcpServers":{"supabase":{"command":"npx","args":["-y","@supabase/mcp-server-supabase@latest","--access-token","<personal-access-token>"]}}}

```

Replace `<personal-access-token>` with your personal access token.
  4. Save the configuration file.
  5. Open Cursor and navigate to **Settings/MCP**. You should see a green active status after the server is successfully connected.


### Windsurf[#](https://supabase.com/docs/guides/getting-started/mcp#windsurf)
  1. Open [Windsurf](https://docs.codeium.com/windsurf) and navigate to the Cascade assistant.
  2. Tap on the hammer (MCP) icon, then **Configure** to open the configuration file.
  3. Add the following configuration:
macOSWindowsWindows (WSL)Linux
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
{"mcpServers":{"supabase":{"command":"npx","args":["-y","@supabase/mcp-server-supabase@latest","--access-token","<personal-access-token>"]}}}

```

Replace `<personal-access-token>` with your personal access token.
  4. Save the configuration file and reload by tapping **Refresh** in the Cascade assistant.
  5. You should see a green active status after the server is successfully connected.


### Visual Studio Code (Copilot)[#](https://supabase.com/docs/guides/getting-started/mcp#visual-studio-code-copilot)
  1. Open [VS Code](https://code.visualstudio.com/) and create a `.vscode` directory in your project root if it doesn't exist.
  2. Create a `.vscode/mcp.json` file if it doesn't exist and open it.
  3. Add the following configuration:
macOSWindowsWindows (WSL)Linux
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
{"inputs":[{"type":"promptString","id":"supabase-access-token","description":"Supabase personal access token","password":true}],"servers":{"supabase":{"command":"npx","args":["-y","@supabase/mcp-server-supabase@latest"],"env":{"SUPABASE_ACCESS_TOKEN":"${input:supabase-access-token}"}}}}

```

  4. Save the configuration file.
  5. Open Copilot chat and switch to "Agent" mode. You should see a tool icon that you can tap to confirm the MCP tools are available. Once you begin using the server, you will be prompted to enter your personal access token. Enter the token that you created earlier.


For more info on using MCP in VS Code, see the [Copilot documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).
### Cline[#](https://supabase.com/docs/guides/getting-started/mcp#cline)
  1. Open the [Cline](https://github.com/cline/cline) extension in VS Code and tap the **MCP Servers** icon.
  2. Tap **Configure MCP Servers** to open the configuration file.
  3. Add the following configuration:
macOSWindowsWindows (WSL)Linux
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
{"mcpServers":{"supabase":{"command":"npx","args":["-y","@supabase/mcp-server-supabase@latest","--access-token","<personal-access-token>"]}}}

```

Replace `<personal-access-token>` with your personal access token.
  4. Save the configuration file. Cline should automatically reload the configuration.
  5. You should see a green active status after the server is successfully connected.


### Claude desktop[#](https://supabase.com/docs/guides/getting-started/mcp#claude-desktop)
  1. Open [Claude desktop](https://claude.ai/download) and navigate to **Settings**.
  2. Under the **Developer** tab, tap **Edit Config** to open the configuration file.
  3. Add the following configuration:
macOSWindowsWindows (WSL)Linux
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
{"mcpServers":{"supabase":{"command":"npx","args":["-y","@supabase/mcp-server-supabase@latest","--access-token","<personal-access-token>"]}}}

```

Replace `<personal-access-token>` with your personal access token.
  4. Save the configuration file and restart Claude desktop.
  5. From the new chat screen, you should see a hammer (MCP) icon appear with the new MCP server available.


### Claude code[#](https://supabase.com/docs/guides/getting-started/mcp#claude-code)
  1. Create a `.mcp.json` file in your project root if it doesn't exist.
  2. Add the following configuration:
macOSWindowsWindows (WSL)Linux
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
{"mcpServers":{"supabase":{"command":"npx","args":["-y","@supabase/mcp-server-supabase@latest","--access-token","<personal-access-token>"]}}}

```

Replace `<personal-access-token>` with your personal access token.
  3. Save the configuration file.
  4. Restart [Claude code](https://claude.ai/code) to apply the new configuration.


### Next steps[#](https://supabase.com/docs/guides/getting-started/mcp#next-steps)
Your AI tool is now connected to Supabase using MCP. Try asking your AI assistant to create a new project, create a table, or fetch project config.
For a full list of tools available, see the [GitHub README](https://github.com/supabase-community/supabase-mcp#tools). If you experience any issues, [submit an bug report](https://github.com/supabase-community/supabase-mcp/issues/new?template=1.Bug_report.md).
## MCP for local Supabase instances[#](https://supabase.com/docs/guides/getting-started/mcp#mcp-for-local-supabase-instances)
The Supabase MCP server connects directly to the cloud platform to access your database. If you are running a local instance of Supabase, you can instead use the [Postgres MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) to connect to your local database. This MCP server runs all queries as read-only transactions.
### Step 1: Find your database connection string[#](https://supabase.com/docs/guides/getting-started/mcp#step-1-find-your-database-connection-string)
To connect to your local Supabase instance, you need to get the connection string for your local database. You can find your connection string by running:
```

1
supabasestatus

```

or if you are using `npx`:
```

1
npxsupabasestatus

```

This will output a list of details about your local Supabase instance. Copy the `DB URL` field in the output.
### Step 2: Configure the MCP server[#](https://supabase.com/docs/guides/getting-started/mcp#step-2-configure-the-mcp-server)
Configure your client with the following:
macOSWindowsWindows (WSL)Linux
```

1
2
3
4
5
6
7
8
{"mcpServers":{"supabase":{"command":"npx","args":["-y","@modelcontextprotocol/server-postgres","<connection-string>"]}}}

```

Replace `<connection-string>` with your connection string.
### Next steps[#](https://supabase.com/docs/guides/getting-started/mcp#next-steps)
Your AI tool is now connected to your local Supabase instance using MCP. Try asking the AI tool to query your database using natural language commands.
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/getting-started/mcp.mdx)
### Is this helpful?
No Yes
### On this page
[Step 1: Create a personal access token (PAT)](https://supabase.com/docs/guides/getting-started/mcp#step-1-create-a-personal-access-token-pat)[Step 2: Configure in your AI tool](https://supabase.com/docs/guides/getting-started/mcp#step-2-configure-in-your-ai-tool)[Cursor](https://supabase.com/docs/guides/getting-started/mcp#cursor)[Windsurf](https://supabase.com/docs/guides/getting-started/mcp#windsurf)[Visual Studio Code (Copilot)](https://supabase.com/docs/guides/getting-started/mcp#visual-studio-code-copilot)[Cline](https://supabase.com/docs/guides/getting-started/mcp#cline)[Claude desktop](https://supabase.com/docs/guides/getting-started/mcp#claude-desktop)[Claude code](https://supabase.com/docs/guides/getting-started/mcp#claude-code)[Next steps](https://supabase.com/docs/guides/getting-started/mcp#next-steps)[MCP for local Supabase instances](https://supabase.com/docs/guides/getting-started/mcp#mcp-for-local-supabase-instances)[Step 1: Find your database connection string](https://supabase.com/docs/guides/getting-started/mcp#step-1-find-your-database-connection-string)[Step 2: Configure the MCP server](https://supabase.com/docs/guides/getting-started/mcp#step-2-configure-the-mcp-server)[Next steps](https://supabase.com/docs/guides/getting-started/mcp#next-steps)
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



