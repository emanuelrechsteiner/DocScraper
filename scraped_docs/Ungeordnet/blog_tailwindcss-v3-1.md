---
url: https://tailwindcss.com/blog/tailwindcss-v3-1
scraped_at: 2025-05-25T08:29:08.904751
title: Tailwind CSS v3.1: You wanna get nuts? Come on, let's get nuts! - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
June 7, 2022
# Tailwind CSS v3.1: You wanna get nuts? Come on, let's get nuts!
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
It's been about six months since we released [Tailwind CSS v3.0](https://tailwindcss.com/blog/tailwindcss-v3), and even though we've been collecting a lot of little improvements in the codebase since then, we just didn't have _that-one-feature_ yet that makes you say _"okay, it's release-cuttin' time"_.
Then on a random Saturday night a couple of weeks ago, I was talking to Robin in our Discord about coming up with a way to target the `html` element using `:has` and a class deeper in the document, and explained how I thought it would look if we added support for arbitrary variants — something I've wanted to tackle for over a year:
![Adam Wathan: I think if we do arbitrary variants, the syntax should just be that exact thing, '\[html:has\(&\)\]:bg-blue-500'. Feel like that is pretty flexible, like anything you can do with a real variant you can also do with an arbitrary variant since they are the same thing. '\[&>*:not\(:first-child\)\]:pl-4'.
Robin: This is going to break my brain haha because '\[html:has\(&\)\]:bg-blue-500' would be used as a literal inside the '&'. That in combination with other variants... 🤯.
Adam Wathan: 😅 it'll be a brain melter for sure. The CSS would be this lol 'html:has\(\[html:has\(&\)\]:bg-blue-500 {"{"} background: blue 500 }'.
Robin: exactly haha. ok, now I want to try that brb.](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdiscord-message.225e322a.png&w=3840&q=75)
Twenty minutes later Robin had a working proof of concept _(in six lines of code!)_ , and after another hour or so of Jordan performing regex miracles in our class detection engine, [arbitrary variants](https://github.com/tailwindlabs/tailwindcss/pull/8299) were born and we had our release-worthy feature.
So here it is — Tailwind CSS v3.1! For a complete list of every fix and improvement check out the [release notes](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.1.0), but here's the highlights:
  * [First-party TypeScript types](https://tailwindcss.com/blog/tailwindcss-v3-1#first-party-type-script-types)
  * [Built-in support for CSS imports in the CLI](https://tailwindcss.com/blog/tailwindcss-v3-1#built-in-support-for-css-imports-in-the-cli)
  * [Change color opacity when using the theme function](https://tailwindcss.com/blog/tailwindcss-v3-1#change-color-opacity-when-using-the-theme-function)
  * [Easier CSS variable color configuration](https://tailwindcss.com/blog/tailwindcss-v3-1#easier-css-variable-color-configuration)
  * [Border spacing utilities](https://tailwindcss.com/blog/tailwindcss-v3-1#border-spacing-utilities)
  * [Enabled and optional variants](https://tailwindcss.com/blog/tailwindcss-v3-1#enabled-and-optional-variants)
  * [Prefers-contrast variants](https://tailwindcss.com/blog/tailwindcss-v3-1#prefers-contrast-variants)
  * [Style native dialog backdrops](https://tailwindcss.com/blog/tailwindcss-v3-1#style-native-dialog-backdrops)
  * [Arbitrary values but for variants](https://tailwindcss.com/blog/tailwindcss-v3-1#arbitrary-values-but-for-variants)


Upgrade your projects by installing the latest version of `tailwindcss` from npm:
```
npm install tailwindcss@latest
```

Or spin up a [Tailwind Play](https://play.tailwindcss.com) to play around with all of the new goodies right in the browser.
## [First-party TypeScript types](https://tailwindcss.com/blog/tailwindcss-v3-1#first-party-typescript-types)
We're now shipping types for all of our JS APIs you work with when using Tailwind, most notably the `tailwind.config.js` file. This means you get all sorts of useful IDE support, and makes it a lot easier to make changes to your configuration without referencing the documentation quite as much.
To set it up, just add the type annotation above your config definition:
tailwind.config.js
```
/** @type {import('tailwindcss').Config} */module.exports = { content: [  // ... ], theme: {  extend: {}, }, plugins: [],};
```

If you're a big TypeScript nerd you might enjoy poking around the actual [type definitions](https://github.com/tailwindlabs/tailwindcss/blob/4a745439f010aca2ea24bb7fd9ab0ac3e15a40c1/types/config.d.ts) — lots of interesting stuff going on there to support such a potentially complex object.
## [Built-in support for CSS imports in the CLI](https://tailwindcss.com/blog/tailwindcss-v3-1#built-in-support-for-css-imports-in-the-cli)
If you're using our CLI tool to compile your CSS, [`postcss-import`](https://github.com/postcss/postcss-import) is now baked right in so you can organize your custom CSS into multiple files without any additional configuration.
main.css
select2-theme.css
```
@import "tailwindcss/base";@import "./select2-theme.css";@import "tailwindcss/components";@import "tailwindcss/utilities";
```

If you're not using our CLI tool and instead using Tailwind as a PostCSS plugin, you'll still need to install and configure `postcss-import` yourself just like you do with `autoprefixer`, but if you _are_ using our CLI tool this will totally just work now.
This is especially handy if you're using our [standalone CLI](https://tailwindcss.com/blog/standalone-cli) and don't want to install any node dependencies at all.
## [Change color opacity when using the theme function](https://tailwindcss.com/blog/tailwindcss-v3-1#change-color-opacity-when-using-the-theme-function)
I don't think tons of people know about this, but Tailwind exposes a [`theme()` function](https://v3.tailwindcss.com/docs/functions-and-directives#theme) to your CSS files that lets you grab values from your config file — sort of turning them into variables that you can reuse.
select2-theme.css
```
.select2-dropdown { border-radius: theme(borderRadius.lg); background-color: theme(colors.gray.100); color: theme(colors.gray.900);}/* ... */
```

One limitation though was that you couldn't adjust the alpha channel any colors you grabbed this way. So in v3.1 we've added support for using a slash syntax to adjust the opacity, like you can with the modern `rgb` and `hsl` CSS color functions:
select2-theme.css
```
.select2-dropdown { border-radius: theme(borderRadius.lg); background-color: theme(colors.gray.100 / 50%); color: theme(colors.gray.900);}/* ... */
```

We've made this work with the `theme` function in your `tailwind.config.js` file, too:
tailwind.config.js
```
module.exports = { content: [  // ... ], theme: {  extend: {   colors: ({ theme }) => ({    primary: theme("colors.blue.500"),    "primary-fade": theme("colors.blue.500 / 75%"),   }),  }, }, plugins: [],};
```

You can even use this stuff in arbitrary values which is pretty wild — honestly surprisingly useful for weird custom gradients and stuff:
```
<div class="bg-[image:linear-gradient(to_right,theme(colors.red.500)_75%,theme(colors.red.500/25%))]"> <!-- ... --></div>
```

Anything to avoid editing a CSS file am I right?
## [Easier CSS variable color configuration](https://tailwindcss.com/blog/tailwindcss-v3-1#easier-css-variable-color-configuration)
If you like to define and configure your colors as CSS variables, you probably have some horrible boilerplate like this in your `tailwind.config.js` file right now:
tailwind.config.js
```
function withOpacityValue(variable) { return ({ opacityValue }) => {  if (opacityValue === undefined) {   return `rgb(var(${variable}))`;  }  return `rgb(var(${variable}) / ${opacityValue})`; };}module.exports = { theme: {  colors: {   primary: withOpacityValue("--color-primary"),   secondary: withOpacityValue("--color-secondary"),   // ...  }, },};
```

We've made this way less awful in v3.1 by adding support for defining your colors with a format string instead of having to use a function:
tailwind.config.js
```
module.exports = { theme: {  colors: {   primary: "rgb(var(--color-primary) / <alpha-value>)",   secondary: "rgb(var(--color-secondary) / <alpha-value>)",   // ...  }, },};
```

Instead of writing a function that receives that `opacityValue` argument, you can just write a string with an `<alpha-value>` placeholder, and Tailwind will replace that placeholder with the correct alpha value based on the utility.
If you haven't seen any of this before, check out our updated [Using CSS variables](https://v3.tailwindcss.com/docs/customizing-colors#using-css-variables) documentation for more details.
## [Border spacing utilities](https://tailwindcss.com/blog/tailwindcss-v3-1#border-spacing-utilities)
We've added new set of utilities for the `border-spacing` property, so you can control the space between table borders when using [separate borders](https://v3.tailwindcss.com/docs/border-collapse#separate):
State| City  
---|---  
Indiana| Indianapolis  
Ohio| Columbus  
Michigan| Detroit  
```
<table class="border-separate border-spacing-2 ..."> <thead>  <tr>   <th class="border border-slate-300 ...">State</th>   <th class="border border-slate-300 ...">City</th>  </tr> </thead> <tbody>  <tr>   <td class="border border-slate-300 ...">Indiana</td>   <td class="border border-slate-300 ...">Indianapolis</td>  </tr>  <!-- ... --> </tbody></table>
```

I know what you're thinking — _"I have never in my life wanted to build a table that looks like that..."_ — but listen for a second!
One situation where this is actually super useful is when building a table with a sticky header row and you want a persistent bottom border under the headings:
Scroll this table to see the sticky header row in action
Name| Email| Role  
---|---|---  
Courtney Henry| courtney.henry@example.com| Admin  
Tom Cook| tom.cook@example.com| Member  
Whitney Francis| whitney.francis@example.com| Admin  
Leonard Krasner| leonard.krasner@example.com| Owner  
Floyd Miles| floyd.miles@example.com| Member  
Emily Selman| emily.selman@example.com| Member  
Kristin Watson| kristin.watson@example.com| Admin  
Emma Dorsey| emma.dorsey@example.com| Member  
Alicia Bell| alicia.bell@example.com| Admin  
Jenny Wilson| jenny.wilson@example.com| Owner  
Anna Roberts| anna.roberts@example.com| Member  
Benjamin Russel| benjamin.russel@example.com| Member  
Jeffrey Webb| jeffrey.webb@example.com| Admin  
Kathryn Murphy| kathryn.murphy@example.com| Member  
```
<table class="border-separateborder-spacing-0"> <thead class="bg-gray-50">  <tr>   <th class="sticky top-0 z-10 border-b border-gray-300 ...">Name</th>   <th class="sticky top-0 z-10 border-b border-gray-300 ...">Email</th>   <th class="sticky top-0 z-10 border-b border-gray-300 ...">Role</th>  </tr> </thead> <tbody class="bg-white">  <tr>   <td class="border-b border-gray-200 ...">Courtney Henry</td>   <td class="border-b border-gray-200 ...">courtney.henry@example.com</td>   <td class="border-b border-gray-200 ...">Admin</td>  </tr>  <!-- ... --> </tbody></table>
```

You might think you could just use `border-collapse` here since you actually don't want any space between the borders but you'd be mistaken. Without `border-separate` and `border-spacing-0`, the border will scroll away instead of sticking under the headings. CSS is fun isn't it?
Check out the [border spacing documentation](https://v3.tailwindcss.com/docs/border-spacing) for some more details.
## [Enabled and optional variants](https://tailwindcss.com/blog/tailwindcss-v3-1#enabled-and-optional-variants)
We've added new variants for the `:enabled` and `:optional` pseudo-classes, which target form elements when they are, well, enabled and optional.
_"But Adam why would I ever need these, enabled and optional aren't even states, they are the defaults. Do you even make websites?"_
Ouch, that hurts because it's true — I pretty much just write emails and answer the same questions over and over again on GitHub now.
But check out this disabled button example:
Processing...
```
<button type="button" class="bg-indigo-500 hover:bg-indigo-400 disabled:opacity-75 ..." disabled>Processing...</button>
```

Notice how when you hover over the button, the background still changes color even though it's disabled? Before this release, you'd usually fix that like this:
```
<button type="button" class="bg-indigo-500 hover:bg-indigo-400 disabled:opacity-75 disabled:hover:bg-indigo-500 ..." disabled> Processing...</button>
```

But with the new `enabled` modifier, you can write it like this instead:
Processing...
```
<button type="button" class="bg-indigo-500 hover:enabled:bg-indigo-400 disabled:opacity-75 ..." disabled> Processing...</button>
```

Instead of overriding the hover color back to the default color when the button is disabled, we combine the `hover` and `enabled` variants to just not apply the hover styles when the button is disabled in the first place. I think that's better!
Here's an example combining the new `optional` modifier with our [sibling state features](https://v3.tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-sibling-state) to hide a little "Required" notice for fields that aren't required:
Email
Required
Name
Required
Submit
```
<form> <div>  <label for="email" ...>Email</label>  <div>   <input required class="peer ..." id="email" />   <div class="peer-optional:hidden ...">Required</div>  </div> </div> <div>  <label for="name" ...>Name</label>  <div>   <input class="peer ..." id="name" />   <div class="peer-optional:hidden ...">Required</div>  </div> </div> <!-- ... --></form>
```

This lets you use the same markup for all of your form groups and letting CSS handle all of the conditional rendering for you instead of handling it yourself. Kinda neat!
## [Prefers-contrast variants](https://tailwindcss.com/blog/tailwindcss-v3-1#prefers-contrast-variants)
Did you know there's a `prefers-contrast` media query? Well there is, and now Tailwind supports it out of the box.
Use the new `contrast-more` and `contrast-less` variants to modify your design when the user has requested more or less contrast, usually through an operating system accessibility preference like "Increase contrast" on macOS.
Try emulating `prefers-contrast: more` in your developer tools to see the changes
Social Security Number
We need this to steal your identity.
```
<form> <label class="block">  <span class="block text-sm font-medium text-slate-700">Social Security Number</span>  <input   class="border-slate-200 placeholder-slate-400 contrast-more:border-slate-400contrast-more:placeholder-slate-500"  />  <p class="mt-2 text-sm text-slate-600 opacity-10 contrast-more:opacity-100">We need this to steal your identity.</p> </label></form>
```

I wrote [some documentation](https://v3.tailwindcss.com/docs/hover-focus-and-other-states#prefers-contrast) for this but honestly I wrote more here than I did there.
## [Style native dialog backdrops](https://tailwindcss.com/blog/tailwindcss-v3-1#style-native-dialog-backdrops)
There's a pretty new [HTML `<dialog>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) with surprisingly decent [browser support](https://caniuse.com/dialog) that is worth playing with if you like to live on the bleeding edge.
Dialogs have this new `::backdrop` pseudo-element that's rendered while the dialog is open, and Tailwind CSS v3.1 adds a new `backdrop` modifier you can use to style this baby:
```
<dialog class="backdrop:bg-slate-900/50 ..."> <form method="dialog">  <!-- ... -->  <button value="cancel">Cancel</button>  <button>Submit</button> </form></dialog>
```

I recommend reading the [MDN Dialog documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog) if you want to dig in to this thing more — it's exciting stuff but there's a lot to know.
## [Arbitrary values but for variants](https://tailwindcss.com/blog/tailwindcss-v3-1#arbitrary-values-but-for-variants)
Okay so this one is the real highlight for me — you know how we give you the [`addVariant` API](https://v3.tailwindcss.com/docs/plugins#adding-variants) for creating your own custom variants?
tailwind.config.js
```
const plugin = require("tailwindcss/plugin");module.exports = { // ... plugins: [  plugin(function ({ addVariant }) {   addVariant("third", "&:nth-child(3)");  }), ],};
```

...and you know how we have [arbitrary values](https://v3.tailwindcss.com/docs/adding-custom-styles#using-arbitrary-values) for using any value you want with a utility directly in your HTML?
```
<!--] --><div class="top-[117px]"> <!-- ... --></div>
```

Well Tailwind CSS v3.1 introduces [arbitrary variants](https://v3.tailwindcss.com/docs/hover-focus-and-other-states#using-arbitrary-variants), letting you create your own ad hoc variants directly in your HTML:
```
<div class="[&:nth-child(3)]:py-0"> <!-- ... --></div>
```

This is super useful for variants that sort of feel like they need to be parameterized, for example adding a style if the browser supports a specific CSS feature using a `@supports` query:
```
<div class="bg-white [@supports(backdrop-filter:blur(0))]:bg-white/50[@supports(backdrop-filter:blur(0))]:backdrop-blur"> <!-- ... --></div>
```

You can even use this feature to target child elements with arbitrary variants like `[&>*]`:
  * ![](https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)
Kristen Ramos
kristen.ramos@example.com
  * ![](https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)
Floyd Miles
floyd.miles@example.com
  * ![](https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)
Courtney Henry
courtney.henry@example.com


```
<ul role="list" class="space-y-4 [&>*]:rounded-lg[&>*]:bg-white[&>*]:p-4[&>*]:shadow"> <li class="flex">  <img class="h-10 w-10 rounded-full" src="..." alt="" />  <div class="ml-3 overflow-hidden">   <p class="text-sm font-medium text-slate-900">Kristen Ramos</p>   <p class="truncate text-sm text-slate-500">kristen.ramos@example.com</p>  </div> </li> <!-- ... --></ul>
```

You can even style the first `p` inside the `div` in the second child `li` but only on `hover`:
Try hovering over the text “Floyd Miles”
  * ![](https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)
Kristen Ramos
kristen.ramos@example.com
  * ![](https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)
Floyd Miles
floyd.miles@example.com
  * ![](https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)
Courtney Henry
courtney.henry@example.com


```
<ul role="list" class="space-y-4 [&>*]:rounded-lg [&>*]:bg-white [&>*]:p-4 [&>*]:shadow hover:[&>li:nth-child(2)>div>p:first-child]:text-indigo-500"> <!-- ... --> <li class="flex">  <img class="h-10 w-10 rounded-full" src="..." alt="" />  <div class="ml-3 overflow-hidden">   <p class="text-sm font-medium text-slate-900">Floyd Miles</p>   <p class="truncate text-sm text-slate-500">floyd.miles@example.com</p>  </div> </li> <!-- ... --></ul>
```

Now _should_ you do this? Probably not very often, but honestly it can be a pretty useful escape hatch when trying to style HTML you can't directly change. It's a sharp knife, but the best chefs aren't preparing food with safety scissors.
Play with them a bit and I'll bet you find they are a great tool when the situation calls for it. We're using them in a couple of tricky spots in these new website templates we're working on and the experience is much nicer than creating a custom class.
So that's Tailwind CSS v3.1! It's only a minor version change, so there are no breaking changes and you should be able to update your project by just installing the latest version:
```
npm install tailwindcss@latest
```

For the complete list of changes including bug fixes and a few minor improvements I didn't talk about here, dig in to the [release notes](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.1.0) on GitHub.
I've already got a bunch of ideas for Tailwind CSS v3.2 _(maybe even text shadows finally?!)_ , but right now we're working hard to push these new [website templates](https://tailwindcss.com/blog/2022-05-23-headless-ui-v1-6-tailwind-ui-team-management#tailwind-css-templates-are-coming-soon) over the finish line. Look for another update on that topic in the next week or two!
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

