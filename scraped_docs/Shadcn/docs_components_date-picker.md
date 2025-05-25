---
url: https://ui.shadcn.com/docs/components/date-picker
scraped_at: 2025-05-24T22:26:31.297123
title: Date Picker - shadcn/ui
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
Date Picker
# Date Picker
A date picker component with range and presets.
PreviewCode
Style: New York
Open in Copy
Pick a date
## [](https://ui.shadcn.com/docs/components/date-picker#installation)Installation
The Date Picker is built using a composition of the `<Popover />` and the `<Calendar />` components.
See installation instructions for the [Popover](https://ui.shadcn.com/docs/components/popover#installation) and the [Calendar](https://ui.shadcn.com/docs/components/calendar#installation) components.
## [](https://ui.shadcn.com/docs/components/date-picker#usage)Usage
```
"use client"
import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
 Popover,
 PopoverContent,
 PopoverTrigger,
} from "@/components/ui/popover"
export function DatePickerDemo() {
 const [date, setDate] = React.useState<Date>()
 return (
  <Popover>
   <PopoverTrigger asChild>
    <Button
     variant={"outline"}
     className={cn(
      "w-[280px] justify-start text-left font-normal",
      !date && "text-muted-foreground"
     )}
    >
     <CalendarIcon className="mr-2 h-4 w-4" />
     {date ? format(date, "PPP") : <span>Pick a date</span>}
    </Button>
   </PopoverTrigger>
   <PopoverContent className="w-auto p-0">
    <Calendar
     mode="single"
     selected={date}
     onSelect={setDate}
     initialFocus
    />
   </PopoverContent>
  </Popover>
 )
}
```
Copy
See the [React DayPicker](https://react-day-picker.js.org) documentation for more information.
## [](https://ui.shadcn.com/docs/components/date-picker#examples)Examples
### [](https://ui.shadcn.com/docs/components/date-picker#date-picker)Date Picker
PreviewCode
Style: New York
Open in Copy
Pick a date
### [](https://ui.shadcn.com/docs/components/date-picker#date-range-picker)Date Range Picker
PreviewCode
Style: New York
Open in Copy
Jan 20, 2022 - Feb 09, 2022
### [](https://ui.shadcn.com/docs/components/date-picker#with-presets)With Presets
PreviewCode
Style: New York
Open in Copy
Pick a date
### [](https://ui.shadcn.com/docs/components/date-picker#form)Form
PreviewCode
Style: New York
Copy
Date of birthPick a date
Your date of birth is used to calculate your age.
Submit
[Data Table](https://ui.shadcn.com/docs/components/data-table)[Dialog](https://ui.shadcn.com/docs/components/dialog)
On This Page
  * [Installation](https://ui.shadcn.com/docs/components/date-picker#installation)
  * [Usage](https://ui.shadcn.com/docs/components/date-picker#usage)
  * [Examples](https://ui.shadcn.com/docs/components/date-picker#examples)
    * [Date Picker](https://ui.shadcn.com/docs/components/date-picker#date-picker)
    * [Date Range Picker](https://ui.shadcn.com/docs/components/date-picker#date-range-picker)
    * [With Presets](https://ui.shadcn.com/docs/components/date-picker#with-presets)
    * [Form](https://ui.shadcn.com/docs/components/date-picker#form)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

