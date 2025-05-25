---
url: https://ui.shadcn.com/docs/components/sidebar
scraped_at: 2025-05-24T22:29:06.568405
title: Sidebar - shadcn/ui
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
Sidebar
# Sidebar
A composable, themeable and customizable sidebar component.
![sidebar-07](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-07-light.png&w=3840&q=75)![sidebar-07](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-07-dark.png&w=3840&q=75)
A sidebar that collapses to icons.
Sidebars are one of the most complex components to build. They are central to any application and often contain a lot of moving parts.
I don't like building sidebars. So I built 30+ of them. All kinds of configurations. Then I extracted the core components into `sidebar.tsx`.
We now have a solid foundation to build on top of. Composable. Themeable. Customizable.
[Browse the Blocks Library](https://ui.shadcn.com/blocks).
## [](https://ui.shadcn.com/docs/components/sidebar#installation)Installation
CLIManual
### Run the following command to install `sidebar.tsx`
pnpmnpmyarnbun
```
pnpm dlx shadcn@latest add sidebar

```

Copy
### Add the following colors to your CSS file
The command above should install the colors for you. If not, copy and paste the following in your CSS file.
We'll go over the colors later in the [theming section](https://ui.shadcn.com/docs/components/sidebar#theming).
app/globals.css
```
@layer base {
 :root {
  --sidebar-background: 0 0% 98%;
  --sidebar-foreground: 240 5.3% 26.1%;
  --sidebar-primary: 240 5.9% 10%;
  --sidebar-primary-foreground: 0 0% 98%;
  --sidebar-accent: 240 4.8% 95.9%;
  --sidebar-accent-foreground: 240 5.9% 10%;
  --sidebar-border: 220 13% 91%;
  --sidebar-ring: 217.2 91.2% 59.8%;
 }
 .dark {
  --sidebar-background: 240 5.9% 10%;
  --sidebar-foreground: 240 4.8% 95.9%;
  --sidebar-primary: 224.3 76.3% 48%;
  --sidebar-primary-foreground: 0 0% 100%;
  --sidebar-accent: 240 3.7% 15.9%;
  --sidebar-accent-foreground: 240 4.8% 95.9%;
  --sidebar-border: 240 3.7% 15.9%;
  --sidebar-ring: 217.2 91.2% 59.8%;
 }
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#structure)Structure
A `Sidebar` component is composed of the following parts:
  * `SidebarProvider` - Handles collapsible state.
  * `Sidebar` - The sidebar container.
  * `SidebarHeader` and `SidebarFooter` - Sticky at the top and bottom of the sidebar.
  * `SidebarContent` - Scrollable content.
  * `SidebarGroup` - Section within the `SidebarContent`.
  * `SidebarTrigger` - Trigger for the `Sidebar`.

![Sidebar Structure](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fsidebar-structure.png&w=1920&q=75) ![Sidebar Structure](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fsidebar-structure-dark.png&w=1920&q=75)
## [](https://ui.shadcn.com/docs/components/sidebar#usage)Usage
app/layout.tsx
```
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
export default function Layout({ children }: { children: React.ReactNode }) {
 return (
  <SidebarProvider>
   <AppSidebar />
   <main>
    <SidebarTrigger />
    {children}
   </main>
  </SidebarProvider>
 )
}
```
Copy
components/app-sidebar.tsx
```
import {
 Sidebar,
 SidebarContent,
 SidebarFooter,
 SidebarGroup,
 SidebarHeader,
} from "@/components/ui/sidebar"
export function AppSidebar() {
 return (
  <Sidebar>
   <SidebarHeader />
   <SidebarContent>
    <SidebarGroup />
    <SidebarGroup />
   </SidebarContent>
   <SidebarFooter />
  </Sidebar>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#your-first-sidebar)Your First Sidebar
Let's start with the most basic sidebar. A collapsible sidebar with a menu.
Add a `SidebarProvider` and `SidebarTrigger` at the root of your application.
app/layout.tsx
```
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
export default function Layout({ children }: { children: React.ReactNode }) {
 return (
  <SidebarProvider>
   <AppSidebar />
   <main>
    <SidebarTrigger />
    {children}
   </main>
  </SidebarProvider>
 )
}
```
Copy
### Create a new sidebar component at `components/app-sidebar.tsx`.
components/app-sidebar.tsx
```
import { Sidebar, SidebarContent } from "@/components/ui/sidebar"
export function AppSidebar() {
 return (
  <Sidebar>
   <SidebarContent />
  </Sidebar>
 )
}
```
Copy
### Now, let's add a `SidebarMenu` to the sidebar.
We'll use the `SidebarMenu` component in a `SidebarGroup`.
components/app-sidebar.tsx
```
import { Calendar, Home, Inbox, Search, Settings } from "lucide-react"
import {
 Sidebar,
 SidebarContent,
 SidebarGroup,
 SidebarGroupContent,
 SidebarGroupLabel,
 SidebarMenu,
 SidebarMenuButton,
 SidebarMenuItem,
} from "@/components/ui/sidebar"
// Menu items.
const items = [
 {
  title: "Home",
  url: "#",
  icon: Home,
 },
 {
  title: "Inbox",
  url: "#",
  icon: Inbox,
 },
 {
  title: "Calendar",
  url: "#",
  icon: Calendar,
 },
 {
  title: "Search",
  url: "#",
  icon: Search,
 },
 {
  title: "Settings",
  url: "#",
  icon: Settings,
 },
]
export function AppSidebar() {
 return (
  <Sidebar>
   <SidebarContent>
    <SidebarGroup>
     <SidebarGroupLabel>Application</SidebarGroupLabel>
     <SidebarGroupContent>
      <SidebarMenu>
       {items.map((item) => (
        <SidebarMenuItem key={item.title}>
         <SidebarMenuButton asChild>
          <a href={item.url}>
           <item.icon />
           <span>{item.title}</span>
          </a>
         </SidebarMenuButton>
        </SidebarMenuItem>
       ))}
      </SidebarMenu>
     </SidebarGroupContent>
    </SidebarGroup>
   </SidebarContent>
  </Sidebar>
 )
}
```
Copy
### You've created your first sidebar.
![sidebar-demo](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-demo-light.png&w=3840&q=75)![sidebar-demo](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-demo-dark.png&w=3840&q=75)
Your first sidebar.
## [](https://ui.shadcn.com/docs/components/sidebar#components)Components
The components in `sidebar.tsx` are built to be composable i.e you build your sidebar by putting the provided components together. They also compose well with other shadcn/ui components such as `DropdownMenu`, `Collapsible` or `Dialog` etc.
**If you need to change the code in`sidebar.tsx` , you are encouraged to do so. The code is yours. Use `sidebar.tsx` as a starting point and build your own.**
In the next sections, we'll go over each component and how to use them.
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarprovider)SidebarProvider
The `SidebarProvider` component is used to provide the sidebar context to the `Sidebar` component. You should always wrap your application in a `SidebarProvider` component.
### [](https://ui.shadcn.com/docs/components/sidebar#props)Props
Name| Type| Description  
---|---|---  
`defaultOpen`| `boolean`| Default open state of the sidebar.  
`open`| `boolean`| Open state of the sidebar (controlled).  
`onOpenChange`| `(open: boolean) => void`| Sets open state of the sidebar (controlled).  
### [](https://ui.shadcn.com/docs/components/sidebar#width)Width
If you have a single sidebar in your application, you can use the `SIDEBAR_WIDTH` and `SIDEBAR_WIDTH_MOBILE` variables in `sidebar.tsx` to set the width of the sidebar.
components/ui/sidebar.tsx
```
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
```
Copy
For multiple sidebars in your application, you can use the `style` prop to set the width of the sidebar.
To set the width of the sidebar, you can use the `--sidebar-width` and `--sidebar-width-mobile` CSS variables in the `style` prop.
components/ui/sidebar.tsx
```
<SidebarProvider
 style={{
  "--sidebar-width": "20rem",
  "--sidebar-width-mobile": "20rem",
 }}
>
 <Sidebar />
</SidebarProvider>
```
Copy
This will handle the width of the sidebar but also the layout spacing.
### [](https://ui.shadcn.com/docs/components/sidebar#keyboard-shortcut)Keyboard Shortcut
The `SIDEBAR_KEYBOARD_SHORTCUT` variable is used to set the keyboard shortcut used to open and close the sidebar.
To trigger the sidebar, you use the `cmd+b` keyboard shortcut on Mac and `ctrl+b` on Windows.
You can change the keyboard shortcut by updating the `SIDEBAR_KEYBOARD_SHORTCUT` variable.
components/ui/sidebar.tsx
```
const SIDEBAR_KEYBOARD_SHORTCUT = "b"
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#persisted-state)Persisted State
The `SidebarProvider` supports persisting the sidebar state across page reloads and server-side rendering. It uses cookies to store the current state of the sidebar. When the sidebar state changes, a default cookie named `sidebar_state` is set with the current open/closed state. This cookie is then read on subsequent page loads to restore the sidebar state.
To persist sidebar state in Next.js, set up your `SidebarProvider` in `app/layout.tsx` like this:
app/layout.tsx
```
import { cookies } from "next/headers"
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
export async function Layout({ children }: { children: React.ReactNode }) {
 const cookieStore = await cookies()
 const defaultOpen = cookieStore.get("sidebar_state")?.value === "true"
 return (
  <SidebarProvider defaultOpen={defaultOpen}>
   <AppSidebar />
   <main>
    <SidebarTrigger />
    {children}
   </main>
  </SidebarProvider>
 )
}
```
Copy
You can change the name of the cookie by updating the `SIDEBAR_COOKIE_NAME` variable in `sidebar.tsx`.
components/ui/sidebar.tsx
```
const SIDEBAR_COOKIE_NAME = "sidebar_state"
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebar)Sidebar
The main `Sidebar` component used to render a collapsible sidebar.
```
import { Sidebar } from "@/components/ui/sidebar"
export function AppSidebar() {
 return <Sidebar />
}
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#props-1)Props
Property| Type| Description  
---|---|---  
`side`| `left` or `right`| The side of the sidebar.  
`variant`| `sidebar`, `floating`, or `inset`| The variant of the sidebar.  
`collapsible`| `offcanvas`, `icon`, or `none`| Collapsible state of the sidebar.  
### [](https://ui.shadcn.com/docs/components/sidebar#side)side
Use the `side` prop to change the side of the sidebar.
Available options are `left` and `right`.
```
import { Sidebar } from "@/components/ui/sidebar"
export function AppSidebar() {
 return <Sidebar side="left | right" />
}
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#variant)variant
Use the `variant` prop to change the variant of the sidebar.
Available options are `sidebar`, `floating` and `inset`.
```
import { Sidebar } from "@/components/ui/sidebar"
export function AppSidebar() {
 return <Sidebar variant="sidebar | floating | inset" />
}
```
Copy
**Note:** If you use the `inset` variant, remember to wrap your main content in a `SidebarInset` component.
```
<SidebarProvider>
 <Sidebar variant="inset" />
 <SidebarInset>
  <main>{children}</main>
 </SidebarInset>
</SidebarProvider>
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#collapsible)collapsible
Use the `collapsible` prop to make the sidebar collapsible.
Available options are `offcanvas`, `icon` and `none`.
```
import { Sidebar } from "@/components/ui/sidebar"
export function AppSidebar() {
 return <Sidebar collapsible="offcanvas | icon | none" />
}
```
Copy
Prop| Description  
---|---  
`offcanvas`| A collapsible sidebar that slides in from the left or right.  
`icon`| A sidebar that collapses to icons.  
`none`| A non-collapsible sidebar.  
## [](https://ui.shadcn.com/docs/components/sidebar#usesidebar)useSidebar
The `useSidebar` hook is used to control the sidebar.
```
import { useSidebar } from "@/components/ui/sidebar"
export function AppSidebar() {
 const {
  state,
  open,
  setOpen,
  openMobile,
  setOpenMobile,
  isMobile,
  toggleSidebar,
 } = useSidebar()
}
```
Copy
Property| Type| Description  
---|---|---  
`state`| `expanded` or `collapsed`| The current state of the sidebar.  
`open`| `boolean`| Whether the sidebar is open.  
`setOpen`| `(open: boolean) => void`| Sets the open state of the sidebar.  
`openMobile`| `boolean`| Whether the sidebar is open on mobile.  
`setOpenMobile`| `(open: boolean) => void`| Sets the open state of the sidebar on mobile.  
`isMobile`| `boolean`| Whether the sidebar is on mobile.  
`toggleSidebar`| `() => void`| Toggles the sidebar. Desktop and mobile.  
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarheader)SidebarHeader
Use the `SidebarHeader` component to add a sticky header to the sidebar.
The following example adds a `<DropdownMenu>` to the `SidebarHeader`.
![sidebar-header](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-header-light.png&w=3840&q=75)![sidebar-header](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-header-dark.png&w=3840&q=75)
A sidebar header with a dropdown menu.
components/app-sidebar.tsx
```
<Sidebar>
 <SidebarHeader>
  <SidebarMenu>
   <SidebarMenuItem>
    <DropdownMenu>
     <DropdownMenuTrigger asChild>
      <SidebarMenuButton>
       Select Workspace
       <ChevronDown className="ml-auto" />
      </SidebarMenuButton>
     </DropdownMenuTrigger>
     <DropdownMenuContent className="w-[--radix-popper-anchor-width]">
      <DropdownMenuItem>
       <span>Acme Inc</span>
      </DropdownMenuItem>
      <DropdownMenuItem>
       <span>Acme Corp.</span>
      </DropdownMenuItem>
     </DropdownMenuContent>
    </DropdownMenu>
   </SidebarMenuItem>
  </SidebarMenu>
 </SidebarHeader>
</Sidebar>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarfooter)SidebarFooter
Use the `SidebarFooter` component to add a sticky footer to the sidebar.
The following example adds a `<DropdownMenu>` to the `SidebarFooter`.
![sidebar-footer](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-footer-light.png&w=3840&q=75)![sidebar-footer](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-footer-dark.png&w=3840&q=75)
A sidebar footer with a dropdown menu.
components/app-sidebar.tsx
```
export function AppSidebar() {
 return (
  <SidebarProvider>
   <Sidebar>
    <SidebarHeader />
    <SidebarContent />
    <SidebarFooter>
     <SidebarMenu>
      <SidebarMenuItem>
       <DropdownMenu>
        <DropdownMenuTrigger asChild>
         <SidebarMenuButton>
          <User2 /> Username
          <ChevronUp className="ml-auto" />
         </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent
         side="top"
         className="w-[--radix-popper-anchor-width]"
        >
         <DropdownMenuItem>
          <span>Account</span>
         </DropdownMenuItem>
         <DropdownMenuItem>
          <span>Billing</span>
         </DropdownMenuItem>
         <DropdownMenuItem>
          <span>Sign out</span>
         </DropdownMenuItem>
        </DropdownMenuContent>
       </DropdownMenu>
      </SidebarMenuItem>
     </SidebarMenu>
    </SidebarFooter>
   </Sidebar>
  </SidebarProvider>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarcontent)SidebarContent
The `SidebarContent` component is used to wrap the content of the sidebar. This is where you add your `SidebarGroup` components. It is scrollable.
```
import { Sidebar, SidebarContent } from "@/components/ui/sidebar"
export function AppSidebar() {
 return (
  <Sidebar>
   <SidebarContent>
    <SidebarGroup />
    <SidebarGroup />
   </SidebarContent>
  </Sidebar>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebargroup)SidebarGroup
Use the `SidebarGroup` component to create a section within the sidebar.
A `SidebarGroup` has a `SidebarGroupLabel`, a `SidebarGroupContent` and an optional `SidebarGroupAction`.
![sidebar-group](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-group-light.png&w=3840&q=75)![sidebar-group](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-group-dark.png&w=3840&q=75)
A sidebar group.
```
import { Sidebar, SidebarContent, SidebarGroup } from "@/components/ui/sidebar"
export function AppSidebar() {
 return (
  <Sidebar>
   <SidebarContent>
    <SidebarGroup>
     <SidebarGroupLabel>Application</SidebarGroupLabel>
     <SidebarGroupAction>
      <Plus /> <span className="sr-only">Add Project</span>
     </SidebarGroupAction>
     <SidebarGroupContent></SidebarGroupContent>
    </SidebarGroup>
   </SidebarContent>
  </Sidebar>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#collapsible-sidebargroup)Collapsible SidebarGroup
To make a `SidebarGroup` collapsible, wrap it in a `Collapsible`.
![sidebar-group-collapsible](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-group-collapsible-light.png&w=3840&q=75)![sidebar-group-collapsible](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-group-collapsible-dark.png&w=3840&q=75)
A collapsible sidebar group.
```
export function AppSidebar() {
 return (
  <Collapsible defaultOpen className="group/collapsible">
   <SidebarGroup>
    <SidebarGroupLabel asChild>
     <CollapsibleTrigger>
      Help
      <ChevronDown className="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180" />
     </CollapsibleTrigger>
    </SidebarGroupLabel>
    <CollapsibleContent>
     <SidebarGroupContent />
    </CollapsibleContent>
   </SidebarGroup>
  </Collapsible>
 )
}
```
Copy
**Note:** We wrap the `CollapsibleTrigger` in a `SidebarGroupLabel` to render a button.
## [](https://ui.shadcn.com/docs/components/sidebar#sidebargroupaction)SidebarGroupAction
Use the `SidebarGroupAction` component to add an action button to the `SidebarGroup`.
```
export function AppSidebar() {
 return (
  <SidebarGroup>
   <SidebarGroupLabel asChild>Projects</SidebarGroupLabel>
   <SidebarGroupAction title="Add Project">
    <Plus /> <span className="sr-only">Add Project</span>
   </SidebarGroupAction>
   <SidebarGroupContent />
  </SidebarGroup>
 )
}
```
Copy
![sidebar-group-action](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-group-action-light.png&w=3840&q=75)![sidebar-group-action](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-group-action-dark.png&w=3840&q=75)
A sidebar group with an action button.
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarmenu)SidebarMenu
The `SidebarMenu` component is used for building a menu within a `SidebarGroup`.
A `SidebarMenu` component is composed of `SidebarMenuItem`, `SidebarMenuButton`, `<SidebarMenuAction />` and `<SidebarMenuSub />` components.
![Sidebar Menu](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fsidebar-menu.png&w=1920&q=75) ![Sidebar Menu](https://ui.shadcn.com/_next/image?url=%2Fimages%2Fsidebar-menu-dark.png&w=1920&q=75)
Here's an example of a `SidebarMenu` component rendering a list of projects.
![sidebar-menu](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-light.png&w=3840&q=75)![sidebar-menu](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-dark.png&w=3840&q=75)
A sidebar menu with a list of projects.
```
<Sidebar>
 <SidebarContent>
  <SidebarGroup>
   <SidebarGroupLabel>Projects</SidebarGroupLabel>
   <SidebarGroupContent>
    <SidebarMenu>
     {projects.map((project) => (
      <SidebarMenuItem key={project.name}>
       <SidebarMenuButton asChild>
        <a href={project.url}>
         <project.icon />
         <span>{project.name}</span>
        </a>
       </SidebarMenuButton>
      </SidebarMenuItem>
     ))}
    </SidebarMenu>
   </SidebarGroupContent>
  </SidebarGroup>
 </SidebarContent>
</Sidebar>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarmenubutton)SidebarMenuButton
The `SidebarMenuButton` component is used to render a menu button within a `SidebarMenuItem`.
### [](https://ui.shadcn.com/docs/components/sidebar#link-or-anchor)Link or Anchor
By default, the `SidebarMenuButton` renders a button but you can use the `asChild` prop to render a different component such as a `Link` or an `a` tag.
```
<SidebarMenuButton asChild>
 <a href="#">Home</a>
</SidebarMenuButton>
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#icon-and-label)Icon and Label
You can render an icon and a truncated label inside the button. Remember to wrap the label in a `<span>`.
```
<SidebarMenuButton asChild>
 <a href="#">
  <Home />
  <span>Home</span>
 </a>
