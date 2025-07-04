---
url: https://tailwindcss.com/blog/automatic-class-sorting-with-prettier
scraped_at: 2025-05-25T08:45:14.418085
title: Automatic Class Sorting with Prettier - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
January 24, 2022
# Automatic Class Sorting with Prettier
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freinink.dd880af3.jpg&w=96&q=75)
Jonathan Reinink
[@reinink](https://twitter.com/reinink)
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
[![Tailwind CSS v3.4](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner.79c40690.jpg&w=3840&q=75)](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)
People have been talking about the best way to sort your utility classes in Tailwind projects for [at least four years](https://github.com/tailwindlabs/discuss/issues/97). Today we're excited to announce that you can finally stop worrying about it with the release of our official [Prettier plugin for Tailwind CSS](https://github.com/tailwindlabs/prettier-plugin-tailwindcss).
This plugin scans your templates for class attributes containing Tailwind CSS classes, and then sorts those classes automatically following our [recommended class order](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#how-classes-are-sorted).
```
<!-- Before --><button class="text-white px-4 sm:px-8 py-2 sm:py-3 bg-sky-700 hover:bg-sky-800">...</button><!-- After --><button class="bg-sky-700 px-4 py-2 text-white hover:bg-sky-800 sm:px-8 sm:py-3">...</button>
```

It works seamlessly with custom Tailwind configurations, and because it's just a [Prettier](https://prettier.io/) plugin, it works anywhere Prettier works — including every popular editor and IDE, and of course on the command line.
To get started, install `prettier-plugin-tailwindcss` as a dev-dependency:
```
npm install -D prettier prettier-plugin-tailwindcss
```

Then add the plugin to your [Prettier configuration file](https://prettier.io/docs/en/configuration):
```
{ "plugins": ["prettier-plugin-tailwindcss"]}
```

You can also [load the plugin by using the `--plugin` flag with the Prettier CLI, or by using the `plugins` option with the Prettier API](https://prettier.io/docs/en/plugins.html#using-plugins).
## [How classes are sorted](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#how-classes-are-sorted)
At its core, all this plugin does is organize your classes in the same order that Tailwind orders them in your CSS.
This means that any classes in the base layer will be sorted first, followed by classes in the components layer, and then finally classes in the utilities layer.
```
<!-- `container` is a component so it comes first --><div class="container mx-auto px-6"> <!-- ... --></div>
```

Utilities themselves are sorted in the same order we sort them in the CSS as well, which means that any classes that override other classes always appear later in the class list:
```
<div class="pt-2 p-4"><div class="p-4 pt-2">  <!-- ... --> </div></div>
```

The actual order of the different utilities is loosely based on the box model, and tries to put high impact classes that affect the layout at the beginning and decorative classes at the end, while also trying to keep related utilities together:
```
<div class="text-gray-700 shadow-md p-3 border-gray-300 ml-4 h-24 flex border-2"><div class="ml-4 flex h-24 border-2 border-gray-300 p-3 text-gray-700 shadow-md">  <!-- ... --> </div></div>
```

Modifiers like `hover:` and `focus:` are grouped together and sorted after any plain utilities:
```
<div class="hover:opacity-75 opacity-50 hover:scale-150 scale-125"><div class="scale-125 opacity-50 hover:scale-150 hover:opacity-75">  <!-- ... --> </div></div>
```

Responsive modifiers like `md:` and `lg:` are grouped together at the end in the same order they're configured in your theme — which is smallest to largest by default:
```
<div class="lg:grid-cols-4 grid sm:grid-cols-3 grid-cols-2"><div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4">  <!-- ... --> </div></div>
```

Any custom classes that don't come from Tailwind plugins (like classes for targeting a third-party library) are always sorted to the front, so it's easy to see when an element is using them:
```
<div class="p-3 shadow-xl select2-dropdown"><div class="select2-dropdown p-3 shadow-xl">  <!-- ... --> </div></div>
```

## [Customization](https://tailwindcss.com/blog/automatic-class-sorting-with-prettier#customization)
We think [Prettier gets it right](https://prettier.io/docs/en/option-philosophy.html) when it comes to being opinionated and offering little in terms of customizability — at the end of the day the biggest benefit to sorting your classes is that it's just one less thing to argue with your team about.
We've tried really hard to come up with a sort order that is easy to understand and communicates the most important information as fast as possible.
The plugin _will_ respect your `tailwind.config.js` file and work with any Tailwind plugins you've installed, but **there is no way to change the sort order**. Just like with Prettier, we think that the benefits of auto-formatting will quickly outweigh any stylistic preferences you have and that you'll get used to it pretty fast.
Ready to try it out? [Check out the full documentation on GitHub →](https://github.com/tailwindlabs/prettier-plugin-tailwindcss)
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

