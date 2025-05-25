---
url: https://ui.shadcn.com/docs/components/dropdown-menu
scraped_at: 2025-05-24T22:26:05.257086
title: Dropdown Menu - shadcn/ui
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
Dropdown Menu
# Dropdown Menu
Displays a menu to the user — such as a set of actions or functions — triggered by a button.
[Docs](https://www.radix-ui.com/docs/primitives/components/dropdown-menu)[API Reference](https://www.radix-ui.com/docs/primitives/components/dropdown-menu#api-reference)
PreviewCode
Style: New York
Open in Copy
Open
## [](https://ui.shadcn.com/docs/components/dropdown-menu#installation)Installation
CLIManual
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest add dropdown-menu

```

Copy
## [](https://ui.shadcn.com/docs/components/dropdown-menu#usage)Usage
```
import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuLabel,
 DropdownMenuSeparator,
 DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
```
Copy
```
<DropdownMenu>
 <DropdownMenuTrigger>Open</DropdownMenuTrigger>
 <DropdownMenuContent>
  <DropdownMenuLabel>My Account</DropdownMenuLabel>
  <DropdownMenuSeparator />
  <DropdownMenuItem>Profile</DropdownMenuItem>
  <DropdownMenuItem>Billing</DropdownMenuItem>
  <DropdownMenuItem>Team</DropdownMenuItem>
  <DropdownMenuItem>Subscription</DropdownMenuItem>
 </DropdownMenuContent>
</DropdownMenu>
```
Copy
## [](https://ui.shadcn.com/docs/components/dropdown-menu#examples)Examples
### [](https://ui.shadcn.com/docs/components/dropdown-menu#checkboxes)Checkboxes
PreviewCode
Style: New York
Open in Copy
Open
### [](https://ui.shadcn.com/docs/components/dropdown-menu#radio-group)Radio Group
PreviewCode
Style: New York
Open in Copy
Open
## [](https://ui.shadcn.com/docs/components/dropdown-menu#changelog)Changelog
### [](https://ui.shadcn.com/docs/components/dropdown-menu#2024-10-16-classes-for-icons)2024-10-16 Classes for icons
Added `gap-2 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0` to the `DropdownMenuItem` to automatically style icon inside the dropdown menu item.
Add the following classes to the `DropdownMenuItem` in your `dropdown-menu.tsx` file.
dropdown-menu.tsx
```
const DropdownMenuItem = React.forwardRef<
 React.ElementRef<typeof DropdownMenuPrimitive.Item>,
 React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item> & {
  inset?: boolean
 }
>(({ className, inset, ...props }, ref) => (
 <DropdownMenuPrimitive.Item
  ref={ref}
  className={cn(
   "relative ... gap-2 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
   inset && "pl-8",
   className
  )}
  {...props}
 />
))
```
Copy
### [](https://ui.shadcn.com/docs/components/dropdown-menu#2024-10-25-classes-for-dropdownmenusubtrigger-)2024-10-25 Classes for `<DropdownMenuSubTrigger />`
Added `gap-2 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0` to the `<DropdownMenuSubTrigger />` to automatically style icon inside.
Add the following classes to the `cva` call in your `dropdown-menu.tsx` file.
dropdown-menu.tsx
```
<DropdownMenuPrimitive.SubTrigger
 ref={ref}
 className={cn(
  "flex cursor-default gap-2 select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent data-[state=open]:bg-accent [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  inset && "pl-8",
  className
 )}
 {...props}
>
 {/* ... */}
</DropdownMenuPrimitive.SubTrigger>
```
Copy
[Drawer](https://ui.shadcn.com/docs/components/drawer)[Form](https://ui.shadcn.com/docs/components/form)
On This Page
  * [Installation](https://ui.shadcn.com/docs/components/dropdown-menu#installation)
  * [Usage](https://ui.shadcn.com/docs/components/dropdown-menu#usage)
  * [Examples](https://ui.shadcn.com/docs/components/dropdown-menu#examples)
    * [Checkboxes](https://ui.shadcn.com/docs/components/dropdown-menu#checkboxes)
    * [Radio Group](https://ui.shadcn.com/docs/components/dropdown-menu#radio-group)
  * [Changelog](https://ui.shadcn.com/docs/components/dropdown-menu#changelog)
    * [2024-10-16 Classes for icons](https://ui.shadcn.com/docs/components/dropdown-menu#2024-10-16-classes-for-icons)
    * [2024-10-25 Classes for <DropdownMenuSubTrigger />](https://ui.shadcn.com/docs/components/dropdown-menu#2024-10-25-classes-for-dropdownmenusubtrigger-)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

