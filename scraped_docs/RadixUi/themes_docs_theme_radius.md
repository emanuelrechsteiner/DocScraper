---
url: https://www.radix-ui.com/themes/docs/theme/radius
scraped_at: 2025-06-07T09:34:18.172593
title: Radius – Radix Themes
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
# Radius
Choosing the right radius setting in your theme.
## [Theme setting](https://www.radix-ui.com/themes/docs/theme/radius#theme-setting)
Theme `radius` setting manages the radius factor applied to the components:
```

<Theme radius="medium">

<TextField.Root size="3" placeholder="Reply…">

<TextField.Slot side="right" px="1">

<Button size="2">Send</Button>

</TextField.Slot>

</TextField.Root>

</Theme>


```

`none`
Send
`small`
Send
`medium`
Send
`large`
Send
`full`
Send
The resulting `border-radius` is contextual and differs depending on the component. For example, when set to `full`, a [Button](https://www.radix-ui.com/themes/docs/components/button) becomes pill-shaped, while a [Checkbox](https://www.radix-ui.com/themes/docs/components/checkbox) will never become fully rounded to prevent any confusion between it and a [Radio](https://www.radix-ui.com/themes/docs/components/radio).
Save
```

<Theme radius="full">

<Flex align="center" gap="3">

<Button>Save</Button>

<Switch defaultChecked />

<Checkbox defaultChecked />

</Flex>

</Theme>


```

## [Radius overrides](https://www.radix-ui.com/themes/docs/theme/radius#radius-overrides)
Certain components allow you to override the radius factor using their own `radius` prop.
SaveSaveSaveSaveSave
```

<Flex align="center" gap="3">

<Button radius="none">Save</Button>

<Button radius="small">Save</Button>

<Button radius="medium">Save</Button>

<Button radius="large">Save</Button>

<Button radius="full">Save</Button>

</Flex>


```

Components that render panels, like Card, Dialog, and Popover, among others, won’t have the `radius` prop, but will inherit the radius setting from the theme. The `radius` prop is also unavailable on most text-based components.
## [Radius scale](https://www.radix-ui.com/themes/docs/theme/radius#radius-scale)
Radius values used in the components are derived from a 6-step scale.
1
2
3
4
5
6
While you can’t use a specific step on a particular component directly—the `radius` prop is used to set just the radius factor—you can use the radius scale to style your own components.
Radius tokens are accessed using CSS variables. You can use these tokens to style your custom components, ensuring they are consistent with the rest of your theme.
```

/* Radius values that automatically respond to the radius factor */

var(--radius-1);

var(--radius-2);

var(--radius-3);

var(--radius-4);

var(--radius-5);

var(--radius-6);

/* A multiplier that controls the theme radius */

var(--radius-factor);

/*

 * A variable used to calculate a fully rounded radius.

 * Usually used within a CSS `max()` function.

 */

var(--radius-full);

/*

 * A variable used to calculate radius of a thumb element.

 * Usually used within a CSS `max()` function.

 */

var(--radius-thumb);


```

#### Quick nav
  * [Theme setting](https://www.radix-ui.com/themes/docs/theme/radius#theme-setting)
  * [Radius overrides](https://www.radix-ui.com/themes/docs/theme/radius#radius-overrides)
  * [Radius scale](https://www.radix-ui.com/themes/docs/theme/radius#radius-scale)


Previous[Breakpoints](https://www.radix-ui.com/themes/docs/theme/breakpoints)
Next[Shadows](https://www.radix-ui.com/themes/docs/theme/shadows)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/themes/docs/theme/radius.mdx "Edit this page on GitHub.")

