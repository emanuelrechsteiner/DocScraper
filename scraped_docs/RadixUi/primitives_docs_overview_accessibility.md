---
url: https://www.radix-ui.com/primitives/docs/overview/accessibility
scraped_at: 2025-06-07T09:41:26.934506
title: Accessibility – Radix Primitives
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
Overview
# Accessibility
Radix Primitives follow the WAI-ARIA authoring practices guidelines and are tested in a wide selection of modern browsers and commonly used assistive technologies.
We take care of many of the difficult implementation details related to accessibility, including `aria` and `role` attributes, focus management, and keyboard navigation. That means that users should be able to use our components as-is in most contexts and rely on functionality to follow the expected accessibility design patterns.
## [WAI-ARIA](https://www.radix-ui.com/primitives/docs/overview/accessibility#wai-aria)
[WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/), published and maintained by the W3C, specifies the semantics for many common UI patterns that show up in Radix Primitives. This is designed to provide meaning for controls that aren't built using elements provided by the browser. For example, if you use a `div` instead of a `button` element to create a button, there are attributes you need to add to the `div` in order to convey that it's a button for screen readers or voice recognition tools.
In addition to semantics, there are behaviors that are expected from different types of components. A `button` element is going to respond to certain interactions in ways that a `div` will not, so it's up to the developer to reimplement those interactions with JavaScript. The [WAI-ARIA authoring practices](https://www.w3.org/TR/wai-aria-practices-1.2/) provide additional guidance for implementing behaviors for various controls that come with Radix Primitives.
## [Accessible Labels](https://www.radix-ui.com/primitives/docs/overview/accessibility#accessible-labels)
With many built-in form controls, the native HTML `label` element is designed to provide semantic meaning and context for corresponding `input` elements. For non-form control elements, or for custom controls like those provided by Radix Primitives, [WAI-ARIA provides a specification](https://www.w3.org/TR/wai-aria-1.2/#namecalculation) for how to provide accessible names and descriptions to those controls.
Where possible, Radix Primitives include abstractions to make labelling our controls simple. The [`Label`](https://www.radix-ui.com/primitives/docs/components/label) primitive is designed to work with many of our controls. Ultimately it's up to you to provide those labels so that users have the proper context when navigating your application.
## [Keyboard Navigation](https://www.radix-ui.com/primitives/docs/overview/accessibility#keyboard-navigation)
Many complex components, like [`Tabs`](https://www.radix-ui.com/primitives/docs/components/tabs) and [`Dialog`](https://www.radix-ui.com/primitives/docs/components/dialog), come with expectations from users on how to interact with their content using a keyboard or other non-mouse input modalities. Radix Primitives provide basic keyboard support in accordance with the [WAI-ARIA authoring practices](https://www.w3.org/TR/wai-aria-practices-1.2/).
## [Focus Management](https://www.radix-ui.com/primitives/docs/overview/accessibility#focus-management)
Proper keyboard navigation and good labelling often go hand-in-hand with managing focus. When a user interacts with an element and something changes as a result, it's often helpful to move focus with the interaction so that the next tab stop is logical depending on the new context of the app. And for screen reader users, moving focus often results in an announcement to convey this new context, which relies on proper labelling.
In many Radix Primitives, we move focus based on the interactions a user normally takes in a given component. For example, in [`AlertDialog`](https://www.radix-ui.com/primitives/docs/components/alert-dialog), when the modal is opened, focus is programmatically moved to a `Cancel` button element to anticipate a response to the prompt.
#### Quick nav
  * [WAI-ARIA](https://www.radix-ui.com/primitives/docs/overview/accessibility#wai-aria)
  * [Accessible Labels](https://www.radix-ui.com/primitives/docs/overview/accessibility#accessible-labels)
  * [Keyboard Navigation](https://www.radix-ui.com/primitives/docs/overview/accessibility#keyboard-navigation)
  * [Focus Management](https://www.radix-ui.com/primitives/docs/overview/accessibility#focus-management)


Previous[Getting started](https://www.radix-ui.com/primitives/docs/overview/getting-started)
Next[Releases](https://www.radix-ui.com/primitives/docs/overview/releases)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/primitives/docs/overview/accessibility.mdx "Edit this page on GitHub.")