</SidebarMenuButton>
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#isactive)isActive
Use the `isActive` prop to mark a menu item as active.
```
<SidebarMenuButton asChild isActive>
 <a href="#">Home</a>
</SidebarMenuButton>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarmenuaction)SidebarMenuAction
The `SidebarMenuAction` component is used to render a menu action within a `SidebarMenuItem`.
This button works independently of the `SidebarMenuButton` i.e you can have the `<SidebarMenuButton />` as a clickable link and the `<SidebarMenuAction />` as a button.
```
<SidebarMenuItem>
 <SidebarMenuButton asChild>
  <a href="#">
   <Home />
   <span>Home</span>
  </a>
 </SidebarMenuButton>
 <SidebarMenuAction>
  <Plus /> <span className="sr-only">Add Project</span>
 </SidebarMenuAction>
</SidebarMenuItem>
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#dropdownmenu)DropdownMenu
Here's an example of a `SidebarMenuAction` component rendering a `DropdownMenu`.
![sidebar-menu-action](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-action-light.png&w=3840&q=75)![sidebar-menu-action](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-action-dark.png&w=3840&q=75)
A sidebar menu action with a dropdown menu.
```
<SidebarMenuItem>
 <SidebarMenuButton asChild>
  <a href="#">
   <Home />
   <span>Home</span>
  </a>
 </SidebarMenuButton>
 <DropdownMenu>
  <DropdownMenuTrigger asChild>
   <SidebarMenuAction>
    <MoreHorizontal />
   </SidebarMenuAction>
  </DropdownMenuTrigger>
  <DropdownMenuContent side="right" align="start">
   <DropdownMenuItem>
    <span>Edit Project</span>
   </DropdownMenuItem>
   <DropdownMenuItem>
    <span>Delete Project</span>
   </DropdownMenuItem>
  </DropdownMenuContent>
 </DropdownMenu>
</SidebarMenuItem>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarmenusub)SidebarMenuSub
The `SidebarMenuSub` component is used to render a submenu within a `SidebarMenu`.
Use `<SidebarMenuSubItem />` and `<SidebarMenuSubButton />` to render a submenu item.
![sidebar-menu-sub](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-sub-light.png&w=3840&q=75)![sidebar-menu-sub](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-sub-dark.png&w=3840&q=75)
A sidebar menu with a submenu.
```
<SidebarMenuItem>
 <SidebarMenuButton />
 <SidebarMenuSub>
  <SidebarMenuSubItem>
   <SidebarMenuSubButton />
  </SidebarMenuSubItem>
  <SidebarMenuSubItem>
   <SidebarMenuSubButton />
  </SidebarMenuSubItem>
 </SidebarMenuSub>
