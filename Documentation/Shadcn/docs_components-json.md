---
url: https://ui.shadcn.com/docs/components-json
scraped_at: 2025-05-24T22:26:24.767300
title: components.json - shadcn/ui
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
components.json
# components.json
Configuration for your project.
The `components.json` file holds configuration for your project.
We use it to understand how your project is set up and how to generate components customized for your project.
Note: The `components.json` file is optional and **only required if you're using the CLI** to add components to your project. If you're using the copy and paste method, you don't need this file.
You can create a `components.json` file in your project by running the following command:
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest init

```

Copy
See the [CLI section](https://ui.shadcn.com/docs/cli) for more information.
## [](https://ui.shadcn.com/docs/components-json#schema)$schema
You can see the JSON Schema for `components.json` [here](https://ui.shadcn.com/schema.json).
components.json
```
{
 "$schema": "https://ui.shadcn.com/schema.json"
}
```
Copy
## [](https://ui.shadcn.com/docs/components-json#style)style
The style for your components. **This cannot be changed after initialization.**
components.json
```
{
 "style": "new-york"
}
```
Copy
The `default` style has been deprecated. Use the `new-york` style instead.
## [](https://ui.shadcn.com/docs/components-json#tailwind)tailwind
Configuration to help the CLI understand how Tailwind CSS is set up in your project.
See the [installation section](https://ui.shadcn.com/docs/installation) for how to set up Tailwind CSS.
### [](https://ui.shadcn.com/docs/components-json#tailwindconfig)tailwind.config
Path to where your `tailwind.config.js` file is located. **For Tailwind CSS v4, leave this blank.**
components.json
```
{
 "tailwind": {
  "config": "tailwind.config.js" | "tailwind.config.ts"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#tailwindcss)tailwind.css
Path to the CSS file that imports Tailwind CSS into your project.
components.json
```
{
 "tailwind": {
  "css": "styles/global.css"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#tailwindbasecolor)tailwind.baseColor
This is used to generate the default color palette for your components. **This cannot be changed after initialization.**
components.json
```
{
 "tailwind": {
  "baseColor": "gray" | "neutral" | "slate" | "stone" | "zinc"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#tailwindcssvariables)tailwind.cssVariables
You can choose between using CSS variables or Tailwind CSS utility classes for theming.
To use utility classes for theming set `tailwind.cssVariables` to `false`. For CSS variables, set `tailwind.cssVariables` to `true`.
components.json
```
{
 "tailwind": {
  "cssVariables": `true` | `false`
 }
}
```
Copy
For more information, see the [theming docs](https://ui.shadcn.com/docs/theming).
**This cannot be changed after initialization.** To switch between CSS variables and utility classes, you'll have to delete and re-install your components.
### [](https://ui.shadcn.com/docs/components-json#tailwindprefix)tailwind.prefix
The prefix to use for your Tailwind CSS utility classes. Components will be added with this prefix.
components.json
```
{
 "tailwind": {
  "prefix": "tw-"
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/components-json#rsc)rsc
Whether or not to enable support for React Server Components.
The CLI automatically adds a `use client` directive to client components when set to `true`.
components.json
```
{
 "rsc": `true` | `false`
}
```
Copy
## [](https://ui.shadcn.com/docs/components-json#tsx)tsx
Choose between TypeScript or JavaScript components.
Setting this option to `false` allows components to be added as JavaScript with the `.jsx` file extension.
components.json
```
{
 "tsx": `true` | `false`
}
```
Copy
## [](https://ui.shadcn.com/docs/components-json#aliases)aliases
The CLI uses these values and the `paths` config from your `tsconfig.json` or `jsconfig.json` file to place generated components in the correct location.
Path aliases have to be set up in your `tsconfig.json` or `jsconfig.json` file.
**Important:** If you're using the `src` directory, make sure it is included under `paths` in your `tsconfig.json` or `jsconfig.json` file.
### [](https://ui.shadcn.com/docs/components-json#aliasesutils)aliases.utils
Import alias for your utility functions.
components.json
```
{
 "aliases": {
  "utils": "@/lib/utils"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#aliasescomponents)aliases.components
Import alias for your components.
components.json
```
{
 "aliases": {
  "components": "@/components"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#aliasesui)aliases.ui
Import alias for `ui` components.
The CLI will use the `aliases.ui` value to determine where to place your `ui` components. Use this config if you want to customize the installation directory for your `ui` components.
components.json
```
{
 "aliases": {
  "ui": "@/app/ui"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#aliaseslib)aliases.lib
Import alias for `lib` functions such as `format-date` or `generate-id`.
components.json
```
{
 "aliases": {
  "lib": "@/lib"
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/components-json#aliaseshooks)aliases.hooks
Import alias for `hooks` such as `use-media-query` or `use-toast`.
components.json
```
{
 "aliases": {
  "hooks": "@/hooks"
 }
}
```
Copy
[Installation](https://ui.shadcn.com/docs/installation)[Theming](https://ui.shadcn.com/docs/theming)
On This Page
  * [$schema](https://ui.shadcn.com/docs/components-json#schema)
  * [style](https://ui.shadcn.com/docs/components-json#style)
  * [tailwind](https://ui.shadcn.com/docs/components-json#tailwind)
    * [tailwind.config](https://ui.shadcn.com/docs/components-json#tailwindconfig)
    * [tailwind.css](https://ui.shadcn.com/docs/components-json#tailwindcss)
    * [tailwind.baseColor](https://ui.shadcn.com/docs/components-json#tailwindbasecolor)
    * [tailwind.cssVariables](https://ui.shadcn.com/docs/components-json#tailwindcssvariables)
    * [tailwind.prefix](https://ui.shadcn.com/docs/components-json#tailwindprefix)
  * [rsc](https://ui.shadcn.com/docs/components-json#rsc)
  * [tsx](https://ui.shadcn.com/docs/components-json#tsx)
  * [aliases](https://ui.shadcn.com/docs/components-json#aliases)
    * [aliases.utils](https://ui.shadcn.com/docs/components-json#aliasesutils)
    * [aliases.components](https://ui.shadcn.com/docs/components-json#aliasescomponents)
    * [aliases.ui](https://ui.shadcn.com/docs/components-json#aliasesui)
    * [aliases.lib](https://ui.shadcn.com/docs/components-json#aliaseslib)
    * [aliases.hooks](https://ui.shadcn.com/docs/components-json#aliaseshooks)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

