---
url: https://react.dev/learn/build-a-react-app-from-scratch
scraped_at: 2025-05-25T08:30:26.390268
title: Build a React app from Scratch – React
---

Join us for React Conf on Oct 7-8.
[Learn more.](https://conf.react.dev/)
[![logo by @sawaratsuki1004](https://react.dev/_next/image?url=%2Fimages%2Fuwu.png&w=128&q=75)](https://react.dev/)
[React](https://react.dev/)
[v19.1](https://react.dev/versions)
Search`⌘``Ctrl``K`
[Learn](https://react.dev/learn)
[Reference](https://react.dev/reference/react)
[Community](https://react.dev/community)
[Blog](https://react.dev/blog)
[](https://react.dev/community/translations)
[](https://github.com/facebook/react/releases)
### GET STARTED
  * [Quick Start ](https://react.dev/learn "Quick Start")
    * [Tutorial: Tic-Tac-Toe ](https://react.dev/learn/tutorial-tic-tac-toe "Tutorial: Tic-Tac-Toe")
    * [Thinking in React ](https://react.dev/learn/thinking-in-react "Thinking in React")
  * [Installation ](https://react.dev/learn/installation "Installation")
    * [Creating a React App ](https://react.dev/learn/creating-a-react-app "Creating a React App")
    * [Build a React App from Scratch ](https://react.dev/learn/build-a-react-app-from-scratch "Build a React App from Scratch")
    * [Add React to an Existing Project ](https://react.dev/learn/add-react-to-an-existing-project "Add React to an Existing Project")
  * [Setup ](https://react.dev/learn/setup "Setup")
    * [Editor Setup ](https://react.dev/learn/editor-setup "Editor Setup")
    * [Using TypeScript ](https://react.dev/learn/typescript "Using TypeScript")
    * [React Developer Tools ](https://react.dev/learn/react-developer-tools "React Developer Tools")
    * [React Compiler ](https://react.dev/learn/react-compiler "React Compiler")
### LEARN REACT
  * [Describing the UI ](https://react.dev/learn/describing-the-ui "Describing the UI")
    * [Your First Component ](https://react.dev/learn/your-first-component "Your First Component")
    * [Importing and Exporting Components ](https://react.dev/learn/importing-and-exporting-components "Importing and Exporting Components")
    * [Writing Markup with JSX ](https://react.dev/learn/writing-markup-with-jsx "Writing Markup with JSX")
    * [JavaScript in JSX with Curly Braces ](https://react.dev/learn/javascript-in-jsx-with-curly-braces "JavaScript in JSX with Curly Braces")
    * [Passing Props to a Component ](https://react.dev/learn/passing-props-to-a-component "Passing Props to a Component")
    * [Conditional Rendering ](https://react.dev/learn/conditional-rendering "Conditional Rendering")
    * [Rendering Lists ](https://react.dev/learn/rendering-lists "Rendering Lists")
    * [Keeping Components Pure ](https://react.dev/learn/keeping-components-pure "Keeping Components Pure")
    * [Your UI as a Tree ](https://react.dev/learn/understanding-your-ui-as-a-tree "Your UI as a Tree")
  * [Adding Interactivity ](https://react.dev/learn/adding-interactivity "Adding Interactivity")
    * [Responding to Events ](https://react.dev/learn/responding-to-events "Responding to Events")
    * [State: A Component's Memory ](https://react.dev/learn/state-a-components-memory "State: A Component's Memory")
    * [Render and Commit ](https://react.dev/learn/render-and-commit "Render and Commit")
    * [State as a Snapshot ](https://react.dev/learn/state-as-a-snapshot "State as a Snapshot")
    * [Queueing a Series of State Updates ](https://react.dev/learn/queueing-a-series-of-state-updates "Queueing a Series of State Updates")
    * [Updating Objects in State ](https://react.dev/learn/updating-objects-in-state "Updating Objects in State")
    * [Updating Arrays in State ](https://react.dev/learn/updating-arrays-in-state "Updating Arrays in State")
  * [Managing State ](https://react.dev/learn/managing-state "Managing State")
    * [Reacting to Input with State ](https://react.dev/learn/reacting-to-input-with-state "Reacting to Input with State")
    * [Choosing the State Structure ](https://react.dev/learn/choosing-the-state-structure "Choosing the State Structure")
    * [Sharing State Between Components ](https://react.dev/learn/sharing-state-between-components "Sharing State Between Components")
    * [Preserving and Resetting State ](https://react.dev/learn/preserving-and-resetting-state "Preserving and Resetting State")
    * [Extracting State Logic into a Reducer ](https://react.dev/learn/extracting-state-logic-into-a-reducer "Extracting State Logic into a Reducer")
    * [Passing Data Deeply with Context ](https://react.dev/learn/passing-data-deeply-with-context "Passing Data Deeply with Context")
    * [Scaling Up with Reducer and Context ](https://react.dev/learn/scaling-up-with-reducer-and-context "Scaling Up with Reducer and Context")
  * [Escape Hatches ](https://react.dev/learn/escape-hatches "Escape Hatches")
    * [Referencing Values with Refs ](https://react.dev/learn/referencing-values-with-refs "Referencing Values with Refs")
    * [Manipulating the DOM with Refs ](https://react.dev/learn/manipulating-the-dom-with-refs "Manipulating the DOM with Refs")
    * [Synchronizing with Effects ](https://react.dev/learn/synchronizing-with-effects "Synchronizing with Effects")
    * [You Might Not Need an Effect ](https://react.dev/learn/you-might-not-need-an-effect "You Might Not Need an Effect")
    * [Lifecycle of Reactive Effects ](https://react.dev/learn/lifecycle-of-reactive-effects "Lifecycle of Reactive Effects")
    * [Separating Events from Effects ](https://react.dev/learn/separating-events-from-effects "Separating Events from Effects")
    * [Removing Effect Dependencies ](https://react.dev/learn/removing-effect-dependencies "Removing Effect Dependencies")
    * [Reusing Logic with Custom Hooks ](https://react.dev/learn/reusing-logic-with-custom-hooks "Reusing Logic with Custom Hooks")


Is this page useful?
[Learn React](https://react.dev/learn)
[Installation](https://react.dev/learn/installation)
# Build a React app from Scratch[](https://react.dev/learn/build-a-react-app-from-scratch#undefined "Link for this heading")
If your app has constraints not well-served by existing frameworks, you prefer to build your own framework, or you just want to learn the basics of a React app, you can build a React app from scratch.
##### Deep Dive
#### Consider using a framework [](https://react.dev/learn/build-a-react-app-from-scratch#consider-using-a-framework "Link for Consider using a framework ")
Show Details
Starting from scratch is an easy way to get started using React, but a major tradeoff to be aware of is that going this route is often the same as building your own adhoc framework. As your requirements evolve, you may need to solve more framework-like problems that our recommended frameworks already have well developed and supported solutions for.
For example, if in the future your app needs support for server-side rendering (SSR), static site generation (SSG), and/or React Server Components (RSC), you will have to implement those on your own. Similarly, future React features that require integrating at the framework level will have to be implemented on your own if you want to use them.
Our recommended frameworks also help you build better performing apps. For example, reducing or eliminating waterfalls from network requests makes for a better user experience. This might not be a high priority when you are building a toy project, but if your app gains users you may want to improve its performance.
Going this route also makes it more difficult to get support, since the way you develop routing, data-fetching, and other features will be unique to your situation. You should only choose this option if you are comfortable tackling these problems on your own, or if you’re confident that you will never need these features.
For a list of recommended frameworks, check out [Creating a React App](https://react.dev/learn/creating-a-react-app).
## Step 1: Install a build tool [](https://react.dev/learn/build-a-react-app-from-scratch#step-1-install-a-build-tool "Link for Step 1: Install a build tool ")
The first step is to install a build tool like `vite`, `parcel`, or `rsbuild`. These build tools provide features to package and run source code, provide a development server for local development and a build command to deploy your app to a production server.
### Vite [](https://react.dev/learn/build-a-react-app-from-scratch#vite "Link for Vite ")
[Vite](https://vite.dev/) is a build tool that aims to provide a faster and leaner development experience for modern web projects.
Terminal
Copy
npm create vite@latest my-app -- --template react
Vite is opinionated and comes with sensible defaults out of the box. Vite has a rich ecosystem of plugins to support fast refresh, JSX, Babel/SWC, and other common features. See Vite’s [React plugin](https://vite.dev/plugins/#vitejs-plugin-react) or [React SWC plugin](https://vite.dev/plugins/#vitejs-plugin-react-swc) and [React SSR example project](https://vite.dev/guide/ssr.html#example-projects) to get started.
Vite is already being used as a build tool in one of our [recommended frameworks](https://react.dev/learn/creating-a-react-app): [React Router](https://reactrouter.com/start/framework/installation).
### Parcel [](https://react.dev/learn/build-a-react-app-from-scratch#parcel "Link for Parcel ")
[Parcel](https://parceljs.org/) combines a great out-of-the-box development experience with a scalable architecture that can take your project from just getting started to massive production applications.
Terminal
Copy
npm install --save-dev parcel
Parcel supports fast refresh, JSX, TypeScript, Flow, and styling out of the box. See [Parcel’s React recipe](https://parceljs.org/recipes/react/#getting-started) to get started.
### Rsbuild [](https://react.dev/learn/build-a-react-app-from-scratch#rsbuild "Link for Rsbuild ")
[Rsbuild](https://rsbuild.dev/) is an Rspack-powered build tool that provides a seamless development experience for React applications. It comes with carefully tuned defaults and performance optimizations ready to use.
Terminal
Copy
npx create-rsbuild --template react
Rsbuild includes built-in support for React features like fast refresh, JSX, TypeScript, and styling. See [Rsbuild’s React guide](https://rsbuild.dev/guide/framework/react) to get started.
### Note
#### Metro for React Native [](https://react.dev/learn/build-a-react-app-from-scratch#react-native "Link for Metro for React Native ")
If you’re starting from scratch with React Native you’ll need to use [Metro](https://metrobundler.dev/), the JavaScript bundler for React Native. Metro supports bundling for platforms like iOS and Android, but lacks many features when compared to the tools here. We recommend starting with Vite, Parcel, or Rsbuild unless your project requires React Native support.
## Step 2: Build Common Application Patterns [](https://react.dev/learn/build-a-react-app-from-scratch#step-2-build-common-application-patterns "Link for Step 2: Build Common Application Patterns ")
The build tools listed above start off with a client-only, single-page app (SPA), but don’t include any further solutions for common functionality like routing, data fetching, or styling.
The React ecosystem includes many tools for these problems. We’ve listed a few that are widely used as a starting point, but feel free to choose other tools if those work better for you.
### Routing [](https://react.dev/learn/build-a-react-app-from-scratch#routing "Link for Routing ")
Routing determines what content or pages to display when a user visits a particular URL. You need to set up a router to map URLs to different parts of your app. You’ll also need to handle nested routes, route parameters, and query parameters. Routers can be configured within your code, or defined based on your component folder and file structures.
Routers are a core part of modern applications, and are usually integrated with data fetching (including prefetching data for a whole page for faster loading), code splitting (to minimize client bundle sizes), and page rendering approaches (to decide how each page gets generated).
We suggest using:
  * [React Router](https://reactrouter.com/start/data/custom)
  * [Tanstack Router](https://tanstack.com/router/latest)


### Data Fetching [](https://react.dev/learn/build-a-react-app-from-scratch#data-fetching "Link for Data Fetching ")
Fetching data from a server or other data source is a key part of most applications. Doing this properly requires handling loading states, error states, and caching the fetched data, which can be complex.
Purpose-built data fetching libraries do the hard work of fetching and caching the data for you, letting you focus on what data your app needs and how to display it. These libraries are typically used directly in your components, but can also be integrated into routing loaders for faster pre-fetching and better performance, and in server rendering as well.
Note that fetching data directly in components can lead to slower loading times due to network request waterfalls, so we recommend prefetching data in router loaders or on the server as much as possible! This allows a page’s data to be fetched all at once as the page is being displayed.
If you’re fetching data from most backends or REST-style APIs, we suggest using:
  * [React Query](https://react-query.tanstack.com/)
  * [SWR](https://swr.vercel.app/)
  * [RTK Query](https://redux-toolkit.js.org/rtk-query/overview)


If you’re fetching data from a GraphQL API, we suggest using:
  * [Apollo](https://www.apollographql.com/docs/react)
  * [Relay](https://relay.dev/)


### Code-splitting [](https://react.dev/learn/build-a-react-app-from-scratch#code-splitting "Link for Code-splitting ")
Code-splitting is the process of breaking your app into smaller bundles that can be loaded on demand. An app’s code size increases with every new feature and additional dependency. Apps can become slow to load because all of the code for the entire app needs to be sent before it can be used. Caching, reducing features/dependencies, and moving some code to run on the server can help mitigate slow loading but are incomplete solutions that can sacrifice functionality if overused.
Similarly, if you rely on the apps using your framework to split the code, you might encounter situations where loading becomes slower than if no code splitting were happening at all. For example, [lazily loading](https://react.dev/reference/react/lazy) a chart delays sending the code needed to render the chart, splitting the chart code from the rest of the app. [Parcel supports code splitting with React.lazy](https://parceljs.org/recipes/react/#code-splitting). However, if the chart loads its data _after_ it has been initially rendered you are now waiting twice. This is a waterfall: rather than fetching the data for the chart and sending the code to render it simultaneously, you must wait for each step to complete one after the other.
Splitting code by route, when integrated with bundling and data fetching, can reduce the initial load time of your app and the time it takes for the largest visible content of the app to render ([Largest Contentful Paint](https://web.dev/articles/lcp)).
For code-splitting instructions, see your build tool docs:
  * [Vite build optimizations](https://vite.dev/guide/features.html#build-optimizations)
  * [Parcel code splitting](https://parceljs.org/features/code-splitting/)
  * [Rsbuild code splitting](https://rsbuild.dev/guide/optimization/code-splitting)


### Improving Application Performance [](https://react.dev/learn/build-a-react-app-from-scratch#improving-application-performance "Link for Improving Application Performance ")
Since the build tool you select only support single page apps (SPAs) you’ll need to implement other [rendering patterns](https://www.patterns.dev/vanilla/rendering-patterns) like server-side rendering (SSR), static site generation (SSG), and/or React Server Components (RSC). Even if you don’t need these features at first, in the future there may be some routes that would benefit SSR, SSG or RSC.
  * **Single-page apps (SPA)** load a single HTML page and dynamically updates the page as the user interacts with the app. SPAs are easier to get started with, but they can have slower initial load times. SPAs are the default architecture for most build tools.
  * **Streaming Server-side rendering (SSR)** renders a page on the server and sends the fully rendered page to the client. SSR can improve performance, but it can be more complex to set up and maintain than a single-page app. With the addition of streaming, SSR can be very complex to set up and maintain. See [Vite’s SSR guide](https://vite.dev/guide/ssr).
  * **Static site generation (SSG)** generates static HTML files for your app at build time. SSG can improve performance, but it can be more complex to set up and maintain than server-side rendering. See [Vite’s SSG guide](https://vite.dev/guide/ssr.html#pre-rendering-ssg).
  * **React Server Components (RSC)** lets you mix build-time, server-only, and interactive components in a single React tree. RSC can improve performance, but it currently requires deep expertise to set up and maintain. See [Parcel’s RSC examples](https://github.com/parcel-bundler/rsc-examples).


Your rendering strategies need to integrate with your router so apps built with your framework can choose the rendering strategy on a per-route level. This will enable different rendering strategies without having to rewrite your whole app. For example, the landing page for your app might benefit from being statically generated (SSG), while a page with a content feed might perform best with server-side rendering.
Using the right rendering strategy for the right routes can decrease the time it takes for the first byte of content to be loaded ([Time to First Byte](https://web.dev/articles/ttfb)), the first piece of content to render ([First Contentful Paint](https://web.dev/articles/fcp)), and the largest visible content of the app to render ([Largest Contentful Paint](https://web.dev/articles/lcp)).
### And more… [](https://react.dev/learn/build-a-react-app-from-scratch#and-more "Link for And more… ")
These are just a few examples of the features a new app will need to consider when building from scratch. Many limitations you’ll hit can be difficult to solve as each problem is interconnected with the others and can require deep expertise in problem areas you may not be familiar with.
If you don’t want to solve these problems on your own, you can [get started with a framework](https://react.dev/learn/creating-a-react-app) that provides these features out of the box.
[PreviousCreating a React App](https://react.dev/learn/creating-a-react-app)[NextAdd React to an Existing Project](https://react.dev/learn/add-react-to-an-existing-project)
[](https://opensource.fb.com/)
Copyright © Meta Platforms, Inc
no uwu plz
uwu?
Logo by[@sawaratsuki1004](https://twitter.com/sawaratsuki1004)
[Learn React](https://react.dev/learn)
[Quick Start](https://react.dev/learn)
[Installation](https://react.dev/learn/installation)
[Describing the UI](https://react.dev/learn/describing-the-ui)
[Adding Interactivity](https://react.dev/learn/adding-interactivity)
[Managing State](https://react.dev/learn/managing-state)
[Escape Hatches](https://react.dev/learn/escape-hatches)
[API Reference](https://react.dev/reference/react)
[React APIs](https://react.dev/reference/react)
[React DOM APIs](https://react.dev/reference/react-dom)
[Community](https://react.dev/community)
[Code of Conduct](https://github.com/facebook/react/blob/main/CODE_OF_CONDUCT.md)
[Meet the Team](https://react.dev/community/team)
[Docs Contributors](https://react.dev/community/docs-contributors)
[Acknowledgements](https://react.dev/community/acknowledgements)
More
[Blog](https://react.dev/blog)
[React Native](https://reactnative.dev/)
[Privacy](https://opensource.facebook.com/legal/privacy)
[Terms](https://opensource.fb.com/legal/terms/)
[](https://www.facebook.com/react)[](https://twitter.com/reactjs)[](https://bsky.app/profile/react.dev)[](https://github.com/facebook/react)
## On this page
  * [Overview](https://react.dev/learn/build-a-react-app-from-scratch)
  * [Step 1: Install a build tool ](https://react.dev/learn/build-a-react-app-from-scratch#step-1-install-a-build-tool)
  * [Vite ](https://react.dev/learn/build-a-react-app-from-scratch#vite)
  * [Parcel ](https://react.dev/learn/build-a-react-app-from-scratch#parcel)
  * [Rsbuild ](https://react.dev/learn/build-a-react-app-from-scratch#rsbuild)
  * [Step 2: Build Common Application Patterns ](https://react.dev/learn/build-a-react-app-from-scratch#step-2-build-common-application-patterns)
  * [Routing ](https://react.dev/learn/build-a-react-app-from-scratch#routing)
  * [Data Fetching ](https://react.dev/learn/build-a-react-app-from-scratch#data-fetching)
  * [Code-splitting ](https://react.dev/learn/build-a-react-app-from-scratch#code-splitting)
  * [Improving Application Performance ](https://react.dev/learn/build-a-react-app-from-scratch#improving-application-performance)
  * [And more… ](https://react.dev/learn/build-a-react-app-from-scratch#and-more)



