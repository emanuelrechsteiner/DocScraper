---
url: https://ui.shadcn.com/blocks
scraped_at: 2025-05-24T22:28:08.377313
title: Building Blocks for the Web - shadcn/ui
---

[shadcn/ui](https://ui.shadcn.com/)[Docs](https://ui.shadcn.com/docs/installation)[Components](https://ui.shadcn.com/docs/components)[Blocks](https://ui.shadcn.com/blocks)[Charts](https://ui.shadcn.com/charts)[Themes](https://ui.shadcn.com/themes)[Colors](https://ui.shadcn.com/colors)
Toggle MenuSearch documentation...
Search documentation...Search...`⌘K`
[GitHub](https://github.com/shadcn-ui/ui)Toggle theme
[Tailwind CSSGet Started with Tailwind v4](https://ui.shadcn.com/docs/tailwind-v4)
# Building Blocks for the Web
Clean, modern building blocks. Copy and paste into your apps. Works with all React frameworks. Open Source. Free forever.
[Browse Blocks](https://ui.shadcn.com/blocks#blocks)[Add a block](https://ui.shadcn.com/docs/blocks)
[Featured](https://ui.shadcn.com/blocks)[Sidebar](https://ui.shadcn.com/blocks/sidebar)[Authentication](https://ui.shadcn.com/blocks/authentication)[Login](https://ui.shadcn.com/blocks/login)
PreviewCode
[A dashboard with sidebar, charts and data table.](https://ui.shadcn.com/blocks#dashboard-01)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/dashboard-01 "Open in New Tab")
npx shadcn add dashboard-01
Open in 
![dashboard-01](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fdashboard-01-light.png&w=3840&q=75)![dashboard-01](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fdashboard-01-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
      * data.json
  * components
    * app-sidebar.tsx
    * chart-area-interactive.tsx
    * data-table.tsx
    * nav-documents.tsx
    * nav-main.tsx
    * nav-secondary.tsx
    * nav-user.tsx
    * section-cards.tsx
    * site-header.tsx


app/dashboard/page.tsx
```
import { AppSidebar } from "@/components/app-sidebar"
import { ChartAreaInteractive } from "@/components/chart-area-interactive"
import { DataTable } from "@/components/data-table"
import { SectionCards } from "@/components/section-cards"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import data from "./data.json"
export default function Page() {
 return (
  <SidebarProvider>
   <AppSidebar variant="inset" />
   <SidebarInset>
    <SiteHeader />
    <div className="flex flex-1 flex-col">
     <div className="@container/main flex flex-1 flex-col gap-2">
      <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
       <SectionCards />
       <div className="px-4 lg:px-6">
        <ChartAreaInteractive />
       </div>
       <DataTable data={data} />
      </div>
     </div>
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar that collapses to icons.](https://ui.shadcn.com/blocks#sidebar-07)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-07 "Open in New Tab")
npx shadcn add sidebar-07
Open in 
![sidebar-07](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-07-light.png&w=3840&q=75)![sidebar-07](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-07-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * nav-main.tsx
    * nav-projects.tsx
    * nav-user.tsx
    * team-switcher.tsx


app/dashboard/page.tsx
```
import { AppSidebar } from "@/components/app-sidebar"
import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbLink,
 BreadcrumbList,
 BreadcrumbPage,
 BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
 SidebarInset,
 SidebarProvider,
 SidebarTrigger,
} from "@/components/ui/sidebar"
export default function Page() {
 return (
  <SidebarProvider>
   <AppSidebar />
   <SidebarInset>
    <header className="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12">
     <div className="flex items-center gap-2 px-4">
      <SidebarTrigger className="-ml-1" />
      <Separator orientation="vertical" className="mr-2 h-4" />
      <Breadcrumb>
       <BreadcrumbList>
        <BreadcrumbItem className="hidden md:block">
         <BreadcrumbLink href="#">
          Building Your Application
         </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator className="hidden md:block" />
        <BreadcrumbItem>
         <BreadcrumbPage>Data Fetching</BreadcrumbPage>
        </BreadcrumbItem>
       </BreadcrumbList>
      </Breadcrumb>
     </div>
    </header>
    <div className="flex flex-1 flex-col gap-4 p-4 pt-0">
     <div className="grid auto-rows-min gap-4 md:grid-cols-3">
      <div className="aspect-video rounded-xl bg-muted/50" />
      <div className="aspect-video rounded-xl bg-muted/50" />
      <div className="aspect-video rounded-xl bg-muted/50" />
     </div>
     <div className="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar with submenus.](https://ui.shadcn.com/blocks#sidebar-03)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-03 "Open in New Tab")
npx shadcn add sidebar-03
Open in 
![sidebar-03](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-03-light.png&w=3840&q=75)![sidebar-03](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-03-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx


app/dashboard/page.tsx
```
import { AppSidebar } from "@/components/app-sidebar"
import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbLink,
 BreadcrumbList,
 BreadcrumbPage,
 BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
 SidebarInset,
 SidebarProvider,
 SidebarTrigger,
} from "@/components/ui/sidebar"
export default function Page() {
 return (
  <SidebarProvider>
   <AppSidebar />
   <SidebarInset>
    <header className="flex h-16 shrink-0 items-center gap-2 border-b">
     <div className="flex items-center gap-2 px-3">
      <SidebarTrigger />
      <Separator orientation="vertical" className="mr-2 h-4" />
      <Breadcrumb>
       <BreadcrumbList>
        <BreadcrumbItem className="hidden md:block">
         <BreadcrumbLink href="#">
          Building Your Application
         </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator className="hidden md:block" />
        <BreadcrumbItem>
         <BreadcrumbPage>Data Fetching</BreadcrumbPage>
        </BreadcrumbItem>
       </BreadcrumbList>
      </Breadcrumb>
     </div>
    </header>
    <div className="flex flex-1 flex-col gap-4 p-4">
     <div className="grid auto-rows-min gap-4 md:grid-cols-3">
      <div className="aspect-video rounded-xl bg-muted/50" />
      <div className="aspect-video rounded-xl bg-muted/50" />
      <div className="aspect-video rounded-xl bg-muted/50" />
     </div>
     <div className="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A login page with a muted background color.](https://ui.shadcn.com/blocks#login-03)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/login-03 "Open in New Tab")
npx shadcn add login-03
Open in 
![login-03](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-03-light.png&w=3840&q=75)![login-03](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-03-dark.png&w=3840&q=75)
Files
  * app
    * login
      * page.tsx
  * components
    * login-form.tsx


app/login/page.tsx
```
import { GalleryVerticalEnd } from "lucide-react"
import { LoginForm } from "@/components/login-form"
export default function LoginPage() {
 return (
  <div className="flex min-h-svh flex-col items-center justify-center gap-6 bg-muted p-6 md:p-10">
   <div className="flex w-full max-w-sm flex-col gap-6">
    <a href="#" className="flex items-center gap-2 self-center font-medium">
     <div className="flex h-6 w-6 items-center justify-center rounded-md bg-primary text-primary-foreground">
      <GalleryVerticalEnd className="size-4" />
     </div>
     Acme Inc.
    </a>
    <LoginForm />
   </div>
  </div>
 )
}

```

PreviewCode
[A login page with form and image.](https://ui.shadcn.com/blocks#login-04)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/login-04 "Open in New Tab")
npx shadcn add login-04
Open in 
![login-04](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-04-light.png&w=3840&q=75)![login-04](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-04-dark.png&w=3840&q=75)
Files
  * app
    * login
      * page.tsx
  * components
    * login-form.tsx


app/login/page.tsx
```
import { LoginForm } from "@/components/login-form"
export default function LoginPage() {
 return (
  <div className="flex min-h-svh flex-col items-center justify-center bg-muted p-6 md:p-10">
   <div className="w-full max-w-sm md:max-w-3xl">
    <LoginForm />
   </div>
  </div>
 )
}

```

[Browse all blocks](https://ui.shadcn.com/blocks/sidebar)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

