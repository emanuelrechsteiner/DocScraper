---
url: https://www.radix-ui.com/colors/docs/overview/custom-palettes
scraped_at: 2025-06-07T09:40:16.924540
title: Custom palettes – Radix Colors
---

[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[Radix Homepage](https://www.radix-ui.com/)[Made by WorkOS](https://workos.com)
[ThemesThemes](https://www.radix-ui.com/)[PrimitivesPrimitives](https://www.radix-ui.com/primitives)[IconsIcons](https://www.radix-ui.com/icons)[ColorsColors](https://www.radix-ui.com/colors)
[Documentation](https://www.radix-ui.com/colors/docs)[Custom palette](https://www.radix-ui.com/colors/custom)[Blog](https://www.radix-ui.com/blog)[](https://github.com/radix-ui/colors)
#### Overview
[Installation](https://www.radix-ui.com/colors/docs/overview/installation)[Usage](https://www.radix-ui.com/colors/docs/overview/usage)[Aliasing](https://www.radix-ui.com/colors/docs/overview/aliasing)[Custom palettes](https://www.radix-ui.com/colors/docs/overview/custom-palettes)[Releases](https://www.radix-ui.com/colors/docs/overview/releases)
#### Palette composition
[Scales](https://www.radix-ui.com/colors/docs/palette-composition/scales)[Composing a palette](https://www.radix-ui.com/colors/docs/palette-composition/composing-a-palette)[Understanding the scale](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale)
# Custom palettes
Learn how to create custom Radix Colors palettes.
Use the [custom color palette tool](https://www.radix-ui.com/colors/custom) to generate a Radix Colors scale based just on a couple reference colors. Once you are happy with the result, paste the generated CSS into your project and use them the same way you would use the regular Radix Colors scales.
The generated scales are based on the Radix Colors scales themselves, so they will work well with similar component designs. As long as you use a reasonable background color, the contrast ratios will be similar to what Radix Colors provide.
## [What you get](https://www.radix-ui.com/colors/docs/overview/custom-palettes#what-you-get)
Your custom color palette will include Radix Colors steps 1 through 12, as well as their alpha variants and wide-gamut color definitions. Wide-gamut color definitions are needed to ensure that alpha colors are displayed with full saturation in wide-gamut color spaces, such as on Apple’s displays that support P3. This is because alpha blending works differently in P3 than in sRGB.
Learn about the base palette composition in the [Understanding the scale](https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale) guide. The generated CSS also includes a few extra colors used exclusively in [Radix Themes](https://www.radix-ui.com/themes/docs), such as:
  * Surface color, used by certain `variant="surface"` components
  * Indicator color, used by components like Checkbox, Radio, and Tabs
  * Track color, used by components like Slider and Progress Bar


Feel free to remove colors from the generated CSS that you don’t need.
## [Color formats](https://www.radix-ui.com/colors/docs/overview/custom-palettes#color-formats)
You can use any common CSS color format in the input fields, or even wide-gamut color spaces, such as `color(display-p3 1 0.5 0)`. The generated CSS will provide the closest sRGB fallbacks.
## [Dark theme](https://www.radix-ui.com/colors/docs/overview/custom-palettes#dark-theme)
To generate dark theme colors, toggle the appearance to dark in the website header. Make sure to paste the generated CSS after your light theme color overrides.
#### Quick nav
  * [What you get](https://www.radix-ui.com/colors/docs/overview/custom-palettes#what-you-get)
  * [Color formats](https://www.radix-ui.com/colors/docs/overview/custom-palettes#color-formats)
  * [Dark theme](https://www.radix-ui.com/colors/docs/overview/custom-palettes#dark-theme)


Previous[Aliasing](https://www.radix-ui.com/colors/docs/overview/aliasing)
Next[Releases](https://www.radix-ui.com/colors/docs/overview/releases)
[Edit this page on GitHub.](https://github.com/radix-ui/website/edit/main/data/colors/docs/overview/custom-palettes.mdx "Edit this page on GitHub.")

