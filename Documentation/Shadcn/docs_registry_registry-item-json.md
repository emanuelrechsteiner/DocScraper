---
url: https://ui.shadcn.com/docs/registry/registry-item-json
scraped_at: 2025-05-24T22:26:34.586862
title: registry-item.json - shadcn/ui
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
registry-item.json
# registry-item.json
Specification for registry items.
The `registry-item.json` schema is used to define your custom registry items.
registry-item.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "hello-world",
 "type": "registry:block",
 "title": "Hello World",
 "description": "A simple hello world component.",
 "files": [
  {
   "path": "registry/new-york/hello-world/hello-world.tsx",
   "type": "registry:component"
  },
  {
   "path": "registry/new-york/hello-world/use-hello-world.ts",
   "type": "registry:hook"
  }
 ],
 "cssVars": {
  "theme": {
   "font-heading": "Poppins, sans-serif"
  },
  "light": {
   "brand": "20 14.3% 4.1%"
  },
  "dark": {
   "brand": "20 14.3% 4.1%"
  }
 }
}
```
Copy
[See more examples](https://ui.shadcn.com/docs/registry/examples)
## [](https://ui.shadcn.com/docs/registry/registry-item-json#definitions)Definitions
You can see the JSON Schema for `registry-item.json` [here](https://ui.shadcn.com/schema/registry-item.json).
### [](https://ui.shadcn.com/docs/registry/registry-item-json#schema)$schema
The `$schema` property is used to specify the schema for the `registry-item.json` file.
registry-item.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json"
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#name)name
The name of the item. This is used to identify the item in the registry. It should be unique for your registry.
registry-item.json
```
{
 "name": "hello-world"
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#title)title
A human-readable title for your registry item. Keep it short and descriptive.
registry-item.json
```
{
 "title": "Hello World"
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#description)description
A description of your registry item. This can be longer and more detailed than the `title`.
registry-item.json
```
{
 "description": "A simple hello world component."
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#type)type
The `type` property is used to specify the type of your registry item. This is used to determine the type and target path of the item when resolved for a project.
registry-item.json
```
{
 "type": "registry:block"
}
```
Copy
The following types are supported:
Type| Description  
---|---  
`registry:block`| Use for complex components with multiple files.  
`registry:component`| Use for simple components.  
`registry:lib`| Use for lib and utils.  
`registry:hook`| Use for hooks.  
`registry:ui`| Use for UI components and single-file primitives  
`registry:page`| Use for page or file-based routes.  
`registry:file`| Use for miscellaneous files.  
`registry:style`| Use for registry styles. eg. `new-york`  
`registry:theme`| Use for themes.  
### [](https://ui.shadcn.com/docs/registry/registry-item-json#author)author
The `author` property is used to specify the author of the registry item.
It can be unique to the registry item or the same as the author of the registry.
registry-item.json
```
{
 "author": "John Doe <john@doe.com>"
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#dependencies)dependencies
The `dependencies` property is used to specify the dependencies of your registry item. This is for `npm` packages.
Use `@version` to specify the version of your registry item.
registry-item.json
```
{
 "dependencies": [
  "@radix-ui/react-accordion",
  "zod",
  "lucide-react",
  "name@1.0.2"
 ]
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#registrydependencies)registryDependencies
Used for registry dependencies. Can be names or URLs. Use the name of the item to reference shadcn/ui components and urls to reference other registries.
  * For `shadcn/ui` registry items such as `button`, `input`, `select`, etc use the name eg. `['button', 'input', 'select']`.
  * For custom registry items use the URL of the registry item eg. `['https://example.com/r/hello-world.json']`.


registry-item.json
```
{
 "registryDependencies": [
  "button",
  "input",
  "select",
  "https://example.com/r/editor.json"
 ]
}
```
Copy
Note: The CLI will automatically resolve remote registry dependencies.
### [](https://ui.shadcn.com/docs/registry/registry-item-json#files)files
The `files` property is used to specify the files of your registry item. Each file has a `path`, `type` and `target` (optional) property.
**The`target` property is required for `registry:page` and `registry:file` types.**
registry-item.json
```
{
 "files": [
  {
   "path": "registry/new-york/hello-world/page.tsx",
   "type": "registry:page",
   "target": "app/hello/page.tsx"
  },
  {
   "path": "registry/new-york/hello-world/hello-world.tsx",
   "type": "registry:component"
  },
  {
   "path": "registry/new-york/hello-world/use-hello-world.ts",
   "type": "registry:hook"
  },
  {
   "path": "registry/new-york/hello-world/.env",
   "type": "registry:file",
   "target": "~/.env"
  }
 ]
}
```
Copy
#### [](https://ui.shadcn.com/docs/registry/registry-item-json#path)path
The `path` property is used to specify the path to the file in your registry. This path is used by the build script to parse, transform and build the registry JSON payload.
#### [](https://ui.shadcn.com/docs/registry/registry-item-json#type-1)type
The `type` property is used to specify the type of the file. See the [type](https://ui.shadcn.com/docs/registry/registry-item-json#type) section for more information.
#### [](https://ui.shadcn.com/docs/registry/registry-item-json#target)target
The `target` property is used to indicate where the file should be placed in a project. This is optional and only required for `registry:page` and `registry:file` types.
By default, the `shadcn` cli will read a project's `components.json` file to determine the target path. For some files, such as routes or config you can specify the target path manually.
Use `~` to refer to the root of the project e.g `~/foo.config.js`.
### [](https://ui.shadcn.com/docs/registry/registry-item-json#tailwind)tailwind
**DEPRECATED:** Use `cssVars.theme` instead for Tailwind v4 projects.
The `tailwind` property is used for tailwind configuration such as `theme`, `plugins` and `content`.
You can use the `tailwind.config` property to add colors, animations and plugins to your registry item.
registry-item.json
```
{
 "tailwind": {
  "config": {
   "theme": {
    "extend": {
     "colors": {
      "brand": "hsl(var(--brand))"
     },
     "keyframes": {
      "wiggle": {
       "0%, 100%": { "transform": "rotate(-3deg)" },
       "50%": { "transform": "rotate(3deg)" }
      }
     },
     "animation": {
      "wiggle": "wiggle 1s ease-in-out infinite"
     }
    }
   }
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#cssvars)cssVars
Use to define CSS variables for your registry item.
registry-item.json
```
{
 "cssVars": {
  "theme": {
   "font-heading": "Poppins, sans-serif"
  },
  "light": {
   "brand": "20 14.3% 4.1%",
   "radius": "0.5rem"
  },
  "dark": {
   "brand": "20 14.3% 4.1%"
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#css)css
Use `css` to add new rules to the project's CSS file eg. `@layer base`, `@layer components`, `@utility`, `@keyframes`, etc.
registry-item.json
```
{
 "css": {
  "@layer base": {
   "body": {
    "font-size": "var(--text-base)",
    "line-height": "1.5"
   }
  },
  "@layer components": {
   "button": {
    "background-color": "var(--color-primary)",
    "color": "var(--color-white)"
   }
  },
  "@utility text-magic": {
   "font-size": "var(--text-base)",
   "line-height": "1.5"
  },
  "@keyframes wiggle": {
   "0%, 100%": {
    "transform": "rotate(-3deg)"
   },
   "50%": {
    "transform": "rotate(3deg)"
   }
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#docs)docs
Use `docs` to show custom documentation or message when installing your registry item via the CLI.
registry-item.json
```
{
 "docs": "Remember to add the FOO_BAR environment variable to your .env file."
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#categories)categories
Use `categories` to organize your registry item.
registry-item.json
```
{
 "categories": ["sidebar", "dashboard"]
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/registry-item-json#meta)meta
Use `meta` to add additional metadata to your registry item. You can add any key/value pair that you want to be available to the registry item.
registry-item.json
```
{
 "meta": { "foo": "bar" }
}
```
Copy
[registry.json](https://ui.shadcn.com/docs/registry/registry-json)
On This Page
  * [Definitions](https://ui.shadcn.com/docs/registry/registry-item-json#definitions)
    * [$schema](https://ui.shadcn.com/docs/registry/registry-item-json#schema)
    * [name](https://ui.shadcn.com/docs/registry/registry-item-json#name)
    * [title](https://ui.shadcn.com/docs/registry/registry-item-json#title)
    * [description](https://ui.shadcn.com/docs/registry/registry-item-json#description)
    * [type](https://ui.shadcn.com/docs/registry/registry-item-json#type)
    * [author](https://ui.shadcn.com/docs/registry/registry-item-json#author)
    * [dependencies](https://ui.shadcn.com/docs/registry/registry-item-json#dependencies)
    * [registryDependencies](https://ui.shadcn.com/docs/registry/registry-item-json#registrydependencies)
    * [files](https://ui.shadcn.com/docs/registry/registry-item-json#files)
    * [tailwind](https://ui.shadcn.com/docs/registry/registry-item-json#tailwind)
    * [cssVars](https://ui.shadcn.com/docs/registry/registry-item-json#cssvars)
    * [css](https://ui.shadcn.com/docs/registry/registry-item-json#css)
    * [docs](https://ui.shadcn.com/docs/registry/registry-item-json#docs)
    * [categories](https://ui.shadcn.com/docs/registry/registry-item-json#categories)
    * [meta](https://ui.shadcn.com/docs/registry/registry-item-json#meta)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

