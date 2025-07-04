---
url: https://tailwindcss.com/blog/tailwindcss-1-6
scraped_at: 2025-05-25T08:34:19.479748
title: Tailwind CSS v1.6.0 - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
July 28, 2020
# Tailwind CSS v1.6.0
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
It's like Tailwind CSS v1.5 except now there's animation support, overscroll utilities, and more!
There aren't supposed to be any breaking changes here, but I thought that [last time](https://github.com/tailwindlabs/tailwindcss/releases/tag/v1.5.0) too. If I _did_ break something, first person to report it gets a Tailwind shirt.
## [New features](https://tailwindcss.com/blog/tailwindcss-1-6#new-features)
### [Animation support](https://tailwindcss.com/blog/tailwindcss-1-6#animation-support)
Tailwind CSS v1.6 adds a brand new `animation` core plugin, with 4 general purpose animations included out of the box:
  * `animate-spin`
  * `animate-ping`
  * `animate-pulse`
  * `animate-bounce`


```
<button type="button" class="bg-indigo-600 ..." disabled> <svg class="mr-3 h-5 w-5 animate-spin ..." viewBox="0 0 24 24">  <!-- ... --> </svg> Processing</button>
```

These are completely customizable as always, using the `animation` and `keyframes` sections of your `tailwind.config.js` theme:
```
module.exports = { theme: {  extend: {   animation: {    wiggle: "wiggle 1s ease-in-out infinite",   },   keyframes: {    wiggle: {     "0%, 100%": { transform: "rotate(-3deg)" },     "50%": { transform: "rotate(3deg)" },    },   },  }, },};
```

For more information and a live demo, [read the new animation documentation](https://v1.tailwindcss.com/docs/animation). For behind the scenes details about the design rationale, [check out the pull request](https://github.com/tailwindlabs/tailwindcss/pull/2068).
### [New `prefers-reduced-motion` variants](https://tailwindcss.com/blog/tailwindcss-1-6#new-prefers-reduced-motion-variants)
To go along with the new animation features, we've also added new `motion-safe` and `motion-reduce` variants that allow you to conditionally apply CSS based on the [`prefers-reduced-motion` media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion).
These can be useful in conjunction with transition and animation utilities to disable problematic motion for users who are sensitive to it:
```
<div class="transition duration-150 ease-in-out motion-reduce:transition-none ... ..."></div>
```

...or to explicitly opt-in to motion to make sure it's only being shown to users who haven't opted out:
```
<div class="duration-150 ease-in-out motion-safe:transition ... ..."></div>
```

These can be combined with responsive variants and pseudo-class variants as well:
```
<!-- With responsive variants --><div class="sm:motion-reduce:translate-y-0"></div><!-- With pseudo-class variants --><div class="motion-reduce:hover:translate-y-0"></div><!-- With responsive and pseudo-class variants --><div class="sm:motion-reduce:hover:translate-y-0"></div>
```

These are currently not enabled for any utilities by default, but you can enabled them as needed in the `variants` section of your `tailwind.config.js` file:
```
module.exports = { // ... variants: {  translate: ["responsive", "hover", "focus", "motion-safe", "motion-reduce"], },};
```

For more details, check out [the updated variants documentation](https://v1.tailwindcss.com/docs/pseudo-class-variants).
### [New `overscroll-behavior` utilities](https://tailwindcss.com/blog/tailwindcss-1-6#new-overscroll-behavior-utilities)
We've also added new utilities for the [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior) property.
You can use these utilities to control how "scroll chaining" works in your sites, and avoid scrolling the whole page when you reach the top or bottom of an embedded scrollable area.
```
<div class="overscroll-y-contain ..."> <!-- ... --></button>
```

Note that this is currently **not supported in Safari** , but in my opinion it's not a huge deal to treat this as a progressive enhancement anyways, since it falls back fairly gracefully.
This plugin can be configured in your `tailwind.config.js` file as `overscrollBehavior`:
```
module.exports = { // ... // Disabling the plugin corePlugins: {  overscrollBehavior: false, }, // Customizing the enabled variants variants: {  overscrollBehavior: ["responsive", "hover"], },};
```

### [Generate your CSS without an input file](https://tailwindcss.com/blog/tailwindcss-1-6#generate-your-css-without-an-input-file)
If you never write any custom CSS and you're sick of creating this file all the time...
```
@tailwind base;@tailwind components;@tailwind utilities;
```

...then I've got news for you baby — if you're using our `tailwindcss` CLI tool you can start depositing those 58 characters into your savings account instead of wasting them on a pointless CSS file.
The input file argument is now optional in the CLI tool, so if you don't actually _need_ a custom CSS file, you can just write this:
```
npx tailwindcss build -o compiled.css
```

Your kids are going to be so grateful for the extra time you get to spend together.
Want to talk about this post? [Discuss this on GitHub →](https://github.com/tailwindcss/tailwindcss/discussions/2088)
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