</SidebarMenuItem>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#collapsible-sidebarmenu)Collapsible SidebarMenu
To make a `SidebarMenu` component collapsible, wrap it and the `SidebarMenuSub` components in a `Collapsible`.
![sidebar-menu-collapsible](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-collapsible-light.png&w=3840&q=75)![sidebar-menu-collapsible](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-collapsible-dark.png&w=3840&q=75)
A collapsible sidebar menu.
```
<SidebarMenu>
 <Collapsible defaultOpen className="group/collapsible">
  <SidebarMenuItem>
   <CollapsibleTrigger asChild>
    <SidebarMenuButton />
   </CollapsibleTrigger>
   <CollapsibleContent>
    <SidebarMenuSub>
     <SidebarMenuSubItem />
    </SidebarMenuSub>
   </CollapsibleContent>
  </SidebarMenuItem>
 </Collapsible>
</SidebarMenu>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarmenubadge)SidebarMenuBadge
The `SidebarMenuBadge` component is used to render a badge within a `SidebarMenuItem`.
![sidebar-menu-badge](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-badge-light.png&w=3840&q=75)![sidebar-menu-badge](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-menu-badge-dark.png&w=3840&q=75)
A sidebar menu with a badge.
```
<SidebarMenuItem>
 <SidebarMenuButton />
 <SidebarMenuBadge>24</SidebarMenuBadge>
