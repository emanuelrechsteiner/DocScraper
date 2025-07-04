---
url: https://ui.shadcn.com/blocks/authentication
scraped_at: 2025-05-24T22:28:44.661652
title: Building Blocks for the Web - shadcn/ui
---

[shadcn/ui](https://ui.shadcn.com/)[Docs](https://ui.shadcn.com/docs/installation)[Components](https://ui.shadcn.com/docs/components)[Blocks](https://ui.shadcn.com/blocks)[Charts](https://ui.shadcn.com/charts)[Themes](https://ui.shadcn.com/themes)[Colors](https://ui.shadcn.com/colors)
Toggle MenuSearch documentation...
Search documentation...Search...`⌘K`
[GitHub](https://github.com/shadcn-ui/ui)Toggle theme
[Tailwind CSSGet Started with Tailwind v4](https://ui.shadcn.com/docs/tailwind-v4)
# Building Blocks for the Web
Clean, modern building blocks. Copy and paste into your apps. Works with all React frameworks. Open Source. Free forever.
[Browse Blocks](https://ui.shadcn.com/blocks/authentication#blocks)[Add a block](https://ui.shadcn.com/docs/blocks)
[Featured](https://ui.shadcn.com/blocks)[Sidebar](https://ui.shadcn.com/blocks/sidebar)[Authentication](https://ui.shadcn.com/blocks/authentication)[Login](https://ui.shadcn.com/blocks/login)
PreviewCode
[A simple login form.](https://ui.shadcn.com/blocks/authentication#login-01)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/login-01 "Open in New Tab")
npx shadcn add login-01
Open in 
![login-01](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-01-light.png&w=3840&q=75)![login-01](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-01-dark.png&w=3840&q=75)
Files
  * app
    * login
      * page.tsx
  * components
    * login-form.tsx


app/login/page.tsx
```
import { LoginForm } from "@/components/login-form"
export default function Page() {
 return (
  <div className="flex min-h-svh w-full items-center justify-center p-6 md:p-10">
   <div className="w-full max-w-sm">
    <LoginForm />
   </div>
  </div>
 )
}

```

PreviewCode
[A two column login page with a cover image.](https://ui.shadcn.com/blocks/authentication#login-02)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/login-02 "Open in New Tab")
npx shadcn add login-02
Open in 
![login-02](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-02-light.png&w=3840&q=75)![login-02](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-02-dark.png&w=3840&q=75)
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
  <div className="grid min-h-svh lg:grid-cols-2">
   <div className="flex flex-col gap-4 p-6 md:p-10">
    <div className="flex justify-center gap-2 md:justify-start">
     <a href="#" className="flex items-center gap-2 font-medium">
      <div className="flex h-6 w-6 items-center justify-center rounded-md bg-primary text-primary-foreground">
       <GalleryVerticalEnd className="size-4" />
      </div>
      Acme Inc.
     </a>
    </div>
    <div className="flex flex-1 items-center justify-center">
     <div className="w-full max-w-xs">
      <LoginForm />
     </div>
    </div>
   </div>
   <div className="relative hidden bg-muted lg:block">
    <img
     src="/placeholder.svg"
     alt="Image"
     className="absolute inset-0 h-full w-full object-cover dark:brightness-[0.2] dark:grayscale"
    />
   </div>
  </div>
 )
}

```

PreviewCode
[A login page with a muted background color.](https://ui.shadcn.com/blocks/authentication#login-03)
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
[A login page with form and image.](https://ui.shadcn.com/blocks/authentication#login-04)
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

PreviewCode
[A simple email-only login page.](https://ui.shadcn.com/blocks/authentication#login-05)
[Open in New Tab](https://ui.shadcn.com/view/styles/new-york/login-05 "Open in New Tab")
npx shadcn add login-05
Open in 
![login-05](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-05-light.png&w=3840&q=75)![login-05](https://ui.shadcn.com/_next/image?url=%2Fr%2Fstyles%2Fnew-york%2Flogin-05-dark.png&w=3840&q=75)
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
  <div className="flex min-h-svh flex-col items-center justify-center gap-6 bg-background p-6 md:p-10">
   <div className="w-full max-w-sm">
    <LoginForm />
   </div>
  </div>
 )
}

```

Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

