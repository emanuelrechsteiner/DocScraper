---
url: https://tailwindcss.com/blog/tailwindcss-v3-2
scraped_at: 2025-05-25T08:52:00.788631
title: Tailwind CSS v3.2: Dynamic breakpoints, multi-config, and container queries, oh my! - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
October 19, 2022
# Tailwind CSS v3.2: Dynamic breakpoints, multi-config, and container queries, oh my!
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
![Tailwind CSS v3.2](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcard.65ec124d.jpg&w=3840&q=75)
Tailwind CSS v3.2 is here with an absolutely _massive_ amount of new stuff, including support for dynamic breakpoints, multiple config files in a single project, nested groups, parameterized variants, container queries, and more.
As always check out the [release notes](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.2.0) for every nitty-gritty fix and improvement, but here's the highlight reel:
  * [Multiple config files in one project using `@config`](https://tailwindcss.com/blog/tailwindcss-v3-2#multiple-config-files-in-one-project-using-config)
  * [Browser-support-based styling with `supports-*`](https://tailwindcss.com/blog/tailwindcss-v3-2#browser-support-based-styling-with-supports)
  * [ARIA attribute variants](https://tailwindcss.com/blog/tailwindcss-v3-2#aria-attribute-variants)
  * [Data attribute variants](https://tailwindcss.com/blog/tailwindcss-v3-2#data-attribute-variants)
  * [Max-width and dynamic breakpoints](https://tailwindcss.com/blog/tailwindcss-v3-2#max-width-and-dynamic-breakpoints)
  * [Dynamic `group-*` and `peer-*` variants](https://tailwindcss.com/blog/tailwindcss-v3-2#dynamic-group-and-peer-variants)
  * [Dynamic variants with `matchVariant`](https://tailwindcss.com/blog/tailwindcss-v3-2#dynamic-variants-with-match-variant)
  * [Nested `group` and multiple `peer` support using variant modifiers](https://tailwindcss.com/blog/tailwindcss-v3-2#nested-group-and-multiple-peer-support-using-variant-modifiers)
  * [Container queries](https://tailwindcss.com/blog/tailwindcss-v3-2#container-queries)


Upgrade your projects by installing the latest version of `tailwindcss` from npm:
```
npm install -D tailwindcss@latest
```

Or play with the new features in [Tailwind Play](https://play.tailwindcss.com) where you can try everything out instantly, right in the browser.
## [Multiple config files in one project using @config](https://tailwindcss.com/blog/tailwindcss-v3-2#multiple-config-files-in-one-project-using-config)
We've added a new `@config` directive that you can use in a CSS file to specify which Tailwind CSS config to use for that file:
./styles/admin.css
./styles/client.css
```
@config "./tailwind.admin.config.js";@tailwind base;@tailwind components;@tailwind utilities;
```

This makes it a lot easier to build multiple stylesheets in a single project that have separate Tailwind configurations. For example, you might have one config file for the customer-facing part of your site, and another config for the admin/backend area.
You've always technically been able to do this with enough webpack wizardry, but the new `@config` directive makes it super easy and accessible to everyone, even in projects where you don't have as much control over the build tool configuration.
## [Browser-support-based styling with supports-*](https://tailwindcss.com/blog/tailwindcss-v3-2#browser-support-based-styling-with-supports-)
You can now conditionally style things based on whether a certain feature is supported in the user's browser with the `supports-[...]` variant, which generates [@supports rules](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports) under the hood.
```
<div class="flex supports-[display:grid]:grid ..."> <!-- ... --></div>
```

The `supports-[...]` variant takes anything you'd use with `@supports (...)` between the square brackets, like a property/value pair, and even expressions using `and` and `or`.
If you only need to check if a property itself is supported, you can even just specify the property name and Tailwind will fill in the blanks for you:
```
<div class="bg-black/75 supports-[backdrop-filter]:bg-black/25supports-[backdrop-filter]:backdrop-blur ..."> <!-- ... --></div>
```

## [ARIA attribute variants](https://tailwindcss.com/blog/tailwindcss-v3-2#aria-attribute-variants)
You can now conditionally style things based on [ARIA attributes](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes) with the new `aria-*` variants.
For example, you can update the background color of an element based on whether the `aria-checked` state is `true`:
```
<span class="bg-gray-600 aria-checked:bg-blue-600" aria-checked="true" role="checkbox"> <!-- ... --></span>
```

By default we've included modifiers for the most common boolean ARIA attributes:
Modifier| CSS  
---|---  
`aria-checked`| `&[aria-checked="true"]`  
`aria-disabled`| `&[aria-disabled="true"]`  
`aria-expanded`| `&[aria-expanded="true"]`  
`aria-hidden`| `&[aria-hidden="true"]`  
`aria-pressed`| `&[aria-pressed="true"]`  
`aria-readonly`| `&[aria-readonly="true"]`  
`aria-required`| `&[aria-required="true"]`  
`aria-selected`| `&[aria-selected="true"]`  
You can customize which `aria-*` modifiers are available by editing `theme.aria` or `theme.extend.aria` in your `tailwind.config.js` file:
tailwind.config.js
```
module.exports = { theme: {  extend: {   aria: {    asc: 'sort="ascending"',    desc: 'sort="descending"',   },  }, },};
```

If you need to use a one-off `aria` modifier that doesn’t make sense to include in your theme, or for more complex ARIA attributes that take specific values, use square brackets to generate a property on the fly using any arbitrary value.
Invoice #| Client| Amount  
---|---|---  
#100| Pendant Publishing| $2,000.00  
#101| Kruger Industrial Smoothing| $545.00  
#102| J. Peterman| $10,000.25  
HTML
Generated CSS
```
<table> <thead>  <tr>   <th    aria-sort="ascending"    class="aria-[sort=ascending]:bg-[url('/img/down-arrow.svg')]aria-[sort=descending]:bg-[url('/img/up-arrow.svg')]"   >    Invoice #   </th>   <!-- ... -->  </tr> </thead> <!-- ... --></table>
```

ARIA state modifiers can also target parent and sibling elements using the `group-aria-*` and `peer-aria-*` modifiers:
HTML
Generated CSS
```
<table> <thead>  <tr>   <th aria-sort="ascending" class="group">    Invoice #    <svg     class="group-aria-[sort=ascending]:rotate-0group-aria-[sort=descending]:rotate-180"    >     <!-- ... -->    </svg>   </th>   <!-- ... -->  </tr> </thead> <!-- ... --></table>
```

## [Data attribute variants](https://tailwindcss.com/blog/tailwindcss-v3-2#data-attribute-variants)
You can now conditionally style things based on [data attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes) with the new `data-*` variants.
Since there are no standard `data-*` attributes by definition, we only support arbitrary values out of the box, for example:
```
<!-- Will apply --><div data-size="large" class="data-[size=large]:p-8"> <!-- ... --></div><!-- Will not apply --><div data-size="medium" class="data-[size=large]:p-8"> <!-- ... --></div><!-- Generated CSS --><style> .data-\[size\=large\]\:p-8[data-size="large"] {  padding: 2rem; }</style>
```

You can configure shortcuts for common data attribute selectors you're using in your project under the `data` key in the `theme` section of your `tailwind.config.js` file:
```
// tailwind.config.jsmodule.exports = { theme: {  data: {   checked: 'ui~="checked"',  }, }, // ...};
```

```
<div data-ui="checked active" class="data-checked:underline"> <!-- ... --></div>
```

These variants also work as `group-*` and `peer-*` variants like many other variants in the framework:
```
<div data-size="large" class="group"> <div class="group-data-[size=large]:p-8">  <!-- Will apply `p-8` --> </div></div><div data-size="medium" class="group"> <div class="group-data-[size=large]:p-8">  <!-- Will not apply `p-8` --> </div></div>
```

## [Max-width and dynamic breakpoints](https://tailwindcss.com/blog/tailwindcss-v3-2#max-width-and-dynamic-breakpoints)
We've added a new `max-*` variant that lets you apply max-width media queries based on your configured breakpoints:
```
<div class="max-lg:p-8"> <!-- Will apply `p-8` until the `lg` breakpoint kicks in --></div>
```

As a general rule I would still recommend using min-width breakpoints personally, but this feature does unlock one useful workflow benefit which is not having to _undo_ some style at a different breakpoint.
For example, without this feature you often end up doing things like this:
```
<div class="md:sr-only xl:not-sr-only"> <!-- ... --></div>
```

With this feature, you can avoid undoing that style by stacking a `max-*` variant on the original declaration:
```
<div class="md:max-xl:sr-only"> <!-- ... --></div>
```

Along with this, we've added support for arbitrary values, and a new `min-*` variant that only accepts arbitrary values, so you can do things like this:
```
<div class="min-[712px]:max-[877px]:right-16 ..."> <!-- ... --></div>
```

It's important to note that **these features will only be available if your project uses a simple`screens` configuration.**
These features are a lot more complicated than they look due to needing to ensure that all of these media queries are sorted in the final CSS in a way that gives you the expected behavior in the browser. So for now, they will only work if your `screens` configuration is a simple object with string values, like the default configuration:
```
// tailwind.config.jsmodule.exports = { theme: {  screens: {   sm: "640px",   md: "768px",   lg: "1024px",   xl: "1280px",   "2xl": "1536px",  }, },};
```

If you have a complex configuration where you already have `max-width` breakpoints defined, or range-based media queries, or _anything_ other than just strings, these features won't be available. We might be able to figure that out in the future but it just creates so many questions about how the CSS should be ordered that we don't have answers for yet.
So for now (and possibly forever), if you want to use these features, your `screens` configuration needs to be simple. My hope is that these features make complex `screens` configurations unnecessary anyways.
## [Dynamic group-* and peer-* variants](https://tailwindcss.com/blog/tailwindcss-v3-2#dynamic-group-and-peer-variants)
It's now possible to create custom `group-*` and `peer-*` variants on the fly by passing your own selector to be "groupified" or "peerified" between square brackets:
HTML
Generated CSS
```
<div class="group is-published"> <div class="group-[.is-published]:block hidden">Published</div></div>
```

For more control, you can use the `&` character to mark where `.group` or `.peer` should end up in the final selector relative to the selector you are passing in:
HTML
Generated CSS
```
<div> <input type="text" class="peer" /> <div class="peer-[:nth-of-type(3)_&]:block hidden">  <!-- ... --> </div></div>
```

Let's be serious you're probably going to use these features like three times in your entire life but it's still pretty cool. Hoping we can use this as a building block to make `group` and `peer` work more automatically with variants registered by third-party plugins in the future.
## [Dynamic variants with matchVariant](https://tailwindcss.com/blog/tailwindcss-v3-2#dynamic-variants-with-matchvariant)
You've probably noticed this new `variant-[...]` syntax in a lot of these new features — this is all powered by a new `matchVariant` plugin API that makes it possible to create what we're calling "dynamic variants".
Here's an example of creating a `placement-*` variant for some imaginary tooltip library that uses a `data-placement` attribute to tell you where the tooltip is currently positioned:
```
let plugin = require("tailwindcss/plugin");module.exports = { // ... plugins: [  plugin(function ({ matchVariant }) {   matchVariant(    "placement",    (value) => {     return `&[data-placement=${value}]`;    },    {     values: {      t: "top",      r: "right",      b: "bottom",      l: "left",     },    },   );  }), ],};
```

The variant defined above would give you variants like `placement-t` and `placement-b`, but would also support the arbitrary portion in square brackets, so if this imaginary tooltip library had other potential values that you didn't feel the need to create built-in values for, you could still do stuff like this:
```
<div class="placement-[top-start]:mb-2 ..."> <!-- ... --></div>
```

When defining a custom variant with this API, it's often important that you have some control over which order the CSS is generated in to make sure each class has the right precedence with respect to other values that come from the same variant. To support this, there's a `sort` function you can provide when defining your variant:
```
matchVariant("min", (value) => `@media (min-width: ${value})`, { sort(a, z) {  return parseInt(a) - parseInt(z); },});
```

## [Nested group and multiple peer support using variant modifiers](https://tailwindcss.com/blog/tailwindcss-v3-2#nested-group-and-multiple-peer-support-using-variant-modifiers)
Sometimes you can run into problems when you have multiple `group` chunks nested within each other because Tailwind has no real way to disambiguate between them.
To solve this, we're adding support for _variant modifiers_ , which are a new dynamic chunk that you can add to the end of a variant (inspired by our optional opacity modifier syntax) that you can use to give each group/peer your own identifier.
Here's what it looks like:
```
<div class="group/sidebar ..."> <!-- ... --> <div class="group/navitem ...">  <a href="#" class="opacity-50 group-hover/navitem:bg-black/75group-hover/sidebar:opacity-75">   <!-- ... -->  </a> </div> <!-- ... --></div>
```

This lets you give each group a clear name that makes sense for that context on the fly, and Tailwind will generate the necessary CSS to make it work.
I'm really excited to have a solution out there for this because it's something I've been trying to land on a good approach for solving for several years, and this is the first thing we've come up with that really feels like it offers the power and flexibility I think it should.
## [Container queries](https://tailwindcss.com/blog/tailwindcss-v3-2#container-queries)
I can barely believe it but [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Container_Queries) are finally real and the browser support is dangerously close to making these ready for production — in fact if you're building an [Electron](https://www.electronjs.org/) app you could use these today.
Today we're releasing `@tailwindcss/container-queries` which is a new first-party plugin that adds container query support to the framework, using a new `@` syntax to differentiate them from normal media queries:
```
<div class="@container"> <div class="block @lg:flex">  <!-- ... --> </div></div>
```

Out-of-the-box we include a set of container sizes that match our default `max-width` scale:
Name| Value  
---|---  
xs| 20rem  
sm| 24rem  
md| 28rem  
lg| 32rem  
xl| 36rem  
2xl| 42rem  
3xl| 48rem  
4xl| 56rem  
5xl| 64rem  
6xl| 72rem  
7xl| 80rem  
You can configure which values are available using the `containers` key in your `tailwind.config.js` file:
```
// tailwind.config.jsmodule.exports = { theme: {  extend: {   containers: {    "2xs": "16rem",    // etc...   },  }, },};
```

We also include support for arbitrary values, using the `@[...]` syntax:
```
<div class="@container"> <div class="block @[618px]:flex">  <!-- ... --> </div></div>
```

...and named containers using the same variant modifier syntax we're now shipping for `group-*` and `peer-*` variants:
```
<div class="@container/main"> <!-- ... --> <div>  <div class="block @lg/main:flex">   <!-- ... -->  </div> </div></div>
```

Right now we're starting with simple `min-width` based container queries, but we plan to expand the scope over time, and when it feels like we've really nailed the APIs we'll bring it all into core.
For complete documentation, check out the plugin [on GitHub](https://github.com/tailwindlabs/tailwindcss-container-queries).
So there you have it — Tailwind CSS v3.2! Major improvements but just a minor version change, so no breaking changes and you should be able to update your project by just updating your dependency:
```
npm install -D tailwindcss@latest
```

Yeah I hear you in the back, still no text shadows, but hey at least you can style the sibling of a checkbox when the checkbox's parent is the third child in a list without leaving your HTML. Priorities people.
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

