---
url: https://react.dev/learn/reacting-to-input-with-state
scraped_at: 2025-05-25T08:35:15.695434
title: Reacting to Input with State – React
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
# Reacting to Input with State[](https://react.dev/learn/reacting-to-input-with-state#undefined "Link for this heading")
React provides a declarative way to manipulate the UI. Instead of manipulating individual pieces of the UI directly, you describe the different states that your component can be in, and switch between them in response to the user input. This is similar to how designers think about the UI.
### You will learn
  * How declarative UI programming differs from imperative UI programming
  * How to enumerate the different visual states your component can be in
  * How to trigger the changes between the different visual states from code


## How declarative UI compares to imperative [](https://react.dev/learn/reacting-to-input-with-state#how-declarative-ui-compares-to-imperative "Link for How declarative UI compares to imperative ")
When you design UI interactions, you probably think about how the UI _changes_ in response to user actions. Consider a form that lets the user submit an answer:
  * When you type something into the form, the “Submit” button **becomes enabled.**
  * When you press “Submit”, both the form and the button **become disabled,** and a spinner **appears.**
  * If the network request succeeds, the form **gets hidden,** and the “Thank you” message **appears.**
  * If the network request fails, an error message **appears,** and the form **becomes enabled** again.


In **imperative programming,** the above corresponds directly to how you implement interaction. You have to write the exact instructions to manipulate the UI depending on what just happened. Here’s another way to think about this: imagine riding next to someone in a car and telling them turn by turn where to go.
![In a car driven by an anxious-looking person representing JavaScript, a passenger orders the driver to execute a sequence of complicated turn by turn navigations.](https://react.dev/images/docs/illustrations/i_imperative-ui-programming.png)
Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)
They don’t know where you want to go, they just follow your commands. (And if you get the directions wrong, you end up in the wrong place!) It’s called _imperative_ because you have to “command” each element, from the spinner to the button, telling the computer _how_ to update the UI.
In this example of imperative UI programming, the form is built _without_ React. It only uses the browser [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model):
index.jsindex.html
index.js
ResetFork
```
async function handleFormSubmit(e) {
 e.preventDefault();
 disable(textarea);
 disable(button);
 show(loadingMessage);
 hide(errorMessage);
 try {
  await submitForm(textarea.value);
  show(successMessage);
  hide(form);
 } catch (err) {
  show(errorMessage);
  errorMessage.textContent = err.message;
 } finally {
  hide(loadingMessage);
  enable(textarea);
  enable(button);
 }
}
function handleTextareaChange() {
 if (textarea.value.length === 0) {
  disable(button);
 } else {
  enable(button);
 }
}
function hide(el) {
 el.style.display = 'none';
}
function show(el) {
 el.style.display = '';
}
function enable(el) {
 el.disabled = false;
}
function disable(el) {
 el.disabled = true;
}
function submitForm(answer) {
 // Pretend it's hitting the network.
 return new Promise((resolve, reject) => {
  setTimeout(() => {
   if (answer.toLowerCase() === 'istanbul') {
    resolve();
   } else {
    reject(new Error('Good guess but a wrong answer. Try again!'));
   }
  }, 1500);
 });
}
let form = document.getElementById('form');
let textarea = document.getElementById('textarea');
let button = document.getElementById('button');
let loadingMessage = document.getElementById('loading');
let errorMessage = document.getElementById('error');
let successMessage = document.getElementById('success');
form.onsubmit = handleFormSubmit;
textarea.oninput = handleTextareaChange;

```

Show more
Manipulating the UI imperatively works well enough for isolated examples, but it gets exponentially more difficult to manage in more complex systems. Imagine updating a page full of different forms like this one. Adding a new UI element or a new interaction would require carefully checking all existing code to make sure you haven’t introduced a bug (for example, forgetting to show or hide something).
React was built to solve this problem.
In React, you don’t directly manipulate the UI—meaning you don’t enable, disable, show, or hide components directly. Instead, you **declare what you want to show,** and React figures out how to update the UI. Think of getting into a taxi and telling the driver where you want to go instead of telling them exactly where to turn. It’s the driver’s job to get you there, and they might even know some shortcuts you haven’t considered!
![In a car driven by React, a passenger asks to be taken to a specific place on the map. React figures out how to do that.](https://react.dev/images/docs/illustrations/i_declarative-ui-programming.png)
Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)
## Thinking about UI declaratively [](https://react.dev/learn/reacting-to-input-with-state#thinking-about-ui-declaratively "Link for Thinking about UI declaratively ")
You’ve seen how to implement a form imperatively above. To better understand how to think in React, you’ll walk through reimplementing this UI in React below:
  1. **Identify** your component’s different visual states
  2. **Determine** what triggers those state changes
  3. **Represent** the state in memory using `useState`
  4. **Remove** any non-essential state variables
  5. **Connect** the event handlers to set the state


