---
url: https://www.radix-ui.com/blog/themes-3?tab-nav=account
scraped_at: 2025-06-07T09:42:24.020581
title: Radix Themes 3.0 – Radix UI
---

[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Blog](https://www.radix-ui.com/blog)[](https://github.com/radix-ui)
March 23, 2024
# Radix Themes 3.0
New layout engine, new components, and custom color palette generator.
## [Introduction](https://www.radix-ui.com/blog/themes-3?tab-nav=account#introduction)
Radix Themes 3.0 just landed. This release is a big leap towards making Radix Themes the best component library for building modern apps. We’ll present the main highlights in this post.
For the comprehensive changelog and a migration guide, see the [release notes](https://www.radix-ui.com/themes/docs/overview/releases#300).
## [Custom color palettes](https://www.radix-ui.com/blog/themes-3?tab-nav=account#custom-color-palettes)
Radix Themes comes with almost 30 color scales, each with their own light, dark and alpha variants. Under the hood, the color system is powered by [Radix Colors](https://www.radix-ui.com/colors).
Gray
Gold
Bronze
Brown
Yellow
Amber
Orange
Tomato
Red
Ruby
Crimson
Pink
Plum
Purple
Violet
Iris
Indigo
Blue
Cyan
Teal
Jade
Green
Grass
Lime
Mint
Sky
Every scale has been tuned to provide fully accessible contrast ratios, each with steps that correspond to backgrounds, interactive components, borders and text. Offering the most beautiful and intuitive color system you’ve ever used.
Today, we are introducing a new tool which allows you to create your own brand palette for Radix Themes. It’s a simple interface that lets you specify a primary color, a gray color, and your page background, generating a color configuration to copy-paste into your theme styles.
[![](https://workos.imgix.net/images/4c48334e-feb3-4046-9569-bd695b174728.png?auto=format&fit=clip&q=80)](https://www.radix-ui.com/colors/custom)[Create a custom palette →](https://www.radix-ui.com/colors/custom)
## [New components](https://www.radix-ui.com/blog/themes-3?tab-nav=account#new-components)
Radix Themes 3.0 introduces a number of new components for building dashboards and data-heavy interfaces. They are built and designed with the level of rigor and care that you’ve come to expect from Radix, and as usual, they are accessible to keyboard and screen reader users. Here’s a quick overview of the main highlights.
### [Spinner](https://www.radix-ui.com/blog/themes-3?tab-nav=account#spinner)
Spinner is a simple animated loading indicator:
```

<Spinner />


```

It comes with an intuitive API to conditionally render its children when they are done loading. Consider the following example:
Create workspace
```

// Inside the button:

<Spinner loading={loading}>

<CubeIcon />

</Spinner>


```

The implementation looks effortless—the way it should be. Spinner preserves child dimensions while the data is being fetched, so there is no layout shift between the states. This is an ergonomic way to handle loading states in your app because it minimizes the amount of code branching needed in common situations.
### [Skeleton](https://www.radix-ui.com/blog/themes-3?tab-nav=account#skeleton)
Skeleton is another loading component in this release:
Button
```

<Skeleton>

<Button radius="full">Button</Button>

</Skeleton>


```

Skeleton has a similar API to Spinner, but it also fully adopts the shape and size of child components, so you can build the skeleton interface using exactly the same layout that you’d use in the real one:
### Sign in
Email address
Password
CancelSign in
Toggle loading
### [Segmented Control](https://www.radix-ui.com/blog/themes-3?tab-nav=account#segmented-control)
Segmented Control carries a familiar design for toggle buttons that switch between values:
InboxInboxDraftsDraftsSentSent
Segmented Control packs many details that were crafted to be invisible. For example, a bolder font weight is used on the active item, yet there is no layout shift, and the animation is dialed in so that even the font weight change transitions smoothly. Here’s the same demo slowed down:
InboxInboxDraftsDraftsSentSent
 _Even the font weight change is animated_
### [Data List](https://www.radix-ui.com/blog/themes-3?tab-nav=account#data-list)
[Data List](https://www.radix-ui.com/themes/docs/components/data-list) is a component for displaying a list of key-value pairs: Status
    AuthorizedID
    
`u_2J89JSA4GJ`Name
    Vlad MorozEmail
    vlad@workos.comCompany
    [WorkOS](https://workos.com)
What’s special about Data List? It is a common pattern that is deceptively tricky to get right. We had to put together a [secret page](https://themes-playground-modulz.vercel.app/test-data-list) with all the different layout combinations as we designed for:
  * Values of varied length
  * Consistent rhythm between mixed height items
  * Configurable alignment of the label and value
  * Common layout compositions within
  * Leading trim


### [Reset](https://www.radix-ui.com/blog/themes-3?tab-nav=account#reset)
Unlike others, [Reset](https://www.radix-ui.com/themes/docs/components/reset) is an invisible component:
Button
```

<Reset>

<button>Button</button>

</Reset>


```

Reset removes default browser styles from any HTML tag and sets idiomatic layout defaults so that you can build your custom components on top of it.
In most interfaces, these styles are global and affect the entire app, so that tends to be a compromise between removing as much as possible and retaining common defaults. Reset puts a new spin on the ergonomics of the normalization styles that almost any website needs.
### [Radio Cards](https://www.radix-ui.com/blog/themes-3?tab-nav=account#radio-cards)
[Radio Cards](https://www.radix-ui.com/themes/docs/components/radio-cards) is a common pattern for picking a single value out of multiple. They are used for visually engaging forms where each options gets more weight compared to a regular radio button:
8-core CPU32 GB RAM
6-core CPU24 GB RAM
4-core CPU16 GB RAM
### [Checkbox Cards](https://www.radix-ui.com/blog/themes-3?tab-nav=account#checkbox-cards)
[Checkbox Cards](https://www.radix-ui.com/themes/docs/components/checkbox-cards) are similar to Radio Cards, but are used for picking multiple values:
A1 KeyboardUS Layout
Pro MouseZero-lag wireless
Lightning MatNext-gen charging
### [Progress](https://www.radix-ui.com/blog/themes-3?tab-nav=account#progress)
[Progress](https://www.radix-ui.com/themes/docs/components/progress) is yet another loading component. It can be used to indicate the progress of a task, or use an ambiguous animation to indicate indeterminate progress:
Play again
### [Tab Nav](https://www.radix-ui.com/blog/themes-3?tab-nav=account#tab-nav)
[Tab Nav](https://www.radix-ui.com/themes/docs/components/tab-nav) is a component for navigating to a different view. It complements its lookalike [Tabs](https://www.radix-ui.com/themes/docs/components/tabs) sibling, but it is built on top of the Navigation Menu primitive which provides screen reader accessibility and keyboard navigation tailored to links.
  * [AccountAccount](https://www.radix-ui.com/blog/themes-3?tab-nav=account)
  * [DocumentsDocuments](https://www.radix-ui.com/blog/themes-3?tab-nav=documents)
  * [WorkspaceWorkspace](https://www.radix-ui.com/blog/themes-3?tab-nav=workspace)


## [New layout engine](https://www.radix-ui.com/blog/themes-3?tab-nav=account#new-layout-engine)
A new engine makes layout components and their props more powerful and easier to use.
Layout components are a cornerstone feature of Radix Themes. There are just five of them—[Box](https://www.radix-ui.com/themes/docs/components/box), [Flex](https://www.radix-ui.com/themes/docs/components/flex), [Grid](https://www.radix-ui.com/themes/docs/components/grid), [Section](https://www.radix-ui.com/themes/docs/components/section), and [Container](https://www.radix-ui.com/themes/docs/components/container). These components are used to separate layout responsibilities from content and interactivity. When you separate layout concerns from content and interactivity, the compositions you create are more maintainable and easy to reason about.
These components allow you to quickly add structure to views, pages and other interactive elements within your application.
You can learn more about layout components and their props in the [Layout guide](https://www.radix-ui.com/themes/docs/overview/layout).
### [Better layout props](https://www.radix-ui.com/blog/themes-3?tab-nav=account#better-layout-props)
In this release, layout components have received a number of new props and the values they accept have been significantly reworked:
  * 9 new props for working with flex and grid layouts
  * 4 new props for controlling the dimensions of layout components
  * In addition to [space scale values](https://www.radix-ui.com/themes/docs/theme/spacing), all layout props now accept valid CSS values, including when used with the responsive object syntax.


### [Responsive object syntax](https://www.radix-ui.com/blog/themes-3?tab-nav=account#responsive-object-syntax)
In Radix Themes, _responsive object syntax_ is how you build a responsive layout at different breakpoints without leaving the React code where you compose your app itself.
Consider the following piece of code:
```

<Flex width="500px" />


```

This would create a flexbox layout that’s `500px` wide. But what if you wanted to use a different width on mobile? This is possible using the responsive object syntax, where you can specify the value to use at a particular breakpoint:
```

<Flex width={{ initial: "100%", sm: "300px", md: "500px" }} />


```

Now, in addition to [space scale values](https://www.radix-ui.com/themes/docs/theme/spacing), layout props will support valid CSS values. For example, `100px`, `50vw`, or even expressions like `calc(100vw - 200px)` can be used at specific breakpoints.
However, does it perform well? Does it work with server components? Well, here’s how the above `<Flex>` element gets actually rendered into the DOM:
```

<div
	style={{ "--width": "100%", "--width-md": "500px", "--width-sm": "300px" }}
	class="rt-Flex rt-r-w sm:rt-r-w md:rt-r-w"
/>


```

You can see how that the `<Flex>` element was compiled into a combination of utility classes and CSS custom properties. There is no runtime evaluation of the breakpoints, which means the performance is just like vanilla CSS and the component can be rendered on the server.
### [The best of both worlds](https://www.radix-ui.com/blog/themes-3?tab-nav=account#the-best-of-both-worlds)
Altogether, there are 5 layout components with almost 40 props each. Together they form a system that is easy to learn, quick to master, and sets an _incredibly_ high ceiling of what you can achieve without switching between files and losing momentum.
If you have never used such a system, we’d suggest you give it try. It is a great alternative to Tailwind, which is an incredibly powerful tool originally built for the same purpose—layout. However, today it has evolved into an entire styling paradigm that does not discourage you from creating complex styles on the fly, which can violate the separation of concerns mentioned earlier.
Radix Themes layout comes with the full power that utility class frameworks may provide for layout, but it’s also type-safe and guides the developer in maintaining a clear boundary with the other pieces of the interface that they are building.
### [Standalone layout components](https://www.radix-ui.com/blog/themes-3?tab-nav=account#standalone-layout-components)
If you want to use _just_ the layout component from Radix Themes, that’s also possible. Just make sure that JavaScript tree-shaking works on your side, and import the layout essentials CSS:
```

import "@radix-ui/themes/layout.css";


```

## [Zero config setup with Astro and Remix](https://www.radix-ui.com/blog/themes-3?tab-nav=account#zero-config-setup-with-astro-and-remix)
Radix Themes is now much easier to set up with Remix and Astro. In 3.0, we have revisited the way the library is built to ensure support for ESM environments out of the box.
The distribution is now a hybrid ESM/CommonJS package. Depending on your setup, your import resolver will now pick the right version automatically.
## [Contributors](https://www.radix-ui.com/blog/themes-3?tab-nav=account#contributors)
Radix Themes 3.0 is the result of the hard work of many contributors. We’d like to thank everyone who has contributed to this release, whether through code, documentation, design, or community support.
Special thanks to [Alasdair McLeay](https://github.com/penx), [itsMapleLeaf](https://github.com/itsMapleLeaf), and [Sora Morimoto](https://github.com/smorimoto).
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/blog/themes-3.mdx "Edit this page on GitHub.")
#### In this article
  * [Introduction](https://www.radix-ui.com/blog/themes-3?tab-nav=account#introduction)
  * [Custom color palettes](https://www.radix-ui.com/blog/themes-3?tab-nav=account#custom-color-palettes)
  * [New components](https://www.radix-ui.com/blog/themes-3?tab-nav=account#new-components)
  * [Spinner](https://www.radix-ui.com/blog/themes-3?tab-nav=account#spinner)
  * [Skeleton](https://www.radix-ui.com/blog/themes-3?tab-nav=account#skeleton)
  * [Segmented Control](https://www.radix-ui.com/blog/themes-3?tab-nav=account#segmented-control)
  * [Data List](https://www.radix-ui.com/blog/themes-3?tab-nav=account#data-list)
  * [Reset](https://www.radix-ui.com/blog/themes-3?tab-nav=account#reset)
  * [Radio Cards](https://www.radix-ui.com/blog/themes-3?tab-nav=account#radio-cards)
  * [Checkbox Cards](https://www.radix-ui.com/blog/themes-3?tab-nav=account#checkbox-cards)
  * [Progress](https://www.radix-ui.com/blog/themes-3?tab-nav=account#progress)
  * [Tab Nav](https://www.radix-ui.com/blog/themes-3?tab-nav=account#tab-nav)
  * [New layout engine](https://www.radix-ui.com/blog/themes-3?tab-nav=account#new-layout-engine)
  * [Better layout props](https://www.radix-ui.com/blog/themes-3?tab-nav=account#better-layout-props)
  * [Responsive object syntax](https://www.radix-ui.com/blog/themes-3?tab-nav=account#responsive-object-syntax)
  * [The best of both worlds](https://www.radix-ui.com/blog/themes-3?tab-nav=account#the-best-of-both-worlds)
  * [Standalone layout components](https://www.radix-ui.com/blog/themes-3?tab-nav=account#standalone-layout-components)
  * [Zero config setup with Astro and Remix](https://www.radix-ui.com/blog/themes-3?tab-nav=account#zero-config-setup-with-astro-and-remix)
  * [Contributors](https://www.radix-ui.com/blog/themes-3?tab-nav=account#contributors)



