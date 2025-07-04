---
url: https://react.dev/learn/sharing-state-between-components
scraped_at: 2025-05-25T08:31:13.136933
title: Sharing State Between Components – React
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
# Sharing State Between Components[](https://react.dev/learn/sharing-state-between-components#undefined "Link for this heading")
Sometimes, you want the state of two components to always change together. To do it, remove state from both of them, move it to their closest common parent, and then pass it down to them via props. This is known as _lifting state up,_ and it’s one of the most common things you will do writing React code.
### You will learn
  * How to share state between components by lifting it up
  * What are controlled and uncontrolled components


## Lifting state up by example [](https://react.dev/learn/sharing-state-between-components#lifting-state-up-by-example "Link for Lifting state up by example ")
In this example, a parent `Accordion` component renders two separate `Panel`s:
  * `Accordion`
    * `Panel`
    * `Panel`


Each `Panel` component has a boolean `isActive` state that determines whether its content is visible.
Press the Show button for both panels:
App.js
App.js
Download ResetFork
99
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
import { useState } from 'react';
function Panel({ title, children }) {
const [isActive, setIsActive] = useState(false);
return (
<section className="panel">
<h3>{title}</h3>
{isActive ? (
<p>{children}</p>
) : (
<button onClick={() => setIsActive(true)}>
Show
</button>
)}
</section>
);
}
export default function Accordion() {
return (
<>
<h2>Almaty, Kazakhstan</h2>
<Panel title="About">
With a population of about 2 million, Almaty is Kazakhstan's largest city. From 1929 to 1997, it was its capital city.
</Panel>
<Panel title="Etymology">
The name comes from <span lang="kk-KZ">алма</span>, the Kazakh word for "apple" and is often translated as "full of apples". In fact, the region surrounding Almaty is thought to be the ancestral home of the apple, and the wild <i lang="la">Malus sieversii</i> is considered a likely candidate for the ancestor of the modern domestic apple.
</Panel>
</>
);
}
Show more
Notice how pressing one panel’s button does not affect the other panel—they are independent.
![Diagram showing a tree of three components, one parent labeled Accordion and two children labeled Panel. Both Panel components contain isActive with value false.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_child.dark.png&w=1080&q=75)
![Diagram showing a tree of three components, one parent labeled Accordion and two children labeled Panel. Both Panel components contain isActive with value false.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_child.png&w=1080&q=75)
Initially, each `Panel`’s `isActive` state is `false`, so they both appear collapsed
![The same diagram as the previous, with the isActive of the first child Panel component highlighted indicating a click with the isActive value set to true. The second Panel component still contains value false.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_child_clicked.dark.png&w=1080&q=75)
![The same diagram as the previous, with the isActive of the first child Panel component highlighted indicating a click with the isActive value set to true. The second Panel component still contains value false.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_child_clicked.png&w=1080&q=75)
Clicking either `Panel`’s button will only update that `Panel`’s `isActive` state alone
**But now let’s say you want to change it so that only one panel is expanded at any given time.** With that design, expanding the second panel should collapse the first one. How would you do that?
To coordinate these two panels, you need to “lift their state up” to a parent component in three steps:
  1. **Remove** state from the child components.
  2. **Pass** hardcoded data from the common parent.
  3. **Add** state to the common parent and pass it down together with the event handlers.


This will allow the `Accordion` component to coordinate both `Panel`s and only expand one at a time.
### Step 1: Remove state from the child components [](https://react.dev/learn/sharing-state-between-components#step-1-remove-state-from-the-child-components "Link for Step 1: Remove state from the child components ")
You will give control of the `Panel`’s `isActive` to its parent component. This means that the parent component will pass `isActive` to `Panel` as a prop instead. Start by **removing this line** from the `Panel` component:
```

const [isActive, setIsActive] = useState(false);

```

And instead, add `isActive` to the `Panel`’s list of props:
```

function Panel({ title, children, isActive }) {

```

