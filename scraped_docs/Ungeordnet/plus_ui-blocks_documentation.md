---
url: https://tailwindcss.com/plus/ui-blocks/documentation
scraped_at: 2025-05-25T08:36:22.161170
title: UI Blocks Documentation - Tailwind Plus
---

[](https://tailwindcss.com/plus)
[Tailwind UI is now Tailwind PlusLearn more](https://tailwindcss.com/blog/tailwind-plus)
[UI Blocks](https://tailwindcss.com/plus/ui-blocks)[Templates](https://tailwindcss.com/plus/templates)[UI Kit](https://tailwindcss.com/plus/ui-kit)[Sign in](https://tailwindcss.com/plus/login)[Get full access](https://tailwindcss.com/plus#pricing)
  *     * [Marketing](https://tailwindcss.com/plus/ui-blocks/marketing)
    * [Application UI](https://tailwindcss.com/plus/ui-blocks/application-ui)
    * [Ecommerce](https://tailwindcss.com/plus/ui-blocks/ecommerce)
    * [Documentation](https://tailwindcss.com/plus/ui-blocks/documentation)
  * ### [Getting set up](https://tailwindcss.com/plus/ui-blocks/documentation#getting-set-up)
    * [Requirements](https://tailwindcss.com/plus/ui-blocks/documentation#requirements)
    * [Add the Inter font family](https://tailwindcss.com/plus/ui-blocks/documentation#add-the-inter-font-family)
  * ### [Using HTML](https://tailwindcss.com/plus/ui-blocks/documentation#using-html)
    * [Bring your own JavaScript](https://tailwindcss.com/plus/ui-blocks/documentation#bring-your-own-javascript)
    * [Accessibility considerations](https://tailwindcss.com/plus/ui-blocks/documentation#accessibility-considerations)
    * [Dynamic classes](https://tailwindcss.com/plus/ui-blocks/documentation#dynamic-classes)
    * [Transitions](https://tailwindcss.com/plus/ui-blocks/documentation#transitions)
    * [Creating partials/components](https://tailwindcss.com/plus/ui-blocks/documentation#creating-partialscomponents)
  * ### [Using React](https://tailwindcss.com/plus/ui-blocks/documentation#using-react)
    * [Installing dependencies](https://tailwindcss.com/plus/ui-blocks/documentation#installing-dependencies)
    * [Creating components](https://tailwindcss.com/plus/ui-blocks/documentation#creating-components)
  * ### [Using Vue](https://tailwindcss.com/plus/ui-blocks/documentation#using-vue)
    * [Installing dependencies](https://tailwindcss.com/plus/ui-blocks/documentation#installing-dependencies-1)
    * [Creating components](https://tailwindcss.com/plus/ui-blocks/documentation#creating-components-1)
  * ### [Resources and assets](https://tailwindcss.com/plus/ui-blocks/documentation#resources-and-assets)
    * [Icons](https://tailwindcss.com/plus/ui-blocks/documentation#icons)
    * [Images](https://tailwindcss.com/plus/ui-blocks/documentation#images)
    * [Illustrations](https://tailwindcss.com/plus/ui-blocks/documentation#illustrations)
    * [Figma assets](https://tailwindcss.com/plus/ui-blocks/documentation#figma-assets)


5-day Mini-Course
### Build UIs that don’t suck.
**Short, tactical video lessons** from the creator of Tailwind CSS, delivered directly to your inbox **every day for a week**.
[Get the free course](https://tailwindcss.com/build-uis-that-dont-suck)
[UI Blocks](https://tailwindcss.com/plus/ui-blocks)
[Documentation](https://tailwindcss.com/plus/ui-blocks/documentation)
[UI Blocks](https://tailwindcss.com/plus/ui-blocks)
# Documentation
## Getting set up
### Requirements
All of the components in Tailwind Plus are designed for the latest version of Tailwind CSS, which is currently Tailwind CSS v4.1. To make sure that you are on the latest version of Tailwind, update via npm:
```
npm install tailwindcss@latest

```

If you're new to Tailwind CSS, you'll want to [read the Tailwind CSS documentation](https://tailwindcss.com/docs) as well to get the most out of Tailwind Plus.
### Add the Inter font family
We've used [Inter](https://rsms.me/inter) for all of the Tailwind Plus examples because it's a beautiful font for UI design and is completely open-source and free. Using a custom font is nice because it allows us to make the components look the same on all browsers and operating systems.
You can use any font you want in your own project of course, but if you'd like to use Inter, the easiest way is to first add it via the CDN:
```
<link rel="stylesheet" href="https://rsms.me/inter/inter.css" />

```

Then add "InterVariable" to your "sans" font family in your Tailwind theme:
```
@theme {
 --font-sans: InterVariable, sans-serif;
}

```

If you're still on Tailwind CSS v3.x, you can do this in your `tailwind.config.js` file:
```
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
 theme: {
  extend: {
   fontFamily: {
    sans: ['InterVariable', ...defaultTheme.fontFamily.sans],
   },
  },
 },
 // ...
}

```

## Using HTML
### Bring your own JavaScript
All of the components in Tailwind Plus are provided in three formats: React, Vue, and vanilla HTML.
The React and Vue examples are fully functional out-of-the-box, and are powered by [Headless UI](https://headlessui.com/) — a library of unstyled components we designed to integrate perfectly with Tailwind CSS.
The vanilla HTML examples **do not include any JavaScript** and are designed for people who prefer to write any necessary JavaScript themselves, or who want to integrate with a framework other than React or Vue.
The vast majority of components don't need JavaScript at all and are completely ready to go out of the box, but things that are interactive like dropdowns, dialogs, etc. require you to write some JS to make them work the way you'd expect.
In these situations we've provided some simple comments in the HTML to explain things like what classes you need to use for different states _(like a toggle switch being on or off)_ , or what classes we recommend for transitioning elements on to or off of the screen _(like a dialog opening)_.
### Accessibility considerations
We've done our best to ensure that all of the markup in Tailwind Plus is as accessible as possible, but when you're building interactive components, **many accessibility best practices can only be implemented with JavaScript.**
For example:
  * **Making sure components are properly keyboard accessible** _(dropdowns should be navigated with up/down arrow keys, dialogs should close when you press escape, tabs should be selected using the left/right arrow keys, etc.)_
  * **Correctly handling focus** _(you shouldn't be able to tab to an element behind a dialog, the first item in a dropdown should be auto-focused when the dropdown opens, etc.)_
  * **Synchronizing ARIA attributes with component state** _(adding`aria-expanded="true"` when a dropdown is open, setting `aria-checked` to true when a toggle is on, updating `aria-activedescendant` when navigating the options in an autocomplete, etc.)_
  * ...and many other concerns.


If you're using Tailwind Plus with React or Vue, all of this complexity is handled for you automatically by [Headless UI](https://headlessui.dev), but if you are providing your own JS, **it is up to you to follow accessibility best practices when adding interactive behavior.**
To learn more about building accessible UI components, we recommend studying the [WAI-ARIA Authoring Practices](https://www.w3.org/TR/wai-aria-practices/) published by the W3C.
### Dynamic classes
When an element needs different classes applied based on some state _(like a toggle being on or off)_ , we list the classes for each state in a comment directly above the element:
```
<!-- On: "bg-indigo-600", Off: "bg-gray-200" -->
<span
 aria-checked="false"
 class="focus:shadow-outline relative inline-block h-6 w-11 shrink-0 cursor-pointer rounded-full border-2 border-transparent bg-gray-200 transition-colors duration-200 ease-in-out focus:outline-none"
 role="checkbox"
 tabindex="0"
>
 <!-- On: "translate-x-5", Off: "translate-x-0" -->
 <span
  aria-hidden="true"
  class="inline-block size-5 translate-x-0 transform rounded-full bg-white shadow transition duration-200 ease-in-out"
 ></span>
</span>

```

**The HTML we provide is always pre-configured for one of the defined states** , and the classes that you need to change when switching states are always at the very beginning of the class list so they are easy to find.
As an example, to adapt this HTML for [Alpine.js](https://github.com/alpinejs/alpine), you can conditionally apply the correct classes using the `:class` directive based on some state you've declared in `x-data`:
```
<span
 x-data="{ isOn: false }"
 @click="isOn = !isOn"
 :aria-checked="isOn"
 :class="{'bg-indigo-600': isOn, 'bg-gray-200': !isOn }"
 class="focus:shadow-outline relative inline-block h-6 w-11 shrink-0 cursor-pointer rounded-full border-2 border-transparent bg-gray-200 transition-colors duration-200 ease-in-out focus:outline-none"
 role="checkbox"
 tabindex="0"
>
 <span
  aria-hidden="true"
  :class="{'translate-x-5': isOn, 'translate-x-0': !isOn }"
  class="inline-block size-5 translate-x-0 transform rounded-full bg-white shadow transition duration-200 ease-in-out"
 ></span>
</span>

```

_We've included a basic click handler here to demonstrate the general idea, but**please reference the[WAI-ARIA Authoring Practices](https://www.w3.org/TR/wai-aria-practices/) when building components like this** to ensure you implement all of the necessary keyboard interactions and properly manage any required ARIA attributes._
### Transitions
For elements that should be dynamically shown or hidden _(like the panel on a dropdown)_ , we include the recommended transition styles in a comment directly above the dynamic element:
```
<div class="relative ...">
 <button type="button" class="...">Options</button>
 <!--
  Show/hide this element based on the dropdown state
  Entering: "transition ease-out duration-100 transform"
   From: "opacity-0 scale-95"
   To: "opacity-100 scale-100"
  Closing: "transition ease-in duration-75 transform"
   From: "opacity-100 scale-100"
   To: "opacity-0 scale-95"
 -->
 <div class="absolute right-0 mt-2 w-56 origin-top-right rounded-md shadow-lg">
  <div class="rounded-md bg-white shadow-xs">
   <!-- Snipped -->
  </div>
 </div>
</div>

```

As an example, to adapt this HTML for [Alpine.js](https://github.com/alpinejs/alpine) you would use the [`x-transition`](https://github.com/alpinejs/alpine#x-transition) directive to apply the right classes at each point in the transition lifecycle:
```
<div x-data="{ isOpen: false }" class="relative ...">
 <button type="button" @click="isOpen = !isOpen" class="...">Options</button>
 <div
  x-show="isOpen"
  x-transition:enter="transition ease-out duration-100 transform"
  x-transition:enter-start="opacity-0 scale-95"
  x-transition:enter-end="opacity-100 scale-100"
  x-transition:leave="transition ease-in duration-75 transform"
  x-transition:leave-start="opacity-100 scale-100"
  x-transition:leave-end="opacity-0 scale-95"
  class="absolute right-0 mt-2 w-56 origin-top-right rounded-md shadow-lg"
 >
  <div class="rounded-md bg-white shadow-xs">
   <!-- Snipped -->
  </div>
 </div>
</div>

```

_We've included a basic click handler here to demonstrate the general idea, but**please reference the[WAI-ARIA Authoring Practices](https://www.w3.org/TR/wai-aria-practices/) when building components like this** to ensure you implement all of the necessary keyboard interactions and properly manage any required ARIA attributes._
### Creating partials/components
Since the vanilla HTML examples included in Tailwind Plus can't take advantage of things like loops, there is a lot of repetition that wouldn't actually be there in a real-world project where the HTML was being generated from some dynamic data source. We might give you a list component with 5 list items for example that have all the utilities duplicated on each one, whereas in your project you'll actually be generating those list items by looping over an array.
When adapting our examples for your own projects, we recommend creating reusable template partials or JS components as needed to manage any duplication.
Learn more about this in the ["Using components" documentation](https://tailwindcss.com/docs/styling-with-utility-classes#using-components) on the Tailwind CSS website.
## Using React
### Installing dependencies
Tailwind Plus for React depends on [Headless UI](https://headlessui.dev) to power all of the interactive behavior and [Heroicons](https://heroicons.com) for icons, so you'll need to add these two libraries to your project:
```
npm install @headlessui/react @heroicons/react

```

**These libraries and Tailwind Plus itself all require React >= 16**.
### Creating components
All React examples are provided as a simple single component and make no assumptions about how you want to break things down, what prop APIs you want to expose, or where you get any data from.
Some data has been extracted into basic local variables just to clean up duplication and make the code easier to read and understand, but we've tried to do as little as possible to avoid enforcing any unnecessarily rigid opinions.
When you're adapting code from Tailwind Plus for your own projects, you should break the examples down into smaller components as necessary to achieve whatever level of reuse you need for your project.
For example, you might start with this stacked list component:
```
const people = [
 {
  name: 'Calvin Hawkins',
  email: 'calvin.hawkins@example.com',
  image:
   'https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
 },
 {
  name: 'Kristen Ramos',
  email: 'kristen.ramos@example.com',
  image:
   'https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
 },
 {
  name: 'Ted Fox',
  email: 'ted.fox@example.com',
  image:
   'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
 },
]
export default function Example() {
 return (
  <ul className="divide-y divide-gray-200">{people.map((person) => (
    <li key={person.email} className="flex py-4"><img className="size-10 rounded-full" src={person.image} alt="" /><div className="ml-3"><p className="text-sm font-medium text-gray-900">{person.name}</p><p className="text-sm text-gray-500">{person.email}</p></div></li>
   ))}</ul>
 )
}

```

After adapting the content for your own project, breaking it down into separate components, and wiring up your data source, it might look more like this:
```
function HockeyTeamItem({ team }) {
 return (
  <li className="flex py-4"><img className="size-10 rounded-full" src={team.logo} alt="" /><div className="ml-3"><p className="text-sm font-medium text-gray-900">{team.name}</p><p className="text-sm text-gray-500">{team.city}</p></div></li>
 )
}
export default function HockeyTeamList({ teams }) {
 return (
  <ul className="divide-y divide-gray-200">{teams.map((team) => (
    <HockeyTeamItem key={team.id} team={team} />
   ))}</ul>
 )
}

```

Tailwind Plus is more like a set of blueprints, patterns, and ideas than a rigid UI kit. The code you end up with at the end of the day is _yours_ , and you can factor it however you like.
## Using Vue
### Installing dependencies
Tailwind Plus for Vue depends on [Headless UI](https://headlessui.dev) to power all of the interactive behavior and [Heroicons](https://heroicons.com) for icons, so you'll need to add these two libraries to your project:
```
npm install @headlessui/vue @heroicons/vue

```

### Creating components
All Vue examples are provided as a simple single component and make no assumptions about how you want to break things down, what prop APIs you want to expose, or where you get any data from.
Some data has been extracted into basic local variables just to clean up duplication and make the code easier to read and understand, but we've tried to do as little as possible to avoid enforcing any unnecessarily rigid opinions.
When you're adapting code from Tailwind Plus for your own projects, you should break the examples down into smaller components as necessary to achieve whatever level of reuse you need for your project.
For example, you might start with this stacked list component:
```
<template>
 <ul class="divide-y divide-gray-200">
  <li v-for="person in people" :key="person.email" class="flex py-4">
   <img class="size-10 rounded-full" :src="person.image" alt="" />
   <div class="ml-3">
    <p class="text-sm font-medium text-gray-900">{{ person.name }}</p>
    <p class="text-sm text-gray-500">{{ person.email }}</p>
   </div>
  </li>
 </ul>
</template>
<script>
 const people = [
  {
   name: 'Calvin Hawkins',
   email: 'calvin.hawkins@example.com',
   image:
    'https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
  {
   name: 'Kristen Ramos',
   email: 'kristen.ramos@example.com',
   image:
    'https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
  {
   name: 'Ted Fox',
   email: 'ted.fox@example.com',
   image:
    'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
  },
 ]
 export default {
  setup() {
   return {
    people,
   }
  },
 }
</script>

```

After adapting the content for your own project, breaking it down into separate components, and wiring up your data source, it might look more like this:
```
<!-- HockeyTeamList.vue -->
<template>
 <ul class="divide-y divide-gray-200">
  <HockeyTeamItem v-for="team in teams" :key="team.id" :team="team" />
 </ul>
</template>
<script>
 export default {
  props: {
   teams: Array,
  },
 }
</script>
<!-- HockeyTeamListItem.vue -->
<template>
 <li class="flex py-4">
  <img class="size-10 rounded-full" :src="team.logo" alt="" />
  <div class="ml-3">
   <p class="text-sm font-medium text-gray-900">{{ team.name }}</p>
   <p class="text-sm text-gray-500">{{ team.city }}</p>
  </div>
 </li>
</template>
<script>
 export default {
  props: {
   team: Object,
  },
 }
</script>

```

Tailwind Plus is more like a set of blueprints, patterns, and ideas than a rigid UI kit. The code you end up with at the end of the day is _yours_ , and you can factor it however you like.
## Resources and assets
### Icons
All of the icons we use in Tailwind Plus come from [Heroicons](https://heroicons.com), which is a free MIT-licensed icon set we designed and developed ourselves when we started working on Tailwind Plus.
### Images
Images in Tailwind Plus come almost exclusively from [Unsplash](https://unsplash.com). It's a great resource if you need freely-usable photography for your projects.
### Illustrations
Some of the examples in Tailwind Plus use illustrations from the free [Lucid Illustrations](https://lucid.pixsellz.io) pack by [Pixsellz](https://www.pixsellz.io). You can grab the full set of illustrations and check out their other design resources on [their website](https://www.pixsellz.io).
### Figma assets
We used to provide Figma assets for Tailwind Plus, but they were just an absolutely enormous amount of work to maintain and very few people were using them. We made the really hard decision to discontinue them so we can spend more time on the actual code which is where we think we can provide the most value.
Customers of Tailwind Plus can download the final Figma file we released, but please note **the Figma file does not receive updates** and does not contain any examples released after July 14, 2021.
[Download the discontinued Figma kit →](https://tailwindcss.com/plus/download-figma)
### Marketing
  * [Hero Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/heroes)
  * [Feature Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/feature-sections)
  * [Pricing Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/pricing)
  * [Header Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/header)
  * [Newsletter Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/newsletter-sections)
  * [Testimonials](https://tailwindcss.com/plus/ui-blocks/marketing/sections/testimonials)
  * [Team Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/team-sections)
  * [Content Sections](https://tailwindcss.com/plus/ui-blocks/marketing/sections/content-sections)
  * [Logo Clouds](https://tailwindcss.com/plus/ui-blocks/marketing/sections/logo-clouds)
  * [FAQs](https://tailwindcss.com/plus/ui-blocks/marketing/sections/faq-sections)
  * [Footers](https://tailwindcss.com/plus/ui-blocks/marketing/sections/footers)
  * [Headers](https://tailwindcss.com/plus/ui-blocks/marketing/sections/header)
  * [Flyout Menus](https://tailwindcss.com/plus/ui-blocks/marketing/elements/flyout-menus)
  * [Banners](https://tailwindcss.com/plus/ui-blocks/marketing/elements/banners)
  * [Browse all →](https://tailwindcss.com/plus/ui-blocks/marketing)


### Application UI
  * [Tables](https://tailwindcss.com/plus/ui-blocks/application-ui/lists/tables)
  * [Feeds](https://tailwindcss.com/plus/ui-blocks/application-ui/lists/feeds)
  * [Form Layouts](https://tailwindcss.com/plus/ui-blocks/application-ui/forms/form-layouts)
  * [Select Menus](https://tailwindcss.com/plus/ui-blocks/application-ui/forms/select-menus)
  * [Radio Groups](https://tailwindcss.com/plus/ui-blocks/application-ui/forms/radio-groups)
  * [Checkboxes](https://tailwindcss.com/plus/ui-blocks/application-ui/forms/checkboxes)
  * [Comboboxes](https://tailwindcss.com/plus/ui-blocks/application-ui/forms/comboboxes)
  * [Navbars](https://tailwindcss.com/plus/ui-blocks/application-ui/navigation/navbars)
  * [Pagination](https://tailwindcss.com/plus/ui-blocks/application-ui/navigation/pagination)
  * [Sidebar Navigation](https://tailwindcss.com/plus/ui-blocks/application-ui/navigation/sidebar-navigation)
  * [Command Palettes](https://tailwindcss.com/plus/ui-blocks/application-ui/navigation/command-palettes)
  * [Modals](https://tailwindcss.com/plus/ui-blocks/application-ui/overlays/modal-dialogs)
  * [Dropdowns](https://tailwindcss.com/plus/ui-blocks/application-ui/elements/dropdowns)
  * [Buttons](https://tailwindcss.com/plus/ui-blocks/application-ui/elements/buttons)
  * [Browse all →](https://tailwindcss.com/plus/ui-blocks/application-ui)


### Ecommerce
  * [Product Overviews](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/product-overviews)
  * [Product Lists](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/product-lists)
  * [Category Previews](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/category-previews)
  * [Shopping Carts](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/shopping-carts)
  * [Category Filters](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/category-filters)
  * [Product Quickviews](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/product-quickviews)
  * [Product Features](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/product-features)
  * [Store Navigation](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/store-navigation)
  * [Promo Sections](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/promo-sections)
  * [Checkout Forms](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/checkout-forms)
  * [Reviews](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/reviews)
  * [Order Summaries](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/order-summaries)
  * [Order History](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/order-history)
  * [Incentives](https://tailwindcss.com/plus/ui-blocks/ecommerce/components/incentives)
  * [Browse all →](https://tailwindcss.com/plus/ui-blocks/ecommerce)


### Templates & UI Kits
  * [Catalyst UI Kit](https://tailwindcss.com/plus/templates/catalyst)
  * [Personal Website Template](https://tailwindcss.com/plus/templates/spotlight)
  * [Landing Page Template](https://tailwindcss.com/plus/templates/salient)
  * [API Reference Template](https://tailwindcss.com/plus/templates/protocol)
  * [Changelog Template](https://tailwindcss.com/plus/templates/commit)
  * [Info Product Template](https://tailwindcss.com/plus/templates/primer)
  * [Agency Template](https://tailwindcss.com/plus/templates/studio)
  * [Podcast Template](https://tailwindcss.com/plus/templates/transmit)
  * [App Marketing Template](https://tailwindcss.com/plus/templates/pocket)
  * [Documentation Template](https://tailwindcss.com/plus/templates/syntax)
  * [Conference Template](https://tailwindcss.com/plus/templates/keynote)
  * [Browse all →](https://tailwindcss.com/plus/templates)


© 2025 Tailwind Labs Inc. All rights reserved.
[Privacy policy](https://tailwindcss.com/plus/privacy-policy)[Changelog](https://tailwindcss.com/plus/changelog)

