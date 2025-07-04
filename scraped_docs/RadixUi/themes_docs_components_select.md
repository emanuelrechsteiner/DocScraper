---
url: https://www.radix-ui.com/themes/docs/components/select
scraped_at: 2025-06-07T09:34:11.704899
title: Select – Radix Themes
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
# Select
Displays a list of options for the user to pick from—triggered by a button.
[View source](https://github.com/radix-ui/themes/blob/main/packages/radix-ui-themes/src/components/select.tsx)[Report an issue](https://github.com/radix-ui/themes/issues/new?title=\[Select\] Issue)[View in Playground](https://www.radix-ui.com/themes/playground#select)
Apple
```

<Select.Root defaultValue="apple">

<Select.Trigger />

<Select.Content>

<Select.Group>

<Select.Label>Fruits</Select.Label>

<Select.Item value="orange">Orange</Select.Item>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="grape" disabled>

				Grape

</Select.Item>

</Select.Group>

<Select.Separator />

<Select.Group>

<Select.Label>Vegetables</Select.Label>

<Select.Item value="carrot">Carrot</Select.Item>

<Select.Item value="potato">Potato</Select.Item>

</Select.Group>

</Select.Content>

</Select.Root>


```

## [API Reference](https://www.radix-ui.com/themes/docs/components/select#api-reference)
### [Root](https://www.radix-ui.com/themes/docs/components/select#root)
Contains all the parts of a select. It inherits props from the Select primitive [Root](https://www.radix-ui.com/primitives/docs/components/select#root) part.
Prop| Type| Default  
---|---|---  
`size`| `Responsive<"1" | "2" | "3">`| `"2"`  
### [Trigger](https://www.radix-ui.com/themes/docs/components/select#trigger)
The button that toggles the select. This component inherits props from the Select primitive [Trigger](https://www.radix-ui.com/primitives/docs/components/select#trigger) and [Value](https://www.radix-ui.com/primitives/docs/components/select#value) parts. It supports [common margin props](https://www.radix-ui.com/themes/docs/overview/layout#margin-props).
Prop| Type| Default  
---|---|---  
`variant`Prop description| `"classic" | "surface" | "soft" | "ghost"`| `"surface"`  
`color`Prop description| `enum`See full type| No default value  
`radius`Prop description| `"none" | "small" | "medium" | "large" | "full"`| No default value  
`placeholder`| `string`| No default value  
### [Content](https://www.radix-ui.com/themes/docs/components/select#content)
The component that pops out when the select is open. It inherits props from the [Select.Portal primitive](https://www.radix-ui.com/primitives/docs/components/select#portal) and [Select.Content primitive](https://www.radix-ui.com/primitives/docs/components/select#content) parts.
Prop| Type| Default  
---|---|---  
`variant`Prop description| `"solid" | "soft"`| `"solid"`  
`color`Prop description| `enum`See full type| No default value  
`highContrast`Prop description| `boolean`| No default value  
### [Item](https://www.radix-ui.com/themes/docs/components/select#item)
The component that contains the select items. It inherits props from the [Select.Item primitive](https://www.radix-ui.com/primitives/docs/components/select#item) part.
### [Group](https://www.radix-ui.com/themes/docs/components/select#group)
Used to group multiple items. It inherits props from the [Select.Group primitive](https://www.radix-ui.com/primitives/docs/components/select#group) part. Use in conjunction with `Select.Label` to ensure good accessibility via automatic labelling.
### [Label](https://www.radix-ui.com/themes/docs/components/select#label)
Used to render the label of a group, it isn't focusable using arrow keys. It inherits props from the [Select.Label primitive](https://www.radix-ui.com/primitives/docs/components/select#label) part.
### [Separator](https://www.radix-ui.com/themes/docs/components/select#separator)
Used to visually separate items in the Select. It inherits props from the [Select.Separator primitive](https://www.radix-ui.com/primitives/docs/components/select#separator) part.
## [Examples](https://www.radix-ui.com/themes/docs/components/select#examples)
### [Size](https://www.radix-ui.com/themes/docs/components/select#size)
Use the `size` prop to control the size.
AppleAppleApple
```

<Flex gap="3" align="center">

<Select.Root size="1" defaultValue="apple">

<Select.Trigger />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root size="2" defaultValue="apple">

<Select.Trigger />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root size="3" defaultValue="apple">

<Select.Trigger />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

</Flex>


```

### [Variant](https://www.radix-ui.com/themes/docs/components/select#variant)
Use the `variant` prop on `Trigger` and `Content` to customize the visual style.
AppleAppleApple
```

<Flex gap="3" align="center">

<Select.Root defaultValue="apple">

<Select.Trigger variant="surface" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger variant="classic" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger variant="soft" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

</Flex>


```

#### Ghost
Use the `ghost` trigger variant to render the trigger without a visually containing element. Ghost triggers behave differently in layout as they use a negative margin to optically align themselves against their siblings while maintaining their padded active and hover states.
AppleApple
```

<Flex gap="3" align="center">

<Select.Root defaultValue="apple">

<Select.Trigger variant="surface" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger variant="ghost" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

</Flex>


```

### [Color](https://www.radix-ui.com/themes/docs/components/select#color)
Use the `color` prop on `Trigger` and `Content` to assign a specific color value.
AppleAppleAppleApple
```

<Flex gap="3">

<Select.Root defaultValue="apple">

<Select.Trigger color="indigo" variant="soft" />

<Select.Content color="indigo">

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger color="cyan" variant="soft" />

<Select.Content color="cyan">

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger color="orange" variant="soft" />

<Select.Content color="orange">

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger color="crimson" variant="soft" />

<Select.Content color="crimson">

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

</Flex>


```

### [High-contrast](https://www.radix-ui.com/themes/docs/components/select#high-contrast)
Use the `highContrast` prop on `Content` to increase item contrast.
AppleApple
```

<Flex gap="3">

<Select.Root defaultValue="apple">

<Select.Trigger color="gray" />

<Select.Content color="gray" variant="solid">

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger color="gray" />

<Select.Content color="gray" variant="solid" highContrast>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

</Flex>


```

### [Radius](https://www.radix-ui.com/themes/docs/components/select#radius)
Use the `radius` prop to assign a specific radius value.
AppleAppleApple
```

<Flex gap="3">

<Select.Root defaultValue="apple">

<Select.Trigger radius="none" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger radius="large" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

<Select.Root defaultValue="apple">

<Select.Trigger radius="full" />

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

</Flex>


```

### [Placeholder](https://www.radix-ui.com/themes/docs/components/select#placeholder)
Use the `placeholder` prop to create a `Trigger` that doesn’t need an initial value.
Pick a fruit
```

<Select.Root>

<Select.Trigger placeholder="Pick a fruit" />

<Select.Content>

<Select.Group>

<Select.Label>Fruits</Select.Label>

<Select.Item value="orange">Orange</Select.Item>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="grape" disabled>

				Grape

</Select.Item>

</Select.Group>

<Select.Separator />

<Select.Group>

<Select.Label>Vegetables</Select.Label>

<Select.Item value="carrot">Carrot</Select.Item>

<Select.Item value="potato">Potato</Select.Item>

</Select.Group>

</Select.Content>

</Select.Root>


```

### [Position](https://www.radix-ui.com/themes/docs/components/select#position)
Set `position="popper"` prop to position the select menu below the trigger.
Apple
```

<Select.Root defaultValue="apple">

<Select.Trigger />

<Select.Content position="popper">

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>


```

### [With SSR](https://www.radix-ui.com/themes/docs/components/select#with-ssr)
When using server-side rendering, you might notice a layout shift after hydration. This is because Trigger executes client-side code to display the selected item’s text. To avoid that layout shift, you can render it manually by mapping values.
Apple
```

() => {

	const data = {

		apple: "Apple",

		orange: "Orange",

	};

	const [value, setValue] = React.useState("apple");

	return (

		<Select.Root value={value} onValueChange={setValue}>

<Select.Trigger>{data[value]}</Select.Trigger>

<Select.Content>

<Select.Item value="apple">Apple</Select.Item>

<Select.Item value="orange">Orange</Select.Item>

</Select.Content>

</Select.Root>

	);

};


```

### [With an icon](https://www.radix-ui.com/themes/docs/components/select#with-an-icon)
You can customise how Trigger renders the value by controlling its children manually. For example, you can render an icon next to the selected item’s text.
Light
```

() => {

	const data = {

		light: { label: "Light", icon: <SunIcon /> },

		dark: { label: "Dark", icon: <MoonIcon /> },

	};

	const [value, setValue] = React.useState("light");

	return (

		<Flex direction="column" maxWidth="160px">

<Select.Root value={value} onValueChange={setValue}>

<Select.Trigger>

<Flex as="span" align="center" gap="2">

{data[value].icon}

{data[value].label}

</Flex>

</Select.Trigger>

<Select.Content position="popper">

<Select.Item value="light">Light</Select.Item>

<Select.Item value="dark">Dark</Select.Item>

</Select.Content>

</Select.Root>

</Flex>

	);

};


```

#### Quick nav
  * [API Reference](https://www.radix-ui.com/themes/docs/components/select#api-reference)
  * [Root](https://www.radix-ui.com/themes/docs/components/select#root)
  * [Trigger](https://www.radix-ui.com/themes/docs/components/select#trigger)
  * [Content](https://www.radix-ui.com/themes/docs/components/select#content)
  * [Item](https://www.radix-ui.com/themes/docs/components/select#item)
  * [Group](https://www.radix-ui.com/themes/docs/components/select#group)
  * [Label](https://www.radix-ui.com/themes/docs/components/select#label)
  * [Separator](https://www.radix-ui.com/themes/docs/components/select#separator)
  * [Examples](https://www.radix-ui.com/themes/docs/components/select#examples)
  * [Size](https://www.radix-ui.com/themes/docs/components/select#size)
  * [Variant](https://www.radix-ui.com/themes/docs/components/select#variant)
  * [Color](https://www.radix-ui.com/themes/docs/components/select#color)
  * [High-contrast](https://www.radix-ui.com/themes/docs/components/select#high-contrast)
  * [Radius](https://www.radix-ui.com/themes/docs/components/select#radius)
  * [Placeholder](https://www.radix-ui.com/themes/docs/components/select#placeholder)
  * [Position](https://www.radix-ui.com/themes/docs/components/select#position)
  * [With SSR](https://www.radix-ui.com/themes/docs/components/select#with-ssr)
  * [With an icon](https://www.radix-ui.com/themes/docs/components/select#with-an-icon)


Previous[Segmented Control](https://www.radix-ui.com/themes/docs/components/segmented-control)
Next[Separator](https://www.radix-ui.com/themes/docs/components/separator)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/themes/docs/components/select.mdx "Edit this page on GitHub.")

