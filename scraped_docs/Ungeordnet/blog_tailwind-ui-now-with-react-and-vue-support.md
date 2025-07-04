---
url: https://tailwindcss.com/blog/tailwind-ui-now-with-react-and-vue-support
scraped_at: 2025-05-25T08:38:20.932589
title: Tailwind UI: Now with React + Vue support - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
April 14, 2021
# Tailwind UI: Now with React + Vue support
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
[![Tailwind UI: Now for React and Vue](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcard.9e9b9cc2.jpg&w=3840&q=75)](https://tailwindui.com)
Last year we released [Tailwind UI](https://tailwindui.com) — a huge directory of professionally designed UI examples built with Tailwind CSS. Up until now, all of the examples in Tailwind UI have been pure HTML which is sort of the lowest common denominator for all web developers, and makes it possible to adapt them to any templating language or JavaScript framework.
Today we’re excited to add first class support for React and Vue 3 to all of the examples in Tailwind UI, which makes it even easier to adapt them for your projects.
It’s been [a long journey](https://blog.tailwindcss.com/building-react-and-vue-support-for-tailwind-ui) but I am super proud of where we ended up on this one, and really think it’s going to make Tailwind UI a useful tool for a whole new group of Tailwind CSS users.
## [Functional and accessible](https://tailwindcss.com/blog/tailwind-ui-now-with-react-and-vue-support#functional-and-accessible)
All of the React and Vue examples in Tailwind UI are powered [Headless UI](https://headlessui.dev) which is a library of components we developed to decouple all of the complicated JS behavior you need to build complex components like modals and dropdowns from the actual styles and markup.
Headless UI handles all of the ARIA attribute management, keyboard interactions, focus handling, and more for you, meaning all of the React and Vue examples provided in Tailwind UI are fully functional, with no need to write any of that complex JS stuff yourself. All of that gnarly complexity is safely tucked away in your `node_modules` folder where we can make improvements and fix bugs on your behalf, without you ever having to change your own code.
## [Fully customizable](https://tailwindcss.com/blog/tailwind-ui-now-with-react-and-vue-support#fully-customizable)
With Headless UI, we’ve managed to abstract away all of the complicated JS functionality without taking away any control over the actual markup. That means that the entire design is still in entirely under your control.
```
import { useState } from "react";import { Switch } from "@headlessui/react";function classNames(...classes) { return classes.filter(Boolean).join(" ");}export default function Example() { const [enabled, setEnabled] = useState(false); return (  <Switch   checked={enabled}   onChange={setEnabled}   className={classNames(    enabled ? "bg-indigo-600" : "bg-gray-200",    "relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:outline-none",   )}  >   <span className="sr-only">Use setting</span>   <span    aria-hidden="true"    className={classNames(     enabled ? "translate-x-5" : "translate-x-0",     "pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out",    )}   />  </Switch> );}
```

You can copy a React or Vue example from Tailwind UI and change absolutely everything about it, from the border radius to the padding to the box shadows to the font-size, all by simply adding utility classes like you’re used to.
## [Get started](https://tailwindcss.com/blog/tailwind-ui-now-with-react-and-vue-support#get-started)
If you’re already a Tailwind UI customer, all of this stuff is available to you today as a totally free update. Just log into your account, select between HTML, React, or Vue in the dropdown above any component, and grab the code in the format you want.
If you haven’t checked out Tailwind UI yet, browse the free preview components to get a feel for how it all works. It’s an awesome tool for moving fast on a new side-project idea, finding inspiration for a new feature you need to build at work, or learning how to implement a specific little UI trick with Tailwind, and a great way to support our work on open-source projects like Tailwind CSS, Headless UI, and Heroicons.
Want to check it out? [Visit the Tailwind UI website →](https://tailwindui.com)
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

