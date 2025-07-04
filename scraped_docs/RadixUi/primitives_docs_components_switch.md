---
url: https://www.radix-ui.com/primitives/docs/components/switch
scraped_at: 2025-06-07T09:37:21.007779
title: Switch – Radix Primitives
---

[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Documentation](https://www.radix-ui.com/primitives/docs)[Case studies](https://www.radix-ui.com/primitives/case-studies)[Blog](https://www.radix-ui.com/blog)[](https://github.com/radix-ui/primitives)
Search
`/`
#### Overview
[Introduction](https://www.radix-ui.com/primitives/docs/overview/introduction)[Getting started](https://www.radix-ui.com/primitives/docs/overview/getting-started)[Accessibility](https://www.radix-ui.com/primitives/docs/overview/accessibility)[Releases](https://www.radix-ui.com/primitives/docs/overview/releases)
#### Guides
[Styling](https://www.radix-ui.com/primitives/docs/guides/styling)[Animation](https://www.radix-ui.com/primitives/docs/guides/animation)[Composition](https://www.radix-ui.com/primitives/docs/guides/composition)[Server-side rendering](https://www.radix-ui.com/primitives/docs/guides/server-side-rendering)
#### Components
[Accordion](https://www.radix-ui.com/primitives/docs/components/accordion)[Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog)[Aspect Ratio](https://www.radix-ui.com/primitives/docs/components/aspect-ratio)[Avatar](https://www.radix-ui.com/primitives/docs/components/avatar)[Checkbox](https://www.radix-ui.com/primitives/docs/components/checkbox)[Collapsible](https://www.radix-ui.com/primitives/docs/components/collapsible)[Context Menu](https://www.radix-ui.com/primitives/docs/components/context-menu)[Dialog](https://www.radix-ui.com/primitives/docs/components/dialog)[Dropdown Menu](https://www.radix-ui.com/primitives/docs/components/dropdown-menu)[FormPreview](https://www.radix-ui.com/primitives/docs/components/form)[Hover Card](https://www.radix-ui.com/primitives/docs/components/hover-card)[Label](https://www.radix-ui.com/primitives/docs/components/label)[Menubar](https://www.radix-ui.com/primitives/docs/components/menubar)[Navigation Menu](https://www.radix-ui.com/primitives/docs/components/navigation-menu)[One-Time Password FieldPreview](https://www.radix-ui.com/primitives/docs/components/one-time-password-field)[Password Toggle FieldPreview](https://www.radix-ui.com/primitives/docs/components/password-toggle-field)[Popover](https://www.radix-ui.com/primitives/docs/components/popover)[Progress](https://www.radix-ui.com/primitives/docs/components/progress)[Radio Group](https://www.radix-ui.com/primitives/docs/components/radio-group)[Scroll Area](https://www.radix-ui.com/primitives/docs/components/scroll-area)[Select](https://www.radix-ui.com/primitives/docs/components/select)[Separator](https://www.radix-ui.com/primitives/docs/components/separator)[Slider](https://www.radix-ui.com/primitives/docs/components/slider)[Switch](https://www.radix-ui.com/primitives/docs/components/switch)[Tabs](https://www.radix-ui.com/primitives/docs/components/tabs)[Toast](https://www.radix-ui.com/primitives/docs/components/toast)[Toggle](https://www.radix-ui.com/primitives/docs/components/toggle)[Toggle Group](https://www.radix-ui.com/primitives/docs/components/toggle-group)[Toolbar](https://www.radix-ui.com/primitives/docs/components/toolbar)[Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip)
#### Utilities
[Accessible Icon](https://www.radix-ui.com/primitives/docs/utilities/accessible-icon)[Direction Provider](https://www.radix-ui.com/primitives/docs/utilities/direction-provider)[Portal](https://www.radix-ui.com/primitives/docs/utilities/portal)[Slot](https://www.radix-ui.com/primitives/docs/utilities/slot)[Visually Hidden](https://www.radix-ui.com/primitives/docs/utilities/visually-hidden)
Components
# Switch
A control that allows the user to toggle between checked and not checked.
Airplane mode
index.jsxindex.jsxstyles.cssstyles.css
CSS
```

import * as React from "react";

import { Switch } from "radix-ui";

import "./styles.css";

const SwitchDemo = () => (

	<form>

<div style={{ display: "flex", alignItems: "center" }}>

<label
				className="Label"
				htmlFor="airplane-mode"
				style={{ paddingRight: 15 }}
			>

				Airplane mode

</label>

<Switch.Root className="SwitchRoot" id="airplane-mode">

<Switch.Thumb className="SwitchThumb" />

</Switch.Root>

</div>

</form>

);

export default SwitchDemo;

Expand code

```

## Features
Full keyboard navigation.
Can be controlled or uncontrolled.


## Component Reference Links
Version: 1.2.5
Size: [4.06 kB](https://bundlephobia.com/package/@radix-ui/react-switch@1.2.5)
[View source](https://github.com/radix-ui/primitives/tree/main/packages/react/switch/src)
[Report an issue](https://github.com/radix-ui/primitives/issues/new/choose)
[ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch)
## [Installation](https://www.radix-ui.com/primitives/docs/components/switch#installation)
Install the component from your command line.
```

npm install @radix-ui/react-switch


```

## [Anatomy](https://www.radix-ui.com/primitives/docs/components/switch#anatomy)
Import all parts and piece them together.
```

import { Switch } from "radix-ui";

export default () => (

	<Switch.Root>

<Switch.Thumb />

</Switch.Root>

);


```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/switch#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/switch#root)
Contains all the parts of a switch. An `input` will also render when used within a `form` to ensure events propagate correctly.
Prop| Type| Default  
---|---|---  
`asChild`Prop description| `boolean`| `false`  
`defaultChecked`Prop description| `boolean`| No default value  
`checked`Prop description| `boolean`| No default value  
`onCheckedChange`Prop description| `function`See full type| No default value  
`disabled`Prop description| `boolean`| No default value  
`required`Prop description| `boolean`| No default value  
`name`Prop description| `string`| No default value  
`value`Prop description| `string`| `on`  
Data attribute| Values  
---|---  
`[data-state]`| `"checked" | "unchecked" `  
`[data-disabled]`| Present when disabled  
### [Thumb](https://www.radix-ui.com/primitives/docs/components/switch#thumb)
The thumb that is used to visually indicate whether the switch is on or off.
Prop| Type| Default  
---|---|---  
`asChild`Prop description| `boolean`| `false`  
Data attribute| Values  
---|---  
`[data-state]`| `"checked" | "unchecked" `  
`[data-disabled]`| Present when disabled  
## [Accessibility](https://www.radix-ui.com/primitives/docs/components/switch#accessibility)
Adheres to the [`switch` role requirements](https://www.w3.org/WAI/ARIA/apg/patterns/switch).
### [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/switch#keyboard-interactions)
Key| Description  
---|---  
`Space`| Toggles the component's state.  
`Enter`| Toggles the component's state.  
#### Quick nav
  * [Installation](https://www.radix-ui.com/primitives/docs/components/switch#installation)
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/switch#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/switch#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/switch#root)
  * [Thumb](https://www.radix-ui.com/primitives/docs/components/switch#thumb)
  * [Accessibility](https://www.radix-ui.com/primitives/docs/components/switch#accessibility)
  * [Keyboard Interactions](https://www.radix-ui.com/primitives/docs/components/switch#keyboard-interactions)


Previous[Slider](https://www.radix-ui.com/primitives/docs/components/slider)
Next[Tabs](https://www.radix-ui.com/primitives/docs/components/tabs)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/primitives/docs/components/switch.mdx "Edit this page on GitHub.")

