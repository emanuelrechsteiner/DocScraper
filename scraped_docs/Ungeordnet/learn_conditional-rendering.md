---
url: https://react.dev/learn/conditional-rendering
scraped_at: 2025-05-25T08:41:04.245233
title: Conditional Rendering – React
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
[Describing the UI](https://react.dev/learn/describing-the-ui)
# Conditional Rendering[](https://react.dev/learn/conditional-rendering#undefined "Link for this heading")
Your components will often need to display different things depending on different conditions. In React, you can conditionally render JSX using JavaScript syntax like `if` statements, `&&`, and `? :` operators.
### You will learn
  * How to return different JSX depending on a condition
  * How to conditionally include or exclude a piece of JSX
  * Common conditional syntax shortcuts you’ll encounter in React codebases


## Conditionally returning JSX [](https://react.dev/learn/conditional-rendering#conditionally-returning-jsx "Link for Conditionally returning JSX ")
Let’s say you have a `PackingList` component rendering several `Item`s, which can be marked as packed or not:
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
function Item({ name, isPacked }) {
return <li className="item">{name}</li>;
}
export default function PackingList() {
return (
<section>
<h1>Sally Ride's Packing List</h1>
<ul>
<Item
isPacked={true}
name="Space suit"
/>
<Item
isPacked={true}
name="Helmet with a golden leaf"
/>
<Item
isPacked={false}
name="Photo of Tam"
/>
</ul>
</section>
);
}
Show more
Notice that some of the `Item` components have their `isPacked` prop set to `true` instead of `false`. You want to add a checkmark (✅) to packed items if `isPacked={true}`.
You can write this as an [`if`/`else` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) like so:
```

if (isPacked) {
 return <li className="item">{name} ✅</li>;
}
return <li className="item">{name}</li>;

```

If the `isPacked` prop is `true`, this code **returns a different JSX tree.** With this change, some of the items get a checkmark at the end:
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 if (isPacked) {
  return <li className="item">{name} ✅</li>;
 }
 return <li className="item">{name}</li>;
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
Try editing what gets returned in either case, and see how the result changes!
Notice how you’re creating branching logic with JavaScript’s `if` and `return` statements. In React, control flow (like conditions) is handled by JavaScript.
### Conditionally returning nothing with `null` [](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null "Link for this heading")
In some situations, you won’t want to render anything at all. For example, say you don’t want to show packed items at all. A component must return something. In this case, you can return `null`:
```

if (isPacked) {
 return null;
}
return <li className="item">{name}</li>;

```

If `isPacked` is true, the component will return nothing, `null`. Otherwise, it will return JSX to render.
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 if (isPacked) {
  return null;
 }
 return <li className="item">{name}</li>;
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
In practice, returning `null` from a component isn’t common because it might surprise a developer trying to render it. More often, you would conditionally include or exclude the component in the parent component’s JSX. Here’s how to do that!
## Conditionally including JSX [](https://react.dev/learn/conditional-rendering#conditionally-including-jsx "Link for Conditionally including JSX ")
In the previous example, you controlled which (if any!) JSX tree would be returned by the component. You may already have noticed some duplication in the render output:
```

<li className="item">{name} ✅</li>

```

is very similar to
```

<li className="item">{name}</li>

```

Both of the conditional branches return `<li className="item">...</li>`:
```

if (isPacked) {
 return <li className="item">{name} ✅</li>;
}
return <li className="item">{name}</li>;

```

While this duplication isn’t harmful, it could make your code harder to maintain. What if you want to change the `className`? You’d have to do it in two places in your code! In such a situation, you could conditionally include a little JSX to make your code more [DRY.](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
### Conditional (ternary) operator (`? :`) [](https://react.dev/learn/conditional-rendering#conditional-ternary-operator-- "Link for this heading")
JavaScript has a compact syntax for writing a conditional expression — the [conditional operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) or “ternary operator”.
Instead of this:
```

if (isPacked) {
 return <li className="item">{name} ✅</li>;
}
return <li className="item">{name}</li>;

```

You can write this:
```

return (
 <li className="item">
  {isPacked ? name + ' ✅' : name}
 </li>
);

```

You can read it as _“if`isPacked` is true, then (`?`) render `name + ' ✅'`, otherwise (`:`) render `name`”_.
##### Deep Dive
#### Are these two examples fully equivalent? [](https://react.dev/learn/conditional-rendering#are-these-two-examples-fully-equivalent "Link for Are these two examples fully equivalent? ")
Show Details
If you’re coming from an object-oriented programming background, you might assume that the two examples above are subtly different because one of them may create two different “instances” of `<li>`. But JSX elements aren’t “instances” because they don’t hold any internal state and aren’t real DOM nodes. They’re lightweight descriptions, like blueprints. So these two examples, in fact, _are_ completely equivalent. [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) goes into detail about how this works.
Now let’s say you want to wrap the completed item’s text into another HTML tag, like `<del>` to strike it out. You can add even more newlines and parentheses so that it’s easier to nest more JSX in each of the cases:
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 return (
  <li className="item">
   {isPacked ? (
    <del>
     {name + ' ✅'}
    </del>
   ) : (
    name
   )}
  </li>
 );
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
This style works well for simple conditions, but use it in moderation. If your components get messy with too much nested conditional markup, consider extracting child components to clean things up. In React, markup is a part of your code, so you can use tools like variables and functions to tidy up complex expressions.
### Logical AND operator (`&&`) [](https://react.dev/learn/conditional-rendering#logical-and-operator- "Link for this heading")
Another common shortcut you’ll encounter is the [JavaScript logical AND (`&&`) operator.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND#:~:text=The%20logical%20AND%20\(%20%26%26%20\)%20operator,it%20returns%20a%20Boolean%20value.) Inside React components, it often comes up when you want to render some JSX when the condition is true, **or render nothing otherwise.** With `&&`, you could conditionally render the checkmark only if `isPacked` is `true`:
```

return (
 <li className="item">
  {name} {isPacked && '✅'}
 </li>
);

```

You can read this as _“if`isPacked` , then (`&&`) render the checkmark, otherwise, render nothing”_.
Here it is in action:
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 return (
  <li className="item">
   {name} {isPacked && '✅'}
  </li>
 );
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
A [JavaScript && expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND) returns the value of its right side (in our case, the checkmark) if the left side (our condition) is `true`. But if the condition is `false`, the whole expression becomes `false`. React considers `false` as a “hole” in the JSX tree, just like `null` or `undefined`, and doesn’t render anything in its place.
### Pitfall
**Don’t put numbers on the left side of`&&`.**
To test the condition, JavaScript converts the left side to a boolean automatically. However, if the left side is `0`, then the whole expression gets that value (`0`), and React will happily render `0` rather than nothing.
For example, a common mistake is to write code like `messageCount && <p>New messages</p>`. It’s easy to assume that it renders nothing when `messageCount` is `0`, but it really renders the `0` itself!
To fix it, make the left side a boolean: `messageCount > 0 && <p>New messages</p>`.
### Conditionally assigning JSX to a variable [](https://react.dev/learn/conditional-rendering#conditionally-assigning-jsx-to-a-variable "Link for Conditionally assigning JSX to a variable ")
When the shortcuts get in the way of writing plain code, try using an `if` statement and a variable. You can reassign variables defined with [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let), so start by providing the default content you want to display, the name:
```

let itemContent = name;

```

Use an `if` statement to reassign a JSX expression to `itemContent` if `isPacked` is `true`:
```

if (isPacked) {
 itemContent = name + " ✅";
}

```

[Curly braces open the “window into JavaScript”.](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-curly-braces-a-window-into-the-javascript-world) Embed the variable with curly braces in the returned JSX tree, nesting the previously calculated expression inside of JSX:
```

<li className="item">
 {itemContent}
</li>

```

This style is the most verbose, but it’s also the most flexible. Here it is in action:
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 let itemContent = name;
 if (isPacked) {
  itemContent = name + " ✅";
 }
 return (
  <li className="item">
   {itemContent}
  </li>
 );
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
Like before, this works not only for text, but for arbitrary JSX too:
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 let itemContent = name;
 if (isPacked) {
  itemContent = (
   <del>
    {name + " ✅"}
   </del>
  );
 }
 return (
  <li className="item">
   {itemContent}
  </li>
 );
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
If you’re not familiar with JavaScript, this variety of styles might seem overwhelming at first. However, learning them will help you read and write any JavaScript code — and not just React components! Pick the one you prefer for a start, and then consult this reference again if you forget how the other ones work.
## Recap[](https://react.dev/learn/conditional-rendering#recap "Link for Recap")
  * In React, you control branching logic with JavaScript.
  * You can return a JSX expression conditionally with an `if` statement.
  * You can conditionally save some JSX to a variable and then include it inside other JSX by using the curly braces.
  * In JSX, `{cond ? <A /> : <B />}` means _“if`cond` , render `<A />`, otherwise `<B />`”_.
  * In JSX, `{cond && <A />}` means _“if`cond` , render `<A />`, otherwise nothing”_.
  * The shortcuts are common, but you don’t have to use them if you prefer plain `if`.


## Try out some challenges[](https://react.dev/learn/conditional-rendering#challenges "Link for Try out some challenges")
1. Show an icon for incomplete items with `? :` 2. Show the item importance with `&&` 3. Refactor a series of `? :` to `if` and variables 
#### 
Challenge 1 of 3: 
Show an icon for incomplete items with `? :` [](https://react.dev/learn/conditional-rendering#show-an-icon-for-incomplete-items-with-- "Link for this heading")
Use the conditional operator (`cond ? a : b`) to render a ❌ if `isPacked` isn’t `true`.
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 return (
  <li className="item">
   {name} {isPacked && '✅'}
  </li>
 );
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
Show solutionNext Challenge
[PreviousPassing Props to a Component](https://react.dev/learn/passing-props-to-a-component)[NextRendering Lists](https://react.dev/learn/rendering-lists)
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
  * [Overview](https://react.dev/learn/conditional-rendering)
  * [Conditionally returning JSX ](https://react.dev/learn/conditional-rendering#conditionally-returning-jsx)
  * [Conditionally returning nothing with `null` ](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null)
  * [Conditionally including JSX ](https://react.dev/learn/conditional-rendering#conditionally-including-jsx)
  * [Conditional (ternary) operator (`? :`) ](https://react.dev/learn/conditional-rendering#conditional-ternary-operator--)
  * [Logical AND operator (`&&`) ](https://react.dev/learn/conditional-rendering#logical-and-operator-)
  * [Conditionally assigning JSX to a variable ](https://react.dev/learn/conditional-rendering#conditionally-assigning-jsx-to-a-variable)
  * [Recap](https://react.dev/learn/conditional-rendering#recap)
  * [Challenges](https://react.dev/learn/conditional-rendering#challenges)