Now the `Panel`’s parent component can _control_ `isActive` by [passing it down as a prop.](https://react.dev/learn/passing-props-to-a-component) Conversely, the `Panel` component now has _no control_ over the value of `isActive`—it’s now up to the parent component!
### Step 2: Pass hardcoded data from the common parent [](https://react.dev/learn/sharing-state-between-components#step-2-pass-hardcoded-data-from-the-common-parent "Link for Step 2: Pass hardcoded data from the common parent ")
To lift state up, you must locate the closest common parent component of _both_ of the child components that you want to coordinate:
  * `Accordion` _(closest common parent)_
    * `Panel`
    * `Panel`


In this example, it’s the `Accordion` component. Since it’s above both panels and can control their props, it will become the “source of truth” for which panel is currently active. Make the `Accordion` component pass a hardcoded value of `isActive` (for example, `true`) to both panels:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Accordion() {
 return (
  <>
   <h2>Almaty, Kazakhstan</h2>
   <Panel title="About" isActive={true}>
    With a population of about 2 million, Almaty is Kazakhstan's largest city. From 1929 to 1997, it was its capital city.
   </Panel>
   <Panel title="Etymology" isActive={true}>
    The name comes from <span lang="kk-KZ">алма</span>, the Kazakh word for "apple" and is often translated as "full of apples". In fact, the region surrounding Almaty is thought to be the ancestral home of the apple, and the wild <i lang="la">Malus sieversii</i> is considered a likely candidate for the ancestor of the modern domestic apple.
   </Panel>
  </>
 );
}
function Panel({ title, children, isActive }) {
 return (
  <section className="panel">
   <h3>{title}</h3>
   {isActive ? (
    <p>{children}</p>
   ) : (
    <button onClick={() => setIsActive(true)}>
     Show
    </button>
   )}
  </section>
 );
}

```

Show more
Try editing the hardcoded `isActive` values in the `Accordion` component and see the result on the screen.
### Step 3: Add state to the common parent [](https://react.dev/learn/sharing-state-between-components#step-3-add-state-to-the-common-parent "Link for Step 3: Add state to the common parent ")
Lifting state up often changes the nature of what you’re storing as state.
In this case, only one panel should be active at a time. This means that the `Accordion` common parent component needs to keep track of _which_ panel is the active one. Instead of a `boolean` value, it could use a number as the index of the active `Panel` for the state variable:
```

const [activeIndex, setActiveIndex] = useState(0);

```

When the `activeIndex` is `0`, the first panel is active, and when it’s `1`, it’s the second one.
Clicking the “Show” button in either `Panel` needs to change the active index in `Accordion`. A `Panel` can’t set the `activeIndex` state directly because it’s defined inside the `Accordion`. The `Accordion` component needs to _explicitly allow_ the `Panel` component to change its state by [passing an event handler down as a prop](https://react.dev/learn/responding-to-events#passing-event-handlers-as-props):
```

<>
 <Panel
  isActive={activeIndex === 0}
  onShow={() => setActiveIndex(0)}
 >
  ...
 </Panel>
 <Panel
  isActive={activeIndex === 1}
  onShow={() => setActiveIndex(1)}
 >
  ...
 </Panel>
</>

```

The `<button>` inside the `Panel` will now use the `onShow` prop as its click event handler:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Accordion() {
 const [activeIndex, setActiveIndex] = useState(0);
 return (
  <>
   <h2>Almaty, Kazakhstan</h2>
   <Panel
    title="About"
    isActive={activeIndex === 0}
    onShow={() => setActiveIndex(0)}
   >
    With a population of about 2 million, Almaty is Kazakhstan's largest city. From 1929 to 1997, it was its capital city.
   </Panel>
   <Panel
    title="Etymology"
    isActive={activeIndex === 1}
    onShow={() => setActiveIndex(1)}
   >
    The name comes from <span lang="kk-KZ">алма</span>, the Kazakh word for "apple" and is often translated as "full of apples". In fact, the region surrounding Almaty is thought to be the ancestral home of the apple, and the wild <i lang="la">Malus sieversii</i> is considered a likely candidate for the ancestor of the modern domestic apple.
   </Panel>
  </>
 );
}
function Panel({
 title,
 children,
 isActive,
 onShow
}) {
 return (
  <section className="panel">
   <h3>{title}</h3>
   {isActive ? (
    <p>{children}</p>
   ) : (
    <button onClick={onShow}>
     Show
    </button>
   )}
  </section>
 );
}

```

Show more
This completes lifting state up! Moving state into the common parent component allowed you to coordinate the two panels. Using the active index instead of two “is shown” flags ensured that only one panel is active at a given time. And passing down the event handler to the child allowed the child to change the parent’s state.
![Diagram showing a tree of three components, one parent labeled Accordion and two children labeled Panel. Accordion contains an activeIndex value of zero which turns into isActive value of true passed to the first Panel, and isActive value of false passed to the second Panel.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_parent.dark.png&w=1080&q=75)
![Diagram showing a tree of three components, one parent labeled Accordion and two children labeled Panel. Accordion contains an activeIndex value of zero which turns into isActive value of true passed to the first Panel, and isActive value of false passed to the second Panel.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_parent.png&w=1080&q=75)
Initially, `Accordion`’s `activeIndex` is `0`, so the first `Panel` receives `isActive = true`
![The same diagram as the previous, with the activeIndex value of the parent Accordion component highlighted indicating a click with the value changed to one. The flow to both of the children Panel components is also highlighted, and the isActive value passed to each child is set to the opposite: false for the first Panel and true for the second one.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_parent_clicked.dark.png&w=1080&q=75)
![The same diagram as the previous, with the activeIndex value of the parent Accordion component highlighted indicating a click with the value changed to one. The flow to both of the children Panel components is also highlighted, and the isActive value passed to each child is set to the opposite: false for the first Panel and true for the second one.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fsharing_state_parent_clicked.png&w=1080&q=75)
When `Accordion`’s `activeIndex` state changes to `1`, the second `Panel` receives `isActive = true` instead
##### Deep Dive
#### Controlled and uncontrolled components [](https://react.dev/learn/sharing-state-between-components#controlled-and-uncontrolled-components "Link for Controlled and uncontrolled components ")
Show Details
It is common to call a component with some local state “uncontrolled”. For example, the original `Panel` component with an `isActive` state variable is uncontrolled because its parent cannot influence whether the panel is active or not.
In contrast, you might say a component is “controlled” when the important information in it is driven by props rather than its own local state. This lets the parent component fully specify its behavior. The final `Panel` component with the `isActive` prop is controlled by the `Accordion` component.
Uncontrolled components are easier to use within their parents because they require less configuration. But they’re less flexible when you want to coordinate them together. Controlled components are maximally flexible, but they require the parent components to fully configure them with props.
In practice, “controlled” and “uncontrolled” aren’t strict technical terms—each component usually has some mix of both local state and props. However, this is a useful way to talk about how components are designed and what capabilities they offer.
When writing a component, consider which information in it should be controlled (via props), and which information should be uncontrolled (via state). But you can always change your mind and refactor later.
## A single source of truth for each state [](https://react.dev/learn/sharing-state-between-components#a-single-source-of-truth-for-each-state "Link for A single source of truth for each state ")
In a React application, many components will have their own state. Some state may “live” close to the leaf components (components at the bottom of the tree) like inputs. Other state may “live” closer to the top of the app. For example, even client-side routing libraries are usually implemented by storing the current route in the React state, and passing it down by props!
**For each unique piece of state, you will choose the component that “owns” it.** This principle is also known as having a [“single source of truth”.](https://en.wikipedia.org/wiki/Single_source_of_truth) It doesn’t mean that all state lives in one place—but that for _each_ piece of state, there is a _specific_ component that holds that piece of information. Instead of duplicating shared state between components, _lift it up_ to their common shared parent, and _pass it down_ to the children that need it.
Your app will change as you work on it. It is common that you will move state down or back up while you’re still figuring out where each piece of the state “lives”. This is all part of the process!
To see what this feels like in practice with a few more components, read [Thinking in React.](https://react.dev/learn/thinking-in-react)
## Recap[](https://react.dev/learn/sharing-state-between-components#recap "Link for Recap")
  * When you want to coordinate two components, move their state to their common parent.
  * Then pass the information down through props from their common parent.
  * Finally, pass the event handlers down so that the children can change the parent’s state.
  * It’s useful to consider components as “controlled” (driven by props) or “uncontrolled” (driven by state).


## Try out some challenges[](https://react.dev/learn/sharing-state-between-components#challenges "Link for Try out some challenges")
1. Synced inputs 2. Filtering a list 
#### 
Challenge 1 of 2: 
Synced inputs [](https://react.dev/learn/sharing-state-between-components#synced-inputs "Link for this heading")
These two inputs are independent. Make them stay in sync: editing one input should update the other input with the same text, and vice versa.
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function SyncedInputs() {
 return (
  <>
   <Input label="First input" />
   <Input label="Second input" />
  </>
 );
}
function Input({ label }) {
 const [text, setText] = useState('');
 function handleChange(e) {
  setText(e.target.value);
 }
 return (
  <label>
   {label}
   {' '}
   <input
    value={text}
    onChange={handleChange}
   />
  </label>
 );
}

```

Show more
Show hint Show solution
Next Challenge
[PreviousChoosing the State Structure](https://react.dev/learn/choosing-the-state-structure)[NextPreserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state)
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
  * [Overview](https://react.dev/learn/sharing-state-between-components)
  * [Lifting state up by example ](https://react.dev/learn/sharing-state-between-components#lifting-state-up-by-example)
  * [Step 1: Remove state from the child components ](https://react.dev/learn/sharing-state-between-components#step-1-remove-state-from-the-child-components)
  * [Step 2: Pass hardcoded data from the common parent ](https://react.dev/learn/sharing-state-between-components#step-2-pass-hardcoded-data-from-the-common-parent)
  * [Step 3: Add state to the common parent ](https://react.dev/learn/sharing-state-between-components#step-3-add-state-to-the-common-parent)
  * [A single source of truth for each state ](https://react.dev/learn/sharing-state-between-components#a-single-source-of-truth-for-each-state)
  * [Recap](https://react.dev/learn/sharing-state-between-components#recap)
  * [Challenges](https://react.dev/learn/sharing-state-between-components#challenges)



