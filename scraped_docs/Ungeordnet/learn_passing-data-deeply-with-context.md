---
url: https://react.dev/learn/passing-data-deeply-with-context
scraped_at: 2025-05-25T08:42:34.311278
title: Passing Data Deeply with Context – React
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
[Managing State](https://react.dev/learn/managing-state)
# Passing Data Deeply with Context[](https://react.dev/learn/passing-data-deeply-with-context#undefined "Link for this heading")
Usually, you will pass information from a parent component to a child component via props. But passing props can become verbose and inconvenient if you have to pass them through many components in the middle, or if many components in your app need the same information. _Context_ lets the parent component make some information available to any component in the tree below it—no matter how deep—without passing it explicitly through props.
### You will learn
  * What “prop drilling” is
  * How to replace repetitive prop passing with context
  * Common use cases for context
  * Common alternatives to context


## The problem with passing props [](https://react.dev/learn/passing-data-deeply-with-context#the-problem-with-passing-props "Link for The problem with passing props ")
[Passing props](https://react.dev/learn/passing-props-to-a-component) is a great way to explicitly pipe data through your UI tree to the components that use it.
But passing props can become verbose and inconvenient when you need to pass some prop deeply through the tree, or if many components need the same prop. The nearest common ancestor could be far removed from the components that need data, and [lifting state up](https://react.dev/learn/sharing-state-between-components) that high can lead to a situation called “prop drilling”.
Lifting state up
![Diagram with a tree of three components. The parent contains a bubble representing a value highlighted in purple. The value flows down to each of the two children, both highlighted in purple.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_lifting_state.dark.png&w=1920&q=75)
![Diagram with a tree of three components. The parent contains a bubble representing a value highlighted in purple. The value flows down to each of the two children, both highlighted in purple.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_lifting_state.png&w=1920&q=75)
Prop drilling
![Diagram with a tree of ten nodes, each node with two children or less. The root node contains a bubble representing a value highlighted in purple. The value flows down through the two children, each of which pass the value but do not contain it. The left child passes the value down to two children which are both highlighted purple. The right child of the root passes the value through to one of its two children - the right one, which is highlighted purple. That child passed the value through its single child, which passes it down to both of its two children, which are highlighted purple.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_prop_drilling.dark.png&w=1920&q=75)
![Diagram with a tree of ten nodes, each node with two children or less. The root node contains a bubble representing a value highlighted in purple. The value flows down through the two children, each of which pass the value but do not contain it. The left child passes the value down to two children which are both highlighted purple. The right child of the root passes the value through to one of its two children - the right one, which is highlighted purple. That child passed the value through its single child, which passes it down to both of its two children, which are highlighted purple.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_prop_drilling.png&w=1920&q=75)
Wouldn’t it be great if there were a way to “teleport” data to the components in the tree that need it without passing props? With React’s context feature, there is!
## Context: an alternative to passing props [](https://react.dev/learn/passing-data-deeply-with-context#context-an-alternative-to-passing-props "Link for Context: an alternative to passing props ")
Context lets a parent component provide data to the entire tree below it. There are many uses for context. Here is one example. Consider this `Heading` component that accepts a `level` for its size:
App.jsSection.jsHeading.js
App.js
ResetFork
```
import Heading from './Heading.js';
import Section from './Section.js';
export default function Page() {
 return (
  <Section>
   <Heading level={1}>Title</Heading>
   <Heading level={2}>Heading</Heading>
   <Heading level={3}>Sub-heading</Heading>
   <Heading level={4}>Sub-sub-heading</Heading>
   <Heading level={5}>Sub-sub-sub-heading</Heading>
   <Heading level={6}>Sub-sub-sub-sub-heading</Heading>
  </Section>
 );
}

```

Let’s say you want multiple headings within the same `Section` to always have the same size:
App.jsSection.jsHeading.js
App.js
ResetFork
```
import Heading from './Heading.js';
import Section from './Section.js';
export default function Page() {
 return (
  <Section>
   <Heading level={1}>Title</Heading>
   <Section>
    <Heading level={2}>Heading</Heading>
    <Heading level={2}>Heading</Heading>
    <Heading level={2}>Heading</Heading>
    <Section>
     <Heading level={3}>Sub-heading</Heading>
     <Heading level={3}>Sub-heading</Heading>
     <Heading level={3}>Sub-heading</Heading>
     <Section>
      <Heading level={4}>Sub-sub-heading</Heading>
      <Heading level={4}>Sub-sub-heading</Heading>
      <Heading level={4}>Sub-sub-heading</Heading>
     </Section>
    </Section>
   </Section>
  </Section>
 );
}

```

Show more
Currently, you pass the `level` prop to each `<Heading>` separately:
```

<Section>
 <Heading level={3}>About</Heading>
 <Heading level={3}>Photos</Heading>
 <Heading level={3}>Videos</Heading>
</Section>

```

It would be nice if you could pass the `level` prop to the `<Section>` component instead and remove it from the `<Heading>`. This way you could enforce that all headings in the same section have the same size:
```

<Section level={3}>
 <Heading>About</Heading>
 <Heading>Photos</Heading>
 <Heading>Videos</Heading>
</Section>

```

But how can the `<Heading>` component know the level of its closest `<Section>`? **That would require some way for a child to “ask” for data from somewhere above in the tree.**
You can’t do it with props alone. This is where context comes into play. You will do it in three steps:
  1. **Create** a context. (You can call it `LevelContext`, since it’s for the heading level.)
  2. **Use** that context from the component that needs the data. (`Heading` will use `LevelContext`.)
  3. **Provide** that context from the component that specifies the data. (`Section` will provide `LevelContext`.)


Context lets a parent—even a distant one!—provide some data to the entire tree inside of it.
Using context in close children
![Diagram with a tree of three components. The parent contains a bubble representing a value highlighted in orange which projects down to the two children, each highlighted in orange.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_context_close.dark.png&w=1920&q=75)
![Diagram with a tree of three components. The parent contains a bubble representing a value highlighted in orange which projects down to the two children, each highlighted in orange.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_context_close.png&w=1920&q=75)
Using context in distant children
![Diagram with a tree of ten nodes, each node with two children or less. The root parent node contains a bubble representing a value highlighted in orange. The value projects down directly to four leaves and one intermediate component in the tree, which are all highlighted in orange. None of the other intermediate components are highlighted.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_context_far.dark.png&w=1920&q=75)
![Diagram with a tree of ten nodes, each node with two children or less. The root parent node contains a bubble representing a value highlighted in orange. The value projects down directly to four leaves and one intermediate component in the tree, which are all highlighted in orange. None of the other intermediate components are highlighted.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpassing_data_context_far.png&w=1920&q=75)
### Step 1: Create the context [](https://react.dev/learn/passing-data-deeply-with-context#step-1-create-the-context "Link for Step 1: Create the context ")
First, you need to create the context. You’ll need to **export it from a file** so that your components can use it:
App.jsSection.jsHeading.jsLevelContext.js
LevelContext.js
ResetFork
```
import { createContext } from 'react';
export const LevelContext = createContext(1);

```

The only argument to `createContext` is the _default_ value. Here, `1` refers to the biggest heading level, but you could pass any kind of value (even an object). You will see the significance of the default value in the next step.
### Step 2: Use the context [](https://react.dev/learn/passing-data-deeply-with-context#step-2-use-the-context "Link for Step 2: Use the context ")
Import the `useContext` Hook from React and your context:
```

import { useContext } from 'react';
import { LevelContext } from './LevelContext.js';

```

Currently, the `Heading` component reads `level` from props:
```

export default function Heading({ level, children }) {
 // ...
}

```

Instead, remove the `level` prop and read the value from the context you just imported, `LevelContext`:
```

export default function Heading({ children }) {
 const level = useContext(LevelContext);
 // ...
}

```

`useContext` is a Hook. Just like `useState` and `useReducer`, you can only call a Hook immediately inside a React component (not inside loops or conditions). **`useContext`tells React that the`Heading` component wants to read the `LevelContext`.**
Now that the `Heading` component doesn’t have a `level` prop, you don’t need to pass the level prop to `Heading` in your JSX like this anymore:
```

<Section>
 <Heading level={4}>Sub-sub-heading</Heading>
 <Heading level={4}>Sub-sub-heading</Heading>
 <Heading level={4}>Sub-sub-heading</Heading>
</Section>

```

Update the JSX so that it’s the `Section` that receives it instead:
```

<Section level={4}>
 <Heading>Sub-sub-heading</Heading>
 <Heading>Sub-sub-heading</Heading>
 <Heading>Sub-sub-heading</Heading>
</Section>

```

As a reminder, this is the markup that you were trying to get working:
App.jsSection.jsHeading.jsLevelContext.js
App.js
ResetFork
```
import Heading from './Heading.js';
import Section from './Section.js';
export default function Page() {
 return (
  <Section level={1}>
   <Heading>Title</Heading>
   <Section level={2}>
    <Heading>Heading</Heading>
    <Heading>Heading</Heading>
    <Heading>Heading</Heading>
    <Section level={3}>
     <Heading>Sub-heading</Heading>
     <Heading>Sub-heading</Heading>
     <Heading>Sub-heading</Heading>
     <Section level={4}>
      <Heading>Sub-sub-heading</Heading>
      <Heading>Sub-sub-heading</Heading>
      <Heading>Sub-sub-heading</Heading>
     </Section>
    </Section>
   </Section>
  </Section>
 );
}

```

Show more
Notice this example doesn’t quite work, yet! All the headings have the same size because **even though you’re _using_ the context, you have not _provided_ it yet.** React doesn’t know where to get it!
If you don’t provide the context, React will use the default value you’ve specified in the previous step. In this example, you specified `1` as the argument to `createContext`, so `useContext(LevelContext)` returns `1`, setting all those headings to `<h1>`. Let’s fix this problem by having each `Section` provide its own context.
### Step 3: Provide the context [](https://react.dev/learn/passing-data-deeply-with-context#step-3-provide-the-context "Link for Step 3: Provide the context ")
The `Section` component currently renders its children:
```

export default function Section({ children }) {
 return (
  <section className="section">
   {children}
  </section>
 );
}

```

**Wrap them with a context provider** to provide the `LevelContext` to them:
```

import { LevelContext } from './LevelContext.js';
export default function Section({ level, children }) {
 return (
  <section className="section">
   <LevelContext value={level}>
    {children}
   </LevelContext>
  </section>
 );
}

```

This tells React: “if any component inside this `<Section>` asks for `LevelContext`, give them this `level`.” The component will use the value of the nearest `<LevelContext>` in the UI tree above it.
App.jsSection.jsHeading.jsLevelContext.js
App.js
ResetFork
```
import Heading from './Heading.js';
import Section from './Section.js';
export default function Page() {
 return (
  <Section level={1}>
   <Heading>Title</Heading>
   <Section level={2}>
    <Heading>Heading</Heading>
    <Heading>Heading</Heading>
    <Heading>Heading</Heading>
    <Section level={3}>
     <Heading>Sub-heading</Heading>
     <Heading>Sub-heading</Heading>
     <Heading>Sub-heading</Heading>
     <Section level={4}>
      <Heading>Sub-sub-heading</Heading>
      <Heading>Sub-sub-heading</Heading>
      <Heading>Sub-sub-heading</Heading>
     </Section>
    </Section>
   </Section>
  </Section>
 );
}

```

Show more
It’s the same result as the original code, but you did not need to pass the `level` prop to each `Heading` component! Instead, it “figures out” its heading level by asking the closest `Section` above:
  1. You pass a `level` prop to the `<Section>`.
  2. `Section` wraps its children into `<LevelContext value={level}>`.
  3. `Heading` asks the closest value of `LevelContext` above with `useContext(LevelContext)`.


## Using and providing context from the same component [](https://react.dev/learn/passing-data-deeply-with-context#using-and-providing-context-from-the-same-component "Link for Using and providing context from the same component ")
Currently, you still have to specify each section’s `level` manually:
```

export default function Page() {
 return (
  <Section level={1}>
   ...
   <Section level={2}>
    ...
    <Section level={3}>
     ...

```

Since context lets you read information from a component above, each `Section` could read the `level` from the `Section` above, and pass `level + 1` down automatically. Here is how you could do it:
```

import { useContext } from 'react';
import { LevelContext } from './LevelContext.js';
export default function Section({ children }) {
 const level = useContext(LevelContext);
 return (
  <section className="section">
   <LevelContext value={level + 1}>
    {children}
   </LevelContext>
  </section>
 );
}

```

With this change, you don’t need to pass the `level` prop _either_ to the `<Section>` or to the `<Heading>`:
App.jsSection.jsHeading.jsLevelContext.js
App.js
ResetFork
```
import Heading from './Heading.js';
import Section from './Section.js';
export default function Page() {
 return (
  <Section>
   <Heading>Title</Heading>
   <Section>
    <Heading>Heading</Heading>
    <Heading>Heading</Heading>
    <Heading>Heading</Heading>
    <Section>
     <Heading>Sub-heading</Heading>
     <Heading>Sub-heading</Heading>
     <Heading>Sub-heading</Heading>
     <Section>
      <Heading>Sub-sub-heading</Heading>
      <Heading>Sub-sub-heading</Heading>
      <Heading>Sub-sub-heading</Heading>
     </Section>
    </Section>
   </Section>
  </Section>
 );
}

```

Show more
Now both `Heading` and `Section` read the `LevelContext` to figure out how “deep” they are. And the `Section` wraps its children into the `LevelContext` to specify that anything inside of it is at a “deeper” level.
### Note
This example uses heading levels because they show visually how nested components can override context. But context is useful for many other use cases too. You can pass down any information needed by the entire subtree: the current color theme, the currently logged in user, and so on.
## Context passes through intermediate components [](https://react.dev/learn/passing-data-deeply-with-context#context-passes-through-intermediate-components "Link for Context passes through intermediate components ")
You can insert as many components as you like between the component that provides context and the one that uses it. This includes both built-in components like `<div>` and components you might build yourself.
In this example, the same `Post` component (with a dashed border) is rendered at two different nesting levels. Notice that the `<Heading>` inside of it gets its level automatically from the closest `<Section>`:
App.jsSection.jsHeading.jsLevelContext.js
App.js
ResetFork
```
import Heading from './Heading.js';
import Section from './Section.js';
export default function ProfilePage() {
 return (
  <Section>
   <Heading>My Profile</Heading>
   <Post
    title="Hello traveller!"
    body="Read about my adventures."
   />
   <AllPosts />
  </Section>
 );
}
function AllPosts() {
 return (
  <Section>
   <Heading>Posts</Heading>
   <RecentPosts />
  </Section>
 );
}
function RecentPosts() {
 return (
  <Section>
   <Heading>Recent Posts</Heading>
   <Post
    title="Flavors of Lisbon"
    body="...those pastéis de nata!"
   />
   <Post
    title="Buenos Aires in the rhythm of tango"
    body="I loved it!"
   />
  </Section>
 );
}
function Post({ title, body }) {
 return (
  <Section isFancy={true}>
   <Heading>
    {title}
   </Heading>
   <p><i>{body}</i></p>
  </Section>
 );
}

```

Show more
You didn’t do anything special for this to work. A `Section` specifies the context for the tree inside it, so you can insert a `<Heading>` anywhere, and it will have the correct size. Try it in the sandbox above!
**Context lets you write components that “adapt to their surroundings” and display themselves differently depending on _where_ (or, in other words, _in which context_) they are being rendered.**
How context works might remind you of [CSS property inheritance.](https://developer.mozilla.org/en-US/docs/Web/CSS/inheritance) In CSS, you can specify `color: blue` for a `<div>`, and any DOM node inside of it, no matter how deep, will inherit that color unless some other DOM node in the middle overrides it with `color: green`. Similarly, in React, the only way to override some context coming from above is to wrap children into a context provider with a different value.
In CSS, different properties like `color` and `background-color` don’t override each other. You can set all `<div>`’s `color` to red without impacting `background-color`. Similarly, **different React contexts don’t override each other.** Each context that you make with `createContext()` is completely separate from other ones, and ties together components using and providing _that particular_ context. One component may use or provide many different contexts without a problem.
## Before you use context [](https://react.dev/learn/passing-data-deeply-with-context#before-you-use-context "Link for Before you use context ")
Context is very tempting to use! However, this also means it’s too easy to overuse it. **Just because you need to pass some props several levels deep doesn’t mean you should put that information into context.**
Here’s a few alternatives you should consider before using context:
  1. **Start by[passing props.](https://react.dev/learn/passing-props-to-a-component)** If your components are not trivial, it’s not unusual to pass a dozen props down through a dozen components. It may feel like a slog, but it makes it very clear which components use which data! The person maintaining your code will be glad you’ve made the data flow explicit with props.
  2. **Extract components and[pass JSX as `children`](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children) to them.** If you pass some data through many layers of intermediate components that don’t use that data (and only pass it further down), this often means that you forgot to extract some components along the way. For example, maybe you pass data props like `posts` to visual components that don’t use them directly, like `<Layout posts={posts} />`. Instead, make `Layout` take `children` as a prop, and render `<Layout><Posts posts={posts} /></Layout>`. This reduces the number of layers between the component specifying the data and the one that needs it.


If neither of these approaches works well for you, consider context.
## Use cases for context [](https://react.dev/learn/passing-data-deeply-with-context#use-cases-for-context "Link for Use cases for context ")
  * **Theming:** If your app lets the user change its appearance (e.g. dark mode), you can put a context provider at the top of your app, and use that context in components that need to adjust their visual look.
  * **Current account:** Many components might need to know the currently logged in user. Putting it in context makes it convenient to read it anywhere in the tree. Some apps also let you operate multiple accounts at the same time (e.g. to leave a comment as a different user). In those cases, it can be convenient to wrap a part of the UI into a nested provider with a different current account value.
  * **Routing:** Most routing solutions use context internally to hold the current route. This is how every link “knows” whether it’s active or not. If you build your own router, you might want to do it too.
  * **Managing state:** As your app grows, you might end up with a lot of state closer to the top of your app. Many distant components below may want to change it. It is common to [use a reducer together with context](https://react.dev/learn/scaling-up-with-reducer-and-context) to manage complex state and pass it down to distant components without too much hassle.


Context is not limited to static values. If you pass a different value on the next render, React will update all the components reading it below! This is why context is often used in combination with state.
In general, if some information is needed by distant components in different parts of the tree, it’s a good indication that context will help you.
## Recap[](https://react.dev/learn/passing-data-deeply-with-context#recap "Link for Recap")
  * Context lets a component provide some information to the entire tree below it.
  * To pass context: 
    1. Create and export it with `export const MyContext = createContext(defaultValue)`.
    2. Pass it to the `useContext(MyContext)` Hook to read it in any child component, no matter how deep.
    3. Wrap children into `<MyContext value={...}>` to provide it from a parent.
  * Context passes through any components in the middle.
  * Context lets you write components that “adapt to their surroundings”.
  * Before you use context, try passing props or passing JSX as `children`.


## Try out some challenges[](https://react.dev/learn/passing-data-deeply-with-context#challenges "Link for Try out some challenges")
#### 
Challenge 1 of 1: 
Replace prop drilling with context [](https://react.dev/learn/passing-data-deeply-with-context#replace-prop-drilling-with-context "Link for this heading")
In this example, toggling the checkbox changes the `imageSize` prop passed to each `<PlaceImage>`. The checkbox state is held in the top-level `App` component, but each `<PlaceImage>` needs to be aware of it.
Currently, `App` passes `imageSize` to `List`, which passes it to each `Place`, which passes it to the `PlaceImage`. Remove the `imageSize` prop, and instead pass it from the `App` component directly to `PlaceImage`.
You can declare context in `Context.js`.
App.jsContext.jsdata.jsutils.js
App.js
ResetFork
```
import { useState } from 'react';
import { places } from './data.js';
import { getImageUrl } from './utils.js';
export default function App() {
 const [isLarge, setIsLarge] = useState(false);
 const imageSize = isLarge ? 150 : 100;
 return (
  <>
   <label>
    <input
     type="checkbox"
     checked={isLarge}
     onChange={e => {
      setIsLarge(e.target.checked);
     }}
    />
    Use large images
   </label>
   <hr />
   <List imageSize={imageSize} />
  </>
 )
}
function List({ imageSize }) {
 const listItems = places.map(place =>
  <li key={place.id}>
   <Place
    place={place}
    imageSize={imageSize}
   />
  </li>
 );
 return <ul>{listItems}</ul>;
}
function Place({ place, imageSize }) {
 return (
  <>
   <PlaceImage
    place={place}
    imageSize={imageSize}
   />
   <p>
    <b>{place.name}</b>
    {': ' + place.description}
   </p>
  </>
 );
}
function PlaceImage({ place, imageSize }) {
 return (
  <img
   src={getImageUrl(place)}
   alt={place.name}
   width={imageSize}
   height={imageSize}
  />
 );
}

```

Show more
Show solution
[PreviousExtracting State Logic into a Reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer)[NextScaling Up with Reducer and Context](https://react.dev/learn/scaling-up-with-reducer-and-context)
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
  * [Overview](https://react.dev/learn/passing-data-deeply-with-context)
  * [The problem with passing props ](https://react.dev/learn/passing-data-deeply-with-context#the-problem-with-passing-props)
  * [Context: an alternative to passing props ](https://react.dev/learn/passing-data-deeply-with-context#context-an-alternative-to-passing-props)
  * [Step 1: Create the context ](https://react.dev/learn/passing-data-deeply-with-context#step-1-create-the-context)
  * [Step 2: Use the context ](https://react.dev/learn/passing-data-deeply-with-context#step-2-use-the-context)
  * [Step 3: Provide the context ](https://react.dev/learn/passing-data-deeply-with-context#step-3-provide-the-context)
  * [Using and providing context from the same component ](https://react.dev/learn/passing-data-deeply-with-context#using-and-providing-context-from-the-same-component)
  * [Context passes through intermediate components ](https://react.dev/learn/passing-data-deeply-with-context#context-passes-through-intermediate-components)
  * [Before you use context ](https://react.dev/learn/passing-data-deeply-with-context#before-you-use-context)
  * [Use cases for context ](https://react.dev/learn/passing-data-deeply-with-context#use-cases-for-context)
  * [Recap](https://react.dev/learn/passing-data-deeply-with-context#recap)
  * [Challenges](https://react.dev/learn/passing-data-deeply-with-context#challenges)



