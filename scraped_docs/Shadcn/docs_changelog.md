---
url: https://ui.shadcn.com/docs/changelog
scraped_at: 2025-05-24T22:29:26.671649
title: Changelog - shadcn/ui
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
Changelog
# Changelog
Latest updates and announcements.
## [](https://ui.shadcn.com/docs/changelog#august-2024---npx-shadcn-init)August 2024 - npx shadcn init
The new CLI is now available. It's a complete rewrite with a lot of new features and improvements. You can now install components, themes, hooks, utils and more using `npx shadcn add`.
This is a major step towards distributing code that you and your LLMs can access and use.
  1. First up, the cli now has support for all major React framework out of the box. Next.js, Remix, Vite and Laravel. And when you init into a new app, we update your existing Tailwind files instead of overriding.
  2. A component now ship its own dependencies. Take the accordion for example, it can define its Tailwind keyframes. When you add it to your project, we’ll update your tailwind.config.ts file accordingly.
  3. You can also install remote components using url. `npx shadcn add https://acme.com/registry/navbar.json`.
  4. We have also improve the init command. It does framework detection and can even init a brand new Next.js app in one command. `npx shadcn init`.
  5. We have created a new schema that you can use to ship your own component registry. And since it has support for urls, you can even use it to distribute private components.
  6. And a few more updates like better error handling and monorepo support.


You can try the new cli today.
pnpmnpmyarnbun
```
pnpm dlx shadcn init sidebar-01 login-01

```

