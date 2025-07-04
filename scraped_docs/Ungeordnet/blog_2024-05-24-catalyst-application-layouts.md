---
url: https://tailwindcss.com/blog/2024-05-24-catalyst-application-layouts
scraped_at: 2025-05-25T08:39:49.294458
title: Catalyst: Application layouts, navigation menus, description lists, and more - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
May 24, 2024
# Catalyst: Application layouts, navigation menus, description lists, and more
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
![Catalyst application layout preview](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcatalyst-header.5da8820a.jpg&w=3840&q=75)
We just published the first major update to [Catalyst](https://tailwindui.com/templates/catalyst) since releasing the development preview, with two new application layouts, navbar and sidebar components, description lists, and more.
We're also pumped to share that with the release of [Headless UI v2.0 for React](https://tailwindcss.com/blog/headless-ui-v2), Catalyst is no longer in development preview — **it's officially stable** and you can start using it in production today without worrying about breaking changes in the underlying dependencies.
Check out our brand new [live demo site](https://catalyst-demo.tailwindui.com) to see what a full Catalyst project looks and feels like after these updates for yourself.
## [New application layout components](https://tailwindcss.com/blog/2024-05-24-catalyst-application-layouts#new-application-layout-components)
One of the hardest things about trying to get started on a new project idea is getting past the blank canvas so you can actually start building something.
In this update we've added two new application layout components to make it easy to give your project a shape and structure so you have something you can start building with.
The first layout is a classic [sidebar layout](https://catalyst.tailwindui.com/docs/sidebar-layout), that moves the sidebar into a collapsible mobile menu on smaller screens:
![Sidebar layout example](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsidebar-layout.e72f12e0.jpg&w=3840&q=75)
```
import { SidebarLayout } from "@/components/sidebar-layout";import { Navbar } from "@/components/navbar";import { Sidebar } from "@/components/sidebar";function Example({ children }) { return (  <SidebarLayout   sidebar={<Sidebar>{/* Sidebar menu */}</Sidebar>}   navbar={<Navbar>{/* Navbar for mobile screens */}</Navbar>}  >   {/* Your page content */}  </SidebarLayout> );}
```

The second is a simpler [stacked layout](https://catalyst.tailwindui.com/docs/stacked-layout) with a horizontal navigation menu, which is often a great fit for apps with fewer pages:
![Stacked layout example](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fstacked-layout.ec57a472.jpg&w=3840&q=75)
```
import { StackedLayout } from "@/components/stacked-layout";import { Navbar } from "@/components/navbar";import { Sidebar } from "@/components/sidebar";function Example({ children }) { return (  <StackedLayout   navbar={<Navbar>{/* Top navigation menu */}</Navbar>}   sidebar={<Sidebar>{/* Sidebar content for mobile menu */}</Sidebar>}  >   {/* Your page content */}  </StackedLayout> );}
```

And they both support dark mode too, of course:
![Sidebar layout in dark mode](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flayout-dark-mode.29f2de5c.jpg&w=3840&q=75)
We worked really hard to get the APIs for all of these components right, making it easy to position things where you need them to be, optionally include icons, incorporate dropdown menus, and more.
The final result turned out feeling really simple which is exactly what we were going for, and I think you'll find they are a real delight to build with.
Check out the [Sidebar layout documentation](https://catalyst.tailwindui.com/docs/sidebar-layout) and [Stacked layout documentation](https://catalyst.tailwindui.com/docs/stacked-layout) to get started, then dig into the [Navbar](https://catalyst.tailwindui.com/docs/navbar) and [Sidebar](https://catalyst.tailwindui.com/docs/sidebar) components to learn how to structure all of the navigation items.
## [Description lists](https://tailwindcss.com/blog/2024-05-24-catalyst-application-layouts#description-lists)
When we were working on the application layouts we realized we didn't have any great content to demo them with, so we cooked up a `DescriptionList` component to fill in that big empty space. 

Customer
    Michael Foster

Event
    Bear Hug: Live in Concert

Amount
    $150.00 USD

Amount after exchange rate
    US$150.00 → CA$199.79

Fee
    $4.79 USD

Net
    $1,955.00
```
import { DescriptionDetails, DescriptionList, DescriptionTerm } from "@/components/description-list";function Example() { return (  <DescriptionList>   <DescriptionTerm>Customer</DescriptionTerm>   <DescriptionDetails>Michael Foster</DescriptionDetails>   <DescriptionTerm>Event</DescriptionTerm>   <DescriptionDetails>Bear Hug: Live in Concert</DescriptionDetails>   {/* ... */}  </DescriptionList> );}
```

It's a really simple API that works just like the HTML `<dl>` element, but is nicely styled, responsive, and with dark mode support of course.
Check out the [Description list](https://catalyst.tailwindui.com/docs/description-list) documentation for more details.
## [Page headings](https://tailwindcss.com/blog/2024-05-24-catalyst-application-layouts#page-headings)
More components we needed to make the demo look good! We've added `Heading` and `Subheading` components you can use to quickly and consistently title things in your UI.
# Heading
## [Subheading](https://tailwindcss.com/blog/2024-05-24-catalyst-application-layouts#subheading)
```
import { Heading, Subheading } from "@/components/heading";function Example() { return (  <div>   <Heading>Heading</Heading>   <Subheading>Subheading</Subheading>  </div> );}
```

You can control which HTML heading element is rendered using the `level` prop, and like everything else, they're responsive with built-in dark mode support.
See the [Heading](https://catalyst.tailwindui.com/docs/heading) documentation for more examples.
## [Dividers](https://tailwindcss.com/blog/2024-05-24-catalyst-application-layouts#dividers)
Saved the best for last — Catalyst now includes a gray line you can put in between things.
```
import { Divider } from "@/components/divider";function Example() { return <Divider />;}
```

We worked tirelessly on this one, and are so proud to make this part of your application development process easier.
Check out the [Divider](https://catalyst.tailwindui.com/docs/divider) documentation — it does have one prop at least.
Catalyst is included with your Tailwind UI all-access license at no additional cost, so if you've got a license, log in and [download the latest version](https://tailwindui.com/templates/catalyst) to start building.
Looking forward to seeing what you do with it!
## Get all of our updates directly to your inbox.Sign up for our newsletter.
Subscribe
### Learn
  * [Documentation](https://tailwindcss.com/docs)
  * [Showcase](https://tailwindcss.com/showcase)
  * [Blog](https://tailwindcss.com/blog)
  * [Playground](https://play.tailwindcss.com/)


### Resources
  * [Refactoring UI](https://www.refactoringui.com)
  * [Headless UI](https://headlessui.com)
  * [Heroicons](https://heroicons.com)
  * [Hero Patterns](https://heropatterns.com)


### [Tailwind Plus](https://tailwindcss.com/plus?ref=footer)
  * [UI Blocks](https://tailwindcss.com/plus/ui-blocks?ref=footer)
  * [Templates](https://tailwindcss.com/plus/templates?ref=footer)
  * [UI Kit](https://tailwindcss.com/plus/ui-kit?ref=footer)


### Community
  * [GitHub](https://github.com/tailwindlabs/tailwindcss)
  * [Discord](https://tailwindcss.com/discord)
  * [X](https://x.com/tailwindcss)


### Learn
  * [Documentation](https://tailwindcss.com/docs)
  * [Showcase](https://tailwindcss.com/showcase)
  * [Blog](https://tailwindcss.com/blog)
  * [Playground](https://play.tailwindcss.com/)


### [Tailwind Plus](https://tailwindcss.com/plus?ref=footer)
  * [UI Blocks](https://tailwindcss.com/plus/ui-blocks?ref=footer)
  * [Templates](https://tailwindcss.com/plus/templates?ref=footer)
  * [UI Kit](https://tailwindcss.com/plus/ui-kit?ref=footer)


### Resources
  * [Refactoring UI](https://www.refactoringui.com)
  * [Headless UI](https://headlessui.com)
  * [Heroicons](https://heroicons.com)
  * [Hero Patterns](https://heropatterns.com)


### Community
  * [GitHub](https://github.com/tailwindlabs/tailwindcss)
  * [Discord](https://tailwindcss.com/discord)
  * [X](https://x.com/tailwindcss)


Copyright © 2025 Tailwind Labs Inc.·[Trademark Policy](https://tailwindcss.com/brand)

