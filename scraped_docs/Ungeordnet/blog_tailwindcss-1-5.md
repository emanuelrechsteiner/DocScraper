---
url: https://tailwindcss.com/blog/tailwindcss-1-5
scraped_at: 2025-05-25T09:00:00.118351
title: Tailwind CSS v1.5.0 - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
July 15, 2020
# Tailwind CSS v1.5.0
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
I was hoping to save v1.5.0 for something _really_ exciting but we needed a new feature to support the new [`@tailwindcss/typography`](https://github.com/tailwindcss/typography) plugin so h*ck it, we're dropping some new stuff on you early.
No breaking changes, this is a minor release and we're professionals you silly goose.
## [New features](https://tailwindcss.com/blog/tailwindcss-1-5#new-features)
### [Component `variants` support](https://tailwindcss.com/blog/tailwindcss-1-5#component-variants-support)
Until Tailwind CSS v1.5.0, only "utility" classes were really intended to be used with `variants` (like "responsive", "hover", "focus", etc.)
While these are still much more useful for utilities than any other type of class, we now support generating variants for component classes as well, like the `prose` classes in the new `@tailwindcss/typography` plugin:
```
<article class="prose md:prose-lg"> <!-- Content --></article>
```

You can take advantage of this feature in your own component classes by using the new `variants` option in the second argument of the `addComponents` plugin API:
```
plugin(function ({ addComponents })) { addComponents({  '.card': {   // ...  } }, {  variants: ['responsive'] })})
```

...or using the array shorthand you might be familiar with from the `addUtilities` API:
```
plugin(function ({ addComponents })) { addComponents({  '.card': {   // ...  } }, ['responsive'])})
```

To take advantage of these feature in your custom CSS (rather than using the plugin API), you can use a new `@layer` directive to explicitly tell Tailwind that your styles belong to the "components" bucket:
```
@layer components { @responsive {  .card {   /* ... */  } }}
```

This helps Tailwind purge your unused CSS correctly, ensuring it doesn't remove any responsive component variants when using the default "conservative" purge mode.
### [Responsive `container` variants](https://tailwindcss.com/blog/tailwindcss-1-5#responsive-container-variants)
Piggy-backing off of the new component `variants` support, the `container` class now supports variants!
```
<!-- Only lock the width at `md` sizes and above --><div class="md:container"> <!-- ... --></div>
```

We've enabled responsive variants by default, but if you are sick in the head you can also manually enable other variants like `focus`, `group-hover`, whatever:
```
module.exports = { // ... variants: {  container: ["responsive", "focus", "group-hover"], },};
```

### [New `focus-visible` variant](https://tailwindcss.com/blog/tailwindcss-1-5#new-focus-visible-variant)
We've added support for the [`:focus-visible` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible) using a new `focus-visible` variant.
This is super useful for adding focus styles that _only_ appear to keyboard users, and are ignored for mouse users:
```
<button class="focus-visible:shadow-outline focus-visible:outline-none ...">Click me</button>
```

It's not enabled for anything by default, but you can enable it in the `variants` section of your config file:
```
module.exports = { // ... variants: {  backgroundColor: ["responsive", "hover", "focus", "focus-visible"], },};
```

Browser support is still pretty weak on this but getting better. In the mean time, check out the [polyfill](https://github.com/WICG/focus-visible) and corresponding [PostCSS plugin](https://github.com/csstools/postcss-focus-visible) if you'd like to use this in all browsers right away.
### [New `checked` variant](https://tailwindcss.com/blog/tailwindcss-1-5#new-checked-variant)
We've added a new `checked` variant you can use to conditionally style things like checkboxes and radio buttons:
```
<input type="checkbox" class="bg-white checked:bg-blue-500" />
```

It's not enabled for anything by default, but you can enable it in the `variants` section of your config file:
```
module.exports = { // ... variants: {  backgroundColor: ["responsive", "hover", "focus", "checked"], },};
```

Want to talk about this post? [Discuss this on GitHub →](https://github.com/tailwindcss/tailwindcss/discussions/2033)
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

