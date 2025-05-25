---
url: https://ui.shadcn.com/docs
scraped_at: 2025-05-24T22:23:53.116047
title: Introduction - shadcn/ui
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
Introduction
# Introduction
shadcn/ui is a set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks and AI models. Open Source. Open Code.
**This is not a component library. It is how you build your component library.**
You know how most traditional component libraries work: you install a package from NPM, import the components, and use them in your app.
This approach works well until you need to customize a component to fit your design system or require one that isn’t included in the library. **Often, you end up wrapping library components, writing workarounds to override styles, or mixing components from different libraries with incompatible APIs.**
This is what shadcn/ui aims to solve. It is built around the following principles:
  * **Open Code:** The top layer of your component code is open for modification.
  * **Composition:** Every component uses a common, composable interface, making them predictable.
  * **Distribution:** A flat-file schema and command-line tool make it easy to distribute components.
  * **Beautiful Defaults:** Carefully chosen default styles, so you get great design out-of-the-box.
  * **AI-Ready:** Open code for LLMs to read, understand, and improve.


## [](https://ui.shadcn.com/docs#open-code)Open Code
shadcn/ui hands you the actual component code. You have full control to customize and extend the components to your needs. This means:
  * **Full Transparency:** You see exactly how each component is built.
  * **Easy Customization:** Modify any part of a component to fit your design and functionality requirements.
  * **AI Integration:** Access to the code makes it straightforward for LLMs to read, understand, and even improve your components.


_In a typical library, if you need to change a button’s behavior, you have to override styles or wrap the component. With shadcn/ui, you simply edit the button code directly._
### 
How do I pull upstream updates in an Open Code approach?
## [](https://ui.shadcn.com/docs#composition)Composition
Every component in shadcn/ui shares a common, composable interface. **If a component does not exist, we bring it in, make it composable, and adjust its style to match and work with the rest of the design system.**
_A shared, composable interface means it's predictable for both your team and LLMs. You are not learning different APIs for every new component. Even for third-party ones._
## [](https://ui.shadcn.com/docs#distribution)Distribution
shadcn/ui is also a code distribution system. It defines a schema for components and a CLI to distribute them.
  * **Schema:** A flat-file structure that defines the components, their dependencies, and properties.
  * **CLI:** A command-line tool to distribute and install components across projects with cross-framework support.


_You can use the schema to distribute your components to other projects or have AI generate completely new components based on existing schema._
## [](https://ui.shadcn.com/docs#beautiful-defaults)Beautiful Defaults
shadcn/ui comes with a large collection of components that have carefully chosen default styles. They are designed to look good on their own and to work well together as a consistent system:
  * **Good Out-of-the-Box:** Your UI has a clean and minimal look without extra work.
  * **Unified Design:** Components naturally fit with one another. Each component is built to match the others, keeping your UI consistent.
  * **Easily Customizable:** If you want to change something, it's simple to override and extend the defaults.


## [](https://ui.shadcn.com/docs#ai-ready)AI-Ready
The design of shadcn/ui makes it easy for AI tools to work with your code. Its open code and consistent API allow AI models to read, understand, and even generate new components.
_An AI model can learn how your components work and suggest improvements or even create new components that integrate with your existing design._
[Installation](https://ui.shadcn.com/docs/installation)
On This Page
  * [Open Code](https://ui.shadcn.com/docs#open-code)
  * [Composition](https://ui.shadcn.com/docs#composition)
  * [Distribution](https://ui.shadcn.com/docs#distribution)
  * [Beautiful Defaults](https://ui.shadcn.com/docs#beautiful-defaults)
  * [AI-Ready](https://ui.shadcn.com/docs#ai-ready)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

