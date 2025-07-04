---
url: https://www.radix-ui.com/colors/docs/overview/aliasing
scraped_at: 2025-06-07T09:33:28.254107
title: Aliasing – Radix Colors
---

[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Documentation](https://www.radix-ui.com/colors/docs)[Custom palette](https://www.radix-ui.com/colors/custom)[Blog](https://www.radix-ui.com/blog)[](https://github.com/radix-ui/colors)
#### Overview
[Installation](https://www.radix-ui.com/colors/docs/overview/installation)[Usage](https://www.radix-ui.com/colors/docs/overview/usage)[Aliasing](https://www.radix-ui.com/colors/docs/overview/aliasing)[Custom palettes](https://www.radix-ui.com/colors/docs/overview/custom-palettes)[Releases](https://www.radix-ui.com/colors/docs/overview/releases)
#### Palette composition
[Scales](https://www.radix-ui.com/colors/docs/palette-composition/scales)[Composing a palette](https://www.radix-ui.com/colors/docs/palette-composition/composing-a-palette)[Understanding the scale](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale)
# Aliasing
A guide to providing semantic aliases for colors.
## [Semantic aliases](https://www.radix-ui.com/colors/docs/overview/aliasing#semantic-aliases)
Referencing color scales by their actual scale name can work well, like `blue` and `red`. But often, creating semantic aliases like `accent`, `primary`, `neutral`, or `brand` can be helpful, especially when it comes to theming.
CSSCSSCSS-in-JSCSS-in-JS
```

/*

* Note: Importing from the CDN in production is not recommended.

* It's intended for prototyping only.

*/

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/blue.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/green.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/yellow.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/red.css";

:root {

--accent-1: var(--blue-1);

--accent-2: var(--blue-2);

--accent-3: var(--blue-3);

--accent-4: var(--blue-4);

--accent-5: var(--blue-5);

--accent-6: var(--blue-6);

--accent-7: var(--blue-7);

--accent-8: var(--blue-8);

--accent-9: var(--blue-9);

--accent-10: var(--blue-10);

--accent-11: var(--blue-11);

--accent-12: var(--blue-12);

--success-1: var(--green-1);

--success-2: var(--green-2);

/* repeat for all steps */

--warning-1: var(--yellow-1);

--warning-2: var(--yellow-2);

/* repeat for all steps */

--danger-1: var(--red-1);

--danger-2: var(--red-2);

/* repeat for all steps */

}


```

With this approach, you will likely run into issues where you need to use the same scale for multiple semantics. Common examples include:
  * If you map `yellow` to "warning", you might also need `yellow` to communicate "pending".
  * If you map `red` to "danger", you might also need `red` to communicate "error" or "rejected".
  * If you map `green` to "success", you might also need `green` to communicate "valid".
  * If you map `blue` to "accent", you might also need `blue` to communicate "info".


In this scenario, you can choose to define multiple semantic aliases which map to the same scale.
CSSCSSCSS-in-JSCSS-in-JS
```

/*

* Note: Importing from the CDN in production is not recommended.

* It's intended for prototyping only.

*/

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/blue.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/green.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/yellow.css";

:root {

--accent-1: var(--blue-1);

--accent-2: var(--blue-2);

--info-1: var(--blue-1);

--info-2: var(--blue-2);

--success-1: var(--green-1);

--success-2: var(--green-2);

--valid-1: var(--green-1);

--valid-2: var(--green-2);

--warning-1: var(--yellow-1);

--warning-2: var(--yellow-2);

--pending-1: var(--yellow-1);

--pending-2: var(--yellow-2);

}


```

Or you can simply recommend that your teammates defer to the original scale name for situations where there is no appropriate semantic alias.
## [Use case aliases](https://www.radix-ui.com/colors/docs/overview/aliasing#use-case-aliases)
Each step in Radix Colors scales is designed for a specific use case. To help your team know which step to use, you can provide aliases based on the designed use cases.
CSSCSSCSS-in-JSCSS-in-JS
```

/*

* Note: Importing from the CDN in production is not recommended.

* It's intended for prototyping only.

*/

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/blue.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/green.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/yellow.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/red.css";

:root {

--accent-base: var(--blue-1);

--accent-bg-subtle: var(--blue-2);

--accent-bg: var(--blue-3);

--accent-bg-hover: var(--blue-4);

--accent-bg-active: var(--blue-5);

--accent-line: var(--blue-6);

--accent-border: var(--blue-7);

--accent-border-hover: var(--blue-8);

--accent-solid: var(--blue-9);

--accent-solid-hover: var(--blue-10);

--accent-text: var(--blue-11);

--accent-text-contrast: var(--blue-12);

--success-base: var(--green-1);

--success-bg-subtle: var(--green-2);

/* repeat for all steps */

--warning-base: var(--yellow-1);

--warning-bg-subtle: var(--yellow-2);

/* repeat for all steps */

--danger-base: var(--red-1);

--danger-bg-subtle: var(--red-2);

/* repeat for all steps */

}


```

Again, with this approach, you will likely run into issues where you need to use the same step for multiple use cases. Common examples include:
  * Step 9 is designed for solid backgrounds, but it also may work for input placeholder text.
  * Step 8 is designed for hovered component borders, but it also works well for focus rings.


In these cases, you can choose to define multiple aliases which map to the same step.
CSSCSSCSS-in-JSCSS-in-JS
```

/*

* Note: Importing from the CDN in production is not recommended.

* It's intended for prototyping only.

*/

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/gray.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/blue.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/green.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/yellow.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/red.css";

:root {

--gray-solid: var(--gray-9);

--gray-placeholder-text: var(--gray-9);

--accent-border-hover: var(--blue-8);

--accent-focus-ring: var(--blue-8);

}


```

Or you can simply recommend that your teammates defer to the original step number for situations where use cases don't have an alias.
## [Mutable aliases](https://www.radix-ui.com/colors/docs/overview/aliasing#mutable-aliases)
When designing for both light and dark modes, you sometimes need to map a variable to one color in light mode, and another color in dark mode. Common examples include:
  * Components that have a white background in light mode and a subtle gray background in dark mode. For example, Card, Popover, DropdownMenu, HoverCard, Dialog etc.
  * Components that have a transparent black background in light mode and a transparent white background in dark mode. For example, Tooltip.
  * Shadows that are saturated, transparent gray in light mode, and pure black in dark mode.
  * An overlay that is light transparent black in light mode, and a darker transparent black in dark mode.


CSSCSSCSS-in-JSCSS-in-JS
```

/*

* Note: Importing from the CDN in production is not recommended.

* It's intended for prototyping only.

*/

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/slate.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/slate-alpha.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/white-alpha.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/black-alpha.css";

:root {

--panel: white;

--panel-contrast: var(--black-a9);

--shadow: var(--slate-a3);

--overlay: var(--black-a8);

}

.dark {

/* Remap your colors for dark mode */

--panel: var(--slate-2);

--panel-contrast: var(--white-a9);

--shadow: black;

--overlay: var(--black-a11);

}

```

Avoid using specific variable names like "CardBg", or "Tooltip", because you will likely need to use each variable for multiple use cases.
## [Renaming scales](https://www.radix-ui.com/colors/docs/overview/aliasing#renaming-scales)
If you wish, you can rename scales. Reasons might include:
  * Rename a saturated gray to `gray` to keep things simple.
  * Rename `sky` or `grass` to `blue` or `green` to keep the naming intuitive.
  * Rename a scale to match your brand, like how Discord use `blurple`.


CSSCSSCSS-in-JSCSS-in-JS
```

/*

* Note: Importing from the CDN in production is not recommended.

* It's intended for prototyping only.

*/

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/slate.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/sky.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/grass.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/violet.css";

@import "https://cdn.jsdelivr.net/npm/@radix-ui/colors@latest/crimson.css";

:root {

--gray-1: var(--slate-1);

--gray-2: var(--slate-2);

--blue-1: var(--sky-1);

--blue-2: var(--sky-2);

--green-1: var(--grass-1);

--green-2: var(--grass-2);

--blurple-1: var(--violet-1);

--blurple-2: var(--violet-2);

--caribbean-sunset-1: var(--crimson-1);

--caribbean-sunset-2: var(--crimson-2);

}


```

#### Quick nav
  * [Semantic aliases](https://www.radix-ui.com/colors/docs/overview/aliasing#semantic-aliases)
  * [Use case aliases](https://www.radix-ui.com/colors/docs/overview/aliasing#use-case-aliases)
  * [Mutable aliases](https://www.radix-ui.com/colors/docs/overview/aliasing#mutable-aliases)
  * [Renaming scales](https://www.radix-ui.com/colors/docs/overview/aliasing#renaming-scales)


Previous[Usage](https://www.radix-ui.com/colors/docs/overview/usage)
Next[Custom palettes](https://www.radix-ui.com/colors/docs/overview/custom-palettes)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/colors/docs/overview/aliasing.mdx "Edit this page on GitHub.")

