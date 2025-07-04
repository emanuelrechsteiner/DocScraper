---
url: https://ui.shadcn.com/docs/theming
scraped_at: 2025-05-24T22:26:51.245898
title: Theming - shadcn/ui
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
Theming
# Theming
Using CSS Variables and color utilities for theming.
You can choose between using CSS variables (recommended) or utility classes for theming.
## [](https://ui.shadcn.com/docs/theming#css-variables)CSS Variables
```
<div className="bg-backgroundtext-foreground" />
```
Copy
To use CSS variables for theming set `tailwind.cssVariables` to `true` in your `components.json` file.
components.json
```
{
 "style": "default",
 "rsc": true,
 "tailwind": {
  "config": "",
  "css": "app/globals.css",
  "baseColor": "neutral",
  "cssVariables": true
 },
 "aliases": {
  "components": "@/components",
  "utils": "@/lib/utils",
  "ui": "@/registry/new-york-v4/ui",
  "lib": "@/lib",
  "hooks": "@/hooks"
 },
 "iconLibrary": "lucide"
}
```
Copy
## [](https://ui.shadcn.com/docs/theming#utility-classes)Utility classes
```
<div className="bg-zinc-950dark:bg-white" />
```
Copy
To use utility classes for theming set `tailwind.cssVariables` to `false` in your `components.json` file.
components.json
```
{
 "style": "default",
 "rsc": true,
 "tailwind": {
  "config": "",
  "css": "app/globals.css",
  "baseColor": "slate",
  "cssVariables": false
 },
 "aliases": {
  "components": "@/components",
  "utils": "@/lib/utils",
  "ui": "@/registry/new-york-v4/ui",
  "lib": "@/lib",
  "hooks": "@/hooks"
 },
 "iconLibrary": "lucide"
}
```
Copy
## [](https://ui.shadcn.com/docs/theming#convention)Convention
We use a simple `background` and `foreground` convention for colors. The `background` variable is used for the background color of the component and the `foreground` variable is used for the text color.
The `background` suffix is omitted when the variable is used for the background color of the component.
Given the following CSS variables:
```
--primary: oklch(0.205 0 0);
--primary-foreground: oklch(0.985 0 0);
```
Copy
The `background` color of the following component will be `var(--primary)` and the `foreground` color will be `var(--primary-foreground)`.
```
<div className="bg-primary text-primary-foreground">Hello</div>
```
Copy
## [](https://ui.shadcn.com/docs/theming#list-of-variables)List of variables
Here's the list of variables available for customization:
app/globals.css
```
:root {
 --radius: 0.625rem;
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
 --border: oklch(0.922 0 0);
 --input: oklch(0.922 0 0);
 --ring: oklch(0.708 0 0);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
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
 --card: oklch(0.205 0 0);
 --card-foreground: oklch(0.985 0 0);
 --popover: oklch(0.269 0 0);
 --popover-foreground: oklch(0.985 0 0);
 --primary: oklch(0.922 0 0);
 --primary-foreground: oklch(0.205 0 0);
 --secondary: oklch(0.269 0 0);
 --secondary-foreground: oklch(0.985 0 0);
 --muted: oklch(0.269 0 0);
 --muted-foreground: oklch(0.708 0 0);
 --accent: oklch(0.371 0 0);
 --accent-foreground: oklch(0.985 0 0);
 --destructive: oklch(0.704 0.191 22.216);
 --border: oklch(1 0 0 / 10%);
 --input: oklch(1 0 0 / 15%);
 --ring: oklch(0.556 0 0);
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
 --sidebar-border: oklch(1 0 0 / 10%);
 --sidebar-ring: oklch(0.439 0 0);
}
```
Copy
## [](https://ui.shadcn.com/docs/theming#adding-new-colors)Adding new colors
To add new colors, you need to add them to your CSS file and to your `tailwind.config.js` file.
app/globals.css
```
:root {
 --warning: oklch(0.84 0.16 84);
 --warning-foreground: oklch(0.28 0.07 46);
}
.dark {
 --warning: oklch(0.41 0.11 46);
 --warning-foreground: oklch(0.99 0.02 95);
}
@theme inline {
 --color-warning: var(--warning);
 --color-warning-foreground: var(--warning-foreground);
}
```
Copy
You can now use the `warning` utility class in your components.
```
<div className="bg-warningtext-warning-foreground" />
```
Copy
## [](https://ui.shadcn.com/docs/theming#other-color-formats)Other color formats
See the [Tailwind CSS documentation](https://tailwindcss.com/docs/colors) for more information on using colors in Tailwind CSS.
## [](https://ui.shadcn.com/docs/theming#base-colors)Base Colors
For reference, here's a list of the base colors that are available.
### [](https://ui.shadcn.com/docs/theming#stone)Stone
app/globals.css
```
:root {
 --radius: 0.625rem;
 --background: oklch(1 0 0);
 --foreground: oklch(0.147 0.004 49.25);
 --card: oklch(1 0 0);
 --card-foreground: oklch(0.147 0.004 49.25);
 --popover: oklch(1 0 0);
 --popover-foreground: oklch(0.147 0.004 49.25);
 --primary: oklch(0.216 0.006 56.043);
 --primary-foreground: oklch(0.985 0.001 106.423);
 --secondary: oklch(0.97 0.001 106.424);
 --secondary-foreground: oklch(0.216 0.006 56.043);
 --muted: oklch(0.97 0.001 106.424);
 --muted-foreground: oklch(0.553 0.013 58.071);
 --accent: oklch(0.97 0.001 106.424);
 --accent-foreground: oklch(0.216 0.006 56.043);
 --destructive: oklch(0.577 0.245 27.325);
 --border: oklch(0.923 0.003 48.717);
 --input: oklch(0.923 0.003 48.717);
 --ring: oklch(0.709 0.01 56.259);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
 --sidebar: oklch(0.985 0.001 106.423);
 --sidebar-foreground: oklch(0.147 0.004 49.25);
 --sidebar-primary: oklch(0.216 0.006 56.043);
 --sidebar-primary-foreground: oklch(0.985 0.001 106.423);
 --sidebar-accent: oklch(0.97 0.001 106.424);
 --sidebar-accent-foreground: oklch(0.216 0.006 56.043);
 --sidebar-border: oklch(0.923 0.003 48.717);
 --sidebar-ring: oklch(0.709 0.01 56.259);
}
.dark {
 --background: oklch(0.147 0.004 49.25);
 --foreground: oklch(0.985 0.001 106.423);
 --card: oklch(0.216 0.006 56.043);
 --card-foreground: oklch(0.985 0.001 106.423);
 --popover: oklch(0.216 0.006 56.043);
 --popover-foreground: oklch(0.985 0.001 106.423);
 --primary: oklch(0.923 0.003 48.717);
 --primary-foreground: oklch(0.216 0.006 56.043);
 --secondary: oklch(0.268 0.007 34.298);
 --secondary-foreground: oklch(0.985 0.001 106.423);
 --muted: oklch(0.268 0.007 34.298);
 --muted-foreground: oklch(0.709 0.01 56.259);
 --accent: oklch(0.268 0.007 34.298);
 --accent-foreground: oklch(0.985 0.001 106.423);
 --destructive: oklch(0.704 0.191 22.216);
 --border: oklch(1 0 0 / 10%);
 --input: oklch(1 0 0 / 15%);
 --ring: oklch(0.553 0.013 58.071);
 --chart-1: oklch(0.488 0.243 264.376);
 --chart-2: oklch(0.696 0.17 162.48);
 --chart-3: oklch(0.769 0.188 70.08);
 --chart-4: oklch(0.627 0.265 303.9);
 --chart-5: oklch(0.645 0.246 16.439);
 --sidebar: oklch(0.216 0.006 56.043);
 --sidebar-foreground: oklch(0.985 0.001 106.423);
 --sidebar-primary: oklch(0.488 0.243 264.376);
 --sidebar-primary-foreground: oklch(0.985 0.001 106.423);
 --sidebar-accent: oklch(0.268 0.007 34.298);
 --sidebar-accent-foreground: oklch(0.985 0.001 106.423);
 --sidebar-border: oklch(1 0 0 / 10%);
 --sidebar-ring: oklch(0.553 0.013 58.071);
}
```
Copy
### [](https://ui.shadcn.com/docs/theming#zinc)Zinc
app/globals.css
```
:root {
 --radius: 0.625rem;
 --background: oklch(1 0 0);
 --foreground: oklch(0.141 0.005 285.823);
 --card: oklch(1 0 0);
 --card-foreground: oklch(0.141 0.005 285.823);
 --popover: oklch(1 0 0);
 --popover-foreground: oklch(0.141 0.005 285.823);
 --primary: oklch(0.21 0.006 285.885);
 --primary-foreground: oklch(0.985 0 0);
 --secondary: oklch(0.967 0.001 286.375);
 --secondary-foreground: oklch(0.21 0.006 285.885);
 --muted: oklch(0.967 0.001 286.375);
 --muted-foreground: oklch(0.552 0.016 285.938);
 --accent: oklch(0.967 0.001 286.375);
 --accent-foreground: oklch(0.21 0.006 285.885);
 --destructive: oklch(0.577 0.245 27.325);
 --border: oklch(0.92 0.004 286.32);
 --input: oklch(0.92 0.004 286.32);
 --ring: oklch(0.705 0.015 286.067);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
 --sidebar: oklch(0.985 0 0);
 --sidebar-foreground: oklch(0.141 0.005 285.823);
 --sidebar-primary: oklch(0.21 0.006 285.885);
 --sidebar-primary-foreground: oklch(0.985 0 0);
 --sidebar-accent: oklch(0.967 0.001 286.375);
 --sidebar-accent-foreground: oklch(0.21 0.006 285.885);
 --sidebar-border: oklch(0.92 0.004 286.32);
 --sidebar-ring: oklch(0.705 0.015 286.067);
}
.dark {
 --background: oklch(0.141 0.005 285.823);
 --foreground: oklch(0.985 0 0);
 --card: oklch(0.21 0.006 285.885);
 --card-foreground: oklch(0.985 0 0);
 --popover: oklch(0.21 0.006 285.885);
 --popover-foreground: oklch(0.985 0 0);
 --primary: oklch(0.92 0.004 286.32);
 --primary-foreground: oklch(0.21 0.006 285.885);
 --secondary: oklch(0.274 0.006 286.033);
 --secondary-foreground: oklch(0.985 0 0);
 --muted: oklch(0.274 0.006 286.033);
 --muted-foreground: oklch(0.705 0.015 286.067);
 --accent: oklch(0.274 0.006 286.033);
 --accent-foreground: oklch(0.985 0 0);
 --destructive: oklch(0.704 0.191 22.216);
 --border: oklch(1 0 0 / 10%);
 --input: oklch(1 0 0 / 15%);
 --ring: oklch(0.552 0.016 285.938);
 --chart-1: oklch(0.488 0.243 264.376);
 --chart-2: oklch(0.696 0.17 162.48);
 --chart-3: oklch(0.769 0.188 70.08);
 --chart-4: oklch(0.627 0.265 303.9);
 --chart-5: oklch(0.645 0.246 16.439);
 --sidebar: oklch(0.21 0.006 285.885);
 --sidebar-foreground: oklch(0.985 0 0);
 --sidebar-primary: oklch(0.488 0.243 264.376);
 --sidebar-primary-foreground: oklch(0.985 0 0);
 --sidebar-accent: oklch(0.274 0.006 286.033);
 --sidebar-accent-foreground: oklch(0.985 0 0);
 --sidebar-border: oklch(1 0 0 / 10%);
 --sidebar-ring: oklch(0.552 0.016 285.938);
}
```
Copy
### [](https://ui.shadcn.com/docs/theming#neutral)Neutral
app/globals.css
```
:root {
 --radius: 0.625rem;
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
 --border: oklch(0.922 0 0);
 --input: oklch(0.922 0 0);
 --ring: oklch(0.708 0 0);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
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
 --card: oklch(0.205 0 0);
 --card-foreground: oklch(0.985 0 0);
 --popover: oklch(0.205 0 0);
 --popover-foreground: oklch(0.985 0 0);
 --primary: oklch(0.922 0 0);
 --primary-foreground: oklch(0.205 0 0);
 --secondary: oklch(0.269 0 0);
 --secondary-foreground: oklch(0.985 0 0);
 --muted: oklch(0.269 0 0);
 --muted-foreground: oklch(0.708 0 0);
 --accent: oklch(0.269 0 0);
 --accent-foreground: oklch(0.985 0 0);
 --destructive: oklch(0.704 0.191 22.216);
 --border: oklch(1 0 0 / 10%);
 --input: oklch(1 0 0 / 15%);
 --ring: oklch(0.556 0 0);
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
 --sidebar-border: oklch(1 0 0 / 10%);
 --sidebar-ring: oklch(0.556 0 0);
}
```
Copy
### [](https://ui.shadcn.com/docs/theming#gray)Gray
app/globals.css
```
:root {
 --radius: 0.625rem;
 --background: oklch(1 0 0);
 --foreground: oklch(0.13 0.028 261.692);
 --card: oklch(1 0 0);
 --card-foreground: oklch(0.13 0.028 261.692);
 --popover: oklch(1 0 0);
 --popover-foreground: oklch(0.13 0.028 261.692);
 --primary: oklch(0.21 0.034 264.665);
 --primary-foreground: oklch(0.985 0.002 247.839);
 --secondary: oklch(0.967 0.003 264.542);
 --secondary-foreground: oklch(0.21 0.034 264.665);
 --muted: oklch(0.967 0.003 264.542);
 --muted-foreground: oklch(0.551 0.027 264.364);
 --accent: oklch(0.967 0.003 264.542);
 --accent-foreground: oklch(0.21 0.034 264.665);
 --destructive: oklch(0.577 0.245 27.325);
 --border: oklch(0.928 0.006 264.531);
 --input: oklch(0.928 0.006 264.531);
 --ring: oklch(0.707 0.022 261.325);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
 --sidebar: oklch(0.985 0.002 247.839);
 --sidebar-foreground: oklch(0.13 0.028 261.692);
 --sidebar-primary: oklch(0.21 0.034 264.665);
 --sidebar-primary-foreground: oklch(0.985 0.002 247.839);
 --sidebar-accent: oklch(0.967 0.003 264.542);
 --sidebar-accent-foreground: oklch(0.21 0.034 264.665);
 --sidebar-border: oklch(0.928 0.006 264.531);
 --sidebar-ring: oklch(0.707 0.022 261.325);
}
.dark {
 --background: oklch(0.13 0.028 261.692);
 --foreground: oklch(0.985 0.002 247.839);
 --card: oklch(0.21 0.034 264.665);
 --card-foreground: oklch(0.985 0.002 247.839);
 --popover: oklch(0.21 0.034 264.665);
 --popover-foreground: oklch(0.985 0.002 247.839);
 --primary: oklch(0.928 0.006 264.531);
 --primary-foreground: oklch(0.21 0.034 264.665);
 --secondary: oklch(0.278 0.033 256.848);
 --secondary-foreground: oklch(0.985 0.002 247.839);
 --muted: oklch(0.278 0.033 256.848);
 --muted-foreground: oklch(0.707 0.022 261.325);
 --accent: oklch(0.278 0.033 256.848);
 --accent-foreground: oklch(0.985 0.002 247.839);
 --destructive: oklch(0.704 0.191 22.216);
 --border: oklch(1 0 0 / 10%);
 --input: oklch(1 0 0 / 15%);
 --ring: oklch(0.551 0.027 264.364);
 --chart-1: oklch(0.488 0.243 264.376);
 --chart-2: oklch(0.696 0.17 162.48);
 --chart-3: oklch(0.769 0.188 70.08);
 --chart-4: oklch(0.627 0.265 303.9);
 --chart-5: oklch(0.645 0.246 16.439);
 --sidebar: oklch(0.21 0.034 264.665);
 --sidebar-foreground: oklch(0.985 0.002 247.839);
 --sidebar-primary: oklch(0.488 0.243 264.376);
 --sidebar-primary-foreground: oklch(0.985 0.002 247.839);
 --sidebar-accent: oklch(0.278 0.033 256.848);
 --sidebar-accent-foreground: oklch(0.985 0.002 247.839);
 --sidebar-border: oklch(1 0 0 / 10%);
 --sidebar-ring: oklch(0.551 0.027 264.364);
}
```
Copy
### [](https://ui.shadcn.com/docs/theming#slate)Slate
app/globals.css
```
:root {
 --radius: 0.625rem;
 --background: oklch(1 0 0);
 --foreground: oklch(0.129 0.042 264.695);
 --card: oklch(1 0 0);
 --card-foreground: oklch(0.129 0.042 264.695);
 --popover: oklch(1 0 0);
 --popover-foreground: oklch(0.129 0.042 264.695);
 --primary: oklch(0.208 0.042 265.755);
 --primary-foreground: oklch(0.984 0.003 247.858);
 --secondary: oklch(0.968 0.007 247.896);
 --secondary-foreground: oklch(0.208 0.042 265.755);
 --muted: oklch(0.968 0.007 247.896);
 --muted-foreground: oklch(0.554 0.046 257.417);
 --accent: oklch(0.968 0.007 247.896);
 --accent-foreground: oklch(0.208 0.042 265.755);
 --destructive: oklch(0.577 0.245 27.325);
 --border: oklch(0.929 0.013 255.508);
 --input: oklch(0.929 0.013 255.508);
 --ring: oklch(0.704 0.04 256.788);
 --chart-1: oklch(0.646 0.222 41.116);
 --chart-2: oklch(0.6 0.118 184.704);
 --chart-3: oklch(0.398 0.07 227.392);
 --chart-4: oklch(0.828 0.189 84.429);
 --chart-5: oklch(0.769 0.188 70.08);
 --sidebar: oklch(0.984 0.003 247.858);
 --sidebar-foreground: oklch(0.129 0.042 264.695);
 --sidebar-primary: oklch(0.208 0.042 265.755);
 --sidebar-primary-foreground: oklch(0.984 0.003 247.858);
 --sidebar-accent: oklch(0.968 0.007 247.896);
 --sidebar-accent-foreground: oklch(0.208 0.042 265.755);
 --sidebar-border: oklch(0.929 0.013 255.508);
 --sidebar-ring: oklch(0.704 0.04 256.788);
}
.dark {
 --background: oklch(0.129 0.042 264.695);
 --foreground: oklch(0.984 0.003 247.858);
 --card: oklch(0.208 0.042 265.755);
 --card-foreground: oklch(0.984 0.003 247.858);
 --popover: oklch(0.208 0.042 265.755);
 --popover-foreground: oklch(0.984 0.003 247.858);
 --primary: oklch(0.929 0.013 255.508);
 --primary-foreground: oklch(0.208 0.042 265.755);
 --secondary: oklch(0.279 0.041 260.031);
 --secondary-foreground: oklch(0.984 0.003 247.858);
 --muted: oklch(0.279 0.041 260.031);
 --muted-foreground: oklch(0.704 0.04 256.788);
 --accent: oklch(0.279 0.041 260.031);
 --accent-foreground: oklch(0.984 0.003 247.858);
 --destructive: oklch(0.704 0.191 22.216);
 --border: oklch(1 0 0 / 10%);
 --input: oklch(1 0 0 / 15%);
 --ring: oklch(0.551 0.027 264.364);
 --chart-1: oklch(0.488 0.243 264.376);
 --chart-2: oklch(0.696 0.17 162.48);
 --chart-3: oklch(0.769 0.188 70.08);
 --chart-4: oklch(0.627 0.265 303.9);
 --chart-5: oklch(0.645 0.246 16.439);
 --sidebar: oklch(0.208 0.042 265.755);
 --sidebar-foreground: oklch(0.984 0.003 247.858);
 --sidebar-primary: oklch(0.488 0.243 264.376);
 --sidebar-primary-foreground: oklch(0.984 0.003 247.858);
 --sidebar-accent: oklch(0.279 0.041 260.031);
 --sidebar-accent-foreground: oklch(0.984 0.003 247.858);
 --sidebar-border: oklch(1 0 0 / 10%);
 --sidebar-ring: oklch(0.551 0.027 264.364);
}
```
Copy
[components.json](https://ui.shadcn.com/docs/components-json)[Dark mode](https://ui.shadcn.com/docs/dark-mode)
On This Page
  * [CSS Variables](https://ui.shadcn.com/docs/theming#css-variables)
  * [Utility classes](https://ui.shadcn.com/docs/theming#utility-classes)
  * [Convention](https://ui.shadcn.com/docs/theming#convention)
  * [List of variables](https://ui.shadcn.com/docs/theming#list-of-variables)
  * [Adding new colors](https://ui.shadcn.com/docs/theming#adding-new-colors)
  * [Other color formats](https://ui.shadcn.com/docs/theming#other-color-formats)
  * [Base Colors](https://ui.shadcn.com/docs/theming#base-colors)
    * [Stone](https://ui.shadcn.com/docs/theming#stone)
    * [Zinc](https://ui.shadcn.com/docs/theming#zinc)
    * [Neutral](https://ui.shadcn.com/docs/theming#neutral)
    * [Gray](https://ui.shadcn.com/docs/theming#gray)
    * [Slate](https://ui.shadcn.com/docs/theming#slate)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

