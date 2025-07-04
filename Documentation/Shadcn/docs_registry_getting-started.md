---
url: https://ui.shadcn.com/docs/registry/getting-started
scraped_at: 2025-05-24T22:26:47.612045
title: Getting Started - shadcn/ui
---

[shadcn/ui](https://ui.shadcn.com/)[Docs](https://ui.shadcn.com/docs/installation)[Components](https://ui.shadcn.com/docs/components)[Blocks](https://ui.shadcn.com/blocks)[Charts](https://ui.shadcn.com/charts)[Themes](https://ui.shadcn.com/themes)[Colors](https://ui.shadcn.com/colors)
Toggle MenuSearch documentation...
Search documentation...Search...`⌘K`
[GitHub](https://github.com/shadcn-ui/ui)Toggle theme
#### Getting Started 
[Introduction](https://ui.shadcn.com/docs)[Installation](https://ui.shadcn.com/docs/installation)[components.json](https://ui.shadcn.com/docs/components-json)[Theming](https://ui.shadcn.com/docs/theming)[Dark mode](https://ui.shadcn.com/docs/dark-mode)[CLI](https://ui.shadcn.com/docs/cli)[Monorepo](https://ui.shadcn.com/docs/monorepo)[Tailwind v4New](https://ui.shadcn.com/docs/tailwind-v4)[Next.js 15 + React 19](https://ui.shadcn.com/docs/react-19)[Typography](https://ui.shadcn.com/docs/components/typography)[Open in v0](https://ui.shadcn.com/docs/v0)[Blocks](https://ui.shadcn.com/docs/blocks)[Figma](https://ui.shadcn.com/docs/figma)[Changelog](https://ui.shadcn.com/docs/changelog)
#### Installation 
[Next.js](https://ui.shadcn.com/docs/installation/next)[Vite](https://ui.shadcn.com/docs/installation/vite)[Laravel](https://ui.shadcn.com/docs/installation/laravel)[React Router](https://ui.shadcn.com/docs/installation/react-router)[Remix](https://ui.shadcn.com/docs/installation/remix)[Astro](https://ui.shadcn.com/docs/installation/astro)[Tanstack Start](https://ui.shadcn.com/docs/installation/tanstack)[Tanstack Router](https://ui.shadcn.com/docs/installation/tanstack-router)[Manual](https://ui.shadcn.com/docs/installation/manual)
#### Components 
[Accordion](https://ui.shadcn.com/docs/components/accordion)[Alert](https://ui.shadcn.com/docs/components/alert)[Alert Dialog](https://ui.shadcn.com/docs/components/alert-dialog)[Aspect Ratio](https://ui.shadcn.com/docs/components/aspect-ratio)[Avatar](https://ui.shadcn.com/docs/components/avatar)[Badge](https://ui.shadcn.com/docs/components/badge)[Breadcrumb](https://ui.shadcn.com/docs/components/breadcrumb)[Button](https://ui.shadcn.com/docs/components/button)[Calendar](https://ui.shadcn.com/docs/components/calendar)[Card](https://ui.shadcn.com/docs/components/card)[Carousel](https://ui.shadcn.com/docs/components/carousel)[Chart](https://ui.shadcn.com/docs/components/chart)[Checkbox](https://ui.shadcn.com/docs/components/checkbox)[Collapsible](https://ui.shadcn.com/docs/components/collapsible)[Combobox](https://ui.shadcn.com/docs/components/combobox)[Command](https://ui.shadcn.com/docs/components/command)[Context Menu](https://ui.shadcn.com/docs/components/context-menu)[Data Table](https://ui.shadcn.com/docs/components/data-table)[Date Picker](https://ui.shadcn.com/docs/components/date-picker)[Dialog](https://ui.shadcn.com/docs/components/dialog)[Drawer](https://ui.shadcn.com/docs/components/drawer)[Dropdown Menu](https://ui.shadcn.com/docs/components/dropdown-menu)[Form](https://ui.shadcn.com/docs/components/form)[Hover Card](https://ui.shadcn.com/docs/components/hover-card)[Input](https://ui.shadcn.com/docs/components/input)[Input OTP](https://ui.shadcn.com/docs/components/input-otp)[Label](https://ui.shadcn.com/docs/components/label)[Menubar](https://ui.shadcn.com/docs/components/menubar)[Navigation Menu](https://ui.shadcn.com/docs/components/navigation-menu)[Pagination](https://ui.shadcn.com/docs/components/pagination)[Popover](https://ui.shadcn.com/docs/components/popover)[Progress](https://ui.shadcn.com/docs/components/progress)[Radio Group](https://ui.shadcn.com/docs/components/radio-group)[Resizable](https://ui.shadcn.com/docs/components/resizable)[Scroll Area](https://ui.shadcn.com/docs/components/scroll-area)[Select](https://ui.shadcn.com/docs/components/select)[Separator](https://ui.shadcn.com/docs/components/separator)[Sheet](https://ui.shadcn.com/docs/components/sheet)[Sidebar](https://ui.shadcn.com/docs/components/sidebar)[Skeleton](https://ui.shadcn.com/docs/components/skeleton)[Slider](https://ui.shadcn.com/docs/components/slider)[Sonner](https://ui.shadcn.com/docs/components/sonner)[Switch](https://ui.shadcn.com/docs/components/switch)[Table](https://ui.shadcn.com/docs/components/table)[Tabs](https://ui.shadcn.com/docs/components/tabs)[Textarea](https://ui.shadcn.com/docs/components/textarea)[Toast](https://ui.shadcn.com/docs/components/toast)[Toggle](https://ui.shadcn.com/docs/components/toggle)[Toggle Group](https://ui.shadcn.com/docs/components/toggle-group)[Tooltip](https://ui.shadcn.com/docs/components/tooltip)
#### Registry New
[Introduction](https://ui.shadcn.com/docs/registry)[Getting Started](https://ui.shadcn.com/docs/registry/getting-started)[Examples](https://ui.shadcn.com/docs/registry/examples)[Open in v0](https://ui.shadcn.com/docs/registry/open-in-v0)[FAQ](https://ui.shadcn.com/docs/registry/faq)[registry.json](https://ui.shadcn.com/docs/registry/registry-json)[registry-item.json](https://ui.shadcn.com/docs/registry/registry-item-json)
[Docs](https://ui.shadcn.com/docs)
Getting Started
# Getting Started
Learn how to get setup and run your own component registry.
This guide will walk you through the process of setting up your own component registry.
It assumes you already have a project with components and would like to turn it into a registry.
If you're starting a new registry project, you can use the [registry template](https://github.com/shadcn-ui/registry-template) as a starting point. We have already configured it for you.
## [](https://ui.shadcn.com/docs/registry/getting-started#registryjson)registry.json
The `registry.json` file is only required if you're using the `shadcn` CLI to build your registry.
If you're using a different build system, you can skip this step as long as your build system produces valid JSON files that conform to the [registry-item schema specification](https://ui.shadcn.com/docs/registry/registry-item-json).
### [](https://ui.shadcn.com/docs/registry/getting-started#add-a-registryjson-file)Add a registry.json file
Create a `registry.json` file in the root of your project. Your project can be a Next.js, Remix, Vite, or any other project that supports React.
registry.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry.json",
 "name": "acme",
 "homepage": "https://acme.com",
 "items": [
  // ...
 ]
}
```
Copy
This `registry.json` file must conform to the [registry schema specification](https://ui.shadcn.com/docs/registry/registry-json).
## [](https://ui.shadcn.com/docs/registry/getting-started#add-a-registry-item)Add a registry item
### [](https://ui.shadcn.com/docs/registry/getting-started#create-your-component)Create your component
Add your first component. Here's an example of a simple `<HelloWorld />` component:
registry/new-york/hello-world/hello-world.tsx
```
import { Button } from "@/components/ui/button"
export function HelloWorld() {
 return <Button>Hello World</Button>
}
```
Copy
**Note:** This example places the component in the `registry/new-york` directory. You can place it anywhere in your project as long as you set the correct path in the `registry.json` file and you follow the `registry/[NAME]` directory structure.
```
registry
└── new-york
  └── hello-world
    └── hello-world.tsx
```
Copy
**Important:** If you're placing your component in a custom directory, make sure it is configured in your `tailwind.config.ts` file.
```
// tailwind.config.ts
export default {
 content: ["./registry/**/*.{js,ts,jsx,tsx}"],
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/getting-started#add-your-component-to-the-registry)Add your component to the registry
To add your component to the registry, you need to add your component definition to `registry.json`.
registry.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry.json",
 "name": "acme",
 "homepage": "https://acme.com",
 "items": [
  {
   "name": "hello-world",
   "type": "registry:block",
   "title": "Hello World",
   "description": "A simple hello world component.",
   "files": [
    {
     "path": "registry/new-york/hello-world/hello-world.tsx",
     "type": "registry:component"
    }
   ]
  }
 ]
}
```
Copy
You define your registry item by adding a `name`, `type`, `title`, `description` and `files`.
For every file you add, you must specify the `path` and `type` of the file. The `path` is the relative path to the file from the root of your project. The `type` is the type of the file.
You can read more about the registry item schema and file types in the [registry item schema docs](https://ui.shadcn.com/docs/registry/registry-item-json).
## [](https://ui.shadcn.com/docs/registry/getting-started#build-your-registry)Build your registry
### [](https://ui.shadcn.com/docs/registry/getting-started#install-the-shadcn-cli)Install the shadcn CLI
Note: the `build` command is currently only available in the `shadcn@canary` version of the CLI.
pnpmnpmyarnbun
```
pnpm add shadcn@canary

```

Copy
### [](https://ui.shadcn.com/docs/registry/getting-started#add-a-build-script)Add a build script
Add a `registry:build` script to your `package.json` file.
package.json
```
{
 "scripts": {
  "registry:build": "shadcn build"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/getting-started#run-the-build-script)Run the build script
Run the build script to generate the registry JSON files.
pnpmnpmyarnbun
```
pnpm registry:build

```

Copy
**Note:** By default, the build script will generate the registry JSON files in `public/r` e.g `public/r/hello-world.json`.
You can change the output directory by passing the `--output` option. See the [shadcn build command](https://ui.shadcn.com/docs/cli#build) for more information.
## [](https://ui.shadcn.com/docs/registry/getting-started#serve-your-registry)Serve your registry
If you're running your registry on Next.js, you can now serve your registry by running the `next` server. The command might differ for other frameworks.
pnpmnpmyarnbun
```
pnpm dev

```

Copy
Your files will now be served at `http://localhost:3000/r/[NAME].json` eg. `http://localhost:3000/r/hello-world.json`.
## [](https://ui.shadcn.com/docs/registry/getting-started#publish-your-registry)Publish your registry
To make your registry available to other developers, you can publish it by deploying your project to a public URL.
## [](https://ui.shadcn.com/docs/registry/getting-started#adding-auth)Adding Auth
The `shadcn` CLI does not offer a built-in way to add auth to your registry. We recommend handling authorization on your registry server.
A common simple approach is to use a `token` query parameter to authenticate requests to your registry. e.g. `http://localhost:3000/r/hello-world.json?token=[SECURE_TOKEN_HERE]`.
Use the secure token to authenticate requests and return a 401 Unauthorized response if the token is invalid. Both the `shadcn` CLI and `Open in v0` will handle the 401 response and display a message to the user.
**Note:** Make sure to encrypt and expire tokens.
## [](https://ui.shadcn.com/docs/registry/getting-started#guidelines)Guidelines
Here are some guidelines to follow when building components for a registry.
  * Place your registry item in the `registry/[STYLE]/[NAME]` directory. I'm using `new-york` as an example. It can be anything you want as long as it's nested under the `registry` directory.
  * The following properties are required for the block definition: `name`, `description`, `type` and `files`.
  * Make sure to list all registry dependencies in `registryDependencies`. A registry dependency is the name of the component in the registry eg. `input`, `button`, `card`, etc or a URL to a registry item eg. `http://localhost:3000/r/editor.json`.
  * Make sure to list all dependencies in `dependencies`. A dependency is the name of the package in the registry eg. `zod`, `sonner`, etc. To set a version, you can use the `name@version` format eg. `zod@^3.20.0`.
  * **Imports should always use the`@/registry` path.** eg. `import { HelloWorld } from "@/registry/new-york/hello-world/hello-world"`
  * Ideally, place your files within a registry item in `components`, `hooks`, `lib` directories.


## [](https://ui.shadcn.com/docs/registry/getting-started#install-using-the-cli)Install using the CLI
To install a registry item using the `shadcn` CLI, use the `add` command followed by the URL of the registry item.
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest add http://localhost:3000/r/hello-world.json

```

Copy
[Introduction](https://ui.shadcn.com/docs/registry)[Examples](https://ui.shadcn.com/docs/registry/examples)
On This Page
  * [registry.json](https://ui.shadcn.com/docs/registry/getting-started#registryjson)
    * [Add a registry.json file](https://ui.shadcn.com/docs/registry/getting-started#add-a-registryjson-file)
  * [Add a registry item](https://ui.shadcn.com/docs/registry/getting-started#add-a-registry-item)
    * [Create your component](https://ui.shadcn.com/docs/registry/getting-started#create-your-component)
    * [Add your component to the registry](https://ui.shadcn.com/docs/registry/getting-started#add-your-component-to-the-registry)
  * [Build your registry](https://ui.shadcn.com/docs/registry/getting-started#build-your-registry)
    * [Install the shadcn CLI](https://ui.shadcn.com/docs/registry/getting-started#install-the-shadcn-cli)
    * [Add a build script](https://ui.shadcn.com/docs/registry/getting-started#add-a-build-script)
    * [Run the build script](https://ui.shadcn.com/docs/registry/getting-started#run-the-build-script)
  * [Serve your registry](https://ui.shadcn.com/docs/registry/getting-started#serve-your-registry)
  * [Publish your registry](https://ui.shadcn.com/docs/registry/getting-started#publish-your-registry)
  * [Adding Auth](https://ui.shadcn.com/docs/registry/getting-started#adding-auth)
  * [Guidelines](https://ui.shadcn.com/docs/registry/getting-started#guidelines)
  * [Install using the CLI](https://ui.shadcn.com/docs/registry/getting-started#install-using-the-cli)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

