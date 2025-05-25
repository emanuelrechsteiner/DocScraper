---
url: https://ui.shadcn.com/docs/installation/tanstack
scraped_at: 2025-05-24T22:28:54.284729
title: TanStack Start - shadcn/ui
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
TanStack Start
# TanStack Start
Install and configure shadcn/ui for TanStack Start.
### [](https://ui.shadcn.com/docs/installation/tanstack#create-project)Create project
Start by creating a new TanStack Start project by following the [Build a Project from Scratch](https://tanstack.com/start/latest/docs/framework/react/build-from-scratch) guide on the TanStack Start website.
**Do not add Tailwind yet. We'll install Tailwind v4 in the next step.**
### [](https://ui.shadcn.com/docs/installation/tanstack#add-tailwind)Add Tailwind
Install `tailwindcss` and its dependencies.
pnpmnpmyarnbun
```
pnpm add tailwindcss @tailwindcss/postcss postcss

```

Copy
### [](https://ui.shadcn.com/docs/installation/tanstack#create-postcssconfigts)Create postcss.config.ts
Create a `postcss.config.ts` file at the root of your project.
postcss.config.ts
```
export default {
 plugins: {
  "@tailwindcss/postcss": {},
 },
}
```
Copy
### [](https://ui.shadcn.com/docs/installation/tanstack#create-appstylesappcss)Create `app/styles/app.css`
Create an `app.css` file in the `app/styles` directory and import `tailwindcss`
app/styles/app.css
```
@import "tailwindcss" source("../");
```
Copy
### [](https://ui.shadcn.com/docs/installation/tanstack#import-appcss)Import `app.css`
app/routes/__root.tsx
```
import type { ReactNode } from "react"
import { Outlet, createRootRoute } from "@tanstack/react-router"
import { Meta, Scripts } from "@tanstack/start"
import appCss from "@/styles/app.css?url"
export const Route = createRootRoute({
 head: () => ({
  meta: [
   {
    charSet: "utf-8",
   },
   {
    name: "viewport",
    content: "width=device-width, initial-scale=1",
   },
   {
    title: "TanStack Start Starter",
   },
  ],
  links: [
   {
    rel: "stylesheet",
    href: appCss,
   },
  ],
 }),
 component: RootComponent,
})
```
Copy
### [](https://ui.shadcn.com/docs/installation/tanstack#edit-tsconfigjson-file)Edit tsconfig.json file
Add the following code to the `tsconfig.json` file to resolve paths.
tsconfig.json
```
{
 "compilerOptions": {
  "jsx": "react-jsx",
  "moduleResolution": "Bundler",
  "module": "ESNext",
  "target": "ES2022",
  "skipLibCheck": true,
  "strictNullChecks": true,
  "baseUrl": ".",
  "paths": {
   "@/*": ["./app/*"]
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/installation/tanstack#run-the-cli)Run the CLI
Run the `shadcn` init command to setup your project:
pnpmnpmyarnbun
```
pnpm dlx shadcn@canary init

```

Copy
This will create a `components.json` file in the root of your project and configure CSS variables inside `app/styles/app.css`.
### [](https://ui.shadcn.com/docs/installation/tanstack#thats-it)That's it
You can now start adding components to your project.
pnpmnpmyarnbun
```
pnpm dlx shadcn@canary add button

```

Copy
The command above will add the `Button` component to your project. You can then import it like this:
app/routes/index.tsx
```
import { Button } from "@/components/ui/button"
function Home() {
 const router = useRouter()
 const state = Route.useLoaderData()
 return (
  <div>
   <Button>Click me</Button>
  </div>
 )
}
```
Copy
[Astro](https://ui.shadcn.com/docs/installation/astro)[Tanstack Router](https://ui.shadcn.com/docs/installation/tanstack-router)
On This Page
  * [Create project](https://ui.shadcn.com/docs/installation/tanstack#create-project)
  * [Add Tailwind](https://ui.shadcn.com/docs/installation/tanstack#add-tailwind)
  * [Create postcss.config.ts](https://ui.shadcn.com/docs/installation/tanstack#create-postcssconfigts)
  * [Create app/styles/app.css](https://ui.shadcn.com/docs/installation/tanstack#create-appstylesappcss)
  * [Import app.css](https://ui.shadcn.com/docs/installation/tanstack#import-appcss)
  * [Edit tsconfig.json file](https://ui.shadcn.com/docs/installation/tanstack#edit-tsconfigjson-file)
  * [Run the CLI](https://ui.shadcn.com/docs/installation/tanstack#run-the-cli)
  * [That's it](https://ui.shadcn.com/docs/installation/tanstack#thats-it)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

