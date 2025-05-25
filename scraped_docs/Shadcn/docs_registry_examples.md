---
url: https://ui.shadcn.com/docs/registry/examples
scraped_at: 2025-05-24T22:26:18.263994
title: Examples - shadcn/ui
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
Examples
# Examples
Examples of registry items: styles, components, css vars, etc.
## [](https://ui.shadcn.com/docs/registry/examples#registrystyle)registry:style
### [](https://ui.shadcn.com/docs/registry/examples#custom-style-that-extends-shadcnui)Custom style that extends shadcn/ui
The following registry item is a custom style that extends shadcn/ui. On `npx shadcn init`, it will:
  * Install `@tabler/icons-react` as a dependency.
  * Add the `login-01` block and `calendar` component to the project.
  * Add the `editor` from a remote registry.
  * Set the `font-sans` variable to `Inter, sans-serif`.
  * Install a `brand` color in light and dark mode.


example-style.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "example-style",
 "type": "registry:style",
 "dependencies": ["@tabler/icons-react"],
 "registryDependencies": [
  "login-01",
  "calendar",
  "https://example.com/r/editor.json"
 ],
 "cssVars": {
  "theme": {
   "font-sans": "Inter, sans-serif"
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
### [](https://ui.shadcn.com/docs/registry/examples#custom-style-from-scratch)Custom style from scratch
The following registry item is a custom style that doesn't extend shadcn/ui. See the `extends: none` field.
It can be used to create a new style from scratch i.e custom components, css vars, dependencies, etc.
On `npx shadcn add`, the following will:
  * Install `tailwind-merge` and `clsx` as dependencies.
  * Add the `utils` registry item from the shadcn/ui registry.
  * Add the `button`, `input`, `label`, and `select` components from a remote registry.
  * Install new css vars: `main`, `bg`, `border`, `text`, `ring`.


example-style.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "extends": "none",
 "name": "new-style",
 "type": "registry:style",
 "dependencies": ["tailwind-merge", "clsx"],
 "registryDependencies": [
  "utils",
  "https://example.com/r/button.json",
  "https://example.com/r/input.json",
  "https://example.com/r/label.json",
  "https://example.com/r/select.json"
 ],
 "cssVars": {
  "theme": {
   "font-sans": "Inter, sans-serif",
  }
  "light": {
   "main": "#88aaee",
   "bg": "#dfe5f2",
   "border": "#000",
   "text": "#000",
   "ring": "#000",
  },
  "dark": {
   "main": "#88aaee",
   "bg": "#272933",
   "border": "#000",
   "text": "#e6e6e6",
   "ring": "#fff",
  }
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/registry/examples#registrytheme)registry:theme
### [](https://ui.shadcn.com/docs/registry/examples#custom-theme)Custom theme
example-theme.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-theme",
 "type": "registry:theme",
 "cssVars": {
  "light": {
   "background": "oklch(1 0 0)",
   "foreground": "oklch(0.141 0.005 285.823)",
   "primary": "oklch(0.546 0.245 262.881)",
   "primary-foreground": "oklch(0.97 0.014 254.604)",
   "ring": "oklch(0.746 0.16 232.661)",
   "sidebar-primary": "oklch(0.546 0.245 262.881)",
   "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
   "sidebar-ring": "oklch(0.746 0.16 232.661)"
  },
  "dark": {
   "background": "oklch(1 0 0)",
   "foreground": "oklch(0.141 0.005 285.823)",
   "primary": "oklch(0.707 0.165 254.624)",
   "primary-foreground": "oklch(0.97 0.014 254.604)",
   "ring": "oklch(0.707 0.165 254.624)",
   "sidebar-primary": "oklch(0.707 0.165 254.624)",
   "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
   "sidebar-ring": "oklch(0.707 0.165 254.624)"
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/examples#custom-colors)Custom colors
The following style will init using shadcn/ui defaults and then add a custom `brand` color.
example-style.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-style",
 "type": "registry:style",
 "cssVars": {
  "light": {
   "brand": "oklch(0.99 0.00 0)"
  },
  "dark": {
   "brand": "oklch(0.14 0.00 286)"
  }
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/registry/examples#registryblock)registry:block
### [](https://ui.shadcn.com/docs/registry/examples#custom-block)Custom block
This blocks installs the `login-01` block from the shadcn/ui registry.
login-01.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "login-01",
 "type": "registry:block",
 "description": "A simple login form.",
 "registryDependencies": ["button", "card", "input", "label"],
 "files": [
  {
   "path": "blocks/login-01/page.tsx",
   "content": "import { LoginForm } ...",
   "type": "registry:page",
   "target": "app/login/page.tsx"
  },
  {
   "path": "blocks/login-01/components/login-form.tsx",
   "content": "...",
   "type": "registry:component"
  }
 ]
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/examples#install-a-block-and-override-primitives)Install a block and override primitives
You can install a block fromt the shadcn/ui registry and override the primitives using your custom ones.
On `npx shadcn add`, the following will:
  * Add the `login-01` block from the shadcn/ui registry.
  * Override the `button`, `input`, and `label` primitives with the ones from the remote registry.


example-style.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-login",
 "type": "registry:block",
 "registryDependencies": [
  "login-01",
  "https://example.com/r/button.json",
  "https://example.com/r/input.json",
  "https://example.com/r/label.json"
 ]
}
```
Copy
## [](https://ui.shadcn.com/docs/registry/examples#css-variables)CSS Variables
### [](https://ui.shadcn.com/docs/registry/examples#custom-theme-variables)Custom Theme Variables
Add custom theme variables to the `theme` object.
example-theme.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-theme",
 "type": "registry:theme",
 "cssVars": {
  "theme": {
   "font-heading": "Inter, sans-serif",
   "shadow-card": "0 0 0 1px rgba(0, 0, 0, 0.1)"
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/examples#override-tailwind-css-variables)Override Tailwind CSS variables
example-theme.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-theme",
 "type": "registry:theme",
 "cssVars": {
  "theme": {
   "spacing": "0.2rem",
   "breakpoint-sm": "640px",
   "breakpoint-md": "768px",
   "breakpoint-lg": "1024px",
   "breakpoint-xl": "1280px",
   "breakpoint-2xl": "1536px"
  }
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/registry/examples#add-custom-css)Add custom CSS
### [](https://ui.shadcn.com/docs/registry/examples#base-styles)Base styles
example-base.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-style",
 "type": "registry:style",
 "css": {
  "@layer base": {
   "h1": {
    "font-size": "var(--text-2xl)"
   },
   "h2": {
    "font-size": "var(--text-xl)"
   }
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/examples#components)Components
example-card.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-card",
 "type": "registry:component",
 "css": {
  "@layer components": {
   "card": {
    "background-color": "var(--color-white)",
    "border-radius": "var(--rounded-lg)",
    "padding": "var(--spacing-6)",
    "box-shadow": "var(--shadow-xl)"
   }
  }
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/registry/examples#add-custom-utilities)Add custom utilities
### [](https://ui.shadcn.com/docs/registry/examples#simple-utility)Simple utility
example-component.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-component",
 "type": "registry:component",
 "css": {
  "@utility content-auto": {
   "content-visibility": "auto"
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/examples#complex-utility)Complex utility
example-utility.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-component",
 "type": "registry:component",
 "css": {
  "@utility scrollbar-hidden": {
   "scrollbar-hidden": {
    "&::-webkit-scrollbar": {
     "display": "none"
    }
   }
  }
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/registry/examples#functional-utilities)Functional utilities
example-functional.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-component",
 "type": "registry:component",
 "css": {
  "@utility tab-*": {
   "tab-size": "var(--tab-size-*)"
  }
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/registry/examples#add-custom-animations)Add custom animations
Note: you need to define both `@keyframes` in css and `theme` in cssVars to use animations.
example-component.json
```
{
 "$schema": "https://ui.shadcn.com/schema/registry-item.json",
 "name": "custom-component",
 "type": "registry:component",
 "cssVars": {
  "theme": {
   "--animate-wiggle": "wiggle 1s ease-in-out infinite"
  }
 },
 "css": {
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
[Getting Started](https://ui.shadcn.com/docs/registry/getting-started)[Open in v0](https://ui.shadcn.com/docs/registry/open-in-v0)
On This Page
  * [registry:style](https://ui.shadcn.com/docs/registry/examples#registrystyle)
    * [Custom style that extends shadcn/ui](https://ui.shadcn.com/docs/registry/examples#custom-style-that-extends-shadcnui)
    * [Custom style from scratch](https://ui.shadcn.com/docs/registry/examples#custom-style-from-scratch)
  * [registry:theme](https://ui.shadcn.com/docs/registry/examples#registrytheme)
    * [Custom theme](https://ui.shadcn.com/docs/registry/examples#custom-theme)
    * [Custom colors](https://ui.shadcn.com/docs/registry/examples#custom-colors)
  * [registry:block](https://ui.shadcn.com/docs/registry/examples#registryblock)
    * [Custom block](https://ui.shadcn.com/docs/registry/examples#custom-block)
    * [Install a block and override primitives](https://ui.shadcn.com/docs/registry/examples#install-a-block-and-override-primitives)
  * [CSS Variables](https://ui.shadcn.com/docs/registry/examples#css-variables)
    * [Custom Theme Variables](https://ui.shadcn.com/docs/registry/examples#custom-theme-variables)
    * [Override Tailwind CSS variables](https://ui.shadcn.com/docs/registry/examples#override-tailwind-css-variables)
  * [Add custom CSS](https://ui.shadcn.com/docs/registry/examples#add-custom-css)
    * [Base styles](https://ui.shadcn.com/docs/registry/examples#base-styles)
    * [Components](https://ui.shadcn.com/docs/registry/examples#components)
  * [Add custom utilities](https://ui.shadcn.com/docs/registry/examples#add-custom-utilities)
    * [Simple utility](https://ui.shadcn.com/docs/registry/examples#simple-utility)
    * [Complex utility](https://ui.shadcn.com/docs/registry/examples#complex-utility)
    * [Functional utilities](https://ui.shadcn.com/docs/registry/examples#functional-utilities)
  * [Add custom animations](https://ui.shadcn.com/docs/registry/examples#add-custom-animations)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

