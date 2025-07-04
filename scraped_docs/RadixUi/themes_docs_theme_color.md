---
url: https://www.radix-ui.com/themes/docs/theme/color
scraped_at: 2025-06-07T09:33:45.113003
title: Color – Radix Themes
---

[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Documentation](https://www.radix-ui.com/themes/docs/overview/getting-started)[Playground](https://www.radix-ui.com/themes/playground)[Blog](https://www.radix-ui.com/blog)[](https://github.com/radix-ui/themes)
#### Overview
[Getting started](https://www.radix-ui.com/themes/docs/overview/getting-started)[Styling](https://www.radix-ui.com/themes/docs/overview/styling)[Layout](https://www.radix-ui.com/themes/docs/overview/layout)[Releases](https://www.radix-ui.com/themes/docs/overview/releases)[Resources](https://www.radix-ui.com/themes/docs/overview/resources)
#### Theme
[Overview](https://www.radix-ui.com/themes/docs/theme/overview)[Color](https://www.radix-ui.com/themes/docs/theme/color)[Dark mode](https://www.radix-ui.com/themes/docs/theme/dark-mode)[Typography](https://www.radix-ui.com/themes/docs/theme/typography)[Spacing](https://www.radix-ui.com/themes/docs/theme/spacing)[Breakpoints](https://www.radix-ui.com/themes/docs/theme/breakpoints)[Radius](https://www.radix-ui.com/themes/docs/theme/radius)[Shadows](https://www.radix-ui.com/themes/docs/theme/shadows)[Cursors](https://www.radix-ui.com/themes/docs/theme/cursors)
#### Layout
[Box](https://www.radix-ui.com/themes/docs/components/box)[Flex](https://www.radix-ui.com/themes/docs/components/flex)[Grid](https://www.radix-ui.com/themes/docs/components/grid)[Container](https://www.radix-ui.com/themes/docs/components/container)[Section](https://www.radix-ui.com/themes/docs/components/section)
#### Typography
[Text](https://www.radix-ui.com/themes/docs/components/text)[Heading](https://www.radix-ui.com/themes/docs/components/heading)[Blockquote](https://www.radix-ui.com/themes/docs/components/blockquote)[Code](https://www.radix-ui.com/themes/docs/components/code)[Em](https://www.radix-ui.com/themes/docs/components/em)[Kbd](https://www.radix-ui.com/themes/docs/components/kbd)[Link](https://www.radix-ui.com/themes/docs/components/link)[Quote](https://www.radix-ui.com/themes/docs/components/quote)[Strong](https://www.radix-ui.com/themes/docs/components/strong)
#### Components
[Alert Dialog](https://www.radix-ui.com/themes/docs/components/alert-dialog)[Aspect Ratio](https://www.radix-ui.com/themes/docs/components/aspect-ratio)[Avatar](https://www.radix-ui.com/themes/docs/components/avatar)[Badge](https://www.radix-ui.com/themes/docs/components/badge)[Button](https://www.radix-ui.com/themes/docs/components/button)[Callout](https://www.radix-ui.com/themes/docs/components/callout)[Card](https://www.radix-ui.com/themes/docs/components/card)[Checkbox](https://www.radix-ui.com/themes/docs/components/checkbox)[Checkbox Group](https://www.radix-ui.com/themes/docs/components/checkbox-group)[Checkbox Cards](https://www.radix-ui.com/themes/docs/components/checkbox-cards)[Context Menu](https://www.radix-ui.com/themes/docs/components/context-menu)[Data List](https://www.radix-ui.com/themes/docs/components/data-list)[Dialog](https://www.radix-ui.com/themes/docs/components/dialog)[Dropdown Menu](https://www.radix-ui.com/themes/docs/components/dropdown-menu)[Hover Card](https://www.radix-ui.com/themes/docs/components/hover-card)[Icon Button](https://www.radix-ui.com/themes/docs/components/icon-button)[Inset](https://www.radix-ui.com/themes/docs/components/inset)[Popover](https://www.radix-ui.com/themes/docs/components/popover)[Progress](https://www.radix-ui.com/themes/docs/components/progress)[Radio](https://www.radix-ui.com/themes/docs/components/radio)[Radio Group](https://www.radix-ui.com/themes/docs/components/radio-group)[Radio Cards](https://www.radix-ui.com/themes/docs/components/radio-cards)[Scroll Area](https://www.radix-ui.com/themes/docs/components/scroll-area)[Segmented Control](https://www.radix-ui.com/themes/docs/components/segmented-control)[Select](https://www.radix-ui.com/themes/docs/components/select)[Separator](https://www.radix-ui.com/themes/docs/components/separator)[Skeleton](https://www.radix-ui.com/themes/docs/components/skeleton)[Slider](https://www.radix-ui.com/themes/docs/components/slider)[Spinner](https://www.radix-ui.com/themes/docs/components/spinner)[Switch](https://www.radix-ui.com/themes/docs/components/switch)[Table](https://www.radix-ui.com/themes/docs/components/table)[Tabs](https://www.radix-ui.com/themes/docs/components/tabs)[Tab Nav](https://www.radix-ui.com/themes/docs/components/tab-nav)[Text Area](https://www.radix-ui.com/themes/docs/components/text-area)[Text Field](https://www.radix-ui.com/themes/docs/components/text-field)[Tooltip](https://www.radix-ui.com/themes/docs/components/tooltip)
#### Utilities
[Accessible Icon](https://www.radix-ui.com/themes/docs/components/accessible-icon)[Portal](https://www.radix-ui.com/themes/docs/components/portal)[Reset](https://www.radix-ui.com/themes/docs/components/reset)[Slot](https://www.radix-ui.com/themes/docs/components/slot)[Theme](https://www.radix-ui.com/themes/docs/components/theme)[Visually Hidden](https://www.radix-ui.com/themes/docs/components/visually-hidden)
Guides
# Color
Understanding the color system and its application in your theme.
Radix Themes comes with a number of color scales, each with their own light, dark and alpha variants. Under the hood, the color system is powered by [Radix Colors](https://www.radix-ui.com/colors).
## [Accents](https://www.radix-ui.com/themes/docs/theme/color#accents)
Accent color is the most dominant color in your theme. It is used for primary buttons, links and other interactive elements. `accentColor` is specified directly on the [Theme](https://www.radix-ui.com/themes/docs/components/theme) component:
```

<Theme accentColor="indigo">

<MyApp />

</Theme>


```

#### Available accent colors
There is a range of accent colors to choose from:
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
#### Accent scale anatomy
Each accent is a 12-step scale that includes a solid and a transparent variant of each color. For example, here’s the `indigo` color scale:
1
2
3
4
5
6
7
8
9
10
11
12
#### Accent scale tokens
Accent color tokens can be accessed using CSS variables. You can use these tokens to style your custom components, ensuring they are accessible and consistent with the rest of your theme.
```

/* Backgrounds */

var(--accent-1);

var(--accent-2);

/* Interactive components */

var(--accent-3);

var(--accent-4);

var(--accent-5);

/* Borders and separators */

var(--accent-6);

var(--accent-7);

var(--accent-8);

/* Solid colors */

var(--accent-9);

var(--accent-10);

/* Accessible text */

var(--accent-11);

var(--accent-12);

/* Functional colors */

var(--accent-surface);

var(--accent-indicator);

var(--accent-track);

var(--accent-contrast);


```

## [Grays](https://www.radix-ui.com/themes/docs/theme/color#grays)
You can also choose between a pure gray or a number of tinted grays. Your accent color will be automatically paired with a gray shade that compliments it. However, you can also specify a custom `grayColor` directly on the [Theme](https://www.radix-ui.com/themes/docs/components/theme) component:
```

<Theme grayColor="mauve">

<MyApp />

</Theme>


```

#### Available gray colors
There is 6 grays to choose from. The difference may seem subtle, but it is impactful especially on pages with a lot of text or in dense UIs.
Gray
Mauve
Slate
Sage
Olive
Sand
#### Gray scale anatomy
Grays are based on the same 12-step color scale that includes a solid and a transparent variant of each color. For example, here’s the `slate` color scale:
1
2
3
4
5
6
7
8
9
10
11
12
#### Gray scale tokens
Gray color tokens can be accessed using CSS variables. You can use these tokens to style your custom components, ensuring they are accessible and consistent with the rest of your theme.
```

/* Backgrounds */

var(--gray-1);

var(--gray-2);

/* Interactive components */

var(--gray-3);

var(--gray-4);

var(--gray-5);

/* Borders and separators */

var(--gray-6);

var(--gray-7);

var(--gray-8);

/* Solid colors */

var(--gray-9);

var(--gray-10);

/* Accessible text */

var(--gray-11);

var(--gray-12);

/* Functional colors */

var(--gray-surface);

var(--gray-indicator);

var(--gray-track);

var(--gray-contrast);


```

## [Color overrides](https://www.radix-ui.com/themes/docs/theme/color#color-overrides)
When available, the `color` prop on the components can be used to override the theme accent. Nested components will automatically inherit the new accent color.
There are new commits.Refresh
There are new commits.Refresh
```

<Theme accentColor="indigo">

<Flex align="start" direction={{ initial: "column", sm: "row" }} gap="4">

<Callout.Root>

<Callout.Icon>

<InfoCircledIcon />

</Callout.Icon>

<Callout.Text>

<Flex as="span" align="center" gap="4">

<Text>There are new commits.</Text>

<Button variant="surface" size="1" my="-2">

						Refresh

</Button>

</Flex>

</Callout.Text>

</Callout.Root>

<Callout.Root color="gray">

<Callout.Icon>

<InfoCircledIcon />

</Callout.Icon>

<Callout.Text>

<Flex as="span" align="center" gap="4">

<Text>There are new commits.</Text>

<Button variant="surface" size="1" my="-2">

						Refresh

</Button>

</Flex>

</Callout.Text>

</Callout.Root>

</Flex>

</Theme>


```

#### Individual color tokens
Individual colors can be accessed directly using similar CSS variables by their corresponding names. For example, the reds are accessed via `--red-1`, `--red-2`, and so on up to `--red-12`.
## [High contrast](https://www.radix-ui.com/themes/docs/theme/color#high-contrast)
Most of the time, components with a `color` prop also provide a `highContrast` option that achieves appearance that stands out against the page background:
Edit profileEdit profile
```

<Flex gap="4">

<Button variant="classic" color="gray">

		Edit profile

</Button>

<Button variant="classic" color="gray" highContrast>

		Edit profile

</Button>

</Flex>


```

## [Focus and selection](https://www.radix-ui.com/themes/docs/theme/color#focus-and-selection)
Radix Themes automatically adjusts the focus and selection colors depending on the accent color of the current component. Most of the time, setting the `color` prop will intelligently change the focus and selection colors to avoid a mismatch of conflicting hues:
Complete your account setup in [settings](https://www.radix-ui.com/themes/docs/theme/color)Complete your account setup in [settings](https://www.radix-ui.com/themes/docs/theme/color)Complete your account setup in [settings](https://www.radix-ui.com/themes/docs/theme/color)
```

<Theme accentColor="indigo">

<Flex direction="column" gap="4">

<Text>

			Complete your account setup in <Link href="#">settings</Link>

</Text>

<Text color="gray">

			Complete your account setup in <Link href="#">settings</Link>

</Text>

<Text color="red">

			Complete your account setup in <Link href="#">settings</Link>

</Text>

</Flex>

</Theme>


```

#### Focus scale tokens
Focus color tokens can be accessed using CSS variables that follow a similar naming structure like the other scales, e.g. `--focus-1`, `--focus-2`, and so on up to `--focus-12`.
Most of the components use `--focus-8` for the focus outline color.
## [Alpha colors](https://www.radix-ui.com/themes/docs/theme/color#alpha-colors)
Every color has an alpha variant which is designed to appear visually the same when placed over the page background. This is a powerful tool that allows colors to look naturally when overlayed over another background. All numerical color steps have a corresponding alpha variant.
```

/* Solid colors */

var(--red-1);

var(--red-2);

...

var(--red-12);

/* Alpha colors */

var(--red-a1);

var(--red-a2);

...

var(--red-a12);


```

Alpha colors are used automatically within Radix Themes components—no additional configuration is required.
## [Backgrounds](https://www.radix-ui.com/themes/docs/theme/color#backgrounds)
A number of background colors are used to create a sense of visual hierarchy in Radix Themes UIs. These colors are used for backgrounds, cards, and other surfaces.
```

/* Page background */

var(--color-background);

/* Panel backgrounds, such as cards, tables, popovers, dropdown menus, etc. */

var(--color-panel-solid);

var(--color-panel-translucent);

/* Form component backgrounds, such as text fields, checkboxes, select, etc. */

var(--color-surface);

/* Dialog overlays */

var(--color-overlay);


```

### [Panel background](https://www.radix-ui.com/themes/docs/theme/color#panel-background)
The `panelBackground` prop controls whether panelled elements use a solid or a translucent background color. The default `translucent` value creates a subtle overlay effect:
```

<Theme panelBackground="translucent">

<MyApp />

</Theme>


```

### Sign up
Email address
Password[Forgot password?](https://www.radix-ui.com/themes/docs/theme/color)
Create accountSign in
While `solid` is useful when you'd prefer to present information unobstructed.
```

<Theme panelBackground="solid">

<MyApp />

</Theme>


```

### Sign up
Email address
Password[Forgot password?](https://www.radix-ui.com/themes/docs/theme/color)
Create accountSign in
## [Customization](https://www.radix-ui.com/themes/docs/theme/color#customization)
Radix Themes colors can be customized by overriding the corresponding CSS variables of the token system. Refer to the [source code](https://github.com/radix-ui/themes/blob/main/packages/radix-ui-themes/src/styles/tokens/color.css) for the full list of the color tokens.
Make sure that your CSS is applied after the Radix Themes styles so that it takes precedence.
### [Brand color](https://www.radix-ui.com/themes/docs/theme/color#brand-color)
You can replace a specific color with your brand color by remapping the corresponding token. Usually, you’d override **step 9** of the scale that you are using as your theme accent.
```

.radix-themes {

	--my-brand-color: #3052f6;

	--indigo-9: var(--my-brand-color);

	--indigo-a9: var(--my-brand-color);

}


```

In this example, using solid-colored `indigo` components will now reference your custom color.
### [Custom palette](https://www.radix-ui.com/themes/docs/theme/color#custom-palette)
You can use the [custom color palette tool](https://www.radix-ui.com/colors/custom) to generate a custom palette based just on a couple reference colors. Once you are happy with the result, paste the generated CSS into your project. You can rename the generated colors to match the accent that you want to use in your theme.
To generate dark theme colors, toggle the appearance to use the dark theme. Make sure to paste the generated CSS after your light theme color overrides.
[![](https://workos.imgix.net/images/4c48334e-feb3-4046-9569-bd695b174728.png?auto=format&fit=clip&q=80)](https://www.radix-ui.com/colors/custom)[Create a custom palette →](https://www.radix-ui.com/colors/custom)
### [Color aliasing](https://www.radix-ui.com/themes/docs/theme/color#color-aliasing)
You may prefer to use generic color names to refer to the color shades that you want to use. For example, it is common to refer to `crimson`, `jade`, and `indigo` as `red`, `green`, and `blue` respectively.
In this case, you can remap Radix Themes tokens in place of one another and reclaim the color names you want to use:
```

.radix-themes {

	--red-1: var(--ruby-1);

	--red-2: var(--ruby-2);

	--red-3: var(--ruby-3);

	--red-4: var(--ruby-4);

	--red-5: var(--ruby-5);

	--red-6: var(--ruby-6);

	--red-7: var(--ruby-7);

	--red-8: var(--ruby-8);

	--red-9: var(--ruby-9);

	--red-10: var(--ruby-10);

	--red-11: var(--ruby-11);

	--red-12: var(--ruby-12);

	--red-a1: var(--ruby-a1);

	--red-a2: var(--ruby-a2);

	--red-a3: var(--ruby-a3);

	--red-a4: var(--ruby-a4);

	--red-a5: var(--ruby-a5);

	--red-a6: var(--ruby-a6);

	--red-a7: var(--ruby-a7);

	--red-a8: var(--ruby-a8);

	--red-a9: var(--ruby-a9);

	--red-a10: var(--ruby-a10);

	--red-a11: var(--ruby-a11);

	--red-a12: var(--ruby-a12);

	--red-surface: var(--ruby-surface);

	--red-indicator: var(--ruby-indicator);

	--red-track: var(--ruby-track);

	--red-contrast: var(--ruby-contrast);

}


```

In this example, using the `red` color in Radix Themes components and tokens would now reference the original `ruby` scale.
## [Individual CSS files](https://www.radix-ui.com/themes/docs/theme/color#individual-css-files)
Color definitions comprise around 20% of the total CSS size that Radix Themes ships with.
If you’d prefer to reduce your CSS bundle size and have access just to the colors you use, you can import the individual CSS files for each color module. Here’s a sample setup:
```

// Base theme tokens

import "@radix-ui/themes/tokens/base.css";

// Include just the colors you use, for example `ruby`, `teal`, and `slate`.

// Remember to import the gray tint that matches your theme setting.

import "@radix-ui/themes/tokens/colors/ruby.css";

import "@radix-ui/themes/tokens/colors/teal.css";

import "@radix-ui/themes/tokens/colors/slate.css";

// Rest of the CSS

import "@radix-ui/themes/components.css";

import "@radix-ui/themes/utilities.css";


```

Please note that the colors you didn’t import will still be accepted by the `color` prop in React. Also, make sure that your developer tooling [preserves](https://www.radix-ui.com/themes/docs/overview/styling#nextjs-import-order) the order of the imported CSS files.
#### Quick nav
  * [Accents](https://www.radix-ui.com/themes/docs/theme/color#accents)
  * [Grays](https://www.radix-ui.com/themes/docs/theme/color#grays)
  * [Color overrides](https://www.radix-ui.com/themes/docs/theme/color#color-overrides)
  * [High contrast](https://www.radix-ui.com/themes/docs/theme/color#high-contrast)
  * [Focus and selection](https://www.radix-ui.com/themes/docs/theme/color#focus-and-selection)
  * [Alpha colors](https://www.radix-ui.com/themes/docs/theme/color#alpha-colors)
  * [Backgrounds](https://www.radix-ui.com/themes/docs/theme/color#backgrounds)
  * [Panel background](https://www.radix-ui.com/themes/docs/theme/color#panel-background)
  * [Customization](https://www.radix-ui.com/themes/docs/theme/color#customization)
  * [Brand color](https://www.radix-ui.com/themes/docs/theme/color#brand-color)
  * [Custom palette](https://www.radix-ui.com/themes/docs/theme/color#custom-palette)
  * [Color aliasing](https://www.radix-ui.com/themes/docs/theme/color#color-aliasing)
  * [Individual CSS files](https://www.radix-ui.com/themes/docs/theme/color#individual-css-files)


Previous[Overview](https://www.radix-ui.com/themes/docs/theme/overview)
Next[Dark mode](https://www.radix-ui.com/themes/docs/theme/dark-mode)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/themes/docs/theme/color.mdx "Edit this page on GitHub.")

