---
url: https://ui.shadcn.com/docs/installation/manual
scraped_at: 2025-05-24T22:23:59.807209
title: Manual Installation - shadcn/ui
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
Manual Installation
# Manual Installation
Add dependencies to your project manually.
### [](https://ui.shadcn.com/docs/installation/manual#add-tailwind-css)Add Tailwind CSS
Components are styled using Tailwind CSS. You need to install Tailwind CSS in your project.
[Follow the Tailwind CSS installation instructions to get started.](https://tailwindcss.com/docs/installation)
### [](https://ui.shadcn.com/docs/installation/manual#add-dependencies)Add dependencies
Add the following dependencies to your project:
pnpmnpmyarnbun
```
pnpm add class-variance-authority clsx tailwind-merge lucide-react tw-animate-css

```

Copy
### [](https://ui.shadcn.com/docs/installation/manual#configure-path-aliases)Configure path aliases
Configure the path aliases in your `tsconfig.json` file.
tsconfig.json
```
{
 "compilerOptions": {
  "baseUrl": ".",
  "paths": {
   "@/*": ["./*"]
  }
 }
}
```
Copy
The `@` alias is a preference. You can use other aliases if you want.
### [](https://ui.shadcn.com/docs/installation/manual#configure-styles)Configure styles
Add the following to your styles/globals.css file. You can learn more about using CSS variables for theming in the [theming section](https://ui.shadcn.com/docs/theming).
src/styles/globals.css
```
@import "tailwindcss";
@import "tw-animate-css";
@custom-variant dark (&:is(.dark *));
:root {
 --background: oklch(1 0 0);
 --foreground: oklch(0.145 0 0);
 --card: oklch(1 0 0);
 --card-foreground: oklch(0.145 0 0);
 --popover: oklch(1 0 0);
 --popover-foreground: oklch(0.145 0 0);
 --primary: oklch(0.205 0 0);
 --primary-foreground: oklch(0.985 0 0);
 --secondary: oklch(0.97 0 0);
 --secondary-foreground: oklch(0.205 0 0);
 --muted: oklch(0.97 0 0);
 --muted-foreground: oklch(0.556 0 0);
 --accent: oklch(0.97 0 0);
 --accent-foreground: oklch(0.205 0 0);
 --destructive: oklch(0.577 0.245 27.325);
 --destructive-foreground: oklch(0.577 0.245 27.325);
 --border: oklch(0.922 0 0);
 --input: oklch(0.922 0 0);
 --ring: oklch(0.708 0 0);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
 --radius: 0.625rem;
 --sidebar: oklch(0.985 0 0);
 --sidebar-foreground: oklch(0.145 0 0);
 --sidebar-primary: oklch(0.205 0 0);
 --sidebar-primary-foreground: oklch(0.985 0 0);
 --sidebar-accent: oklch(0.97 0 0);
 --sidebar-accent-foreground: oklch(0.205 0 0);
 --sidebar-border: oklch(0.922 0 0);
 --sidebar-ring: oklch(0.708 0 0);
}
.dark {
 --background: oklch(0.145 0 0);
 --foreground: oklch(0.985 0 0);
 --card: oklch(0.145 0 0);
 --card-foreground: oklch(0.985 0 0);
 --popover: oklch(0.145 0 0);
 --popover-foreground: oklch(0.985 0 0);
 --primary: oklch(0.985 0 0);
 --primary-foreground: oklch(0.205 0 0);
 --secondary: oklch(0.269 0 0);
 --secondary-foreground: oklch(0.985 0 0);
 --muted: oklch(0.269 0 0);
 --muted-foreground: oklch(0.708 0 0);
 --accent: oklch(0.269 0 0);
 --accent-foreground: oklch(0.985 0 0);
 --destructive: oklch(0.396 0.141 25.723);
 --destructive-foreground: oklch(0.637 0.237 25.331);
 --border: oklch(0.269 0 0);
 --input: oklch(0.269 0 0);
 --ring: oklch(0.439 0 0);
 --chart-1: oklch(0.488 0.243 264.376);
 --chart-2: oklch(0.696 0.17 162.48);
 --chart-3: oklch(0.769 0.188 70.08);
 --chart-4: oklch(0.627 0.265 303.9);
 --chart-5: oklch(0.645 0.246 16.439);
 --sidebar: oklch(0.205 0 0);
 --sidebar-foreground: oklch(0.985 0 0);
 --sidebar-primary: oklch(0.488 0.243 264.376);
 --sidebar-primary-foreground: oklch(0.985 0 0);
 --sidebar-accent: oklch(0.269 0 0);
 --sidebar-accent-foreground: oklch(0.985 0 0);
 --sidebar-border: oklch(0.269 0 0);
 --sidebar-ring: oklch(0.439 0 0);
}
@theme inline {
 --color-background: var(--background);
 --color-foreground: var(--foreground);
 --color-card: var(--card);
 --color-card-foreground: var(--card-foreground);
 --color-popover: var(--popover);
 --color-popover-foreground: var(--popover-foreground);
 --color-primary: var(--primary);
 --color-primary-foreground: var(--primary-foreground);
 --color-secondary: var(--secondary);
 --color-secondary-foreground: var(--secondary-foreground);
 --color-muted: var(--muted);
 --color-muted-foreground: var(--muted-foreground);
 --color-accent: var(--accent);
 --color-accent-foreground: var(--accent-foreground);
 --color-destructive: var(--destructive);
 --color-destructive-foreground: var(--destructive-foreground);
 --color-border: var(--border);
 --color-input: var(--input);
 --color-ring: var(--ring);
 --color-chart-1: var(--chart-1);
 --color-chart-2: var(--chart-2);
 --color-chart-3: var(--chart-3);
 --color-chart-4: var(--chart-4);
 --color-chart-5: var(--chart-5);
 --radius-sm: calc(var(--radius) - 4px);
 --radius-md: calc(var(--radius) - 2px);
 --radius-lg: var(--radius);
 --radius-xl: calc(var(--radius) + 4px);
 --color-sidebar: var(--sidebar);
 --color-sidebar-foreground: var(--sidebar-foreground);
 --color-sidebar-primary: var(--sidebar-primary);
 --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
 --color-sidebar-accent: var(--sidebar-accent);
 --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
 --color-sidebar-border: var(--sidebar-border);
 --color-sidebar-ring: var(--sidebar-ring);
}
@layer base {
 * {
  @apply border-border outline-ring/50;
 }
 body {
  @apply bg-background text-foreground;
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/installation/manual#add-a-cn-helper)Add a cn helper
lib/utils.ts
```
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
export function cn(...inputs: ClassValue[]) {
 return twMerge(clsx(inputs))
}
```
Copy
### [](https://ui.shadcn.com/docs/installation/manual#create-a-componentsjson-file)Create a `components.json` file
Create a `components.json` file in the root of your project.
components.json
```
{
 "$schema": "https://ui.shadcn.com/schema.json",
 "style": "new-york",
 "rsc": false,
 "tsx": true,
 "tailwind": {
  "config": "",
  "css": "src/styles/globals.css",
  "baseColor": "neutral",
  "cssVariables": true,
  "prefix": ""
 },
 "aliases": {
  "components": "@/components",
  "utils": "@/lib/utils",
  "ui": "@/components/ui",
  "lib": "@/lib",
  "hooks": "@/hooks"
 },
 "iconLibrary": "lucide"
}
```
Copy
### [](https://ui.shadcn.com/docs/installation/manual#thats-it)That's it
You can now start adding components to your project.
[Tanstack Router](https://ui.shadcn.com/docs/installation/tanstack-router)[Accordion](https://ui.shadcn.com/docs/components/accordion)
On This Page
  * [Add Tailwind CSS](https://ui.shadcn.com/docs/installation/manual#add-tailwind-css)
  * [Add dependencies](https://ui.shadcn.com/docs/installation/manual#add-dependencies)
  * [Configure path aliases](https://ui.shadcn.com/docs/installation/manual#configure-path-aliases)
  * [Configure styles](https://ui.shadcn.com/docs/installation/manual#configure-styles)
  * [Add a cn helper](https://ui.shadcn.com/docs/installation/manual#add-a-cn-helper)
  * [Create a components.json file](https://ui.shadcn.com/docs/installation/manual#create-a-componentsjson-file)
  * [That's it](https://ui.shadcn.com/docs/installation/manual#thats-it)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

