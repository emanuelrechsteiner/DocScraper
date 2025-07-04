---
url: https://tailwindcss.com/blog/headless-ui-unstyled-accessible-ui-components
scraped_at: 2025-05-25T08:35:51.682736
title: Headless UI: Unstyled, Accessible UI Components - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
October 6, 2020
# Headless UI: Unstyled, Accessible UI Components
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
![Headless UI Logo](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fheadless-ui-card.6c478fa0.png&w=3840&q=75)
One of the biggest pain points when building modern web applications is building custom components like select menus, dropdowns, toggles, modals, tabs, radio groups — components that are pretty similar from project to project, but never quite the _same_.
You could use an off-the-shelf package, but they usually come tightly coupled with their own provided styles. It ends up being very hard to get them to match the look and feel of your own project, and almost always involves writing a bunch of CSS overrides, which feels like a big step backwards when working Tailwind CSS.
The other option is building your own components from scratch. At first it seems easy, but then you remember you need to add support for keyboard navigation, managing ARIA attributes, focus trapping, and all of a sudden you're spending 3-4 weeks trying to build a truly bullet-proof dropdown menu.
We think there's a better option, so we're building it.
**[Headless UI](https://headlessui.dev) is a set of completely unstyled, fully accessible UI components for React and Vue** _(and soon Alpine.js)_ that make it easy to build these sorts of custom components without worrying about any of the complex implementation details yourself, and without sacrificing the ability to style them from scratch with simple utility classes.
Here's what it looks like to build a custom dropdown _(one of many components the library includes)_ using `@headlessui/react`, with complete keyboard navigation support and ARIA attribute management, styled with simple Tailwind CSS utilities:
```
import { Menu } from "@headlessui/react";function MyDropdown() { return (  <Menu as="div" className="relative">   <Menu.Button className="rounded bg-blue-600 px-4 py-2 text-white ...">Options</Menu.Button>   <Menu.Items className="absolute right-0 mt-1">    <Menu.Item>     {({ active }) => (      <a className={`${active && "bg-blue-500 text-white"} ...`} href="/account-settings">       Account settings      </a>     )}    </Menu.Item>    <Menu.Item>     {({ active }) => (      <a className={`${active && "bg-blue-500 text-white"} ...`} href="/documentation">       Documentation      </a>     )}    </Menu.Item>    <Menu.Item disabled>     <span className="opacity-75 ...">Invite a friend (coming soon!)</span>    </Menu.Item>   </Menu.Items>  </Menu> );}
```

Here's what you're getting for free in that example, without having to write a single line of code related to it yourself:
  * The dropdown panel opens on click, spacebar, enter, or when using the arrow keys
  * The dropdown closes when you press escape, or click outside of it
  * You can navigate the items using the up and down arrow keys
  * You can jump the first item using the `Home` key, and the last item using the `End` key
  * Disabled items are automatically skipped when navigating with the keyboard
  * Hovering over an item with your mouse after navigating with the keyboard will switch to mouse position based focusing
  * Items are announced properly to screen readers while navigating them with the keyboard
  * The dropdown button is properly announced to screenreaders as controlling a menu
  * ...and probably tons more that I'm forgetting.


All without writing the letters `aria` anywhere in your own code, and without writing a single event listener. And you still have complete control over the design!
There are [over 3000 lines of tests for this component](https://github.com/tailwindlabs/headlessui/blob/c7b91dc7315b1f49c1a469f70eb1f6eba6a2e31c/packages/%40headlessui-react/src/components/menu/menu.test.tsx). Pretty nice that you didn't have to do that yourself, right?
Here's a fully-styled live demo _(taken from[Tailwind UI](https://tailwindui.com))_ so you can see it in action:
Make sure to try it with the keyboard or a screen reader to really appreciate it!
We just tagged v0.2.0, which currently includes the following components:
  * [Menu Button](https://codesandbox.io/s/headlessuivue-menu-example-70br3?file=/src/App.vue) (or dropdown)
  * [Listbox](https://codesandbox.io/s/headlessuivue-listbox-example-mi67g?file=/src/App.vue) (or custom select)
  * [Switch](https://codesandbox.io/s/headlessuivue-switch-example-8ycp6?file=/src/App.vue) (or toggle)
  * ...with many more on the way.


To learn more and dive in, [**head over to the Headless UI website**](https://headlessui.dev) and read the documentation.
If you've followed my work online for the last few years, you might remember my fascination with [renderless UI components](https://adamwathan.me/renderless-components-in-vuejs/) — something I was really started getting into towards the [end of 2017](https://fullstackradio.com/79). I've wanted a library like this to exist for years, but until we started growing the team we just didn't have the resources to make it happen.
Earlier this year [we hired Robin Malfait](https://blog.tailwindcss.com/from-900-to-1-how-we-hired-robin-malfait), and he's been working on Headless UI full-time ever since.
The biggest motivation for this project is that we'd really like to add production-ready JS examples to [Tailwind UI](https://tailwindui.com), which is currently an HTML-only, bring-your-own-JavaScript sort of project. This is great for lots of our customers who want full control over how everything works, but for many others it's a point of friction.
We didn't want to add 200 lines of gnarly JS to every component example, so we started working on Headless UI as a way to _extract_ all of that noise, without giving up any flexibility in the actual UI design.
## [Why reinvent the wheel?](https://tailwindcss.com/blog/headless-ui-unstyled-accessible-ui-components#why-reinvent-the-wheel)
We're not the first people to try and tackle this problem. [Downshift](https://github.com/downshift-js/downshift) was the first library I saw that got me excited about this idea back in 2017, [Reach UI](https://reach.tech/) and [Reakit](https://reakit.io/) started development in 2018, and [React Aria](https://react-spectrum.adobe.com/react-aria/getting-started.html) was released most recently, just earlier this year.
We decided to try our own take on the problem for a few reasons:
  * Existing solutions are focused almost entirely on React, and we'd like to bring these ideas to other ecosystems like Vue, Alpine, and hopefully more in the future.
  * These libraries are going to be foundational for adding JS support to Tailwind UI, and since that's what keeps the business running it felt important to have complete decision-making power over how the libraries worked and what they supported.
  * We have our own ideas on what the APIs should look like for these components, and want to be able to explore those ideas freely.
  * We want to make sure it is always super easy to style these components with Tailwind, rather than having to write custom CSS.


We think what we've come up with so far hits a great balance between flexibility and developer experience, and we're grateful there are other people working on similar problems that we can learn from and share our ideas with.
## [What's next](https://tailwindcss.com/blog/headless-ui-unstyled-accessible-ui-components#whats-next)
We've got quite a few more components to develop for Headless UI, including:
  * Modal
  * Radio group
  * Tabs
  * Accordion
  * Combobox
  * Datepicker


...and likely many more. We're also about to start on Alpine.js support, and we're hoping to be able to tag a v1.0 for React, Vue, and Alpine near the end of the year.
After that we'll start exploring other frameworks, with the hope that we can eventually offer the same tools for ecosystems like Svelte, Angular, and Ember, either first-class or with community partners.
If you'd like to keep up with what we're doing, be sure to [follow the project on GitHub](https://github.com/tailwindlabs/headlessui).
Want to talk about this post? [Discuss this on GitHub →](https://github.com/tailwindcss/tailwindcss/discussions/2508)
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