Copy
### [](https://ui.shadcn.com/docs/changelog#update-your-project)Update Your Project
To update an existing project to use the new CLI, update your `components.json` file to include import aliases for your **components** , **utils** , **ui** , **lib** and **hooks**.
components.json
```
{
 "$schema": "https://ui.shadcn.com/schema.json",
 "style": "new-york",
 "tailwind": {
  // ...
 },
 "aliases": {
  "components": "@/components",
  "utils": "@/lib/utils",
  "ui": "@/components/ui",
  "lib": "@/lib",
  "hooks": "@/hooks"
 }
}
```
Copy
If you're using a different import alias prefix eg `~`, replace `@` with your prefix.
## [](https://ui.shadcn.com/docs/changelog#april-2024---introducing-lift-mode)April 2024 - Introducing Lift Mode
We're introducing a new mode for [Blocks](https://ui.shadcn.com/blocks) called **Lift Mode**.
Enable Lift Mode to automatically "lift" smaller components from a block template for copy and paste.
[![Lift Mode](https://ui.shadcn.com/_next/image?url=%2Fimages%2Flift-mode-light.png&w=3840&q=75)![Lift Mode](https://ui.shadcn.com/_next/image?url=%2Fimages%2Flift-mode-dark.png&w=3840&q=75)View the blocks library](https://ui.shadcn.com/blocks)
With Lift Mode, you'll be able to copy the smaller components that make up a block template, like cards, buttons, and forms, and paste them directly into your project.
Visit the [Blocks](https://ui.shadcn.com/blocks) page to try it out.
## [](https://ui.shadcn.com/docs/changelog#march-2024---introducing-blocks)March 2024 - Introducing Blocks
One of the most requested features since launch has been layouts: admin dashboards with sidebar, marketing page sections, cards and more.
**Today, we're launching[**Blocks**](https://ui.shadcn.com/blocks)**.
[![Admin dashboard](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fdashboard-1.jpg&w=1920&q=75)![Admin dashboard](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fdashboard-1-dark.jpg&w=1920&q=75)View the blocks library](https://ui.shadcn.com/blocks)
Blocks are ready-made components that you can use to build your apps. They are fully responsive, accessible, and composable, meaning they are built using the same principles as the rest of the components in shadcn/ui.
We're starting with dashboard layouts and authentication pages, with plans to add more blocks in the coming weeks.
### [](https://ui.shadcn.com/docs/changelog#open-source)Open Source
Blocks are open source. You can find the source on GitHub. Use them in your projects, customize them and contribute back.
[![AI Playground](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fdashboard-2.jpg&w=1920&q=75)![AI Playground](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fdashboard-2-dark.jpg&w=1920&q=75)View the blocks library](https://ui.shadcn.com/blocks)
### [](https://ui.shadcn.com/docs/changelog#request-a-block)Request a Block
We're also introducing a "Request a Block" feature. If there's a specific block you'd like to see, simply create a request on GitHub and the community can upvote and build it.
[![Settings Page](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fdashboard-3.jpg&w=1920&q=75)![Settings Page](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fdashboard-3-dark.jpg&w=1920&q=75)View the blocks library](https://ui.shadcn.com/blocks)
### [](https://ui.shadcn.com/docs/changelog#v0)v0
If you have a [v0](https://v0.dev) account, you can use the **Edit in v0** feature to open the code on v0 for prompting and further generation.
That's it. _Looking forward to seeing what you build with Blocks_.
## [](https://ui.shadcn.com/docs/changelog#march-2024---breadcrumb-and-input-otp)March 2024 - Breadcrumb and Input OTP
We've added a new Breadcrumb component and an Input OTP component.
### [](https://ui.shadcn.com/docs/changelog#breadcrumb)Breadcrumb
An accessible and flexible breadcrumb component. It has support for collapsed items, custom separators, bring-your-own routing `<Link />` and composable with other shadcn/ui components.
PreviewCode
Style: New York
Copy
  1. [Home](https://ui.shadcn.com/)
  2. MoreToggle menu
  3. [Components](https://ui.shadcn.com/docs/components)
  4. Breadcrumb


[See more examples](https://ui.shadcn.com/docs/components/breadcrumb)
### [](https://ui.shadcn.com/docs/changelog#input-otp)Input OTP
A fully featured input OTP component. It has support for numeric and alphanumeric codes, custom length, copy-paste and accessible. Input OTP is built on top of [input-otp](https://github.com/guilhermerodz/input-otp) by [@guilherme_rodz](https://twitter.com/guilherme_rodz).
PreviewCode
Style: New York
Copy
[Read the docs](https://ui.shadcn.com/docs/components/input-otp)
If you have a [v0](https://v0.dev), the new components are available for generation.
## [](https://ui.shadcn.com/docs/changelog#december-2023---new-components-cli-and-more)December 2023 - New components, CLI and more
We've added new components to shadcn/ui and made a lot of improvements to the CLI.
Here's a quick overview of what's new:
  * [**Carousel**](https://ui.shadcn.com/docs/changelog#carousel) - A carousel component with motion, swipe gestures and keyboard support.
  * [**Drawer**](https://ui.shadcn.com/docs/changelog#drawer) - A drawer component that looks amazing on mobile.
  * [**Pagination**](https://ui.shadcn.com/docs/changelog#pagination) - A pagination component with page navigation, previous and next buttons.
  * [**Resizable**](https://ui.shadcn.com/docs/changelog#resizable) - A resizable component for building resizable panel groups and layouts.
  * [**Sonner**](https://ui.shadcn.com/docs/changelog#sonner) - The last toast component you'll ever need.
  * [**CLI updates**](https://ui.shadcn.com/docs/changelog#cli-updates) - Support for custom **Tailwind prefix** and `tailwind.config.ts`.


### [](https://ui.shadcn.com/docs/changelog#carousel)Carousel
We've added a fully featured carousel component with motion, swipe gestures and keyboard support. Built on top of [Embla Carousel](https://www.embla-carousel.com).
It has support for infinite looping, autoplay, vertical orientation, and more.
PreviewCode
Style: New York
Copy
1
2
3
4
5
Previous slideNext slide
### [](https://ui.shadcn.com/docs/changelog#drawer)Drawer
Oh the drawer component 😍. Built on top of [Vaul](https://github.com/emilkowalski/vaul) by [emilkowalski_](https://twitter.com/emilkowalski_).
Try opening the following drawer on mobile. It looks amazing!
PreviewCode
Style: New York
Copy
Open Drawer
### [](https://ui.shadcn.com/docs/changelog#pagination)Pagination
We've added a pagination component with page navigation, previous and next buttons. Simple, flexible and works with your framework's `<Link />` component.
PreviewCode
Style: New York
Copy
  * [Previous](https://ui.shadcn.com/docs/changelog)
  * [1](https://ui.shadcn.com/docs/changelog)
  * [2](https://ui.shadcn.com/docs/changelog)
  * [3](https://ui.shadcn.com/docs/changelog)
  * More pages
  * [Next](https://ui.shadcn.com/docs/changelog)


### [](https://ui.shadcn.com/docs/changelog#resizable)Resizable
Build resizable panel groups and layouts with this `<Resizable />` component.
PreviewCode
Style: New York
Copy
One
Two
Three
`<Resizable />` is built using [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) by [bvaughn](https://github.com/bvaughn). It has support for mouse, touch and keyboard.
### [](https://ui.shadcn.com/docs/changelog#sonner)Sonner
Another one by [emilkowalski_](https://twitter.com/emilkowalski_). The last toast component you'll ever need. Sonner is now availabe in shadcn/ui.
PreviewCode
Style: New York
Copy
Show Toast
### [](https://ui.shadcn.com/docs/changelog#cli-updates)CLI updates
This has been one of the most requested features. You can now configure a custom Tailwind prefix and the cli will automatically prefix your utility classes when adding components.
This means you can now easily add shadcn/ui components to existing projects like Docusaurus, Nextra...etc. A drop-in for your existing design system with no conflict. 🔥
```
<AlertDialog className="tw-grid tw-gap-4 tw-border tw-bg-background tw-shadow-lg" />
```
Copy
It works with `cn`, `cva` and CSS variables.
The cli can now also detect `tailwind.config.ts` and add the TypeScript version of the config for you.
That's it. Happy Holidays.
## [](https://ui.shadcn.com/docs/changelog#july-2023---javascript)July 2023 - JavaScript
This project and the components are written in TypeScript. **We recommend using TypeScript for your project as well**.
However we provide a JavaScript version of the components, available via the [cli](https://ui.shadcn.com/docs/cli).
```
Would you like to use TypeScript (recommended)? no
```
Copy
To opt-out of TypeScript, you can use the `tsx` flag in your `components.json` file.
components.json
```
{
 "style": "default",
 "tailwind": {
  "config": "tailwind.config.js",
  "css": "src/app/globals.css",
  "baseColor": "zinc",
  "cssVariables": true
 },
 "rsc": false,
 "tsx": false,
 "aliases": {
  "utils": "~/lib/utils",
  "components": "~/components"
 }
}
```
Copy
To configure import aliases, you can use the following `jsconfig.json`:
jsconfig.json
```
{
 "compilerOptions": {
  "paths": {
   "@/*": ["./*"]
  }
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/changelog#june-2023---new-cli-styles-and-more)June 2023 - New CLI, Styles and more
I have a lot of updates to share with you today:
  * [**New CLI**](https://ui.shadcn.com/docs/changelog#new-cli) - Rewrote the CLI from scratch. You can now add components, dependencies and configure import paths.
  * [**Theming**](https://ui.shadcn.com/docs/changelog#theming-with-css-variables-or-tailwind-colors) - Choose between using CSS variables or Tailwind CSS utility classes for theming.
  * [**Base color**](https://ui.shadcn.com/docs/changelog#base-color) - Configure the base color for your project. This will be used to generate the default color palette for your components.
  * [**React Server Components**](https://ui.shadcn.com/docs/changelog#react-server-components) - Opt out of using React Server Components. The CLI will automatically append or remove the `use client` directive.
  * [**Styles**](https://ui.shadcn.com/docs/changelog#styles) - Introducing a new concept called _Style_. A style comes with its own set of components, animations, icons and more.
  * [**Exit animations**](https://ui.shadcn.com/docs/changelog#exit-animations) - Added exit animations to all components.
  * [**Other updates**](https://ui.shadcn.com/docs/changelog#other-updates) - New `icon` button size, updated `sheet` component and more.
  * [**Updating your project**](https://ui.shadcn.com/docs/changelog#updating-your-project) - How to update your project to get the latest changes.


### [](https://ui.shadcn.com/docs/changelog#new-cli)New CLI
I've been working on a new CLI for the past few weeks. It's a complete rewrite. It comes with a lot of new features and improvements.
### [](https://ui.shadcn.com/docs/changelog#init)`init`
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest init

```

Copy
When you run the `init` command, you will be asked a few questions to configure `components.json`:
```
Which style would you like to use? › Default
Which color would you like to use as base color? › Slate
Where is your global CSS file? › › app/globals.css
Do you want to use CSS variables for colors? › no / yes
Where is your tailwind.config.js located? › tailwind.config.js
Configure the import alias for components: › @/components
Configure the import alias for utils: › @/lib/utils
Are you using React Server Components? › no / yes
```
Copy
This file contains all the information about your components: where to install them, the import paths, how they are styled...etc.
You can use this file to change the import path of a component, set a baseColor or change the styling method.
components.json
```
{
 "style": "default",
 "tailwind": {
  "config": "tailwind.config.ts",
  "css": "src/app/globals.css",
  "baseColor": "zinc",
  "cssVariables": true
 },
 "rsc": false,
 "aliases": {
  "utils": "~/lib/utils",
  "components": "~/components"
 }
}
```
Copy
This means you can now use the CLI with any directory structure including `src` and `app` directories.
### [](https://ui.shadcn.com/docs/changelog#add)`add`
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest add

```

Copy
The `add` command is now much more capable. You can now add UI components but also import more complex components (coming soon).
The CLI will automatically resolve all components and dependencies, format them based on your custom config and add them to your project.
### [](https://ui.shadcn.com/docs/changelog#diff-experimental)`diff` (experimental)
pnpmnpmyarnbun
```
pnpm dlx shadcn diff

```

Copy
We're also introducing a new `diff` command to help you keep track of upstream updates.
You can use this command to see what has changed in the upstream repository and update your project accordingly.
Run the `diff` command to get a list of components that have updates available:
pnpmnpmyarnbun
```
pnpm dlx shadcn diff

```

Copy
```
The following components have updates available:
- button
 - /path/to/my-app/components/ui/button.tsx
- toast
 - /path/to/my-app/components/ui/use-toast.ts
 - /path/to/my-app/components/ui/toaster.tsx
```
Copy
Then run `diff [component]` to see the changes:
pnpmnpmyarnbun
```
pnpm dlx shadcn diff alert

```

Copy
```
const alertVariants = cva(
- "relative w-full rounded-lg border",
+ "relative w-full pl-12 rounded-lg border"
)
```
Copy
### [](https://ui.shadcn.com/docs/changelog#theming-with-css-variables-or-tailwind-colors)Theming with CSS Variables or Tailwind Colors
You can choose between using CSS variables or Tailwind CSS utility classes for theming.
When you add new components, the CLI will automatically use the correct theming methods based on your `components.json` configuration.
#### [](https://ui.shadcn.com/docs/changelog#utility-classes)Utility classes
```
<div className="bg-zinc-950dark:bg-white" />
```
Copy
To use utility classes for theming set `tailwind.cssVariables` to `false` in your `components.json` file.
components.json
```
{
 "tailwind": {
  "config": "tailwind.config.js",
  "css": "app/globals.css",
  "baseColor": "slate",
  "cssVariables": false
 }
}
```
Copy
#### [](https://ui.shadcn.com/docs/changelog#css-variables)CSS Variables
```
<div className="bg-backgroundtext-foreground" />
```
Copy
To use CSS variables classes for theming set `tailwind.cssVariables` to `true` in your `components.json` file.
components.json
```
{
 "tailwind": {
  "config": "tailwind.config.js",
  "css": "app/globals.css",
  "baseColor": "slate",
  "cssVariables": true
 }
}
```
Copy
### [](https://ui.shadcn.com/docs/changelog#base-color)Base color
You can now configure the base color for your project. This will be used to generate the default color palette for your components.
components.json
```
{
 "tailwind": {
  "config": "tailwind.config.js",
  "css": "app/globals.css",
  "baseColor": "zinc",
  "cssVariables": false
 }
}
```
Copy
Choose between `gray`, `neutral`, `slate`, `stone` or `zinc`.
If you have `cssVariables` set to `true`, we will set the base colors as CSS variables in your `globals.css` file. If you have `cssVariables` set to `false`, we will inline the Tailwind CSS utility classes in your components.
### [](https://ui.shadcn.com/docs/changelog#react-server-components)React Server Components
If you're using a framework that does not support React Server Components, you can now opt out by setting `rsc` to `false`. We will automatically append or remove the `use client` directive when adding components.
components.json
```
{
 "rsc": false
}
```
Copy
### [](https://ui.shadcn.com/docs/changelog#styles)Styles
We are introducing a new concept called _Style_.
_You can think of style as the visual foundation: shapes, icons, animations & typography._ A style comes with its own set of components, animations, icons and more.
We are shipping two styles: `default` and `new-york` (with more coming soon).
![Default vs New York style](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fstyle.jpg&w=1920&q=75)
The `default` style is the one you are used to. It's the one we've been using since the beginning of this project. It uses `lucide-react` for icons and `tailwindcss-animate` for animations.
The `new-york` style is a new style. It ships with smaller buttons, cards with shadows and a new set of icons from [Radix Icons](https://icons.radix-ui.com).
When you run the `init` command, you will be asked which style you would like to use. This is saved in your `components.json` file.
components.json
```
{
 "style": "new-york"
}
```
Copy
### [](https://ui.shadcn.com/docs/changelog#theming)Theming
Start with a style as the base then theme using CSS variables or Tailwind CSS utility classes to completely change the look of your components.
![Style with theming](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fstyle-with-theming.jpg&w=1920&q=75)
### [](https://ui.shadcn.com/docs/changelog#exit-animations)Exit animations
I added exit animations to all components. Click on the combobox below to see the subtle exit animation.
PreviewCode
Style: New York
Copy
Select framework...
The animations can be customized using utility classes.
### [](https://ui.shadcn.com/docs/changelog#other-updates)Other updates
### [](https://ui.shadcn.com/docs/changelog#button)Button
  * Added a new button size `icon`:


PreviewCode
Style: New York
Copy
### [](https://ui.shadcn.com/docs/changelog#sheet)Sheet
  * Renamed `position` to `side` to match the other elements.


PreviewCode
Style: New York
Copy
toprightbottomleft
  * Removed the `size` props. Use `className="w-[200px] md:w-[450px]"` for responsive sizing.


### [](https://ui.shadcn.com/docs/changelog#updating-your-project)Updating your project
Since we follow a copy and paste approach, you will need to manually update your project to get the latest changes.
Note: we are working on a [`diff`](https://ui.shadcn.com/docs/changelog#diff-experimental) command to help you keep track of upstream updates.
### [](https://ui.shadcn.com/docs/changelog#add-componentsjson)Add `components.json`
Creating a `components.json` file at the root:
components.json
```
{
 "style": "default",
 "rsc": true,
 "tailwind": {
  "config": "tailwind.config.js",
  "css": "app/globals.css",
  "baseColor": "slate",
  "cssVariables": true
 },
 "aliases": {
  "components": "@/components",
  "utils": "@/lib/utils"
 }
}
```
Copy
Update the values for `tailwind.css` and `aliases` to match your project structure.
### [](https://ui.shadcn.com/docs/changelog#button-1)Button
Add the `icon` size to the `buttonVariants`:
components/ui/button.tsx
```
const buttonVariants = cva({
 variants: {
  size: {
   default: "h-10 px-4 py-2",
   sm: "h-9 rounded-md px-3",
   lg: "h-11 rounded-md px-8",
   icon: "h-10 w-10",
  },
 },
})
```
Copy
### [](https://ui.shadcn.com/docs/changelog#sheet-1)Sheet
  1. Replace the content of `sheet.tsx` with the following:


components/ui/sheet.tsx
```
"use client"
import * as React from "react"
import * as SheetPrimitive from "@radix-ui/react-dialog"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"
import { cn } from "@/lib/utils"
const Sheet = SheetPrimitive.Root
const SheetTrigger = SheetPrimitive.Trigger
const SheetClose = SheetPrimitive.Close
const SheetPortal = ({
 className,
 ...props
}: SheetPrimitive.DialogPortalProps) => (
 <SheetPrimitive.Portal className={cn(className)} {...props} />
)
SheetPortal.displayName = SheetPrimitive.Portal.displayName
const SheetOverlay = React.forwardRef<
 React.ElementRef<typeof SheetPrimitive.Overlay>,
 React.ComponentPropsWithoutRef<typeof SheetPrimitive.Overlay>
>(({ className, ...props }, ref) => (
 <SheetPrimitive.Overlay
  className={cn(
   "fixed inset-0 z-50 bg-background/80 backdrop-blur-sm data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
   className
  )}
  {...props}
  ref={ref}
 />
))
SheetOverlay.displayName = SheetPrimitive.Overlay.displayName
const sheetVariants = cva(
 "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:duration-300 data-[state=open]:duration-500",
 {
  variants: {
   side: {
    top: "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top",
    bottom:
     "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom",
    left: "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm",
    right:
     "inset-y-0 right-0 h-full w-3/4 border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm",
   },
  },
  defaultVariants: {
   side: "right",
  },
 }
)
interface SheetContentProps
 extends React.ComponentPropsWithoutRef<typeof SheetPrimitive.Content>,
  VariantProps<typeof sheetVariants> {}
const SheetContent = React.forwardRef<
 React.ElementRef<typeof SheetPrimitive.Content>,
 SheetContentProps
>(({ side = "right", className, children, ...props }, ref) => (
 <SheetPortal>
  <SheetOverlay />
  <SheetPrimitive.Content
   ref={ref}
   className={cn(sheetVariants({ side }), className)}
   {...props}
  >
   {children}
   <SheetPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary">
    <X className="h-4 w-4" />
    <span className="sr-only">Close</span>
   </SheetPrimitive.Close>
  </SheetPrimitive.Content>
 </SheetPortal>
))
SheetContent.displayName = SheetPrimitive.Content.displayName
const SheetHeader = ({
 className,
 ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
 <div
  className={cn(
   "flex flex-col space-y-2 text-center sm:text-left",
   className
  )}
  {...props}
 />
)
SheetHeader.displayName = "SheetHeader"
const SheetFooter = ({
 className,
 ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
 <div
  className={cn(
   "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
   className
  )}
  {...props}
 />
)
SheetFooter.displayName = "SheetFooter"
const SheetTitle = React.forwardRef<
 React.ElementRef<typeof SheetPrimitive.Title>,
 React.ComponentPropsWithoutRef<typeof SheetPrimitive.Title>
>(({ className, ...props }, ref) => (
 <SheetPrimitive.Title
  ref={ref}
  className={cn("text-lg font-semibold text-foreground", className)}
  {...props}
 />
))
SheetTitle.displayName = SheetPrimitive.Title.displayName
const SheetDescription = React.forwardRef<
 React.ElementRef<typeof SheetPrimitive.Description>,
 React.ComponentPropsWithoutRef<typeof SheetPrimitive.Description>
>(({ className, ...props }, ref) => (
 <SheetPrimitive.Description
  ref={ref}
  className={cn("text-sm text-muted-foreground", className)}
  {...props}
 />
))
SheetDescription.displayName = SheetPrimitive.Description.displayName
export {
 Sheet,
 SheetTrigger,
 SheetClose,
 SheetContent,
 SheetHeader,
 SheetFooter,
 SheetTitle,
 SheetDescription,
}
```
Copy
  1. Rename `position` to `side`


```
- <Sheet position="right" />
+ <Sheet side="right" />
```
Copy
### [](https://ui.shadcn.com/docs/changelog#thank-you)Thank you
I'd like to thank everyone who has been using this project, providing feedback and contributing to it. I really appreciate it. Thank you 🙏
[Figma](https://ui.shadcn.com/docs/figma)[Next.js](https://ui.shadcn.com/docs/installation/next)
Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

