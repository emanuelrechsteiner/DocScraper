---
url: https://www.radix-ui.com/themes/docs/components/text-field
scraped_at: 2025-06-07T09:35:42.113932
title: Text Field – Radix Themes
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
Components
# Text Field
Captures user input with an optional slot for buttons and icons.
[View source](https://github.com/radix-ui/themes/blob/main/packages/radix-ui-themes/src/components/text-field.tsx)[Report an issue](https://github.com/radix-ui/themes/issues/new?title=\[TextField\] Issue)[View in Playground](https://www.radix-ui.com/themes/playground#text-field)
```

<TextField.Root placeholder="Search the docs…">

<TextField.Slot>

<MagnifyingGlassIcon height="16" width="16" />

</TextField.Slot>

</TextField.Root>


```

## [API Reference](https://www.radix-ui.com/themes/docs/components/text-field#api-reference)
### [Root](https://www.radix-ui.com/themes/docs/components/text-field#root)
Groups Slot and Input parts. This component is based on the `div` element and supports [common margin props](https://www.radix-ui.com/themes/docs/overview/layout#margin-props).
Prop| Type| Default  
---|---|---  
`size`| `Responsive<"1" | "2" | "3">`| `"2"`  
`variant`Prop description| `"classic" | "surface" | "soft"`| `"surface"`  
`color`Prop description| `enum`See full type| No default value  
`radius`Prop description| `"none" | "small" | "medium" | "large" | "full"`| No default value  
### [Slot](https://www.radix-ui.com/themes/docs/components/text-field#slot)
Contains icons or buttons associated with an Input.
Prop| Type| Default  
---|---|---  
`side`| `"left" | "right"`| No default value  
`color`Prop description| `enum`See full type| No default value  
`gap`| `Responsive<enum | string>`See full type| No default value  
`px`| `Responsive<enum | string>`See full type| No default value  
`pl`| `Responsive<enum | string>`See full type| No default value  
`pr`| `Responsive<enum | string>`See full type| No default value  
## [Examples](https://www.radix-ui.com/themes/docs/components/text-field#examples)
### [Size](https://www.radix-ui.com/themes/docs/components/text-field#size)
Use the `size` prop to control the size.
```

<Flex direction="column" gap="3">

<Box maxWidth="200px">

<TextField.Root size="1" placeholder="Search the docs…" />

</Box>

<Box maxWidth="250px">

<TextField.Root size="2" placeholder="Search the docs…" />

</Box>

<Box maxWidth="300px">

<TextField.Root size="3" placeholder="Search the docs…" />

</Box>

</Flex>


```

Use matching component sizes when composing Text Field with buttons. However, don’t use size 1 inputs with buttons—at this size, there is not enough vertical space to nest other interactive elements.
```

<Flex direction="column" gap="3" maxWidth="400px">

<Box maxWidth="200px">

<TextField.Root placeholder="Search the docs…" size="1">

<TextField.Slot>

<MagnifyingGlassIcon height="16" width="16" />

</TextField.Slot>

</TextField.Root>

</Box>

<Box maxWidth="250px">

<TextField.Root placeholder="Search the docs…" size="2">

<TextField.Slot>

<MagnifyingGlassIcon height="16" width="16" />

</TextField.Slot>

<TextField.Slot>

<IconButton size="1" variant="ghost">

<DotsHorizontalIcon height="14" width="14" />

</IconButton>

</TextField.Slot>

</TextField.Root>

</Box>

<Box maxWidth="300px">

<TextField.Root placeholder="Search the docs…" size="3">

<TextField.Slot>

<MagnifyingGlassIcon height="16" width="16" />

</TextField.Slot>

<TextField.Slot pr="3">

<IconButton size="2" variant="ghost">

<DotsHorizontalIcon height="16" width="16" />

</IconButton>

</TextField.Slot>

</TextField.Root>

</Box>

</Flex>


```

### [Variant](https://www.radix-ui.com/themes/docs/components/text-field#variant)
Use the `variant` prop to control the visual style.
```

<Flex direction="column" gap="3" maxWidth="250px">

<TextField.Root variant="surface" placeholder="Search the docs…" />

<TextField.Root variant="classic" placeholder="Search the docs…" />

<TextField.Root variant="soft" placeholder="Search the docs…" />

</Flex>


```

### [Color](https://www.radix-ui.com/themes/docs/components/text-field#color)
Use the `color` prop to assign a specific [color](https://www.radix-ui.com/themes/docs/theme/color).
```

<Flex direction="column" gap="3" maxWidth="250px">

<TextField.Root
		color="indigo"
		variant="soft"
		placeholder="Search the docs…"
	/>

<TextField.Root color="green" variant="soft" placeholder="Search the docs…" />

<TextField.Root color="red" variant="soft" placeholder="Search the docs…" />

</Flex>


```

### [Radius](https://www.radix-ui.com/themes/docs/components/text-field#radius)
Use the `radius` prop to assign a specific radius value.
```

<Flex direction="column" gap="3" maxWidth="250px">

<TextField.Root radius="none" placeholder="Search the docs…" />

<TextField.Root radius="large" placeholder="Search the docs…" />

<TextField.Root radius="full" placeholder="Search the docs…" />

</Flex>


```

#### Quick nav
  * [API Reference](https://www.radix-ui.com/themes/docs/components/text-field#api-reference)
  * [Root](https://www.radix-ui.com/themes/docs/components/text-field#root)
  * [Slot](https://www.radix-ui.com/themes/docs/components/text-field#slot)
  * [Examples](https://www.radix-ui.com/themes/docs/components/text-field#examples)
  * [Size](https://www.radix-ui.com/themes/docs/components/text-field#size)
  * [Variant](https://www.radix-ui.com/themes/docs/components/text-field#variant)
  * [Color](https://www.radix-ui.com/themes/docs/components/text-field#color)
  * [Radius](https://www.radix-ui.com/themes/docs/components/text-field#radius)


Previous[Text Area](https://www.radix-ui.com/themes/docs/components/text-area)
Next[Tooltip](https://www.radix-ui.com/themes/docs/components/tooltip)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/themes/docs/components/text-field.mdx "Edit this page on GitHub.")

