---
url: https://www.radix-ui.com/primitives/docs/components/aspect-ratio
scraped_at: 2025-06-07T09:41:00.488334
title: Aspect Ratio – Radix Primitives
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
# Aspect Ratio
Displays content within a desired ratio.
![Landscape photograph by Tobias Tullius](https://images.unsplash.com/photo-1535025183041-0991a977e25b?w=300&dpr=2&q=80)
index.jsxindex.jsxstyles.cssstyles.css
CSS
```

import * as React from "react";

import { AspectRatio } from "radix-ui";

import "./styles.css";

const AspectRatioDemo = () => (

	<div className="Container">

<AspectRatio.Root ratio={16 / 9}>

<img
				className="Image"
				src="https://images.unsplash.com/photo-1535025183041-0991a977e25b?w=300&dpr=2&q=80"
				alt="Landscape photograph by Tobias Tullius"
			/>

</AspectRatio.Root>

</div>

);

export default AspectRatioDemo;

Expand code

```

## Features
Accepts any custom ratio.


## Component Reference Links
Version: 1.1.7
Size: [1.71 kB](https://bundlephobia.com/package/@radix-ui/react-aspect-ratio@1.1.7)
[View source](https://github.com/radix-ui/primitives/tree/main/packages/react/aspect-ratio/src)
[Report an issue](https://github.com/radix-ui/primitives/issues/new/choose)
## [Installation](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#installation)
Install the component from your command line.
```

npm install @radix-ui/react-aspect-ratio


```

## [Anatomy](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#anatomy)
Import the component.
```

import { AspectRatio } from "radix-ui";

export default () => <AspectRatio.Root />;


```

## [API Reference](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#root)
Contains the content you want to constrain to a given ratio.
Prop| Type| Default  
---|---|---  
`asChild`Prop description| `boolean`| `false`  
`ratio`Prop description| `number`| `1`  
#### Quick nav
  * [Installation](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#installation)
  * [Anatomy](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#anatomy)
  * [API Reference](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/components/aspect-ratio#root)


Previous[Alert Dialog](https://www.radix-ui.com/primitives/docs/components/alert-dialog)
Next[Avatar](https://www.radix-ui.com/primitives/docs/components/avatar)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/primitives/docs/components/aspect-ratio.mdx "Edit this page on GitHub.")

