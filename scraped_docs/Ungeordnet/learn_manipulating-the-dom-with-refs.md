---
url: https://react.dev/learn/manipulating-the-dom-with-refs
scraped_at: 2025-05-25T08:39:13.394056
title: Manipulating the DOM with Refs – React
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
[Escape Hatches](https://react.dev/learn/escape-hatches)
# Manipulating the DOM with Refs[](https://react.dev/learn/manipulating-the-dom-with-refs#undefined "Link for this heading")
React automatically updates the [DOM](https://developer.mozilla.org/docs/Web/API/Document_Object_Model/Introduction) to match your render output, so your components won’t often need to manipulate it. However, sometimes you might need access to the DOM elements managed by React—for example, to focus a node, scroll to it, or measure its size and position. There is no built-in way to do those things in React, so you will need a _ref_ to the DOM node.
### You will learn
  * How to access a DOM node managed by React with the `ref` attribute
  * How the `ref` JSX attribute relates to the `useRef` Hook
  * How to access another component’s DOM node
  * In which cases it’s safe to modify the DOM managed by React


## Getting a ref to the node [](https://react.dev/learn/manipulating-the-dom-with-refs#getting-a-ref-to-the-node "Link for Getting a ref to the node ")
To access a DOM node managed by React, first, import the `useRef` Hook:
```

import { useRef } from 'react';

```

Then, use it to declare a ref inside your component:
```

const myRef = useRef(null);

```

Finally, pass your ref as the `ref` attribute to the JSX tag for which you want to get the DOM node:
```

<div ref={myRef}>

```

The `useRef` Hook returns an object with a single property called `current`. Initially, `myRef.current` will be `null`. When React creates a DOM node for this `<div>`, React will put a reference to this node into `myRef.current`. You can then access this DOM node from your [event handlers](https://react.dev/learn/responding-to-events) and use the built-in [browser APIs](https://developer.mozilla.org/docs/Web/API/Element) defined on it.
```

// You can use any browser APIs, for example:
myRef.current.scrollIntoView();

```

### Example: Focusing a text input [](https://react.dev/learn/manipulating-the-dom-with-refs#example-focusing-a-text-input "Link for Example: Focusing a text input ")
In this example, clicking the button will focus the input:
App.js
App.js
Download ResetFork
```
import { useRef } from 'react';
export default function Form() {
 const inputRef = useRef(null);
 function handleClick() {
  inputRef.current.focus();
 }
 return (
  <>
   <input ref={inputRef} />
   <button onClick={handleClick}>
    Focus the input
   </button>
  </>
 );
}

```

Show more
To implement this:
  1. Declare `inputRef` with the `useRef` Hook.
  2. Pass it as `<input ref={inputRef}>`. This tells React to **put this`<input>` ’s DOM node into `inputRef.current`.**
  3. In the `handleClick` function, read the input DOM node from `inputRef.current` and call [`focus()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on it with `inputRef.current.focus()`.
  4. Pass the `handleClick` event handler to `<button>` with `onClick`.


While DOM manipulation is the most common use case for refs, the `useRef` Hook can be used for storing other things outside React, like timer IDs. Similarly to state, refs remain between renders. Refs are like state variables that don’t trigger re-renders when you set them. Read about refs in [Referencing Values with Refs.](https://react.dev/learn/referencing-values-with-refs)
### Example: Scrolling to an element [](https://react.dev/learn/manipulating-the-dom-with-refs#example-scrolling-to-an-element "Link for Example: Scrolling to an element ")
You can have more than a single ref in a component. In this example, there is a carousel of three images. Each button centers an image by calling the browser [`scrollIntoView()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView) method on the corresponding DOM node:
App.js
App.js
Download ResetFork
```
import { useRef } from 'react';
export default function CatFriends() {
 const firstCatRef = useRef(null);
 const secondCatRef = useRef(null);
 const thirdCatRef = useRef(null);
 function handleScrollToFirstCat() {
  firstCatRef.current.scrollIntoView({
   behavior: 'smooth',
   block: 'nearest',
   inline: 'center'
  });
 }
 function handleScrollToSecondCat() {
  secondCatRef.current.scrollIntoView({
   behavior: 'smooth',
   block: 'nearest',
   inline: 'center'
  });
 }
 function handleScrollToThirdCat() {
  thirdCatRef.current.scrollIntoView({
   behavior: 'smooth',
   block: 'nearest',
   inline: 'center'
  });
 }
 return (
  <>
   <nav>
    <button onClick={handleScrollToFirstCat}>
     Neo
    </button>
    <button onClick={handleScrollToSecondCat}>
     Millie
    </button>
    <button onClick={handleScrollToThirdCat}>
     Bella
    </button>
   </nav>
   <div>
    <ul>
     <li>
      <img
       src="https://placecats.com/neo/300/200"
       alt="Neo"
       ref={firstCatRef}
      />
     </li>
     <li>
      <img
       src="https://placecats.com/millie/200/200"
       alt="Millie"
       ref={secondCatRef}
      />
     </li>
     <li>
      <img
       src="https://placecats.com/bella/199/200"
       alt="Bella"
       ref={thirdCatRef}
      />
     </li>
    </ul>
   </div>
  </>
 );
}

```

Show more
##### Deep Dive
#### How to manage a list of refs using a ref callback [](https://react.dev/learn/manipulating-the-dom-with-refs#how-to-manage-a-list-of-refs-using-a-ref-callback "Link for How to manage a list of refs using a ref callback ")
Show Details
In the above examples, there is a predefined number of refs. However, sometimes you might need a ref to each item in the list, and you don’t know how many you will have. Something like this **wouldn’t work** :
```

<ul>
 {items.map((item) => {
  // Doesn't work!
  const ref = useRef(null);
  return <li ref={ref} />;
 })}
</ul>

```

This is because **Hooks must only be called at the top-level of your component.** You can’t call `useRef` in a loop, in a condition, or inside a `map()` call.
One possible way around this is to get a single ref to their parent element, and then use DOM manipulation methods like [`querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) to “find” the individual child nodes from it. However, this is brittle and can break if your DOM structure changes.
Another solution is to **pass a function to the`ref` attribute.** This is called a [`ref` callback.](https://react.dev/reference/react-dom/components/common#ref-callback) React will call your ref callback with the DOM node when it’s time to set the ref, and with `null` when it’s time to clear it. This lets you maintain your own array or a [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), and access any ref by its index or some kind of ID.
This example shows how you can use this approach to scroll to an arbitrary node in a long list:
App.js
App.js
Download ResetFork
```
import { useRef, useState } from "react";
export default function CatFriends() {
 const itemsRef = useRef(null);
 const [catList, setCatList] = useState(setupCatList);
 function scrollToCat(cat) {
  const map = getMap();
  const node = map.get(cat);
  node.scrollIntoView({
   behavior: "smooth",
   block: "nearest",
   inline: "center",
  });
 }
 function getMap() {
  if (!itemsRef.current) {
   // Initialize the Map on first usage.
   itemsRef.current = new Map();
  }
  return itemsRef.current;
 }
 return (
  <>
   <nav>
    <button onClick={() => scrollToCat(catList[0])}>Neo</button>
    <button onClick={() => scrollToCat(catList[5])}>Millie</button>
    <button onClick={() => scrollToCat(catList[9])}>Bella</button>
   </nav>
   <div>
    <ul>
     {catList.map((cat) => (
      <li
       key={cat}
       ref={(node) => {
        const map = getMap();
        map.set(cat, node);
        return () => {
         map.delete(cat);
        };
       }}
      >
       <img src={cat} />
      </li>
     ))}
    </ul>
   </div>
  </>
 );
}
function setupCatList() {
 const catList = [];
 for (let i = 0; i < 10; i++) {
  catList.push("https://loremflickr.com/320/240/cat?lock=" + i);
 }
 return catList;
}

```

Show more
In this example, `itemsRef` doesn’t hold a single DOM node. Instead, it holds a [Map](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map) from item ID to a DOM node. ([Refs can hold any values!](https://react.dev/learn/referencing-values-with-refs)) The [`ref` callback](https://react.dev/reference/react-dom/components/common#ref-callback) on every list item takes care to update the Map:
```

<li
 key={cat.id}
 ref={node => {
  const map = getMap();
  // Add to the Map
  map.set(cat, node);
  return () => {
   // Remove from the Map
   map.delete(cat);
  };
 }}
>

```

This lets you read individual DOM nodes from the Map later.
### Note
When Strict Mode is enabled, ref callbacks will run twice in development.
Read more about [how this helps find bugs](https://react.dev/reference/react/StrictMode#fixing-bugs-found-by-re-running-ref-callbacks-in-development) in callback refs.
## Accessing another component’s DOM nodes [](https://react.dev/learn/manipulating-the-dom-with-refs#accessing-another-components-dom-nodes "Link for Accessing another component’s DOM nodes ")
### Pitfall
Refs are an escape hatch. Manually manipulating _another_ component’s DOM nodes can make your code fragile.
You can pass refs from parent component to child components [just like any other prop](https://react.dev/learn/passing-props-to-a-component).
```

import { useRef } from 'react';
function MyInput({ ref }) {
 return <input ref={ref} />;
}
function MyForm() {
 const inputRef = useRef(null);
 return <MyInput ref={inputRef} />
}

```

In the above example, a ref is created in the parent component, `MyForm`, and is passed to the child component, `MyInput`. `MyInput` then passes the ref to `<input>`. Because `<input>` is a [built-in component](https://react.dev/reference/react-dom/components/common) React sets the `.current` property of the ref to the `<input>` DOM element.
The `inputRef` created in `MyForm` now points to the `<input>` DOM element returned by `MyInput`. A click handler created in `MyForm` can access `inputRef` and call `focus()` to set the focus on `<input>`.
App.js
App.js
Download ResetFork
```
import { useRef } from 'react';
function MyInput({ ref }) {
 return <input ref={ref} />;
}
export default function MyForm() {
 const inputRef = useRef(null);
 function handleClick() {
  inputRef.current.focus();
 }
 return (
  <>
   <MyInput ref={inputRef} />
   <button onClick={handleClick}>
    Focus the input
   </button>
  </>
 );
}

```

Show more
##### Deep Dive
#### Exposing a subset of the API with an imperative handle [](https://react.dev/learn/manipulating-the-dom-with-refs#exposing-a-subset-of-the-api-with-an-imperative-handle "Link for Exposing a subset of the API with an imperative handle ")
Show Details
In the above example, the ref passed to `MyInput` is passed on to the original DOM input element. This lets the parent component call `focus()` on it. However, this also lets the parent component do something else—for example, change its CSS styles. In uncommon cases, you may want to restrict the exposed functionality. You can do that with [`useImperativeHandle`](https://react.dev/reference/react/useImperativeHandle):
App.js
App.js
Download ResetFork
```
import { useRef, useImperativeHandle } from "react";
function MyInput({ ref }) {
 const realInputRef = useRef(null);
 useImperativeHandle(ref, () => ({
  // Only expose focus and nothing else
  focus() {
   realInputRef.current.focus();
  },
 }));
 return <input ref={realInputRef} />;
};
export default function Form() {
 const inputRef = useRef(null);
 function handleClick() {
  inputRef.current.focus();
 }
 return (
  <>
   <MyInput ref={inputRef} />
   <button onClick={handleClick}>Focus the input</button>
  </>
 );
}

```

Show more
Here, `realInputRef` inside `MyInput` holds the actual input DOM node. However, [`useImperativeHandle`](https://react.dev/reference/react/useImperativeHandle) instructs React to provide your own special object as the value of a ref to the parent component. So `inputRef.current` inside the `Form` component will only have the `focus` method. In this case, the ref “handle” is not the DOM node, but the custom object you create inside [`useImperativeHandle`](https://react.dev/reference/react/useImperativeHandle) call.
## When React attaches the refs [](https://react.dev/learn/manipulating-the-dom-with-refs#when-react-attaches-the-refs "Link for When React attaches the refs ")
In React, every update is split in [two phases](https://react.dev/learn/render-and-commit#step-3-react-commits-changes-to-the-dom):
  * During **render,** React calls your components to figure out what should be on the screen.
  * During **commit,** React applies changes to the DOM.


In general, you [don’t want](https://react.dev/learn/referencing-values-with-refs#best-practices-for-refs) to access refs during rendering. That goes for refs holding DOM nodes as well. During the first render, the DOM nodes have not yet been created, so `ref.current` will be `null`. And during the rendering of updates, the DOM nodes haven’t been updated yet. So it’s too early to read them.
React sets `ref.current` during the commit. Before updating the DOM, React sets the affected `ref.current` values to `null`. After updating the DOM, React immediately sets them to the corresponding DOM nodes.
**Usually, you will access refs from event handlers.** If you want to do something with a ref, but there is no particular event to do it in, you might need an Effect. We will discuss Effects on the next pages.
##### Deep Dive
#### Flushing state updates synchronously with flushSync [](https://react.dev/learn/manipulating-the-dom-with-refs#flushing-state-updates-synchronously-with-flush-sync "Link for Flushing state updates synchronously with flushSync ")
Show Details
Consider code like this, which adds a new todo and scrolls the screen down to the last child of the list. Notice how, for some reason, it always scrolls to the todo that was _just before_ the last added one:
App.js
App.js
Download ResetFork
```
import { useState, useRef } from 'react';
export default function TodoList() {
 const listRef = useRef(null);
 const [text, setText] = useState('');
 const [todos, setTodos] = useState(
  initialTodos
 );
 function handleAdd() {
  const newTodo = { id: nextId++, text: text };
  setText('');
  setTodos([ ...todos, newTodo]);
  listRef.current.lastChild.scrollIntoView({
   behavior: 'smooth',
   block: 'nearest'
  });
 }
 return (
  <>
   <button onClick={handleAdd}>
    Add
   </button>
   <input
    value={text}
    onChange={e => setText(e.target.value)}
   />
   <ul ref={listRef}>
    {todos.map(todo => (
     <li key={todo.id}>{todo.text}</li>
    ))}
   </ul>
  </>
 );
}
let nextId = 0;
let initialTodos = [];
for (let i = 0; i < 20; i++) {
 initialTodos.push({
  id: nextId++,
  text: 'Todo #' + (i + 1)
 });
}

```

Show more
The issue is with these two lines:
```

setTodos([ ...todos, newTodo]);
listRef.current.lastChild.scrollIntoView();

```

In React, [state updates are queued.](https://react.dev/learn/queueing-a-series-of-state-updates) Usually, this is what you want. However, here it causes a problem because `setTodos` does not immediately update the DOM. So the time you scroll the list to its last element, the todo has not yet been added. This is why scrolling always “lags behind” by one item.
To fix this issue, you can force React to update (“flush”) the DOM synchronously. To do this, import `flushSync` from `react-dom` and **wrap the state update** into a `flushSync` call:
```

flushSync(() => {
 setTodos([ ...todos, newTodo]);
});
listRef.current.lastChild.scrollIntoView();

```

This will instruct React to update the DOM synchronously right after the code wrapped in `flushSync` executes. As a result, the last todo will already be in the DOM by the time you try to scroll to it:
App.js
App.js
Download ResetFork
```
import { useState, useRef } from 'react';
import { flushSync } from 'react-dom';
export default function TodoList() {
 const listRef = useRef(null);
 const [text, setText] = useState('');
 const [todos, setTodos] = useState(
  initialTodos
 );
 function handleAdd() {
  const newTodo = { id: nextId++, text: text };
  flushSync(() => {
   setText('');
   setTodos([ ...todos, newTodo]);
  });
  listRef.current.lastChild.scrollIntoView({
   behavior: 'smooth',
   block: 'nearest'
  });
 }
 return (
  <>
   <button onClick={handleAdd}>
    Add
   </button>
   <input
    value={text}
    onChange={e => setText(e.target.value)}
   />
   <ul ref={listRef}>
    {todos.map(todo => (
     <li key={todo.id}>{todo.text}</li>
    ))}
   </ul>
  </>
 );
}
let nextId = 0;
let initialTodos = [];
for (let i = 0; i < 20; i++) {
 initialTodos.push({
  id: nextId++,
  text: 'Todo #' + (i + 1)
 });
}

```

Show more
## Best practices for DOM manipulation with refs [](https://react.dev/learn/manipulating-the-dom-with-refs#best-practices-for-dom-manipulation-with-refs "Link for Best practices for DOM manipulation with refs ")
Refs are an escape hatch. You should only use them when you have to “step outside React”. Common examples of this include managing focus, scroll position, or calling browser APIs that React does not expose.
If you stick to non-destructive actions like focusing and scrolling, you shouldn’t encounter any problems. However, if you try to **modify** the DOM manually, you can risk conflicting with the changes React is making.
To illustrate this problem, this example includes a welcome message and two buttons. The first button toggles its presence using [conditional rendering](https://react.dev/learn/conditional-rendering) and [state](https://react.dev/learn/state-a-components-memory), as you would usually do in React. The second button uses the [`remove()` DOM API](https://developer.mozilla.org/en-US/docs/Web/API/Element/remove) to forcefully remove it from the DOM outside of React’s control.
Try pressing “Toggle with setState” a few times. The message should disappear and appear again. Then press “Remove from the DOM”. This will forcefully remove it. Finally, press “Toggle with setState”:
App.js
App.js
Download ResetFork
```
import { useState, useRef } from 'react';
export default function Counter() {
 const [show, setShow] = useState(true);
 const ref = useRef(null);
 return (
  <div>
   <button
    onClick={() => {
     setShow(!show);
    }}>
    Toggle with setState
   </button>
   <button
    onClick={() => {
     ref.current.remove();
    }}>
    Remove from the DOM
   </button>
   {show && <p ref={ref}>Hello world</p>}
  </div>
 );
}

```

Show more
After you’ve manually removed the DOM element, trying to use `setState` to show it again will lead to a crash. This is because you’ve changed the DOM, and React doesn’t know how to continue managing it correctly.
**Avoid changing DOM nodes managed by React.** Modifying, adding children to, or removing children from elements that are managed by React can lead to inconsistent visual results or crashes like above.
However, this doesn’t mean that you can’t do it at all. It requires caution. **You can safely modify parts of the DOM that React has _no reason_ to update.** For example, if some `<div>` is always empty in the JSX, React won’t have a reason to touch its children list. Therefore, it is safe to manually add or remove elements there.
## Recap[](https://react.dev/learn/manipulating-the-dom-with-refs#recap "Link for Recap")
  * Refs are a generic concept, but most often you’ll use them to hold DOM elements.
  * You instruct React to put a DOM node into `myRef.current` by passing `<div ref={myRef}>`.
  * Usually, you will use refs for non-destructive actions like focusing, scrolling, or measuring DOM elements.
  * A component doesn’t expose its DOM nodes by default. You can opt into exposing a DOM node by using the `ref` prop.
  * Avoid changing DOM nodes managed by React.
  * If you do modify DOM nodes managed by React, modify parts that React has no reason to update.


## Try out some challenges[](https://react.dev/learn/manipulating-the-dom-with-refs#challenges "Link for Try out some challenges")
1. Play and pause the video 2. Focus the search field 3. Scrolling an image carousel 4. Focus the search field with separate components 
#### 
Challenge 1 of 4: 
Play and pause the video [](https://react.dev/learn/manipulating-the-dom-with-refs#play-and-pause-the-video "Link for this heading")
In this example, the button toggles a state variable to switch between a playing and a paused state. However, in order to actually play or pause the video, toggling state is not enough. You also need to call [`play()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play) and [`pause()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/pause) on the DOM element for the `<video>`. Add a ref to it, and make the button work.
App.js
App.js
Download ResetFork
```
import { useState, useRef } from 'react';
export default function VideoPlayer() {
 const [isPlaying, setIsPlaying] = useState(false);
 function handleClick() {
  const nextIsPlaying = !isPlaying;
  setIsPlaying(nextIsPlaying);
 }
 return (
  <>
   <button onClick={handleClick}>
    {isPlaying ? 'Pause' : 'Play'}
   </button>
   <video width="250">
    <source
     src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
     type="video/mp4"
    />
   </video>
  </>
 )
}

```

Show more
For an extra challenge, keep the “Play” button in sync with whether the video is playing even if the user right-clicks the video and plays it using the built-in browser media controls. You might want to listen to `onPlay` and `onPause` on the video to do that.
Show solutionNext Challenge
[PreviousReferencing Values with Refs](https://react.dev/learn/referencing-values-with-refs)[NextSynchronizing with Effects](https://react.dev/learn/synchronizing-with-effects)
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
  * [Overview](https://react.dev/learn/manipulating-the-dom-with-refs)
  * [Getting a ref to the node ](https://react.dev/learn/manipulating-the-dom-with-refs#getting-a-ref-to-the-node)
  * [Example: Focusing a text input ](https://react.dev/learn/manipulating-the-dom-with-refs#example-focusing-a-text-input)
  * [Example: Scrolling to an element ](https://react.dev/learn/manipulating-the-dom-with-refs#example-scrolling-to-an-element)
  * [Accessing another component’s DOM nodes ](https://react.dev/learn/manipulating-the-dom-with-refs#accessing-another-components-dom-nodes)
  * [When React attaches the refs ](https://react.dev/learn/manipulating-the-dom-with-refs#when-react-attaches-the-refs)
  * [Best practices for DOM manipulation with refs ](https://react.dev/learn/manipulating-the-dom-with-refs#best-practices-for-dom-manipulation-with-refs)
  * [Recap](https://react.dev/learn/manipulating-the-dom-with-refs#recap)
  * [Challenges](https://react.dev/learn/manipulating-the-dom-with-refs#challenges)



