---
url: https://ui.shadcn.com/docs/installation/remix
scraped_at: 2025-05-24T22:24:20.067996
title: Remix - shadcn/ui
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
Remix
# Remix
Install and configure shadcn/ui for Remix.
**Note:** The following guide is for Tailwind v4. If you are using Tailwind v3, use `shadcn@2.3.0`.
**Note:** This guide is for Remix. For React Router, see the [React Router](https://ui.shadcn.com/docs/installation/react-router) guide.
### [](https://ui.shadcn.com/docs/installation/remix#create-project)Create project
Start by creating a new Remix project using `create-remix`:
pnpmnpmyarnbun
```
pnpm create remix@latest my-app

```

Copy
### [](https://ui.shadcn.com/docs/installation/remix#run-the-cli)Run the CLI
Run the `shadcn` init command to setup your project:
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest init

```

Copy
### [](https://ui.shadcn.com/docs/installation/remix#configure-componentsjson)Configure components.json
You will be asked a few questions to configure `components.json`:
```
Which style would you like to use? › New York
Which color would you like to use as base color? › Zinc
Do you want to use CSS variables for colors? › no / yes
```
Copy
### [](https://ui.shadcn.com/docs/installation/remix#app-structure)App structure
**Note** : This app structure is only a suggestion. You can place the files wherever you want.
  * Place the UI components in the `app/components/ui` folder.
  * Your own components can be placed in the `app/components` folder.
  * The `app/lib` folder contains all the utility functions. We have a `utils.ts` where we define the `cn` helper.
  * The `app/tailwind.css` file contains the global CSS.


### [](https://ui.shadcn.com/docs/installation/remix#install-tailwind-css)Install Tailwind CSS
pnpmnpmyarnbun
```
pnpm add -D tailwindcss@latest autoprefixer@latest

```

Copy
Then we create a `postcss.config.js` file:
```
export default {
 plugins: {
  tailwindcss: {},
  autoprefixer: {},
 },
}
```
Copy
And finally we add the following to our `remix.config.js` file:
```
/** @type {import('@remix-run/dev').AppConfig} */
export default {
 ...
 tailwind: true,
 postcss: true,
 ...
};
```
Copy
### [](https://ui.shadcn.com/docs/installation/remix#add-tailwindcss-to-your-app)Add `tailwind.css` to your app
In your `app/root.tsx` file, import the `tailwind.css` file:
```
import styles from "./tailwind.css?url"
export const links: LinksFunction = () => [
 { rel: "stylesheet", href: styles },
 ...(cssBundleHref ? [{ rel: "stylesheet", href: cssBundleHref }] : []),
]
```
Copy
### [](https://ui.shadcn.com/docs/installation/remix#thats-it)That's it
You can now start adding components to your project.
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest add button

```

Copy
The command above will add the `Button` component to your project. You can then import it like this:
```
import { Button } from "~/components/ui/button"
export default function Home() {
 return (
  <div>
   <Button>Click me</Button>
  </div>
 )
}
```
Copy
[React Router](https://ui.shadcn.com/docs/installation/react-router)[Astro](https://ui.shadcn.com/docs/installation/astro)
On This Page
  * [Create project](https://ui.shadcn.com/docs/installation/remix#create-project)
  * [Run the CLI](https://ui.shadcn.com/docs/installation/remix#run-the-cli)
  * [Configure components.json](https://ui.shadcn.com/docs/installation/remix#configure-componentsjson)
  * [App structure](https://ui.shadcn.com/docs/installation/remix#app-structure)
  * [Install Tailwind CSS](https://ui.shadcn.com/docs/installation/remix#install-tailwind-css)
  * [Add tailwind.css to your app](https://ui.shadcn.com/docs/installation/remix#add-tailwindcss-to-your-app)
  * [That's it](https://ui.shadcn.com/docs/installation/remix#thats-it)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