</SidebarMenuItem>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarmenuskeleton)SidebarMenuSkeleton
The `SidebarMenuSkeleton` component is used to render a skeleton for a `SidebarMenu`. You can use this to show a loading state when using React Server Components, SWR or react-query.
```
function NavProjectsSkeleton() {
 return (
  <SidebarMenu>
   {Array.from({ length: 5 }).map((_, index) => (
    <SidebarMenuItem key={index}>
     <SidebarMenuSkeleton />
    </SidebarMenuItem>
   ))}
  </SidebarMenu>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarseparator)SidebarSeparator
The `SidebarSeparator` component is used to render a separator within a `Sidebar`.
```
<Sidebar>
 <SidebarHeader />
 <SidebarSeparator />
 <SidebarContent>
  <SidebarGroup />
  <SidebarSeparator />
  <SidebarGroup />
 </SidebarContent>
</Sidebar>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebartrigger)SidebarTrigger
Use the `SidebarTrigger` component to render a button that toggles the sidebar.
The `SidebarTrigger` component must be used within a `SidebarProvider`.
```
<SidebarProvider>
 <Sidebar />
 <main>
  <SidebarTrigger />
 </main>
</SidebarProvider>
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#custom-trigger)Custom Trigger
To create a custom trigger, you can use the `useSidebar` hook.
```
import { useSidebar } from "@/components/ui/sidebar"
export function CustomTrigger() {
 const { toggleSidebar } = useSidebar()
 return <button onClick={toggleSidebar}>Toggle Sidebar</button>
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#sidebarrail)SidebarRail
The `SidebarRail` component is used to render a rail within a `Sidebar`. This rail can be used to toggle the sidebar.
```
<Sidebar>
 <SidebarHeader />
 <SidebarContent>
  <SidebarGroup />
 </SidebarContent>
 <SidebarFooter />
 <SidebarRail />
</Sidebar>
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#data-fetching)Data Fetching
### [](https://ui.shadcn.com/docs/components/sidebar#react-server-components)React Server Components
Here's an example of a `SidebarMenu` component rendering a list of projects using React Server Components.
![sidebar-rsc](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-rsc-light.png&w=3840&q=75)![sidebar-rsc](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-rsc-dark.png&w=3840&q=75)
A sidebar menu using React Server Components.
Skeleton to show loading state.
```
function NavProjectsSkeleton() {
 return (
  <SidebarMenu>
   {Array.from({ length: 5 }).map((_, index) => (
    <SidebarMenuItem key={index}>
     <SidebarMenuSkeleton showIcon />
    </SidebarMenuItem>
   ))}
  </SidebarMenu>
 )
}
```
Copy
Server component fetching data.
```
async function NavProjects() {
 const projects = await fetchProjects()
 return (
  <SidebarMenu>
   {projects.map((project) => (
    <SidebarMenuItem key={project.name}>
     <SidebarMenuButton asChild>
      <a href={project.url}>
       <project.icon />
       <span>{project.name}</span>
      </a>
     </SidebarMenuButton>
    </SidebarMenuItem>
   ))}
  </SidebarMenu>
 )
}
```
Copy
Usage with React Suspense.
```
function AppSidebar() {
 return (
  <Sidebar>
   <SidebarContent>
    <SidebarGroup>
     <SidebarGroupLabel>Projects</SidebarGroupLabel>
     <SidebarGroupContent>
      <React.Suspense fallback={<NavProjectsSkeleton />}>
       <NavProjects />
      </React.Suspense>
     </SidebarGroupContent>
    </SidebarGroup>
   </SidebarContent>
  </Sidebar>
 )
}
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#swr-and-react-query)SWR and React Query
You can use the same approach with [SWR](https://swr.vercel.app/) or [react-query](https://tanstack.com/query/latest/docs/framework/react/overview).
SWR
```
function NavProjects() {
 const { data, isLoading } = useSWR("/api/projects", fetcher)
 if (isLoading) {
  return (
   <SidebarMenu>
    {Array.from({ length: 5 }).map((_, index) => (
     <SidebarMenuItem key={index}>
      <SidebarMenuSkeleton showIcon />
     </SidebarMenuItem>
    ))}
   </SidebarMenu>
  )
 }
 if (!data) {
  return ...
 }
 return (
  <SidebarMenu>
   {data.map((project) => (
    <SidebarMenuItem key={project.name}>
     <SidebarMenuButton asChild>
      <a href={project.url}>
       <project.icon />
       <span>{project.name}</span>
      </a>
     </SidebarMenuButton>
    </SidebarMenuItem>
   ))}
  </SidebarMenu>
 )
}
```
Copy
React Query
```
function NavProjects() {
 const { data, isLoading } = useQuery()
 if (isLoading) {
  return (
   <SidebarMenu>
    {Array.from({ length: 5 }).map((_, index) => (
     <SidebarMenuItem key={index}>
      <SidebarMenuSkeleton showIcon />
     </SidebarMenuItem>
    ))}
   </SidebarMenu>
  )
 }
 if (!data) {
  return ...
 }
 return (
  <SidebarMenu>
   {data.map((project) => (
    <SidebarMenuItem key={project.name}>
     <SidebarMenuButton asChild>
      <a href={project.url}>
       <project.icon />
       <span>{project.name}</span>
      </a>
     </SidebarMenuButton>
    </SidebarMenuItem>
   ))}
  </SidebarMenu>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#controlled-sidebar)Controlled Sidebar
Use the `open` and `onOpenChange` props to control the sidebar.
![sidebar-controlled](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-controlled-light.png&w=3840&q=75)![sidebar-controlled](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Fsidebar-controlled-dark.png&w=3840&q=75)
A controlled sidebar.
```
export function AppSidebar() {
 const [open, setOpen] = React.useState(false)
 return (
  <SidebarProvider open={open} onOpenChange={setOpen}>
   <Sidebar />
  </SidebarProvider>
 )
}
```
Copy
## [](https://ui.shadcn.com/docs/components/sidebar#theming)Theming
We use the following CSS variables to theme the sidebar.
```
@layer base {
 :root {
  --sidebar-background: 0 0% 98%;
  --sidebar-foreground: 240 5.3% 26.1%;
  --sidebar-primary: 240 5.9% 10%;
  --sidebar-primary-foreground: 0 0% 98%;
  --sidebar-accent: 240 4.8% 95.9%;
  --sidebar-accent-foreground: 240 5.9% 10%;
  --sidebar-border: 220 13% 91%;
  --sidebar-ring: 217.2 91.2% 59.8%;
 }
 .dark {
  --sidebar-background: 240 5.9% 10%;
  --sidebar-foreground: 240 4.8% 95.9%;
  --sidebar-primary: 0 0% 98%;
  --sidebar-primary-foreground: 240 5.9% 10%;
  --sidebar-accent: 240 3.7% 15.9%;
  --sidebar-accent-foreground: 240 4.8% 95.9%;
  --sidebar-border: 240 3.7% 15.9%;
  --sidebar-ring: 217.2 91.2% 59.8%;
 }
}
```
Copy
**We intentionally use different variables for the sidebar and the rest of the application** to make it easy to have a sidebar that is styled differently from the rest of the application. Think a sidebar with a darker shade from the main application.
## [](https://ui.shadcn.com/docs/components/sidebar#styling)Styling
Here are some tips for styling the sidebar based on different states.
  * **Styling an element based on the sidebar collapsible state.** The following will hide the `SidebarGroup` when the sidebar is in `icon` mode.


```
<Sidebar collapsible="icon">
 <SidebarContent>
  <SidebarGroup className="group-data-[collapsible=icon]:hidden" />
 </SidebarContent>
</Sidebar>
```
Copy
  * **Styling a menu action based on the menu button active state.** The following will force the menu action to be visible when the menu button is active.


```
<SidebarMenuItem>
 <SidebarMenuButton />
 <SidebarMenuAction className="peer-data-[active=true]/menu-button:opacity-100" />
</SidebarMenuItem>
```
Copy
You can find more tips on using states for styling in this [Twitter thread](https://x.com/shadcn/status/1842329158879420864).
## [](https://ui.shadcn.com/docs/components/sidebar#changelog)Changelog
### [](https://ui.shadcn.com/docs/components/sidebar#2024-10-30-cookie-handling-in-setopen)2024-10-30 Cookie handling in setOpen
  * [#5593](https://github.com/shadcn-ui/ui/pull/5593) - Improved setOpen callback logic in `<SidebarProvider>`.


Update the `setOpen` callback in `<SidebarProvider>` as follows:
```
const setOpen = React.useCallback(
 (value: boolean | ((value: boolean) => boolean)) => {
  const openState = typeof value === "function" ? value(open) : value
  if (setOpenProp) {
   setOpenProp(openState)
  } else {
   _setOpen(openState)
  }
  // This sets the cookie to keep the sidebar state.
  document.cookie = `${SIDEBAR_COOKIE_NAME}=${openState}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`
 },
 [setOpenProp, open]
)
```
Copy
### [](https://ui.shadcn.com/docs/components/sidebar#2024-10-21-fixed-text-sidebar-foreground)2024-10-21 Fixed `text-sidebar-foreground`
  * [#5491](https://github.com/shadcn-ui/ui/pull/5491) - Moved `text-sidebar-foreground` from `<SidebarProvider>` to `<Sidebar>` component.


### [](https://ui.shadcn.com/docs/components/sidebar#2024-10-20-typo-in-usesidebar-hook)2024-10-20 Typo in `useSidebar` hook.
Fixed typo in `useSidebar` hook.
sidebar.tsx
```
- throw new Error("useSidebar must be used within a Sidebar.")
+ throw new Error("useSidebar must be used within a SidebarProvider.")
```
Copy
[Sheet](https://ui.shadcn.com/docs/components/sheet)[Skeleton](https://ui.shadcn.com/docs/components/skeleton)
On This Page
  * [Installation](https://ui.shadcn.com/docs/components/sidebar#installation)
  * [Structure](https://ui.shadcn.com/docs/components/sidebar#structure)
  * [Usage](https://ui.shadcn.com/docs/components/sidebar#usage)
  * [Your First Sidebar](https://ui.shadcn.com/docs/components/sidebar#your-first-sidebar)
  * [Components](https://ui.shadcn.com/docs/components/sidebar#components)
  * [SidebarProvider](https://ui.shadcn.com/docs/components/sidebar#sidebarprovider)
    * [Props](https://ui.shadcn.com/docs/components/sidebar#props)
    * [Width](https://ui.shadcn.com/docs/components/sidebar#width)
    * [Keyboard Shortcut](https://ui.shadcn.com/docs/components/sidebar#keyboard-shortcut)
    * [Persisted State](https://ui.shadcn.com/docs/components/sidebar#persisted-state)
  * [Sidebar](https://ui.shadcn.com/docs/components/sidebar#sidebar)
    * [Props](https://ui.shadcn.com/docs/components/sidebar#props-1)
    * [side](https://ui.shadcn.com/docs/components/sidebar#side)
    * [variant](https://ui.shadcn.com/docs/components/sidebar#variant)
    * [collapsible](https://ui.shadcn.com/docs/components/sidebar#collapsible)
  * [useSidebar](https://ui.shadcn.com/docs/components/sidebar#usesidebar)
  * [SidebarHeader](https://ui.shadcn.com/docs/components/sidebar#sidebarheader)
  * [SidebarFooter](https://ui.shadcn.com/docs/components/sidebar#sidebarfooter)
  * [SidebarContent](https://ui.shadcn.com/docs/components/sidebar#sidebarcontent)
  * [SidebarGroup](https://ui.shadcn.com/docs/components/sidebar#sidebargroup)
  * [Collapsible SidebarGroup](https://ui.shadcn.com/docs/components/sidebar#collapsible-sidebargroup)
  * [SidebarGroupAction](https://ui.shadcn.com/docs/components/sidebar#sidebargroupaction)
  * [SidebarMenu](https://ui.shadcn.com/docs/components/sidebar#sidebarmenu)
  * [SidebarMenuButton](https://ui.shadcn.com/docs/components/sidebar#sidebarmenubutton)
    * [Link or Anchor](https://ui.shadcn.com/docs/components/sidebar#link-or-anchor)
    * [Icon and Label](https://ui.shadcn.com/docs/components/sidebar#icon-and-label)
    * [isActive](https://ui.shadcn.com/docs/components/sidebar#isactive)
  * [SidebarMenuAction](https://ui.shadcn.com/docs/components/sidebar#sidebarmenuaction)
    * [DropdownMenu](https://ui.shadcn.com/docs/components/sidebar#dropdownmenu)
  * [SidebarMenuSub](https://ui.shadcn.com/docs/components/sidebar#sidebarmenusub)
  * [Collapsible SidebarMenu](https://ui.shadcn.com/docs/components/sidebar#collapsible-sidebarmenu)
  * [SidebarMenuBadge](https://ui.shadcn.com/docs/components/sidebar#sidebarmenubadge)
  * [SidebarMenuSkeleton](https://ui.shadcn.com/docs/components/sidebar#sidebarmenuskeleton)
  * [SidebarSeparator](https://ui.shadcn.com/docs/components/sidebar#sidebarseparator)
  * [SidebarTrigger](https://ui.shadcn.com/docs/components/sidebar#sidebartrigger)
    * [Custom Trigger](https://ui.shadcn.com/docs/components/sidebar#custom-trigger)
  * [SidebarRail](https://ui.shadcn.com/docs/components/sidebar#sidebarrail)
  * [Data Fetching](https://ui.shadcn.com/docs/components/sidebar#data-fetching)
    * [React Server Components](https://ui.shadcn.com/docs/components/sidebar#react-server-components)
    * [SWR and React Query](https://ui.shadcn.com/docs/components/sidebar#swr-and-react-query)
  * [Controlled Sidebar](https://ui.shadcn.com/docs/components/sidebar#controlled-sidebar)
  * [Theming](https://ui.shadcn.com/docs/components/sidebar#theming)
  * [Styling](https://ui.shadcn.com/docs/components/sidebar#styling)
  * [Changelog](https://ui.shadcn.com/docs/components/sidebar#changelog)
    * [2024-10-30 Cookie handling in setOpen](https://ui.shadcn.com/docs/components/sidebar#2024-10-30-cookie-handling-in-setopen)
    * [2024-10-21 Fixed text-sidebar-foreground](https://ui.shadcn.com/docs/components/sidebar#2024-10-21-fixed-text-sidebar-foreground)
    * [2024-10-20 Typo in useSidebar hook.](https://ui.shadcn.com/docs/components/sidebar#2024-10-20-typo-in-usesidebar-hook)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

