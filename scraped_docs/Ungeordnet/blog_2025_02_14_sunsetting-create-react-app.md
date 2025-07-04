---
url: https://react.dev/blog/2025/02/14/sunsetting-create-react-app
scraped_at: 2025-05-25T08:43:00.068323
title: Sunsetting Create React App – React
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
[Blog](https://react.dev/blog)
# Sunsetting Create React App[](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#undefined "Link for this heading")
February 14, 2025 by [Matt Carroll](https://twitter.com/mattcarrollcode) and [Ricky Hanlon](https://bsky.app/profile/ricky.fm)
Today, we’re deprecating [Create React App](https://create-react-app.dev/) for new apps, and encouraging existing apps to migrate to a [framework](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#how-to-migrate-to-a-framework), or to [migrate to a build tool](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#how-to-migrate-to-a-build-tool) like Vite, Parcel, or RSBuild.
We’re also providing docs for when a framework isn’t a good fit for your project, you want to build your own framework, or you just want to learn how React works by [building a React app from scratch](https://react.dev/learn/build-a-react-app-from-scratch).
When we released Create React App in 2016, there was no clear way to build a new React app.
To create a React app, you had to install a bunch of tools and wire them up together yourself to support basic features like JSX, linting, and hot reloading. This was very tricky to do correctly, so the [community](https://github.com/react-boilerplate/react-boilerplate) [created](https://github.com/kriasoft/react-starter-kit) [boilerplates](https://github.com/petehunt/react-boilerplate) for [common](https://github.com/gaearon/react-hot-boilerplate) [setups](https://github.com/erikras/react-redux-universal-hot-example). However, boilerplates were difficult to update and fragmentation made it difficult for React to release new features.
Create React App solved these problems by combining several tools into a single recommended configuration. This allowed apps a simple way to upgrade to new tooling features, and allowed the React team to deploy non-trivial tooling changes (Fast Refresh support, React Hooks lint rules) to the broadest possible audience.
This model became so popular that there’s an entire category of tools working this way today.
## Deprecating Create React App [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#deprecating-create-react-app "Link for Deprecating Create React App ")
Although Create React App makes it easy to get started, [there are several limitations](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#limitations-of-build-tools) that make it difficult to build high performant production apps. In principle, we could solve these problems by essentially evolving it into a [framework](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#why-we-recommend-frameworks).
However, since Create React App currently has no active maintainers, and there are many existing frameworks that solve these problems already, we’ve decided to deprecate Create React App.
Starting today, if you install a new app, you will see a deprecation warning:
Console
create-react-app is deprecated. You can find a list of up-to-date React frameworks on react.dev For more info see: react.dev/link/cra This error message will only be shown once per install.
We’ve also added a deprecation notice to the Create React App [website](https://create-react-app.dev/) and GitHub [repo](https://github.com/facebook/create-react-app). Create React App will continue working in maintenance mode, and we’ve published a new version of Create React App to work with React 19.
## How to Migrate to a Framework [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#how-to-migrate-to-a-framework "Link for How to Migrate to a Framework ")
We recommend [creating new React apps](https://react.dev/learn/creating-a-react-app) with a framework. All the frameworks we recommend support client-side rendering ([CSR](https://developer.mozilla.org/en-US/docs/Glossary/CSR)) and single-page apps ([SPA](https://developer.mozilla.org/en-US/docs/Glossary/SPA)), and can be deployed to a CDN or static hosting service without a server.
For existing apps, these guides will help you migrate to a client-only SPA:
  * [Next.js’ Create React App migration guide](https://nextjs.org/docs/app/building-your-application/upgrading/from-create-react-app)
  * [React Router’s framework adoption guide](https://reactrouter.com/upgrading/component-routes).
  * [Expo webpack to Expo Router migration guide](https://docs.expo.dev/router/migrate/from-expo-webpack/)


## How to Migrate to a Build Tool [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#how-to-migrate-to-a-build-tool "Link for How to Migrate to a Build Tool ")
If your app has unusual constraints, or you prefer to solve these problems by building your own framework, or you just want to learn how react works from scratch, you can roll your own custom setup with React using Vite, Parcel or Rsbuild.
For existing apps, these guides will help you migrate to a build tool:
  * [Vite Create React App migration guide](https://www.robinwieruch.de/vite-create-react-app/)
  * [Parcel Create React App migration guide](https://parceljs.org/migration/cra/)
  * [Rsbuild Create React App migration guide](https://rsbuild.dev/guide/migration/cra)


To help get started with Vite, Parcel or Rsbuild, we’ve added new docs for [Building a React App from Scratch](https://react.dev/learn/build-a-react-app-from-scratch).
##### Deep Dive
#### Do I need a framework? [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#do-i-need-a-framework "Link for Do I need a framework? ")
Show Details
Most apps would benefit from a framework, but there are valid cases to build a React app from scratch. A good rule of thumb is if your app needs routing, you would probably benefit from a framework.
Just like Svelte has Sveltekit, Vue has Nuxt, and Solid has SolidStart, [React recommends using a framework](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#why-we-recommend-frameworks) that fully integrates routing into features like data-fetching and code-splitting out of the box. This avoids the pain of needing to write your own complex configurations and essentially build a framework yourself.
However, you can always [build a React app from scratch](https://react.dev/learn/build-a-react-app-from-scratch) using a build tool like Vite, Parcel, or Rsbuild.
Continue reading to learn more about the [limitations of build tools](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#limitations-of-build-tools) and [why we recommend frameworks](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#why-we-recommend-frameworks).
## Limitations of Build Tools [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#limitations-of-build-tools "Link for Limitations of Build Tools ")
Create React App and build tools like it make it easy to get started building a React app. After running `npx create-react-app my-app`, you get a fully configured React app with a development server, linting, and a production build.
For example, if you’re building an internal admin tool, you can start with a landing page:
```

export default function App() {
 return (
  <div>
   <h1>Welcome to the Admin Tool!</h1>
  </div>
 )
}

```

This allows you to immediately start coding in React with features like JSX, default linting rules, and a bundler to run in both development and production. However, this setup is missing the tools you need to build a real production app.
Most production apps need solutions to problems like routing, data fetching, and code splitting.
### Routing [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#routing "Link for Routing ")
Create React App does not include a specific routing solution. If you’re just getting started, one option is to use `useState` to switch between routes. But doing this means that you can’t share links to your app - every link would go to the same page - and structuring your app becomes difficult over time:
```

import {useState} from 'react';
import Home from './Home';
import Dashboard from './Dashboard';
export default function App() {
 // ❌ Routing in state does not create URLs
 const [route, setRoute] = useState('home');
 return (
  <div>
   {route === 'home' && <Home />}
   {route === 'dashboard' && <Dashboard />}
  </div>
 )
}

```

This is why most apps that use Create React App solve add routing with a routing library like [React Router](https://reactrouter.com/) or [Tanstack Router](https://tanstack.com/router/latest). With a routing library, you can add additional routes to the app, which provides opinions on the structure of your app, and allows you to start sharing links to routes. For example, with React Router you can define routes:
```

import {RouterProvider, createBrowserRouter} from 'react-router';
import Home from './Home';
import Dashboard from './Dashboard';
// ✅ Each route has it's own URL
const router = createBrowserRouter([
 {path: '/', element: <Home />},
 {path: '/dashboard', element: <Dashboard />}
]);
export default function App() {
 return (
  <RouterProvider value={router} />
 )
}

```

With this change, you can share a link to `/dashboard` and the app will navigate to the dashboard page . Once you have a routing library, you can add additional features like nested routes, route guards, and route transitions, which are difficult to implement without a routing library.
There’s a tradeoff being made here: the routing library adds complexity to the app, but it also adds features that are difficult to implement without it.
### Data Fetching [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#data-fetching "Link for Data Fetching ")
Another common problem in Create React App is data fetching. Create React App does not include a specific data fetching solution. If you’re just getting started, a common option is to use `fetch` in an effect to load data.
But doing this means that the data is fetched after the component renders, which can cause network waterfalls. Network waterfalls are caused by fetching data when your app renders instead of in parallel while the code is downloading:
```

export default function Dashboard() {
 const [data, setData] = useState(null);
 // ❌ Fetching data in a component causes network waterfalls
 useEffect(() => {
  fetch('/api/data')
   .then(response => response.json())
   .then(data => setData(data));
 }, []);
 return (
  <div>
   {data.map(item => <div key={item.id}>{item.name}</div>)}
  </div>
 )
}

```

Fetching in an effect means the user has to wait longer to see the content, even though the data could have been fetched earlier. To solve this, you can use a data fetching library like [React Query](https://react-query.tanstack.com/), [SWR](https://swr.vercel.app/), [Apollo](https://www.apollographql.com/docs/react), or [Relay](https://relay.dev/) which provide options to prefetch data so the request is started before the component renders.
These libraries work best when integrated with your routing “loader” pattern to specify data dependencies at the route level, which allows the router to optimize your data fetches:
```

export async function loader() {
 const response = await fetch(`/api/data`);
 const data = await response.json();
 return data;
}
// ✅ Fetching data in parallel while the code is downloading
export default function Dashboard({loaderData}) {
 return (
  <div>
   {loaderData.map(item => <div key={item.id}>{item.name}</div>)}
  </div>
 )
}

```

On initial load, the router can fetch the data immediately before the route is rendered. As the user navigates around the app, the router is able to fetch both the data and the route at the same time, parallelizing the fetches. This reduces the time it takes to see the content on the screen, and can improve the user experience.
However, this requires correctly configuring the loaders in your app and trades off complexity for performance.
### Code Splitting [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#code-splitting "Link for Code Splitting ")
Another common problem in Create React App is [code splitting](https://www.patterns.dev/vanilla/bundle-splitting). Create React App does not include a specific code splitting solution. If you’re just getting started, you might not consider code splitting at all.
This means your app is shipped as a single bundle:
```

- bundle.js  75kb

```

But for ideal performance, you should “split” your code into separate bundles so the user only needs to download what they need. This decreases the time the user needs to wait to load your app, by only downloading the code they need to see the page they are on.
```

- core.js   25kb
- home.js   25kb
- dashboard.js 25kb

```

One way to do code-splitting is with `React.lazy`. However, this means that the code is not fetched until the component renders, which can cause network waterfalls. A more optimal solution is to use a router feature that fetches the code in parallel while the code is downloading. For example, React Router provides a `lazy` option to specify that a route should be code split and optimize when it is loaded:
```

import Home from './Home';
import Dashboard from './Dashboard';
// ✅ Routes are downloaded before rendering
const router = createBrowserRouter([
 {path: '/', lazy: () => import('./Home')},
 {path: '/dashboard', lazy: () => import('Dashboard')}
]);

```

Optimized code-splitting is tricky to get right, and it’s easy to make mistakes that can cause the user to download more code than they need. It works best when integrated with your router and data loading solutions to maximize caching, parallelize fetches, and support [“import on interaction”](https://www.patterns.dev/vanilla/import-on-interaction) patterns.
### And more… [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#and-more "Link for And more… ")
These are just a few examples of the limitations of Create React App.
Once you’ve integrated routing, data-fetching, and code splitting, you now also need to consider pending states, navigation interruptions, error messages to the user, and revalidation of the data. There are entire categories of problems that users need to solve like:
  * Accessibility
  * Asset loading
  * Authentication
  * Caching


  * Error handling
  * Mutating data
  * Navigations
  * Optimistic updates


  * Progressive enhancement
  * Server-side rendering
  * Static site generation
  * Streaming


All of these work together to create the most optimal [loading sequence](https://www.patterns.dev/vanilla/loading-sequence).
Solving each of these problems individually in Create React App can be difficult as each problem is interconnected with the others and can require deep expertise in problem areas users may not be familiar with. In order to solve these problems, users end up building their own bespoke solutions on top of Create React App, which was the problem Create React App originally tried to solve.
## Why we Recommend Frameworks [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#why-we-recommend-frameworks "Link for Why we Recommend Frameworks ")
Although you could solve all these pieces yourself in a build tool like Create React App, Vite, or Parcel, it is hard to do well. Just like when Create React App itself integrated several build tools together, you need a tool to integrate all of these features together to provide the best experience to users.
This category of tools that integrates build tools, rendering, routing, data fetching, and code splitting are known as “frameworks” — or if you prefer to call React itself a framework, you might call them “metaframeworks”.
Frameworks impose some opinions about structuring your app in order to provide a much better user experience, in the same way build tools impose some opinions to make tooling easier. This is why we started recommending frameworks like [Next.js](https://nextjs.org/), [React Router](https://reactrouter.com/), and [Expo](https://expo.dev/) for new projects.
Frameworks provide the same getting started experience as Create React App, but also provide solutions to problems users need to solve anyway in real production apps.
##### Deep Dive
#### Server rendering is optional [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#server-rendering-is-optional "Link for Server rendering is optional ")
Show Details
The frameworks we recommend all provide the option to create a [client-side rendered (CSR)](https://developer.mozilla.org/en-US/docs/Glossary/CSR) app.
In some cases, CSR is the right choice for a page, but many times it’s not. Even if most of your app is client-side, there are often individual pages that could benefit from server rendering features like [static-site generation (SSG)](https://developer.mozilla.org/en-US/docs/Glossary/SSG) or [server-side rendering (SSR)](https://developer.mozilla.org/en-US/docs/Glossary/SSR), for example a Terms of Service page, or documentation.
Server rendering generally sends less JavaScript to the client, and a full HTML document which produces a faster [First Contentful Paint (FCP)](https://web.dev/articles/fcp) by reducing [Total Blocking Time (TBD)](https://web.dev/articles/tbt), which can also lower [Interaction to Next Paint (INP)](https://web.dev/articles/inp). This is why the [Chrome team has encouraged](https://web.dev/articles/rendering-on-the-web) developers to consider static or server-side render over a full client-side approach to achieve the best possible performance.
There are tradeoffs to using a server, and it is not always the best option for every page. Generating pages on the server incurs additional cost and takes time to generate which can increase [Time to First Byte (TTFB)](https://web.dev/articles/ttfb). The best performing apps are able to pick the right rendering strategy on a per-page basis, based on the tradeoffs of each strategy.
Frameworks provide the option to use a server on any page if you want to, but do not force you to use a server. This allows you to pick the right rendering strategy for each page in your app.
#### What About Server Components [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#server-components "Link for What About Server Components ")
The frameworks we recommend also include support for React Server Components.
Server Components help solve these problems by moving routing and data fetching to the server, and allowing code splitting to be done for client components based on the data you render, instead of just the route rendered, and reducing the amount of JavaScript shipped for the best possible [loading sequence](https://www.patterns.dev/vanilla/loading-sequence).
Server Components do not require a server. They can be run at build time on your CI server to create a static-site generated app (SSG) app, at runtime on a web server for a server-side rendered (SSR) app.
See [Introducing zero-bundle size React Server Components](https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components) and [the docs](https://react.dev/reference/rsc/server-components) for more info.
### Note
#### Server Rendering is not just for SEO [](https://react.dev/blog/2025/02/14/sunsetting-create-react-app#server-rendering-is-not-just-for-seo "Link for Server Rendering is not just for SEO ")
A common misunderstanding is that server rendering is only for [SEO](https://developer.mozilla.org/en-US/docs/Glossary/SEO).
While server rendering can improve SEO, it also improves performance by reducing the amount of JavaScript the user needs to download and parse before they can see the content on the screen.
This is why the Chrome team [has encouraged](https://web.dev/articles/rendering-on-the-web) developers to consider static or server-side render over a full client-side approach to achieve the best possible performance.
_Thank you to[Dan Abramov](https://bsky.app/profile/danabra.mov) for creating Create React App, and [Joe Haddad](https://github.com/Timer), [Ian Schmitz](https://github.com/ianschmitz), [Brody McKee](https://github.com/mrmckeb), and [many others](https://github.com/facebook/create-react-app/graphs/contributors) for maintaining Create React App over the years. Thank you to [Brooks Lybrand](https://bsky.app/profile/brookslybrand.bsky.social), [Dan Abramov](https://bsky.app/profile/danabra.mov), [Devon Govett](https://bsky.app/profile/devongovett.bsky.social), [Eli White](https://x.com/Eli_White), [Jack Herrington](https://bsky.app/profile/jherr.dev), [Joe Savona](https://x.com/en_JS), [Lauren Tan](https://bsky.app/profile/no.lol), [Lee Robinson](https://x.com/leeerob), [Mark Erikson](https://bsky.app/profile/acemarke.dev), [Ryan Florence](https://x.com/ryanflorence), [Sophie Alpert](https://bsky.app/profile/sophiebits.com), [Tanner Linsley](https://bsky.app/profile/tannerlinsley.com), and [Theo Browne](https://x.com/theo) for reviewing and providing feedback on this post._
[PreviousReact Compiler RC](https://react.dev/blog/2025/04/21/react-compiler-rc)[NextReact 19](https://react.dev/blog/2024/12/05/react-19)
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

