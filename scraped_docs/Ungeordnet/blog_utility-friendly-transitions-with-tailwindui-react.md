---
url: https://tailwindcss.com/blog/utility-friendly-transitions-with-tailwindui-react
scraped_at: 2025-05-25T09:00:40.813803
title: Utility-Friendly Transitions with @tailwindui/react - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
August 27, 2020
# Utility-Friendly Transitions with @tailwindui/react
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frobinmalfait.e0195e4e.jpg&w=96&q=75)
Robin Malfait
[@malfaitrobin](https://twitter.com/malfaitrobin)
Back in February we released [Tailwind UI](https://tailwindui.com), a directory of HTML component examples designed for you to copy and paste into your Tailwind projects as a starting point for your own designs.
We built Tailwind UI as an HTML-only, bring-your-own-JS product to make it as universal as possible, but many designs are inherently interactive and porting those interactive behaviors between JavaScript frameworks is unfortunately not always very easy.
One example of this is enter/leave transitions, like when you toggle a dropdown menu and see it fade in and out.
Vue.js has a really neat `<transition>` component for enter/leave transitions with a very utility-friendly API:
```
<transition enter-active-class="transition-opacity duration-75" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition-opacity duration-150" leave-from-class="opacity-100" leave-to-class="opacity-0"> <div v-show="isShowing">  <!-- Will fade in and out --> </div></transition>
```

But replicating this in React turns out to be much more difficult, because until now there hasn't been a library designed to support utility-driven transition styling.
**So earlier this week, we released the very first version of[@tailwindui/react](https://github.com/tailwindlabs/tailwindui-react), a library that provides low-level primitives for turning utility-first HTML into fully interactive UIs.**
We'll be adding many more components in the coming months _(like dropdowns, toggles, modals, and more, and for Vue too!)_ but thought we'd start with a `<Transition>` component to at least get the current Tailwind UI experience for React users up to par with what's possible in Vue and Alpine.js.
Here's what it looks like to use:
```
import { Transition } from "@tailwindui/react";import { useState } from "react";function MyComponent() { const [isOpen, setIsOpen] = useState(false); return (  <div>   <button onClick={() => setIsOpen(!isOpen)}>Toggle</button>   <Transition    show={isOpen}    enter="transition-opacity duration-75"    enterFrom="opacity-0"    enterTo="opacity-100"    leave="transition-opacity duration-150"    leaveFrom="opacity-100"    leaveTo="opacity-0"   >    {/* Will fade in and out */}   </Transition>  </div> );}
```

[Read the documentation](https://github.com/tailwindlabs/tailwindui-react) to learn more about advanced functionality, like:
  * Rendering without an extra DOM element
  * Co-ordinating related transitions
  * Transitioning on initial mount.


Check it out in action in this CodeSandbox demo:
Try it out on your projects, and if you run into any problems, [report an issue on GitHub](https://github.com/tailwindlabs/tailwindui-react).
Want to talk about this post? [Discuss this on GitHub →](https://github.com/tailwindcss/tailwindcss/discussions/2262)
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