### Step 1: Identify your component’s different visual states [](https://react.dev/learn/reacting-to-input-with-state#step-1-identify-your-components-different-visual-states "Link for Step 1: Identify your component’s different visual states ")
In computer science, you may hear about a [“state machine”](https://en.wikipedia.org/wiki/Finite-state_machine) being in one of several “states”. If you work with a designer, you may have seen mockups for different “visual states”. React stands at the intersection of design and computer science, so both of these ideas are sources of inspiration.
First, you need to visualize all the different “states” of the UI the user might see:
  * **Empty** : Form has a disabled “Submit” button.
  * **Typing** : Form has an enabled “Submit” button.
  * **Submitting** : Form is completely disabled. Spinner is shown.
  * **Success** : “Thank you” message is shown instead of a form.
  * **Error** : Same as Typing state, but with an extra error message.


Just like a designer, you’ll want to “mock up” or create “mocks” for the different states before you add logic. For example, here is a mock for just the visual part of the form. This mock is controlled by a prop called `status` with a default value of `'empty'`:
App.js
App.js
Download ResetFork
```
export default function Form({
 status = 'empty'
}) {
 if (status === 'success') {
  return <h1>That's right!</h1>
 }
 return (
  <>
   <h2>City quiz</h2>
   <p>
    In which city is there a billboard that turns air into drinkable water?
   </p>
   <form>
    <textarea />
    <br />
    <button>
     Submit
    </button>
   </form>
  </>
 )
}

```

Show more
You could call that prop anything you like, the naming is not important. Try editing `status = 'empty'` to `status = 'success'` to see the success message appear. Mocking lets you quickly iterate on the UI before you wire up any logic. Here is a more fleshed out prototype of the same component, still “controlled” by the `status` prop:
App.js
App.js
Download ResetFork
```
export default function Form({
 // Try 'submitting', 'error', 'success':
 status = 'empty'
}) {
 if (status === 'success') {
  return <h1>That's right!</h1>
 }
 return (
  <>
   <h2>City quiz</h2>
   <p>
    In which city is there a billboard that turns air into drinkable water?
   </p>
   <form>
    <textarea disabled={
     status === 'submitting'
    } />
    <br />
    <button disabled={
     status === 'empty' ||
     status === 'submitting'
    }>
     Submit
    </button>
    {status === 'error' &&
     <p className="Error">
      Good guess but a wrong answer. Try again!
     </p>
    }
   </form>
   </>
 );
}

```

Show more
##### Deep Dive
#### Displaying many visual states at once [](https://react.dev/learn/reacting-to-input-with-state#displaying-many-visual-states-at-once "Link for Displaying many visual states at once ")
Show Details
If a component has a lot of visual states, it can be convenient to show them all on one page:
App.jsForm.js
App.js
ResetFork
```
import Form from './Form.js';
let statuses = [
 'empty',
 'typing',
 'submitting',
 'success',
 'error',
];
export default function App() {
 return (
  <>
   {statuses.map(status => (
    <section key={status}>
     <h4>Form ({status}):</h4>
     <Form status={status} />
    </section>
   ))}
  </>
 );
}

```

Show more
Pages like this are often called “living styleguides” or “storybooks”.
### Step 2: Determine what triggers those state changes [](https://react.dev/learn/reacting-to-input-with-state#step-2-determine-what-triggers-those-state-changes "Link for Step 2: Determine what triggers those state changes ")
You can trigger state updates in response to two kinds of inputs:
  * **Human inputs,** like clicking a button, typing in a field, navigating a link.
  * **Computer inputs,** like a network response arriving, a timeout completing, an image loading.


![A finger.](https://react.dev/images/docs/illustrations/i_inputs1.png)
Human inputs
![Ones and zeroes.](https://react.dev/images/docs/illustrations/i_inputs2.png)
Computer inputs
Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)
In both cases, **you must set[state variables](https://react.dev/learn/state-a-components-memory#anatomy-of-usestate) to update the UI.** For the form you’re developing, you will need to change state in response to a few different inputs:
  * **Changing the text input** (human) should switch it from the _Empty_ state to the _Typing_ state or back, depending on whether the text box is empty or not.
  * **Clicking the Submit button** (human) should switch it to the _Submitting_ state.
  * **Successful network response** (computer) should switch it to the _Success_ state.
  * **Failed network response** (computer) should switch it to the _Error_ state with the matching error message.


### Note
Notice that human inputs often require [event handlers](https://react.dev/learn/responding-to-events)!
To help visualize this flow, try drawing each state on paper as a labeled circle, and each change between two states as an arrow. You can sketch out many flows this way and sort out bugs long before implementation.
![Flow chart moving left to right with 5 nodes. The first node labeled 'empty' has one edge labeled 'start typing' connected to a node labeled 'typing'. That node has one edge labeled 'press submit' connected to a node labeled 'submitting', which has two edges. The left edge is labeled 'network error' connecting to a node labeled 'error'. The right edge is labeled 'network success' connecting to a node labeled 'success'.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fresponding_to_input_flow.dark.png&w=1920&q=75)
![Flow chart moving left to right with 5 nodes. The first node labeled 'empty' has one edge labeled 'start typing' connected to a node labeled 'typing'. That node has one edge labeled 'press submit' connected to a node labeled 'submitting', which has two edges. The left edge is labeled 'network error' connecting to a node labeled 'error'. The right edge is labeled 'network success' connecting to a node labeled 'success'.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fresponding_to_input_flow.png&w=1920&q=75)
Form states
### Step 3: Represent the state in memory with `useState` [](https://react.dev/learn/reacting-to-input-with-state#step-3-represent-the-state-in-memory-with-usestate "Link for this heading")
Next you’ll need to represent the visual states of your component in memory with [`useState`.](https://react.dev/reference/react/useState) Simplicity is key: each piece of state is a “moving piece”, and **you want as few “moving pieces” as possible.** More complexity leads to more bugs!
Start with the state that _absolutely must_ be there. For example, you’ll need to store the `answer` for the input, and the `error` (if it exists) to store the last error:
```

const [answer, setAnswer] = useState('');
const [error, setError] = useState(null);

```

Then, you’ll need a state variable representing which one of the visual states that you want to display. There’s usually more than a single way to represent that in memory, so you’ll need to experiment with it.
If you struggle to think of the best way immediately, start by adding enough state that you’re _definitely_ sure that all the possible visual states are covered:
```

const [isEmpty, setIsEmpty] = useState(true);
const [isTyping, setIsTyping] = useState(false);
const [isSubmitting, setIsSubmitting] = useState(false);
const [isSuccess, setIsSuccess] = useState(false);
const [isError, setIsError] = useState(false);

```

Your first idea likely won’t be the best, but that’s ok—refactoring state is a part of the process!
### Step 4: Remove any non-essential state variables [](https://react.dev/learn/reacting-to-input-with-state#step-4-remove-any-non-essential-state-variables "Link for Step 4: Remove any non-essential state variables ")
You want to avoid duplication in the state content so you’re only tracking what is essential. Spending a little time on refactoring your state structure will make your components easier to understand, reduce duplication, and avoid unintended meanings. Your goal is to **prevent the cases where the state in memory doesn’t represent any valid UI that you’d want a user to see.** (For example, you never want to show an error message and disable the input at the same time, or the user won’t be able to correct the error!)
Here are some questions you can ask about your state variables:
  * **Does this state cause a paradox?** For example, `isTyping` and `isSubmitting` can’t both be `true`. A paradox usually means that the state is not constrained enough. There are four possible combinations of two booleans, but only three correspond to valid states. To remove the “impossible” state, you can combine these into a `status` that must be one of three values: `'typing'`, `'submitting'`, or `'success'`.
  * **Is the same information available in another state variable already?** Another paradox: `isEmpty` and `isTyping` can’t be `true` at the same time. By making them separate state variables, you risk them going out of sync and causing bugs. Fortunately, you can remove `isEmpty` and instead check `answer.length === 0`.
  * **Can you get the same information from the inverse of another state variable?** `isError` is not needed because you can check `error !== null` instead.


After this clean-up, you’re left with 3 (down from 7!) _essential_ state variables:
```

const [answer, setAnswer] = useState('');
const [error, setError] = useState(null);
const [status, setStatus] = useState('typing'); // 'typing', 'submitting', or 'success'

```

You know they are essential, because you can’t remove any of them without breaking the functionality.
##### Deep Dive
#### Eliminating “impossible” states with a reducer [](https://react.dev/learn/reacting-to-input-with-state#eliminating-impossible-states-with-a-reducer "Link for Eliminating “impossible” states with a reducer ")
Show Details
These three variables are a good enough representation of this form’s state. However, there are still some intermediate states that don’t fully make sense. For example, a non-null `error` doesn’t make sense when `status` is `'success'`. To model the state more precisely, you can [extract it into a reducer.](https://react.dev/learn/extracting-state-logic-into-a-reducer) Reducers let you unify multiple state variables into a single object and consolidate all the related logic!
### Step 5: Connect the event handlers to set state [](https://react.dev/learn/reacting-to-input-with-state#step-5-connect-the-event-handlers-to-set-state "Link for Step 5: Connect the event handlers to set state ")
Lastly, create event handlers that update the state. Below is the final form, with all event handlers wired up:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Form() {
 const [answer, setAnswer] = useState('');
 const [error, setError] = useState(null);
 const [status, setStatus] = useState('typing');
 if (status === 'success') {
  return <h1>That's right!</h1>
 }
 async function handleSubmit(e) {
  e.preventDefault();
  setStatus('submitting');
  try {
   await submitForm(answer);
   setStatus('success');
  } catch (err) {
   setStatus('typing');
   setError(err);
  }
 }
 function handleTextareaChange(e) {
  setAnswer(e.target.value);
 }
 return (
  <>
   <h2>City quiz</h2>
   <p>
    In which city is there a billboard that turns air into drinkable water?
   </p>
   <form onSubmit={handleSubmit}>
    <textarea
     value={answer}
     onChange={handleTextareaChange}
     disabled={status === 'submitting'}
    />
    <br />
    <button disabled={
     answer.length === 0 ||
     status === 'submitting'
    }>
     Submit
    </button>
    {error !== null &&
     <p className="Error">
      {error.message}
     </p>
    }
   </form>
  </>
 );
}
function submitForm(answer) {
 // Pretend it's hitting the network.
 return new Promise((resolve, reject) => {
  setTimeout(() => {
   let shouldError = answer.toLowerCase() !== 'lima'
   if (shouldError) {
    reject(new Error('Good guess but a wrong answer. Try again!'));
   } else {
    resolve();
   }
  }, 1500);
 });
}

```

Show more
Although this code is longer than the original imperative example, it is much less fragile. Expressing all interactions as state changes lets you later introduce new visual states without breaking existing ones. It also lets you change what should be displayed in each state without changing the logic of the interaction itself.
## Recap[](https://react.dev/learn/reacting-to-input-with-state#recap "Link for Recap")
  * Declarative programming means describing the UI for each visual state rather than micromanaging the UI (imperative).
  * When developing a component: 
    1. Identify all its visual states.
    2. Determine the human and computer triggers for state changes.
    3. Model the state with `useState`.
    4. Remove non-essential state to avoid bugs and paradoxes.
    5. Connect the event handlers to set state.


## Try out some challenges[](https://react.dev/learn/reacting-to-input-with-state#challenges "Link for Try out some challenges")
1. Add and remove a CSS class 2. Profile editor 3. Refactor the imperative solution without React 
#### 
Challenge 1 of 3: 
Add and remove a CSS class [](https://react.dev/learn/reacting-to-input-with-state#add-and-remove-a-css-class "Link for this heading")
Make it so that clicking on the picture _removes_ the `background--active` CSS class from the outer `<div>`, but _adds_ the `picture--active` class to the `<img>`. Clicking the background again should restore the original CSS classes.
Visually, you should expect that clicking on the picture removes the purple background and highlights the picture border. Clicking outside the picture highlights the background, but removes the picture border highlight.
App.js
App.js
Download ResetFork
```
export default function Picture() {
 return (
  <div className="background background--active">
   <img
    className="picture"
    alt="Rainbow houses in Kampung Pelangi, Indonesia"
    src="https://i.imgur.com/5qwVYb1.jpeg"
   />
  </div>
 );
}

```

Show solutionNext Challenge
[PreviousManaging State](https://react.dev/learn/managing-state)[NextChoosing the State Structure](https://react.dev/learn/choosing-the-state-structure)
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
  * [Overview](https://react.dev/learn/reacting-to-input-with-state)
  * [How declarative UI compares to imperative ](https://react.dev/learn/reacting-to-input-with-state#how-declarative-ui-compares-to-imperative)
  * [Thinking about UI declaratively ](https://react.dev/learn/reacting-to-input-with-state#thinking-about-ui-declaratively)
  * [Step 1: Identify your component’s different visual states ](https://react.dev/learn/reacting-to-input-with-state#step-1-identify-your-components-different-visual-states)
  * [Step 2: Determine what triggers those state changes ](https://react.dev/learn/reacting-to-input-with-state#step-2-determine-what-triggers-those-state-changes)
  * [Step 3: Represent the state in memory with `useState` ](https://react.dev/learn/reacting-to-input-with-state#step-3-represent-the-state-in-memory-with-usestate)
  * [Step 4: Remove any non-essential state variables ](https://react.dev/learn/reacting-to-input-with-state#step-4-remove-any-non-essential-state-variables)
  * [Step 5: Connect the event handlers to set state ](https://react.dev/learn/reacting-to-input-with-state#step-5-connect-the-event-handlers-to-set-state)
  * [Recap](https://react.dev/learn/reacting-to-input-with-state#recap)
  * [Challenges](https://react.dev/learn/reacting-to-input-with-state#challenges)



