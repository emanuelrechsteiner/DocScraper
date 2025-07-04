---
url: https://ui.shadcn.com/docs/components/breadcrumb
scraped_at: 2025-05-24T22:24:36.690521
title: Breadcrumb - shadcn/ui
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
Breadcrumb
# Breadcrumb
Displays the path to the current resource using a hierarchy of links.
PreviewCode
Style: New York
Open in Copy
  1. [Home](https://ui.shadcn.com/)
  2. MoreToggle menu
  3. [Components](https://ui.shadcn.com/docs/components)
  4. Breadcrumb


## [](https://ui.shadcn.com/docs/components/breadcrumb#installation)Installation
CLIManual
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest add breadcrumb

```

Copy
## [](https://ui.shadcn.com/docs/components/breadcrumb#usage)Usage
```
import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbLink,
 BreadcrumbList,
 BreadcrumbPage,
 BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
```
Copy
```
<Breadcrumb>
 <BreadcrumbList>
  <BreadcrumbItem>
   <BreadcrumbLink href="/">Home</BreadcrumbLink>
  </BreadcrumbItem>
  <BreadcrumbSeparator />
  <BreadcrumbItem>
   <BreadcrumbLink href="/components">Components</BreadcrumbLink>
  </BreadcrumbItem>
  <BreadcrumbSeparator />
  <BreadcrumbItem>
   <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
  </BreadcrumbItem>
 </BreadcrumbList>
</Breadcrumb>
```
Copy
## [](https://ui.shadcn.com/docs/components/breadcrumb#examples)Examples
### [](https://ui.shadcn.com/docs/components/breadcrumb#custom-separator)Custom separator
Use a custom component as `children` for `<BreadcrumbSeparator />` to create a custom separator.
PreviewCode
Style: New York
Open in Copy
  1. [Home](https://ui.shadcn.com/)
  2. [Components](https://ui.shadcn.com/components)
  3. Breadcrumb


```
import { Slash } from "lucide-react"
...
<Breadcrumb>
 <BreadcrumbList>
  <BreadcrumbItem>
   <BreadcrumbLink href="/">Home</BreadcrumbLink>
  </BreadcrumbItem>
  <BreadcrumbSeparator>
   <Slash />
  </BreadcrumbSeparator>
  <BreadcrumbItem>
   <BreadcrumbLink href="/components">Components</BreadcrumbLink>
  </BreadcrumbItem>
 </BreadcrumbList>
</Breadcrumb>
```
Copy
### [](https://ui.shadcn.com/docs/components/breadcrumb#dropdown)Dropdown
You can compose `<BreadcrumbItem />` with a `<DropdownMenu />` to create a dropdown in the breadcrumb.
PreviewCode
Style: New York
Open in Copy
  1. [Home](https://ui.shadcn.com/)
  2. Components
  3. Breadcrumb


```
import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
...
<BreadcrumbItem>
 <DropdownMenu>
  <DropdownMenuTrigger className="flex items-center gap-1">
   Components
   <ChevronDownIcon />
  </DropdownMenuTrigger>
  <DropdownMenuContent align="start">
   <DropdownMenuItem>Documentation</DropdownMenuItem>
   <DropdownMenuItem>Themes</DropdownMenuItem>
   <DropdownMenuItem>GitHub</DropdownMenuItem>
  </DropdownMenuContent>
 </DropdownMenu>
</BreadcrumbItem>
```
Copy
### [](https://ui.shadcn.com/docs/components/breadcrumb#collapsed)Collapsed
We provide a `<BreadcrumbEllipsis />` component to show a collapsed state when the breadcrumb is too long.
PreviewCode
Style: New York
Open in Copy
  1. [Home](https://ui.shadcn.com/)
  2. More
  3. [Components](https://ui.shadcn.com/docs/components)
  4. Breadcrumb


```
import { BreadcrumbEllipsis } from "@/components/ui/breadcrumb"
...
<Breadcrumb>
 <BreadcrumbList>
  {/* ... */}
  <BreadcrumbItem>
   <BreadcrumbEllipsis />
  </BreadcrumbItem>
  {/* ... */}
 </BreadcrumbList>
</Breadcrumb>
```
Copy
### [](https://ui.shadcn.com/docs/components/breadcrumb#link-component)Link component
To use a custom link component from your routing library, you can use the `asChild` prop on `<BreadcrumbLink />`.
PreviewCode
Style: New York
Open in Copy
  1. [Home](https://ui.shadcn.com/)
  2. [Components](https://ui.shadcn.com/components)
  3. Breadcrumb


```
import { Link } from "next/link"
...
<Breadcrumb>
 <BreadcrumbList>
  <BreadcrumbItem>
   <BreadcrumbLink asChild>
    <Link href="/">Home</Link>
   </BreadcrumbLink>
  </BreadcrumbItem>
  {/* ... */}
 </BreadcrumbList>
</Breadcrumb>
```
Copy
### [](https://ui.shadcn.com/docs/components/breadcrumb#responsive)Responsive
Here's an example of a responsive breadcrumb that composes `<BreadcrumbItem />` with `<BreadcrumbEllipsis />`, `<DropdownMenu />`, and `<Drawer />`.
It displays a dropdown on desktop and a drawer on mobile.
PreviewCode
Style: New York
Open in Copy
  1. [Home](https://ui.shadcn.com/docs/components/breadcrumb)
  2. More
  3. [Data Fetching](https://ui.shadcn.com/docs/components/breadcrumb)
  4. Caching and Revalidating


[Badge](https://ui.shadcn.com/docs/components/badge)[Button](https://ui.shadcn.com/docs/components/button)
On This Page
  * [Installation](https://ui.shadcn.com/docs/components/breadcrumb#installation)
  * [Usage](https://ui.shadcn.com/docs/components/breadcrumb#usage)
  * [Examples](https://ui.shadcn.com/docs/components/breadcrumb#examples)
    * [Custom separator](https://ui.shadcn.com/docs/components/breadcrumb#custom-separator)
    * [Dropdown](https://ui.shadcn.com/docs/components/breadcrumb#dropdown)
    * [Collapsed](https://ui.shadcn.com/docs/components/breadcrumb#collapsed)
    * [Link component](https://ui.shadcn.com/docs/components/breadcrumb#link-component)
    * [Responsive](https://ui.shadcn.com/docs/components/breadcrumb#responsive)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

