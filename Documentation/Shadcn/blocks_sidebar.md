---
url: https://ui.shadcn.com/blocks/sidebar
scraped_at: 2025-05-24T22:29:02.253732
title: Building Blocks for the Web - shadcn/ui
---

[shadcn/ui](https://ui.shadcn.com/)[Docs](https://ui.shadcn.com/docs/installation)[Components](https://ui.shadcn.com/docs/components)[Blocks](https://ui.shadcn.com/blocks)[Charts](https://ui.shadcn.com/charts)[Themes](https://ui.shadcn.com/themes)[Colors](https://ui.shadcn.com/colors)
Toggle MenuSearch documentation...
Search documentation...Search...`⌘K`
[GitHub](https://github.com/shadcn-ui/ui)Toggle theme
[Tailwind CSSGet Started with Tailwind v4](https://ui.shadcn.com/docs/tailwind-v4)
# Building Blocks for the Web
Clean, modern building blocks. Copy and paste into your apps. Works with all React frameworks. Open Source. Free forever.
[Browse Blocks](https://ui.shadcn.com/blocks/sidebar#blocks)[Add a block](https://ui.shadcn.com/docs/blocks)
[Featured](https://ui.shadcn.com/blocks)[Sidebar](https://ui.shadcn.com/blocks/sidebar)[Authentication](https://ui.shadcn.com/blocks/authentication)[Login](https://ui.shadcn.com/blocks/login)
PreviewCode
[A simple sidebar with navigation grouped by section.](https://ui.shadcn.com/blocks/sidebar#sidebar-01)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-01 "Open in New Tab")
npx shadcn add sidebar-01
Open in 
![sidebar-01](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-01-light.png&w=3840&q=75)![sidebar-01](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-01-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * search-form.tsx
    * version-switcher.tsx


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
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
[A sidebar with collapsible sections.](https://ui.shadcn.com/blocks/sidebar#sidebar-02)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-02 "Open in New Tab")
npx shadcn add sidebar-02
Open in 
![sidebar-02](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-02-light.png&w=3840&q=75)![sidebar-02](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-02-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * search-form.tsx
    * version-switcher.tsx


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
    <header className="flex sticky top-0 bg-background h-16 shrink-0 items-center gap-2 border-b px-4">
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
    </header>
    <div className="flex flex-1 flex-col gap-4 p-4">
     {Array.from({ length: 24 }).map((_, index) => (
      <div
       key={index}
       className="aspect-video h-12 w-full rounded-lg bg-muted/50"
      />
     ))}
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar with submenus.](https://ui.shadcn.com/blocks/sidebar#sidebar-03)
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
[A floating sidebar with submenus.](https://ui.shadcn.com/blocks/sidebar#sidebar-04)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-04 "Open in New Tab")
npx shadcn add sidebar-04
Open in 
![sidebar-04](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-04-light.png&w=3840&q=75)![sidebar-04](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-04-dark.png&w=3840&q=75)
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
  <SidebarProvider
   style={
    {
     "--sidebar-width": "19rem",
    } as React.CSSProperties
   }
  >
   <AppSidebar />
   <SidebarInset>
    <header className="flex h-16 shrink-0 items-center gap-2 px-4">
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
[A sidebar with collapsible submenus.](https://ui.shadcn.com/blocks/sidebar#sidebar-05)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-05 "Open in New Tab")
npx shadcn add sidebar-05
Open in 
![sidebar-05](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-05-light.png&w=3840&q=75)![sidebar-05](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-05-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * search-form.tsx


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
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
[A sidebar with submenus as dropdowns.](https://ui.shadcn.com/blocks/sidebar#sidebar-06)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-06 "Open in New Tab")
npx shadcn add sidebar-06
Open in 
![sidebar-06](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-06-light.png&w=3840&q=75)![sidebar-06](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-06-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * nav-main.tsx
    * sidebar-opt-in-form.tsx


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
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
[A sidebar that collapses to icons.](https://ui.shadcn.com/blocks/sidebar#sidebar-07)
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
[An inset sidebar with secondary navigation.](https://ui.shadcn.com/blocks/sidebar#sidebar-08)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-08 "Open in New Tab")
npx shadcn add sidebar-08
Open in 
![sidebar-08](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-08-light.png&w=3840&q=75)![sidebar-08](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-08-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * nav-main.tsx
    * nav-projects.tsx
    * nav-secondary.tsx
    * nav-user.tsx


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
    <header className="flex h-16 shrink-0 items-center gap-2">
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
[Collapsible nested sidebars.](https://ui.shadcn.com/blocks/sidebar#sidebar-09)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-09 "Open in New Tab")
npx shadcn add sidebar-09
Open in 
![sidebar-09](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-09-light.png&w=3840&q=75)![sidebar-09](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-09-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * nav-user.tsx


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
  <SidebarProvider
   style={
    {
     "--sidebar-width": "350px",
    } as React.CSSProperties
   }
  >
   <AppSidebar />
   <SidebarInset>
    <header className="sticky top-0 flex shrink-0 items-center gap-2 border-b bg-background p-4">
     <SidebarTrigger className="-ml-1" />
     <Separator orientation="vertical" className="mr-2 h-4" />
     <Breadcrumb>
      <BreadcrumbList>
       <BreadcrumbItem className="hidden md:block">
        <BreadcrumbLink href="#">All Inboxes</BreadcrumbLink>
       </BreadcrumbItem>
       <BreadcrumbSeparator className="hidden md:block" />
       <BreadcrumbItem>
        <BreadcrumbPage>Inbox</BreadcrumbPage>
       </BreadcrumbItem>
      </BreadcrumbList>
     </Breadcrumb>
    </header>
    <div className="flex flex-1 flex-col gap-4 p-4">
     {Array.from({ length: 24 }).map((_, index) => (
      <div
       key={index}
       className="aspect-video h-12 w-full rounded-lg bg-muted/50"
      />
     ))}
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar in a popover.](https://ui.shadcn.com/blocks/sidebar#sidebar-10)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-10 "Open in New Tab")
npx shadcn add sidebar-10
Open in 
![sidebar-10](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-10-light.png&w=3840&q=75)![sidebar-10](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-10-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * nav-actions.tsx
    * nav-favorites.tsx
    * nav-main.tsx
    * nav-secondary.tsx
    * nav-workspaces.tsx
    * team-switcher.tsx


app/dashboard/page.tsx
```
import { AppSidebar } from "@/components/app-sidebar"
import { NavActions } from "@/components/nav-actions"
import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbList,
 BreadcrumbPage,
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
    <header className="flex h-14 shrink-0 items-center gap-2">
     <div className="flex flex-1 items-center gap-2 px-3">
      <SidebarTrigger />
      <Separator orientation="vertical" className="mr-2 h-4" />
      <Breadcrumb>
       <BreadcrumbList>
        <BreadcrumbItem>
         <BreadcrumbPage className="line-clamp-1">
          Project Management & Task Tracking
         </BreadcrumbPage>
        </BreadcrumbItem>
       </BreadcrumbList>
      </Breadcrumb>
     </div>
     <div className="ml-auto px-3">
      <NavActions />
     </div>
    </header>
    <div className="flex flex-1 flex-col gap-4 px-4 py-10">
     <div className="mx-auto h-24 w-full max-w-3xl rounded-xl bg-muted/50" />
     <div className="mx-auto h-full w-full max-w-3xl rounded-xl bg-muted/50" />
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar with a collapsible file tree.](https://ui.shadcn.com/blocks/sidebar#sidebar-11)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-11 "Open in New Tab")
npx shadcn add sidebar-11
Open in 
![sidebar-11](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-11-light.png&w=3840&q=75)![sidebar-11](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-11-dark.png&w=3840&q=75)
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
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
     <SidebarTrigger className="-ml-1" />
     <Separator orientation="vertical" className="mr-2 h-4" />
     <Breadcrumb>
      <BreadcrumbList>
       <BreadcrumbItem className="hidden md:block">
        <BreadcrumbLink href="#">components</BreadcrumbLink>
       </BreadcrumbItem>
       <BreadcrumbSeparator className="hidden md:block" />
       <BreadcrumbItem className="hidden md:block">
        <BreadcrumbLink href="#">ui</BreadcrumbLink>
       </BreadcrumbItem>
       <BreadcrumbSeparator className="hidden md:block" />
       <BreadcrumbItem>
        <BreadcrumbPage>button.tsx</BreadcrumbPage>
       </BreadcrumbItem>
      </BreadcrumbList>
     </Breadcrumb>
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
[A sidebar with a calendar.](https://ui.shadcn.com/blocks/sidebar#sidebar-12)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-12 "Open in New Tab")
npx shadcn add sidebar-12
Open in 
![sidebar-12](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-12-light.png&w=3840&q=75)![sidebar-12](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-12-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * calendars.tsx
    * date-picker.tsx
    * nav-user.tsx


app/dashboard/page.tsx
```
import { AppSidebar } from "@/components/app-sidebar"
import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbList,
 BreadcrumbPage,
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
    <header className="sticky top-0 flex h-16 shrink-0 items-center gap-2 border-b bg-background px-4">
     <SidebarTrigger className="-ml-1" />
     <Separator orientation="vertical" className="mr-2 h-4" />
     <Breadcrumb>
      <BreadcrumbList>
       <BreadcrumbItem>
        <BreadcrumbPage>October 2024</BreadcrumbPage>
       </BreadcrumbItem>
      </BreadcrumbList>
     </Breadcrumb>
    </header>
    <div className="flex flex-1 flex-col gap-4 p-4">
     <div className="grid auto-rows-min gap-4 md:grid-cols-5">
      {Array.from({ length: 20 }).map((_, i) => (
       <div key={i} className="aspect-square rounded-xl bg-muted/50" />
      ))}
     </div>
    </div>
   </SidebarInset>
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar in a dialog.](https://ui.shadcn.com/blocks/sidebar#sidebar-13)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-13 "Open in New Tab")
npx shadcn add sidebar-13
Open in 
![sidebar-13](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-13-light.png&w=3840&q=75)![sidebar-13](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-13-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * settings-dialog.tsx


app/dashboard/page.tsx
```
import { SettingsDialog } from "@/components/settings-dialog"
export default function Page() {
 return (
  <div className="flex h-svh items-center justify-center">
   <SettingsDialog />
  </div>
 )
}

```

PreviewCode
[A sidebar on the right.](https://ui.shadcn.com/blocks/sidebar#sidebar-14)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-14 "Open in New Tab")
npx shadcn add sidebar-14
Open in 
![sidebar-14](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-14-light.png&w=3840&q=75)![sidebar-14](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-14-dark.png&w=3840&q=75)
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
import {
 SidebarInset,
 SidebarProvider,
 SidebarTrigger,
} from "@/components/ui/sidebar"
export default function Page() {
 return (
  <SidebarProvider>
   <SidebarInset>
    <header className="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
     <SidebarTrigger className="-mr-1 ml-auto rotate-180" />
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
   <AppSidebar side="right" />
  </SidebarProvider>
 )
}

```

PreviewCode
[A left and right sidebar.](https://ui.shadcn.com/blocks/sidebar#sidebar-15)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-15 "Open in New Tab")
npx shadcn add sidebar-15
Open in 
![sidebar-15](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-15-light.png&w=3840&q=75)![sidebar-15](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-15-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * calendars.tsx
    * date-picker.tsx
    * nav-favorites.tsx
    * nav-main.tsx
    * nav-secondary.tsx
    * nav-user.tsx
    * nav-workspaces.tsx
    * sidebar-left.tsx
    * sidebar-right.tsx
    * team-switcher.tsx


app/dashboard/page.tsx
```
import { SidebarLeft } from "@/components/sidebar-left"
import { SidebarRight } from "@/components/sidebar-right"
import {
 Breadcrumb,
 BreadcrumbItem,
 BreadcrumbList,
 BreadcrumbPage,
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
   <SidebarLeft />
   <SidebarInset>
    <header className="sticky top-0 flex h-14 shrink-0 items-center gap-2 bg-background">
     <div className="flex flex-1 items-center gap-2 px-3">
      <SidebarTrigger />
      <Separator orientation="vertical" className="mr-2 h-4" />
      <Breadcrumb>
       <BreadcrumbList>
        <BreadcrumbItem>
         <BreadcrumbPage className="line-clamp-1">
          Project Management & Task Tracking
         </BreadcrumbPage>
        </BreadcrumbItem>
       </BreadcrumbList>
      </Breadcrumb>
     </div>
    </header>
    <div className="flex flex-1 flex-col gap-4 p-4">
     <div className="mx-auto h-24 w-full max-w-3xl rounded-xl bg-muted/50" />
     <div className="mx-auto h-[100vh] w-full max-w-3xl rounded-xl bg-muted/50" />
    </div>
   </SidebarInset>
   <SidebarRight />
  </SidebarProvider>
 )
}

```

PreviewCode
[A sidebar with a sticky site header.](https://ui.shadcn.com/blocks/sidebar#sidebar-16)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/sidebar-16 "Open in New Tab")
npx shadcn add sidebar-16
Open in 
![sidebar-16](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-16-light.png&w=3840&q=75)![sidebar-16](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-16-dark.png&w=3840&q=75)
Files
  * app
    * dashboard
      * page.tsx
  * components
    * app-sidebar.tsx
    * nav-main.tsx
    * nav-projects.tsx
    * nav-secondary.tsx
    * nav-user.tsx
    * search-form.tsx
    * site-header.tsx


app/dashboard/page.tsx
```
import { AppSidebar } from "@/components/app-sidebar"
import { SiteHeader } from "@/components/site-header"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
export default function Page() {
 return (
  <div className="[--header-height:calc(theme(spacing.14))]">
   <SidebarProvider className="flex flex-col">
    <SiteHeader />
    <div className="flex flex-1">
     <AppSidebar />
     <SidebarInset>
      <div className="flex flex-1 flex-col gap-4 p-4">
       <div className="grid auto-rows-min gap-4 md:grid-cols-3">
        <div className="aspect-video rounded-xl bg-muted/50" />
        <div className="aspect-video rounded-xl bg-muted/50" />
        <div className="aspect-video rounded-xl bg-muted/50" />
       </div>
       <div className="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
      </div>
     </SidebarInset>
    </div>
   </SidebarProvider>
  </div>
 )
}

```

Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

