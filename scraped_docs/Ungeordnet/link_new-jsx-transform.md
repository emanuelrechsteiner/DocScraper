---
url: https://react.dev/link/new-jsx-transform
scraped_at: 2025-05-25T08:51:09.308043
title: Introducing the New JSX Transform – React Blog
---

[](https://surveys.savanta.com/survey/selfserve/21e3/210643?list=2)We want to hear from you![Take our 2021 Community Survey!](https://surveys.savanta.com/survey/selfserve/21e3/210643?list=2)
This site is no longer updated.[Go to react.dev](https://react.dev/blog/2023/03/16/introducing-react-dev)
[![](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)React](https://legacy.reactjs.org/)[Docs](https://legacy.reactjs.org/docs/getting-started.html)[Tutorial](https://legacy.reactjs.org/tutorial/tutorial.html)[Blog](https://legacy.reactjs.org/blog/)[Community](https://legacy.reactjs.org/community/support.html)
[v18.2.0](https://legacy.reactjs.org/versions)[ Languages](https://legacy.reactjs.org/languages)[GitHub](https://github.com/facebook/react/)
# Introducing the New JSX Transform
September 22, 2020 by [Luna Ruan](https://twitter.com/lunaruan)
> This blog site has been archived. Go to [react.dev/blog](https://react.dev/blog) to see the recent posts.
Although React 17 [doesn’t contain new features](https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html), it will provide support for a new version of the JSX transform. In this post, we will describe what it is and how to try it.
## [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#whats-a-jsx-transform)What’s a JSX Transform? 
Browsers don’t understand JSX out of the box, so most React users rely on a compiler like Babel or TypeScript to **transform JSX code into regular JavaScript**. Many preconfigured toolkits like Create React App or Next.js also include a JSX transform under the hood.
Together with the React 17 release, we’ve wanted to make a few improvements to the JSX transform, but we didn’t want to break existing setups. This is why we [worked with Babel](https://babeljs.io/blog/2020/03/16/7.9.0#a-new-jsx-transform-11154httpsgithubcombabelbabelpull11154) to **offer a new, rewritten version of the JSX transform** for people who would like to upgrade.
Upgrading to the new transform is completely optional, but it has a few benefits:
  * With the new transform, you can **use JSX without importing React**.
  * Depending on your setup, its compiled output may **slightly improve the bundle size**.
  * It will enable future improvements that **reduce the number of concepts** you need to learn React.


**This upgrade will not change the JSX syntax and is not required.** The old JSX transform will keep working as usual, and there are no plans to remove the support for it.
[React 17 RC](https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html) already includes support for the new transform, so go give it a try! To make it easier to adopt, **we’ve also backported its support** to React 16.14.0, React 15.7.0, and React 0.14.10. You can find the upgrade instructions for different tools [below](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#how-to-upgrade-to-the-new-jsx-transform).
Now let’s take a closer look at the differences between the old and the new transform.
## [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#whats-different-in-the-new-transform)What’s Different in the New Transform? 
When you use JSX, the compiler transforms it into React function calls that the browser can understand. **The old JSX transform** turned JSX into `React.createElement(...)` calls.
For example, let’s say your source code looks like this:
```
import React from 'react';
function App() {
 return <h1>Hello World</h1>;
}
```

Under the hood, the old JSX transform turns it into regular JavaScript:
```
import React from 'react';
function App() {
 return React.createElement('h1', null, 'Hello world');
}
```

> Note
> **Your source code doesn’t need to change in any way.** We’re describing how the JSX transform turns your JSX source code into the JavaScript code a browser can understand.
However, this is not perfect:
  * Because JSX was compiled into `React.createElement`, `React` needed to be in scope if you used JSX.
  * There are some [performance improvements and simplifications](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md#motivation) that `React.createElement` does not allow.


To solve these issues, React 17 introduces two new entry points to the React package that are intended to only be used by compilers like Babel and TypeScript. Instead of transforming JSX to `React.createElement`, **the new JSX transform** automatically imports special functions from those new entry points in the React package and calls them.
Let’s say that your source code looks like this:
```
function App() {
 return <h1>Hello World</h1>;
}
```

This is what the new JSX transform compiles it to:
```
// Inserted by a compiler (don't import it yourself!)
import {jsx as _jsx} from 'react/jsx-runtime';
function App() {
 return _jsx('h1', { children: 'Hello world' });
}
```

Note how our original code **did not need to import React** to use JSX anymore! (But we would still need to import React in order to use Hooks or other exports that React provides.)
**This change is fully compatible with all of the existing JSX code** , so you won’t have to change your components. If you’re curious, you can check out the [technical RFC](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md#detailed-design) for more details about how the new transform works.
> Note
> The functions inside `react/jsx-runtime` and `react/jsx-dev-runtime` must only be used by the compiler transform. If you need to manually create elements in your code, you should keep using `React.createElement`. It will continue to work and is not going away.
## [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#how-to-upgrade-to-the-new-jsx-transform)How to Upgrade to the New JSX Transform 
If you aren’t ready to upgrade to the new JSX transform or if you are using JSX for another library, don’t worry. The old transform will not be removed and will continue to be supported.
If you want to upgrade, you will need two things:
  * **A version of React that supports the new transform** ([React 17 RC](https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html) and higher supports it, but we’ve also released React 16.14.0, React 15.7.0, and React 0.14.10 for people who are still on the older major versions).
  * **A compatible compiler** (see instructions for different tools below).


Since the new JSX transform doesn’t require React to be in scope, [we’ve also prepared an automated script](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#removing-unused-react-imports) that will remove the unnecessary imports from your codebase.
### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#create-react-app)Create React App 
Create React App [4.0.0](https://github.com/facebook/create-react-app/releases/tag/v4.0.0)+ uses the new transform for compatible React versions.
### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#nextjs)Next.js 
Next.js [v9.5.3](https://github.com/vercel/next.js/releases/tag/v9.5.3)+ uses the new transform for compatible React versions.
### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#gatsby)Gatsby 
Gatsby [v2.24.5](https://github.com/gatsbyjs/gatsby/blob/master/packages/gatsby/CHANGELOG.md#22452-2020-08-28)+ uses the new transform for compatible React versions.
> Note
> If you get [this Gatsby error](https://github.com/gatsbyjs/gatsby/issues/26979) after upgrading to React 17 RC, run `npm update` to fix it.
### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#manual-babel-setup)Manual Babel Setup 
Support for the new JSX transform is available in Babel [v7.9.0](https://babeljs.io/blog/2020/03/16/7.9.0) and above.
First, you’ll need to update to the latest Babel and plugin transform.
If you are using `@babel/plugin-transform-react-jsx`:
```
# for npm users
npm update @babel/core @babel/plugin-transform-react-jsx
```

```
# for yarn users
yarn upgrade @babel/core @babel/plugin-transform-react-jsx
```

If you are using `@babel/preset-react`:
```
# for npm users
npm update @babel/core @babel/preset-react
```

```
# for yarn users
yarn upgrade @babel/core @babel/preset-react
```

Currently, the old transform `{"runtime": "classic"}` is the default option. To enable the new transform, you can pass `{"runtime": "automatic"}` as an option to `@babel/plugin-transform-react-jsx` or `@babel/preset-react`:
```
// If you are using @babel/preset-react
{
 "presets": [
  ["@babel/preset-react", {
   "runtime": "automatic"
  }]
 ]
}
```

```
// If you're using @babel/plugin-transform-react-jsx
{
 "plugins": [
  ["@babel/plugin-transform-react-jsx", {
   "runtime": "automatic"
  }]
 ]
}
```

Starting from Babel 8, `"automatic"` will be the default runtime for both plugins. For more information, check out the Babel documentation for [@babel/plugin-transform-react-jsx](https://babeljs.io/docs/en/babel-plugin-transform-react-jsx) and [@babel/preset-react](https://babeljs.io/docs/en/babel-preset-react).
> Note
> If you use JSX with a library other than React, you can use [the `importSource` option](https://babeljs.io/docs/en/babel-preset-react#importsource) to import from that library instead — as long as it provides the necessary entry points. Alternatively, you can keep using the classic transform which will continue to be supported.
> If you’re a library author and you are implementing the `/jsx-runtime` entry point for your library, keep in mind that [there is a case](https://github.com/facebook/react/issues/20031#issuecomment-710346866) in which even the new transform has to fall back to `createElement` for backwards compatibility. In that case, it will auto-import `createElement` directly from the _root_ entry point specified by `importSource`.
### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#eslint)ESLint 
If you are using [eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react), the `react/jsx-uses-react` and `react/react-in-jsx-scope` rules are no longer necessary and can be turned off or removed.
```
{
 // ...
 "rules": {
  // ...
  "react/jsx-uses-react": "off",
  "react/react-in-jsx-scope": "off"
 }
}
```

### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#typescript)TypeScript 
TypeScript supports the new JSX transform in [v4.1](https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/#jsx-factories) and up.
### [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#flow)Flow 
Flow supports the new JSX transform in [v0.126.0](https://github.com/facebook/flow/releases/tag/v0.126.0) and up, by adding `react.runtime=automatic` to your Flow configuration options. 
## [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#removing-unused-react-imports)Removing Unused React Imports 
Because the new JSX transform will automatically import the necessary `react/jsx-runtime` functions, React will no longer need to be in scope when you use JSX. This might lead to unused React imports in your code. It doesn’t hurt to keep them, but if you’d like to remove them, we recommend running a [“codemod”](https://medium.com/@cpojer/effective-javascript-codemods-5a6686bb46fb) script to remove them automatically:
```
cd your_project
npx react-codemod update-react-imports
```

> Note
> If you’re getting errors when running the codemod, try specifying a different JavaScript dialect when `npx react-codemod update-react-imports` asks you to choose one. In particular, at this moment the “JavaScript with Flow” setting supports newer syntax than the “JavaScript” setting even if you don’t use Flow. [File an issue](https://github.com/reactjs/react-codemod/issues) if you run into problems.
> Keep in mind that the codemod output will not always match your project’s coding style, so you might want to run [Prettier](https://prettier.io/) after the codemod finishes for consistent formatting.
Running this codemod will:
  * Remove all unused React imports as a result of upgrading to the new JSX transform.
  * Change all default React imports (i.e. `import React from "react"`) to destructured named imports (ex. `import { useState } from "react"`) which is the preferred style going into the future. This codemod **will not** affect the existing namespace imports (i.e. `import * as React from "react"`) which is also a valid style. The default imports will keep working in React 17, but in the longer term we encourage moving away from them.


For example,
```
import React from 'react';
function App() {
 return <h1>Hello World</h1>;
}
```

will be replaced with
```
function App() {
 return <h1>Hello World</h1>;
}
```

If you use some other import from React — for example, a Hook — then the codemod will convert it to a named import.
For example,
```
import React from 'react';
function App() {
 const [text, setText] = React.useState('Hello World');
 return <h1>{text}</h1>;
}
```

will be replaced with
```
import { useState } from 'react';
function App() {
 const [text, setText] = useState('Hello World');
 return <h1>{text}</h1>;
}
```

In addition to cleaning up unused imports, this will also help you prepare for a future major version of React (not React 17) which will support ES Modules and not have a default export.
## [](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#thanks)Thanks 
We’d like to thank Babel, TypeScript, Create React App, Next.js, Gatsby, ESLint, and Flow maintainers for their help implementing and integrating the new JSX transform. We also want to thank the React community for their feedback and discussion on the related [technical RFC](https://github.com/reactjs/rfcs/pull/107).
Is this page useful?[Edit this page](https://github.com/reactjs/reactjs.org/tree/main/content/blog/2020-09-22-introducing-the-new-jsx-transform.md)
Recent Posts
  * [React Labs: What We've Been Working On – June 2022](https://legacy.reactjs.org/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022.html)
  * [React v18.0](https://legacy.reactjs.org/blog/2022/03/29/react-v18.html)
  * [How to Upgrade to React 18](https://legacy.reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html)
  * [React Conf 2021 Recap](https://legacy.reactjs.org/blog/2021/12/17/react-conf-2021-recap.html)
  * [The Plan for React 18](https://legacy.reactjs.org/blog/2021/06/08/the-plan-for-react-18.html)
  * [Introducing Zero-Bundle-Size React Server Components](https://legacy.reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html)
  * [React v17.0](https://legacy.reactjs.org/blog/2020/10/20/react-v17.html)
  * [Introducing the New JSX Transform](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)
  * [React v17.0 Release Candidate: No New Features](https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html)
  * [React v16.13.0](https://legacy.reactjs.org/blog/2020/02/26/react-v16.13.0.html)
  * [All posts ...](https://legacy.reactjs.org/blog/all.html)


Docs
[Installation](https://legacy.reactjs.org/docs/getting-started.html)[Main Concepts](https://legacy.reactjs.org/docs/hello-world.html)[Advanced Guides](https://legacy.reactjs.org/docs/accessibility.html)[API Reference](https://legacy.reactjs.org/docs/react-api.html)[Hooks](https://legacy.reactjs.org/docs/hooks-intro.html)[Testing](https://legacy.reactjs.org/docs/testing.html)[Contributing](https://legacy.reactjs.org/docs/how-to-contribute.html)[FAQ](https://legacy.reactjs.org/docs/faq-ajax.html)
Channels
[GitHub](https://github.com/facebook/react)[Stack Overflow](https://stackoverflow.com/questions/tagged/reactjs)[Discussion Forums](https://reactjs.org/community/support.html#popular-discussion-forums)[Reactiflux Chat](https://discord.gg/reactiflux)[DEV Community](https://dev.to/t/react)[Facebook](https://www.facebook.com/react)[Twitter](https://twitter.com/reactjs)
Community
[Code of Conduct](https://github.com/facebook/react/blob/main/CODE_OF_CONDUCT.md)[Community Resources](https://legacy.reactjs.org/community/support.html)
More
[Tutorial](https://legacy.reactjs.org/tutorial/tutorial.html)[Blog](https://legacy.reactjs.org/blog)[Acknowledgements](https://legacy.reactjs.org/acknowledgements.html)[React Native](https://reactnative.dev/)[Privacy](https://opensource.facebook.com/legal/privacy)[Terms](https://opensource.facebook.com/legal/terms)
[![Facebook Open Source](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)](https://opensource.facebook.com/projects/)
Copyright © 2025 Meta Platforms, Inc.

