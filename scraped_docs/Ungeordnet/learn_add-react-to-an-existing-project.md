---
url: https://react.dev/learn/add-react-to-an-existing-project
scraped_at: 2025-05-25T08:38:24.201526
title: Add React to an Existing Project – React
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
# Add React to an Existing Project[](https://react.dev/learn/add-react-to-an-existing-project#undefined "Link for this heading")
If you want to add some interactivity to your existing project, you don’t have to rewrite it in React. Add React to your existing stack, and render interactive React components anywhere.
### Note
**You need to install[Node.js](https://nodejs.org/en/) for local development.** Although you can [try React](https://react.dev/learn/installation#try-react) online or with a simple HTML page, realistically most JavaScript tooling you’ll want to use for development requires Node.js.
## Using React for an entire subroute of your existing website [](https://react.dev/learn/add-react-to-an-existing-project#using-react-for-an-entire-subroute-of-your-existing-website "Link for Using React for an entire subroute of your existing website ")
Let’s say you have an existing web app at `example.com` built with another server technology (like Rails), and you want to implement all routes starting with `example.com/some-app/` fully with React.
Here’s how we recommend to set it up:
  1. **Build the React part of your app** using one of the [React-based frameworks](https://react.dev/learn/start-a-new-react-project).
  2. **Specify`/some-app` as the _base path_** in your framework’s configuration (here’s how: [Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath), [Gatsby](https://www.gatsbyjs.com/docs/how-to/previews-deploys-hosting/path-prefix/)).
  3. **Configure your server or a proxy** so that all requests under `/some-app/` are handled by your React app.


This ensures the React part of your app can [benefit from the best practices](https://react.dev/learn/start-a-new-react-project#can-i-use-react-without-a-framework) baked into those frameworks.
Many React-based frameworks are full-stack and let your React app take advantage of the server. However, you can use the same approach even if you can’t or don’t want to run JavaScript on the server. In that case, serve the HTML/CSS/JS export ([`next export` output](https://nextjs.org/docs/advanced-features/static-html-export) for Next.js, default for Gatsby) at `/some-app/` instead.
## Using React for a part of your existing page [](https://react.dev/learn/add-react-to-an-existing-project#using-react-for-a-part-of-your-existing-page "Link for Using React for a part of your existing page ")
Let’s say you have an existing page built with another technology (either a server one like Rails, or a client one like Backbone), and you want to render interactive React components somewhere on that page. That’s a common way to integrate React—in fact, it’s how most React usage looked at Meta for many years!
You can do this in two steps:
  1. **Set up a JavaScript environment** that lets you use the [JSX syntax](https://react.dev/learn/writing-markup-with-jsx), split your code into modules with the [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) / [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) syntax, and use packages (for example, React) from the [npm](https://www.npmjs.com/) package registry.
  2. **Render your React components** where you want to see them on the page.


The exact approach depends on your existing page setup, so let’s walk through some details.
### Step 1: Set up a modular JavaScript environment [](https://react.dev/learn/add-react-to-an-existing-project#step-1-set-up-a-modular-javascript-environment "Link for Step 1: Set up a modular JavaScript environment ")
A modular JavaScript environment lets you write your React components in individual files, as opposed to writing all of your code in a single file. It also lets you use all the wonderful packages published by other developers on the [npm](https://www.npmjs.com/) registry—including React itself! How you do this depends on your existing setup:
  * **If your app is already split into files that use`import` statements,** try to use the setup you already have. Check whether writing `<div />` in your JS code causes a syntax error. If it causes a syntax error, you might need to [transform your JavaScript code with Babel](https://babeljs.io/setup), and enable the [Babel React preset](https://babeljs.io/docs/babel-preset-react) to use JSX.
  * **If your app doesn’t have an existing setup for compiling JavaScript modules,** set it up with [Vite](https://vite.dev/). The Vite community maintains [many integrations with backend frameworks](https://github.com/vitejs/awesome-vite#integrations-with-backends), including Rails, Django, and Laravel. If your backend framework is not listed, [follow this guide](https://vite.dev/guide/backend-integration.html) to manually integrate Vite builds with your backend.


To check whether your setup works, run this command in your project folder:
Terminal
Copy
npm install react react-dom
Then add these lines of code at the top of your main JavaScript file (it might be called `index.js` or `main.js`):
index.js
index.js
Reset[Fork](https://codesandbox.io/api/v1/sandboxes/define?parameters=N4IgZglgNgpgziAXKOAnAxgeggOwCYwAeAdAFYLIjoD2OALjPUiBALYAO1qdABMD-lQwAhgwBK1arwC-PMKmqseAciHD0dALR5FmdFAiM6ygNwAdHBcyYeAYVjDUPOgAsYPIhDh1cAcx4AEgAqALIAMgK0DPQWOugArqxGxABG1HgAnsS4ODCoweE8ALwqADx4EABuPBB4RWYgwuzsDQB8pZgVla2mFlY2YowEThnU8U6D6rw0HLRGNTjeIngWNIu8ClLFAmriknQAFHGJyb4wdACisEn0AEIZAJJ4B8pN7MoAlB_mOJt0xEJ8HkDqUXABGVoBGBQKDUAA0PAA7lwoHgOuDWt8LCA4Sw4LdcI4MkgwMIoHAYNJcex1ABrYRnMhwWhIUBraJ0ZjACw8HgNHDCJINRB8kBqDTEAiVBpwnmiyp5OAQWjC0UABmIGrVMrlDVYwlwqoamDQWFwBBI5B1OF5DTgggg7DocFV3JtvNF3kcdCNYpEGk09tQjudPC93GtHtFKXi0BWSFF4q0QZDcB4MbjkY9DQY3l9ScDDqdadzvE0mkYlSK5B0rCztpAMFIMA0-f9yaLoabLZ9IDlVN1IAI7CGjHQhhdCbdUYaSd9AD0wQBOYhgzX1xPt7SKBfL1frnFyhsFlPFhcAVk1B_7svdDSlABEYCOgThx_BXdILNIcXiCQLUGJRBSXJSlqXiFIDDNIESBcOhWCgVkqCiIxmFKABCB8AHlbCCABNAAFC4eDghDWgsUF4Kgcj3VBZZ2h8OhYFaEIMh4N4OkY5j0XouVSjSTIaKjDDyx4PCxicTxvD8HgaTOSJ6HmA5cGcFwvA8QhBXYWAEQgXgzlDIRtPUGA8A-HhyyEj1yiqGo6lnfY2g6LorI6ASMho9EqJo38vH_IkSTJCkqRAU0TToDJYDgYh0DgCg2RQphEBAAAqPg5TSQhAwgAAvPwRTSVBhk0TKfi_SwcHc9L3TAKJNFJVhoAyEU4GERZAzyCAwB-Xl9VQXxcBFAAmNV2EIHrZOEPAKhwXwRTVMq-hwcFqt6xwBpwTQ6Godh5om2r6GynKYGGoaxsWiqXCG1aeD6jatp2va5QO5NcpOngRvO78lpcABmG67twB7dp4BbnrqpVjpFMEAA4vpwcqLBcAAWAH1qB7aQbBmqIbe6GADZ4cR5bzzR_qMce0H9txqGeDBZGiZ-_GyfuzGnpxw7IfesEzvG76KpoAgbpeo7ueIIaYFYC6LHiKAbppaa_E0XADFyQM6G9YbRr5hGlt8_FCUAwLQOkEKGA4KBRBgZhBBEBhNALN4QGkIA&query=file%3D%252Fsrc%252Findex.js%26utm_medium%3Dsandpack&environment=create-react-app "Open in CodeSandbox")
```
import { createRoot } from 'react-dom/client';
// Clear the existing HTML content
document.body.innerHTML = '<div id="app"></div>';
// Render your React component instead
const root = createRoot(document.getElementById('app'));
root.render(<h1>Hello, world</h1>);

```

If the entire content of your page was replaced by a “Hello, world!”, everything worked! Keep reading.
### Note
Integrating a modular JavaScript environment into an existing project for the first time can feel intimidating, but it’s worth it! If you get stuck, try our [community resources](https://react.dev/community) or the [Vite Chat](https://chat.vite.dev/).
### Step 2: Render React components anywhere on the page [](https://react.dev/learn/add-react-to-an-existing-project#step-2-render-react-components-anywhere-on-the-page "Link for Step 2: Render React components anywhere on the page ")
In the previous step, you put this code at the top of your main file:
```

import { createRoot } from 'react-dom/client';
// Clear the existing HTML content
document.body.innerHTML = '<div id="app"></div>';
// Render your React component instead
const root = createRoot(document.getElementById('app'));
root.render(<h1>Hello, world</h1>);

```

Of course, you don’t actually want to clear the existing HTML content!
Delete this code.
Instead, you probably want to render your React components in specific places in your HTML. Open your HTML page (or the server templates that generate it) and add a unique [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id) attribute to any tag, for example:
```

<!-- ... somewhere in your html ... -->
<nav id="navigation"></nav>
<!-- ... more html ... -->

```

This lets you find that HTML element with [`document.getElementById`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) and pass it to [`createRoot`](https://react.dev/reference/react-dom/client/createRoot) so that you can render your own React component inside:
index.jsindex.html
index.js
Reset[Fork](https://codesandbox.io/api/v1/sandboxes/define?parameters=N4IgZglgNgpgziAXKOAnAxgeggOwCYwAeAdAFYLIjoD2OALjPUiBALYAO1qdABMD-lQwAhgwBK1arwC-PMKmqseAciHD0dALR5FmdFAiM6ygNwAdHBbABXHBoi0eAOWEA3CAHNRDnACFhqAAUAJR8Fjw8mJg8ACoA8gAicYg8AIIa1sJQUACePGzssKxGPMI8OG6e3o4ARgHhPEJ01qg4PAA8ABYAjAB8ABIw2dRyCkpiIhoAhO2YPb3mONIWFjQ4cLw6rE7UBDwAvDw66NbF9MQeMHQAokVGvjkAkniByhXuXnQ-ysGLaxuNSS8Q6CETiIGBLY7Ai_CwKKTEIT4GBBdouD7VPwBSK9WE4EAAGhYcF8uACOSQYCycBg0iJ7HUAGthJcyHBaEhQGsGExECBgA0zCAKsUhSkhWoNMQCK4hQTBSBXCi4D4xTwhQAGYhajVyhWsYS4NVCzBoLC4Agkch6trqkBwQQQdh0OBqgW2iJCjYBOjGkCSrQO1BOl08b3cG0RT0gGrWaB4P0BzRBkNwHix-ORqNChgbROTQOO51p3O8TSaRiufbkLZZ6MwUgwDT59SF4PFngNpu-kANOkKgjsRgEOyGV1IMIeu0Bv0APW6AE5iN1tXXpwXtIo54vl6vCQ1o0mU8W5wBWbV7vvy21CmUJGBD5Gj-Bu5ZLQnE0kVVAUxBUqA0nSIDsNYNQGOayIkJ0dCsFAnJULQPJ0Mw7RTEkADCMQAJoAArXDw0Gwb0FhdDBUDEbaXQiHgvTtF8dCwL0ACyeTCOw7CzPRjGzJ01EURE7Q1LsOT8VG7TsL0MSdBAaYMqgLLyewnT5GmZRybw1BgDw_QxExAAyxCzBJB4dO8-R4PsQrvFUXy0EKtGYO8okCRJUkyTwckKWxynudSIxqT6PCadpukGUZomzEJeAiSRcxkRRH4yV-5KUtStJEmapp0DksBwMQ6BwBQXKIUYzAAFSThEQmEMmEAAF64B4KRCagBCoJo1WLG-FhRXk7oRGAiGaFSrDQDkKRwMI6zJiiEBgIsEQGqgHi4CkABMGrsIQC0ecIeB4I1KQal1Kw4D0lU8EtK04JodDUOwR07YN9C1XVMDrWtW0nZYZ1rRdV24Ld92PQ0z2BvV708BtX0WN1Z0AMz_QE11Aw9PDHaDQ0qm9KTdAAHDDSynZ0AAsSPLYDd1oxjtpg69kPdAAbITcOdKe5Mo1TIO01jEO4yTLPE4zHOU8D6NPbzOM8N0n3bbDp00Hs_VyJLDPEGtMCsN9FjWFAF0MvtjWaLgBg4DAyZ0D662bXLRM_YlJJkj-qUAbSQEMBwUCiDAzCgt7mhJmx7AgNIQA&query=file%3D%252Fsrc%252Findex.js%26utm_medium%3Dsandpack&environment=create-react-app "Open in CodeSandbox")
```
import { createRoot } from 'react-dom/client';
function NavigationBar() {
 // TODO: Actually implement a navigation bar
 return <h1>Hello from React!</h1>;
}
const domNode = document.getElementById('navigation');
const root = createRoot(domNode);
root.render(<NavigationBar />);

```

Notice how the original HTML content from `index.html` is preserved, but your own `NavigationBar` React component now appears inside the `<nav id="navigation">` from your HTML. Read the [`createRoot` usage documentation](https://react.dev/reference/react-dom/client/createRoot#rendering-a-page-partially-built-with-react) to learn more about rendering React components inside an existing HTML page.
When you adopt React in an existing project, it’s common to start with small interactive components (like buttons), and then gradually keep “moving upwards” until eventually your entire page is built with React. If you ever reach that point, we recommend migrating to [a React framework](https://react.dev/learn/start-a-new-react-project) right after to get the most out of React.
## Using React Native in an existing native mobile app [](https://react.dev/learn/add-react-to-an-existing-project#using-react-native-in-an-existing-native-mobile-app "Link for Using React Native in an existing native mobile app ")
[React Native](https://reactnative.dev/) can also be integrated into existing native apps incrementally. If you have an existing native app for Android (Java or Kotlin) or iOS (Objective-C or Swift), [follow this guide](https://reactnative.dev/docs/integration-with-existing-apps) to add a React Native screen to it.
[PreviousBuild a React App from Scratch](https://react.dev/learn/build-a-react-app-from-scratch)[NextSetup](https://react.dev/learn/setup)
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
  * [Overview](https://react.dev/learn/add-react-to-an-existing-project)
  * [Using React for an entire subroute of your existing website ](https://react.dev/learn/add-react-to-an-existing-project#using-react-for-an-entire-subroute-of-your-existing-website)
  * [Using React for a part of your existing page ](https://react.dev/learn/add-react-to-an-existing-project#using-react-for-a-part-of-your-existing-page)
  * [Step 1: Set up a modular JavaScript environment ](https://react.dev/learn/add-react-to-an-existing-project#step-1-set-up-a-modular-javascript-environment)
  * [Step 2: Render React components anywhere on the page ](https://react.dev/learn/add-react-to-an-existing-project#step-2-render-react-components-anywhere-on-the-page)
  * [Using React Native in an existing native mobile app ](https://react.dev/learn/add-react-to-an-existing-project#using-react-native-in-an-existing-native-mobile-app)



