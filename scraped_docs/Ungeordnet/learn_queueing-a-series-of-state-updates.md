---
url: https://react.dev/learn/queueing-a-series-of-state-updates
scraped_at: 2025-05-25T08:29:59.063041
title: Queueing a Series of State Updates – React
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
[Adding Interactivity](https://react.dev/learn/adding-interactivity)
# Queueing a Series of State Updates[](https://react.dev/learn/queueing-a-series-of-state-updates#undefined "Link for this heading")
Setting a state variable will queue another render. But sometimes you might want to perform multiple operations on the value before queueing the next render. To do this, it helps to understand how React batches state updates.
### You will learn
  * What “batching” is and how React uses it to process multiple state updates
  * How to apply several updates to the same state variable in a row


## React batches state updates [](https://react.dev/learn/queueing-a-series-of-state-updates#react-batches-state-updates "Link for React batches state updates ")
You might expect that clicking the “+3” button will increment the counter three times because it calls `setNumber(number + 1)` three times:
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
import { useState } from 'react';
export default function Counter() {
const [number, setNumber] = useState(0);
return (
<>
<h1>{number}</h1>
<button onClick={() => {
setNumber(number + 1);
setNumber(number + 1);
setNumber(number + 1);
}}>+3</button>
</>
)
}
Show more
However, as you might recall from the previous section, [each render’s state values are fixed](https://react.dev/learn/state-as-a-snapshot#rendering-takes-a-snapshot-in-time), so the value of `number` inside the first render’s event handler is always `0`, no matter how many times you call `setNumber(1)`:
```

setNumber(0 + 1);
setNumber(0 + 1);
setNumber(0 + 1);

```

But there is one other factor at play here. **React waits until _all_ code in the event handlers has run before processing your state updates.** This is why the re-render only happens _after_ all these `setNumber()` calls.
This might remind you of a waiter taking an order at the restaurant. A waiter doesn’t run to the kitchen at the mention of your first dish! Instead, they let you finish your order, let you make changes to it, and even take orders from other people at the table.
![An elegant cursor at a restaurant places and order multiple times with React, playing the part of the waiter. After she calls setState\(\) multiple times, the waiter writes down the last one she requested as her final order.](https://react.dev/images/docs/illustrations/i_react-batching.png)
Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)
This lets you update multiple state variables—even from multiple components—without triggering too many [re-renders.](https://react.dev/learn/render-and-commit#re-renders-when-state-updates) But this also means that the UI won’t be updated until _after_ your event handler, and any code in it, completes. This behavior, also known as **batching,** makes your React app run much faster. It also avoids dealing with confusing “half-finished” renders where only some of the variables have been updated.
**React does not batch across _multiple_ intentional events like clicks**—each click is handled separately. Rest assured that React only does batching when it’s generally safe to do. This ensures that, for example, if the first button click disables a form, the second click would not submit it again.
## Updating the same state multiple times before the next render [](https://react.dev/learn/queueing-a-series-of-state-updates#updating-the-same-state-multiple-times-before-the-next-render "Link for Updating the same state multiple times before the next render ")
It is an uncommon use case, but if you would like to update the same state variable multiple times before the next render, instead of passing the _next state value_ like `setNumber(number + 1)`, you can pass a _function_ that calculates the next state based on the previous one in the queue, like `setNumber(n => n + 1)`. It is a way to tell React to “do something with the state value” instead of just replacing it.
Try incrementing the counter now:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Counter() {
 const [number, setNumber] = useState(0);
 return (
  <>
   <h1>{number}</h1>
   <button onClick={() => {
    setNumber(n => n + 1);
    setNumber(n => n + 1);
    setNumber(n => n + 1);
   }}>+3</button>
  </>
 )
}

```

Show more
Here, `n => n + 1` is called an **updater function.** When you pass it to a state setter:
  1. React queues this function to be processed after all the other code in the event handler has run.
  2. During the next render, React goes through the queue and gives you the final updated state.


```

setNumber(n => n + 1);
setNumber(n => n + 1);
setNumber(n => n + 1);

```

Here’s how React works through these lines of code while executing the event handler:
  1. `setNumber(n => n + 1)`: `n => n + 1` is a function. React adds it to a queue.
  2. `setNumber(n => n + 1)`: `n => n + 1` is a function. React adds it to a queue.
  3. `setNumber(n => n + 1)`: `n => n + 1` is a function. React adds it to a queue.


When you call `useState` during the next render, React goes through the queue. The previous `number` state was `0`, so that’s what React passes to the first updater function as the `n` argument. Then React takes the return value of your previous updater function and passes it to the next updater as `n`, and so on:
queued update| `n`| returns  
---|---|---  
`n => n + 1`| `0`| `0 + 1 = 1`  
`n => n + 1`| `1`| `1 + 1 = 2`  
`n => n + 1`| `2`| `2 + 1 = 3`  
React stores `3` as the final result and returns it from `useState`.
This is why clicking “+3” in the above example correctly increments the value by 3.
### What happens if you update state after replacing it [](https://react.dev/learn/queueing-a-series-of-state-updates#what-happens-if-you-update-state-after-replacing-it "Link for What happens if you update state after replacing it ")
What about this event handler? What do you think `number` will be in the next render?
```

<button onClick={() => {
 setNumber(number + 5);
 setNumber(n => n + 1);
}}>

```

App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Counter() {
 const [number, setNumber] = useState(0);
 return (
  <>
   <h1>{number}</h1>
   <button onClick={() => {
    setNumber(number + 5);
    setNumber(n => n + 1);
   }}>Increase the number</button>
  </>
 )
}

```

Here’s what this event handler tells React to do:
  1. `setNumber(number + 5)`: `number` is `0`, so `setNumber(0 + 5)`. React adds _“replace with`5` ”_ to its queue.
  2. `setNumber(n => n + 1)`: `n => n + 1` is an updater function. React adds _that function_ to its queue.


During the next render, React goes through the state queue:
queued update| `n`| returns  
---|---|---  
”replace with `5`”| `0` (unused)| `5`  
`n => n + 1`| `5`| `5 + 1 = 6`  
React stores `6` as the final result and returns it from `useState`.
### Note
You may have noticed that `setState(5)` actually works like `setState(n => 5)`, but `n` is unused!
### What happens if you replace state after updating it [](https://react.dev/learn/queueing-a-series-of-state-updates#what-happens-if-you-replace-state-after-updating-it "Link for What happens if you replace state after updating it ")
Let’s try one more example. What do you think `number` will be in the next render?
```

<button onClick={() => {
 setNumber(number + 5);
 setNumber(n => n + 1);
 setNumber(42);
}}>

```

App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Counter() {
 const [number, setNumber] = useState(0);
 return (
  <>
   <h1>{number}</h1>
   <button onClick={() => {
    setNumber(number + 5);
    setNumber(n => n + 1);
    setNumber(42);
   }}>Increase the number</button>
  </>
 )
}

```

Show more
Here’s how React works through these lines of code while executing this event handler:
  1. `setNumber(number + 5)`: `number` is `0`, so `setNumber(0 + 5)`. React adds _“replace with`5` ”_ to its queue.
  2. `setNumber(n => n + 1)`: `n => n + 1` is an updater function. React adds _that function_ to its queue.
  3. `setNumber(42)`: React adds _“replace with`42` ”_ to its queue.


During the next render, React goes through the state queue:
queued update| `n`| returns  
---|---|---  
”replace with `5`”| `0` (unused)| `5`  
`n => n + 1`| `5`| `5 + 1 = 6`  
”replace with `42`”| `6` (unused)| `42`  
Then React stores `42` as the final result and returns it from `useState`.
To summarize, here’s how you can think of what you’re passing to the `setNumber` state setter:
  * **An updater function** (e.g. `n => n + 1`) gets added to the queue.
  * **Any other value** (e.g. number `5`) adds “replace with `5`” to the queue, ignoring what’s already queued.


After the event handler completes, React will trigger a re-render. During the re-render, React will process the queue. Updater functions run during rendering, so **updater functions must be[pure](https://react.dev/learn/keeping-components-pure)** and only _return_ the result. Don’t try to set state from inside of them or run other side effects. In Strict Mode, React will run each updater function twice (but discard the second result) to help you find mistakes.
### Naming conventions [](https://react.dev/learn/queueing-a-series-of-state-updates#naming-conventions "Link for Naming conventions ")
It’s common to name the updater function argument by the first letters of the corresponding state variable:
```

setEnabled(e => !e);
setLastName(ln => ln.reverse());
setFriendCount(fc => fc * 2);

```

If you prefer more verbose code, another common convention is to repeat the full state variable name, like `setEnabled(enabled => !enabled)`, or to use a prefix like `setEnabled(prevEnabled => !prevEnabled)`.
## Recap[](https://react.dev/learn/queueing-a-series-of-state-updates#recap "Link for Recap")
  * Setting state does not change the variable in the existing render, but it requests a new render.
  * React processes state updates after event handlers have finished running. This is called batching.
  * To update some state multiple times in one event, you can use `setNumber(n => n + 1)` updater function.


## Try out some challenges[](https://react.dev/learn/queueing-a-series-of-state-updates#challenges "Link for Try out some challenges")
1. Fix a request counter 2. Implement the state queue yourself 
#### 
Challenge 1 of 2: 
Fix a request counter [](https://react.dev/learn/queueing-a-series-of-state-updates#fix-a-request-counter "Link for this heading")
You’re working on an art marketplace app that lets the user submit multiple orders for an art item at the same time. Each time the user presses the “Buy” button, the “Pending” counter should increase by one. After three seconds, the “Pending” counter should decrease, and the “Completed” counter should increase.
However, the “Pending” counter does not behave as intended. When you press “Buy”, it decreases to `-1` (which should not be possible!). And if you click fast twice, both counters seem to behave unpredictably.
Why does this happen? Fix both counters.
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function RequestTracker() {
 const [pending, setPending] = useState(0);
 const [completed, setCompleted] = useState(0);
 async function handleClick() {
  setPending(pending + 1);
  await delay(3000);
  setPending(pending - 1);
  setCompleted(completed + 1);
 }
 return (
  <>
   <h3>
    Pending: {pending}
   </h3>
   <h3>
    Completed: {completed}
   </h3>
   <button onClick={handleClick}>
    Buy   
   </button>
  </>
 );
}
function delay(ms) {
 return new Promise(resolve => {
  setTimeout(resolve, ms);
 });
}

```

Show more
Show solutionNext Challenge
[PreviousState as a Snapshot](https://react.dev/learn/state-as-a-snapshot)[NextUpdating Objects in State](https://react.dev/learn/updating-objects-in-state)
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
  * [Overview](https://react.dev/learn/queueing-a-series-of-state-updates)
  * [React batches state updates ](https://react.dev/learn/queueing-a-series-of-state-updates#react-batches-state-updates)
  * [Updating the same state multiple times before the next render ](https://react.dev/learn/queueing-a-series-of-state-updates#updating-the-same-state-multiple-times-before-the-next-render)
  * [What happens if you update state after replacing it ](https://react.dev/learn/queueing-a-series-of-state-updates#what-happens-if-you-update-state-after-replacing-it)
  * [What happens if you replace state after updating it ](https://react.dev/learn/queueing-a-series-of-state-updates#what-happens-if-you-replace-state-after-updating-it)
  * [Naming conventions ](https://react.dev/learn/queueing-a-series-of-state-updates#naming-conventions)
  * [Recap](https://react.dev/learn/queueing-a-series-of-state-updates#recap)
  * [Challenges](https://react.dev/learn/queueing-a-series-of-state-updates#challenges)



