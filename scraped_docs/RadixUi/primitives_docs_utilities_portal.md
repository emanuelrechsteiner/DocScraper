---
url: https://www.radix-ui.com/primitives/docs/utilities/portal
scraped_at: 2025-06-07T09:42:20.697769
title: Portal – Radix Primitives
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
Utilities
# Portal
Renders a React subtree in a different part of the DOM.
## Features
Render any React subtree outside of your App.
Appends to `document.body` by default but can be customized to use a different container.


## Component Reference Links
Version: 1.1.9
Size: [1.72 kB](https://bundlephobia.com/package/@radix-ui/react-portal@1.1.9)
[View source](https://github.com/radix-ui/primitives/tree/main/packages/react/portal/src)
[Report an issue](https://github.com/radix-ui/primitives/issues/new/choose)
## [Installation](https://www.radix-ui.com/primitives/docs/utilities/portal#installation)
Install the component from your command line.
```

npm install @radix-ui/react-portal


```

## [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/portal#anatomy)
Import the component.
```

import { Portal } from "radix-ui";

export default () => <Portal.Root />;


```

## [Basic example](https://www.radix-ui.com/primitives/docs/utilities/portal#basic-example)
Use the portal primitive.
```

import { Portal } from "radix-ui";

export default () => <Portal.Root>Content</Portal.Root>;


```

## [API Reference](https://www.radix-ui.com/primitives/docs/utilities/portal#api-reference)
### [Root](https://www.radix-ui.com/primitives/docs/utilities/portal#root)
Anything you put inside this component will be rendered in a separate `<div>` element. By default, this element will be appended to `document.body` but you can choose a different container by using the `container` prop.
Prop| Type| Default  
---|---|---  
`asChild`Prop description| `boolean`| `false`  
`container`Prop description| `HTMLElement`| No default value  
#### Quick nav
  * [Installation](https://www.radix-ui.com/primitives/docs/utilities/portal#installation)
  * [Anatomy](https://www.radix-ui.com/primitives/docs/utilities/portal#anatomy)
  * [Basic example](https://www.radix-ui.com/primitives/docs/utilities/portal#basic-example)
  * [API Reference](https://www.radix-ui.com/primitives/docs/utilities/portal#api-reference)
  * [Root](https://www.radix-ui.com/primitives/docs/utilities/portal#root)


Previous[Direction Provider](https://www.radix-ui.com/primitives/docs/utilities/direction-provider)
Next[Slot](https://www.radix-ui.com/primitives/docs/utilities/slot)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/primitives/docs/utilities/portal.mdx "Edit this page on GitHub.")

