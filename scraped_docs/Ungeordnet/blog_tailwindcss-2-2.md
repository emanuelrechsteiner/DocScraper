---
url: https://tailwindcss.com/blog/tailwindcss-2-2
scraped_at: 2025-05-25T08:42:59.716983
title: Tailwind CSS v2.2 - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
June 17, 2021
# Tailwind CSS v2.2
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
Well I can't say we were really planning on it but over the last few weeks we've been having a ton of fun dumping new and exciting features into Tailwind and now feels like the right time to cut a release, so here it is — Tailwind CSS v2.2!
This has to be one of the most feature-rich Tailwind releases of all-time. Introducing [Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode) back in v2.1 has opened the doors to a lot of cool features we couldn't have easily added otherwise, and this release is loaded with great examples of that.
Here are the highlights:
  * [All-new high-performance Tailwind CLI](https://tailwindcss.com/blog/tailwindcss-2-2#all-new-high-performance-tailwind-cli)
  * [Before and after variants](https://tailwindcss.com/blog/tailwindcss-2-2#before-and-after-variants)
  * [First-letter/line variants](https://tailwindcss.com/blog/tailwindcss-2-2#first-letter-line-variants)
  * [Selected text variants](https://tailwindcss.com/blog/tailwindcss-2-2#selected-text-variants)
  * [List marker variants](https://tailwindcss.com/blog/tailwindcss-2-2#list-marker-variants)
  * [Sibling selector variants](https://tailwindcss.com/blog/tailwindcss-2-2#sibling-selector-variants)
  * [Exhaustive pseudo-class support](https://tailwindcss.com/blog/tailwindcss-2-2#exhaustive-pseudo-class-support)
  * [Shorthand color opacity syntax](https://tailwindcss.com/blog/tailwindcss-2-2#shorthand-color-opacity-syntax)
  * [Extended arbitrary value support](https://tailwindcss.com/blog/tailwindcss-2-2#extended-arbitrary-value-support)
  * [Improved nesting support](https://tailwindcss.com/blog/tailwindcss-2-2#improved-nesting-support)
  * [Caret color utilities](https://tailwindcss.com/blog/tailwindcss-2-2#caret-color-utilities)
  * [Background origin utilities](https://tailwindcss.com/blog/tailwindcss-2-2#background-origin-utilities)
  * [Simplified transform and filter composition](https://tailwindcss.com/blog/tailwindcss-2-2#simplified-transform-and-filter-composition)
  * [Per-side border color utilities](https://tailwindcss.com/blog/tailwindcss-2-2#per-side-border-color-utilities)
  * [Built-in safelist, transform, and extract support](https://tailwindcss.com/blog/tailwindcss-2-2#built-in-safelist-transform-and-extract-support)


For the full details, [check out the release notes](https://github.com/tailwindlabs/tailwindcss/releases/tag/v2.2.0) on GitHub.
It's important to note that although this is a minor release and there are no breaking changes in the classic engine, **Just-in-Time mode is still in preview and v2.2 introduces a few very small changes that might impact you** , so make sure you read through the [changes and deprecations](https://github.com/tailwindlabs/tailwindcss/releases/tag/v2.2.0#changes-and-deprecations) in the release notes when upgrading.
When you're ready to upgrade, just install the latest version from npm and you're off to the races:
```
npm install -D tailwindcss@latest
```

## [All-new high-performance Tailwind CLI](https://tailwindcss.com/blog/tailwindcss-2-2#all-new-high-performance-tailwind-cli)
We've rewritten the Tailwind CLI tool from the ground-up with a performance-first mindset, while also adding support for a bunch of new features.
```
npx tailwindcss -o dist/tailwind.css --watch --jit --purge="./src/**/*.html"
```

Here are some of the highlights:
  * **No installation or configuration necessary** — simply `npx tailwindcss -o output.css` to compile Tailwind from anywhere. You can even enable JIT mode with the `--jit` flag and pass in your content files using the `--purge` option, all without creating a config file.
  * **Watch mode** — so you can automatically rebuild your CSS whenever you make any changes.
  * **JIT performance optimizations** — since our CLI is Tailwind-specific we've been able to make tons of optimizations that make it the absolute fastest build tool for compiling your CSS in JIT mode.
  * **Minification support** — now you can minify your CSS with [cssnano](https://cssnano.co/) just by adding the `--minify` flag.
  * **PostCSS plugin support** — the new CLI will read and respect any extra plugins you configure using a `postcss.config.js` file.


It's fully backwards-compatible with the previous CLI, so if you've got any scripts set up already you should be able to upgrade to v2.2 without making any changes to your scripts.
Check out our [updated Tailwind CLI documentation](https://v2.tailwindcss.com/docs/installation#using-tailwind-cli) to learn more.
_Note that if you were using the`tailwindcss-cli` wrapper package, you can safely switch to `tailwindcss` as we've managed to resolve the peer-dependency issues that forced us to create the wrapper package in the first place._
## [Before and after pseudo-element variants](https://tailwindcss.com/blog/tailwindcss-2-2#before-and-after-pseudo-element-variants)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
People have been asking for this for years and it's finally here! We've added first-party support for styling pseudo-elements like `before` and `after`:
```
<div class="before:block before:bg-blue-500 after:flex after:bg-pink-300"></div>
```

We set `content: ""` automatically any time you use a `before` or `after` variant to make sure the elements are rendered, but you can override it using the new `content` utilities which have full arbitrary value support:
```
<div class="before:block before:content-['hello'] ..."></div>
```

You can even grab the content from an attribute using the CSS `attr()` function:
```
<div before="hello world" class="before:block before:content-[attr(before)] ..."></div>
```

This can be super helpful when your content has spaces in it, since spaces can't be used in CSS class names.
## [First-letter/line variants](https://tailwindcss.com/blog/tailwindcss-2-2#first-letterline-variants)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
We've added variants for the `first-letter` and `first-line` pseudo-elements, so you can do stuff like drop caps:
```
<p class="first-letter:float-left first-letter:text-4xl first-letter:font-bold"> The night was March 31, 1996, and it was finally time for Bret Hart to face off against Shawn Michaels in the long anticipated Iron Man match — a 60 minute war of endurance where the man who scored the most number of falls would walk away as the WWF World Heavyweight Champion.</p>
```

## [Selected text variants](https://tailwindcss.com/blog/tailwindcss-2-2#selected-text-variants)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
We've added a new `selection` variant that makes it super easy to style highlighted to match your design:
```
<p class="selection:bg-pink-200"> After nearly a grueling hour of warfare with neither man scoring a fall, Hart locked in the Sharpshooter, his signature submission hold. As Michaels screamed in pain, the crowd were certain that Hart was about to walk away from WrestleMania XII as the still-World Heavyweight Champion.</p>
```

We've even built this feature in such a way that it can be applied to a parent element and cascade down, so you can set a highlight color for your whole site by applying a utility to the body:
```
<body class="selection:bg-pink-200"> <!-- ... --> <p>  But Michaels didn't give up — he held on until the bell rang and the designated 60 minutes was up. Hart walked away  content, thinking that without a clear winner, the title was his to hold. He was not prepared for what would happen  next, when Gorilla Monsoon declared the match would continue under sudden death rules. </p></body>
```

## [List marker variants](https://tailwindcss.com/blog/tailwindcss-2-2#list-marker-variants)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
You can use the new `marker` variant to style the bullets or numbers at the beginning of a list:
```
<h1>WrestleMania XII Results</h1><ol class="marker:font-medium marker:text-gray-500"> <li>The British Bulldog, Owen Hart, and Vader defeated Ahmed Johnson, Jake Roberts, and Yokozuna</li> <li>Roddy Piper defeated Goldust</li> <li>Stone Cold Steve Austin defeated Savio Vega</li> <li>The Ultimate Warrior defeated Hunter Hearst Helmsley</li> <li>The Undertaker defeated Diesel</li> <li>Shawn Michaels defeated Bret Hart</li></ol>
```

Like the `selection` variant, we've implemented this in a way that it cascades from the parent, so you don't have to repeat it for each list item.
## [Sibling selector variants](https://tailwindcss.com/blog/tailwindcss-2-2#sibling-selector-variants)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
Tailwind CSS v2.2 adds new `peer-*` variants that behave much like the `group-*` variants, but for targeting sibling elements instead of parent elements.
This is useful for things like styling an element when a preceding checkbox is checked, doing things like floating labels, and lots more:
```
<label> <input type="checkbox" class="peer sr-only" /> <span class="h-4 w-4 bg-gray-200 peer-checked:bg-blue-500">  <!-- ... --> </span></label>
```

Just like `group` can be combined with any other variant, `peer` can as well, so you have variants like `peer-hover`, `peer-focus`, `peer-disabled`, and loads more at your fingertips.
The generated CSS uses the [general sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator) and looks like this:
```
.peer:checked ~ .peer-checked\:bg-blue-500 { background-color: #3b82f6;}
```

So just like in vanilla CSS, it will only work for targeting _previous_ siblings, not siblings that appear later in the DOM.
## [Exhaustive pseudo-class support](https://tailwindcss.com/blog/tailwindcss-2-2#exhaustive-pseudo-class-support)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
We've added variants for basically every single missing pseudo-class we could think of in this release:
  * `only` _(only-child)_
  * `first-of-type`
  * `last-of-type`
  * `only-of-type`
  * `target`
  * `default`
  * `indeterminate`
  * `placeholder-shown`
  * `autofill`
  * `required`
  * `valid`
  * `invalid`
  * `in-range`
  * `out-of-range`


Personal favorite in the list is `placeholder-shown` — when combined with the new sibling selector variants it makes it possible to do cool stuff like floating labels:
```
<div class="relative"> <input id="name" class="peer ..." /> <label for="name" class="peer-placeholder-shown:top-4 peer-focus:top-0 ..."> Name </label></div>
```

## [Shorthand color opacity syntax](https://tailwindcss.com/blog/tailwindcss-2-2#shorthand-color-opacity-syntax)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
Instead of using utilities like `bg-opacity-50`, `text-opacity-25`, or `placeholder-opacity-40`, Tailwind CSS v2.2 gives you a new color opacity shorthand you can use to tweak the alpha channel of a color directly in the color utility itself:
```
<div class="bg-red-500 bg-opacity-25"><div class="bg-red-500/25"></div>
```

This means you can now change the opacity of colors anywhere in Tailwind, even where we previously didn’t have specific opacity utilities, like in gradients for example:
```
<div class="bg-gradient-to-r from-red-500/50"></div>
```

The opacity values are taken from your `opacity` scale, but you can also use arbitrary opacity values using square bracket notation:
```
<div class="bg-red-500/[0.31]"></div>
```

If I'm being honest, I am more excited about never having to create another core plugin like `placeholderOpacity.js` for you people again than I am about actually using the feature. And I'm really excited about the feature, so that says something.
## [Extended arbitrary value support](https://tailwindcss.com/blog/tailwindcss-2-2#extended-arbitrary-value-support)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
We've gone over every core plugin in Tailwind to try and add the most flexible arbitrary value support we possibly could, and I think we've covered pretty much everything at this point.
You should be able to use whatever arbitrary values you want, just about wherever you want:
```
<div class="col-start-[73] object-[50%] placeholder-[#aabbcc] ..."></div>
```

If you find one we missed, open an issue and we'll sort it out.
In addition to making arbitrary value support more comprehensive, we've also added a new type-hint syntax to handle ambiguous situations. For example, if you are using a CSS variable as an arbitrary value, it's not always clear what the generated CSS should be:
```
<!-- Is this a font size utility, or a text color utility? --><div class="text-[var(--mystery-var)]"></div>
```

Now you can provide a hint to the engine by prefixing the arbitrary value with the type name:
```
<div class="text-[color:var(--mystery-var)]"></div>
```

Currently, the supported types are:
  * `length`
  * `color`
  * `angle`
  * `list`


We'll probably flesh this out even more over time as people discover new edge cases but this should get you very far.
## [Improved nesting support](https://tailwindcss.com/blog/tailwindcss-2-2#improved-nesting-support)
Since Tailwind introduces a lot of non-standard CSS at-rules like `@tailwind` and `@apply`, you can often run into weird output when combining it with a PostCSS nesting plugin like `postcss-nested` or `postcss-nesting`.
To ease the pain here, we've included a new PostCSS plugin in the `tailwindcss` package that acts as a lightweight compatibility layer between existing nesting plugins and Tailwind itself.
So if you need nesting support in your project, use our plugin, and stick it before Tailwind in your PostCSS plugin list:
```
// postcss.config.jsmodule.exports = { plugins: [  // ...  require("tailwindcss/nesting"),  require("tailwindcss"),  // ... ],};
```

By default, it uses `postcss-nested` under the hood _(since that's what we use to support nesting in Tailwind plugins)_ , but if you'd like to use `postcss-nesting` instead, just call our plugin as a function and pass through the `postcss-nesting` plugin:
```
// postcss.config.jsmodule.exports = { plugins: [  // ...  require("tailwindcss/nesting")(require("postcss-nesting")),  require("tailwindcss"),  // ... ],};
```

Under the hood, this uses a new `screen()` function we've introduced that you can use to get the expanded media expression from any of your configured breakpoints:
```
/* Input */@media screen(sm) { /* ... */}/* Output */@media (min-width: 640px) { /* ... */}
```

You probably won't need to use this yourself but it could be helpful if you're ever integrating Tailwind with another tool that understands `@media` but doesn't handle `@screen` properly.
```
@screen sm {@media screen(sm) { /* ... */}
```

## [Caret color utilities](https://tailwindcss.com/blog/tailwindcss-2-2#caret-color-utilities)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
You can now set the color of the cursor in form fields using the new `caret-{color}` utilities:
```
<input class="caret-red-500" />
```

These are customizable using the `caretColor` key in the `theme` section of your `tailwind.config.js` file.
## [Background origin utilities](https://tailwindcss.com/blog/tailwindcss-2-2#background-origin-utilities)
We've added new utilities for the `background-origin` property, which let you control where an element's background is positioned relative to the element's border, padding box, or content:
```
<div class="border-4 border-dashed bg-origin-border p-4 ..." style="background-image: url(...)"> Background is rendered under the border</div><div class="border-4 border-dashed bg-origin-padding p-4 ..." style="background-image: url(...)"> Background is rendered within the border but on top of any padding</div><div class="border-4 border-dashed bg-origin-content p-4 ..." style="background-image: url(...)"> Background is rendered within any padding and under the content</div>
```

Learn more in the [background origin documentation](https://v2.tailwindcss.com/docs/background-origin).
## [Simplified transform and filter composition](https://tailwindcss.com/blog/tailwindcss-2-2#simplified-transform-and-filter-composition)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
The `transform`, `filter`, and `backdrop-filter` classes are no longer necessary to "enable" their respective set of composable utilities.
```
<div class="transform scale-50 filter grayscale backdrop-filter backdrop-blur-sm"><div class="scale-50 grayscale backdrop-blur-sm"></div>
```

Now those features are automatically enabled any time you use any of the relevant sub-utilities.
It's important to understand though that because these utilities aren't needed anymore, you can no longer expect transforms and filters to be "dormant" by default. If you were relying on conditionally "activating" transforms or filters by toggling these classes, you will want to make sure you are toggling the sub-utilities themselves instead:
```
<div class="scale-105 -translate-y-1 hover:transform"><div class="hover:scale-105 hover:-translate-y-1"></div>
```

I don't expect this will be a real problem for most people, but it's technically a breaking change which is why we've limited this improvement to the JIT engine only.
## [Per-side border color utilities](https://tailwindcss.com/blog/tailwindcss-2-2#per-side-border-color-utilities)
_This feature is only available in[Just-in-Time mode](https://v2.tailwindcss.com/docs/just-in-time-mode)_.
Requested at least once a month for the last four years, I'm excited to share that we've finally added per-side border color support now that we don't have to sweat the development stylesheet size.
```
<div class="border-2 border-t-blue-500 border-r-pink-500 border-b-green-500 border-l-yellow-500"> <!-- ... --></div>
```

Go forth and build ugly websites! _(Kidding, kidding, I know they are useful settle the hell down.)_
## [Built-in safelist, transform, and extract support](https://tailwindcss.com/blog/tailwindcss-2-2#built-in-safelist-transform-and-extract-support)
We've added first-class support for a bunch of important PurgeCSS features and made them work in the JIT engine as well, which doesn't actually even use PurgeCSS.
First is `safelist`, which is super useful if you need to protect specific classes from being removed from your production CSS, perhaps because they are used in content that comes from a database or similar:
```
module.exports = { purge: {  content: ["./src/**/*.html"],  safelist: [   "bg-blue-500",   "text-center",   "hover:opacity-100",   // ...   "lg:text-right",  ], }, // ...};
```

**Note that while the classic engine will accept regular expressions here, the JIT engine will not**. That's because when we're generating classes on demand, the class doesn't exist until it's used so we have nothing to match the expression against. So if you're using just-in-time mode, make sure you're providing complete class names to get the expected result.
Next is `transform`, which lets you transform content for different file extensions before scanning it for potential class names:
```
let remark = require("remark");module.exports = { purge: {  content: ["./src/**/*.{html,md}"],  transform: {   md: (content) => {    return remark().process(content);   },  }, }, // ...};
```

This is really useful if you have templates that are written in a language that compiles to HTML, like Markdown.
Finally we have `extract`, which lets you customize the logic that Tailwind uses to detect class names in specific file types:
```
module.exports = { purge: {  content: ["./src/**/*.{html,md}"],  extract: {   pug: (content) => {    return /[^<>"'`\s]*/.match(content);   },  }, }, // ...};
```

This is an advanced feature and most users won’t need it. The default extraction logic in Tailwind works extremely well for almost all projects.
For more information on these features, check out our [optimizing for production documentation](https://v2.tailwindcss.com/docs/optimizing-for-production).
## [Upgrading](https://tailwindcss.com/blog/tailwindcss-2-2#upgrading)
To upgrade to Tailwind CSS v2.2, install the latest release from npm:
```
npm install -D tailwindcss@latest
```

If you are using the Just-in-Time mode preview, you'll also want to read through the [changes and deprecations](https://github.com/tailwindlabs/tailwindcss/releases/tag/v2.2.0#changes-and-deprecations) in the release notes.
Ready to upgrade? [Get it from npm →](https://npmjs.com/tailwindcss)
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

