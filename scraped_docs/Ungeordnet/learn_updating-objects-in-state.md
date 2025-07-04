---
url: https://react.dev/learn/updating-objects-in-state
scraped_at: 2025-05-25T08:41:37.630880
title: Updating Objects in State – React
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
# Updating Objects in State[](https://react.dev/learn/updating-objects-in-state#undefined "Link for this heading")
State can hold any kind of JavaScript value, including objects. But you shouldn’t change objects that you hold in the React state directly. Instead, when you want to update an object, you need to create a new one (or make a copy of an existing one), and then set the state to use that copy.
### You will learn
  * How to correctly update an object in React state
  * How to update a nested object without mutating it
  * What immutability is, and how not to break it
  * How to make object copying less repetitive with Immer


## What’s a mutation? [](https://react.dev/learn/updating-objects-in-state#whats-a-mutation "Link for What’s a mutation? ")
You can store any kind of JavaScript value in state.
```

const [x, setX] = useState(0);

```

So far you’ve been working with numbers, strings, and booleans. These kinds of JavaScript values are “immutable”, meaning unchangeable or “read-only”. You can trigger a re-render to _replace_ a value:
```

setX(5);

```

The `x` state changed from `0` to `5`, but the _number`0` itself_ did not change. It’s not possible to make any changes to the built-in primitive values like numbers, strings, and booleans in JavaScript.
Now consider an object in state:
```

const [position, setPosition] = useState({ x: 0, y: 0 });

```

Technically, it is possible to change the contents of _the object itself_. **This is called a mutation:**
```

position.x = 5;

```

However, although objects in React state are technically mutable, you should treat them **as if** they were immutable—like numbers, booleans, and strings. Instead of mutating them, you should always replace them.
## Treat state as read-only [](https://react.dev/learn/updating-objects-in-state#treat-state-as-read-only "Link for Treat state as read-only ")
In other words, you should **treat any JavaScript object that you put into state as read-only.**
This example holds an object in state to represent the current pointer position. The red dot is supposed to move when you touch or move the cursor over the preview area. But the dot stays in the initial position:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function MovingDot() {
 const [position, setPosition] = useState({
  x: 0,
  y: 0
 });
 return (
  <div
   onPointerMove={e => {
    position.x = e.clientX;
    position.y = e.clientY;
   }}
   style={{
    position: 'relative',
    width: '100vw',
    height: '100vh',
   }}>
   <div style={{
    position: 'absolute',
    backgroundColor: 'red',
    borderRadius: '50%',
    transform: `translate(${position.x}px, ${position.y}px)`,
    left: -10,
    top: -10,
    width: 20,
    height: 20,
   }} />
  </div>
 );
}

```

Show more
The problem is with this bit of code.
```

onPointerMove={e => {
 position.x = e.clientX;
 position.y = e.clientY;
}}

```

This code modifies the object assigned to `position` from [the previous render.](https://react.dev/learn/state-as-a-snapshot#rendering-takes-a-snapshot-in-time) But without using the state setting function, React has no idea that object has changed. So React does not do anything in response. It’s like trying to change the order after you’ve already eaten the meal. While mutating state can work in some cases, we don’t recommend it. You should treat the state value you have access to in a render as read-only.
To actually [trigger a re-render](https://react.dev/learn/state-as-a-snapshot#setting-state-triggers-renders) in this case, **create a _new_ object and pass it to the state setting function:**
```

onPointerMove={e => {
 setPosition({
  x: e.clientX,
  y: e.clientY
 });
}}

```

With `setPosition`, you’re telling React:
  * Replace `position` with this new object
  * And render this component again


Notice how the red dot now follows your pointer when you touch or hover over the preview area:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function MovingDot() {
 const [position, setPosition] = useState({
  x: 0,
  y: 0
 });
 return (
  <div
   onPointerMove={e => {
    setPosition({
     x: e.clientX,
     y: e.clientY
    });
   }}
   style={{
    position: 'relative',
    width: '100vw',
    height: '100vh',
   }}>
   <div style={{
    position: 'absolute',
    backgroundColor: 'red',
    borderRadius: '50%',
    transform: `translate(${position.x}px, ${position.y}px)`,
    left: -10,
    top: -10,
    width: 20,
    height: 20,
   }} />
  </div>
 );
}

```

Show more
##### Deep Dive
#### Local mutation is fine [](https://react.dev/learn/updating-objects-in-state#local-mutation-is-fine "Link for Local mutation is fine ")
Show Details
Code like this is a problem because it modifies an _existing_ object in state:
```

position.x = e.clientX;
position.y = e.clientY;

```

But code like this is **absolutely fine** because you’re mutating a fresh object you have _just created_ :
```

const nextPosition = {};
nextPosition.x = e.clientX;
nextPosition.y = e.clientY;
setPosition(nextPosition);

```

In fact, it is completely equivalent to writing this:
```

setPosition({
 x: e.clientX,
 y: e.clientY
});

```

Mutation is only a problem when you change _existing_ objects that are already in state. Mutating an object you’ve just created is okay because _no other code references it yet._ Changing it isn’t going to accidentally impact something that depends on it. This is called a “local mutation”. You can even do local mutation [while rendering.](https://react.dev/learn/keeping-components-pure#local-mutation-your-components-little-secret) Very convenient and completely okay!
## Copying objects with the spread syntax [](https://react.dev/learn/updating-objects-in-state#copying-objects-with-the-spread-syntax "Link for Copying objects with the spread syntax ")
In the previous example, the `position` object is always created fresh from the current cursor position. But often, you will want to include _existing_ data as a part of the new object you’re creating. For example, you may want to update _only one_ field in a form, but keep the previous values for all other fields.
These input fields don’t work because the `onChange` handlers mutate the state:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Form() {
 const [person, setPerson] = useState({
  firstName: 'Barbara',
  lastName: 'Hepworth',
  email: 'bhepworth@sculpture.com'
 });
 function handleFirstNameChange(e) {
  person.firstName = e.target.value;
 }
 function handleLastNameChange(e) {
  person.lastName = e.target.value;
 }
 function handleEmailChange(e) {
  person.email = e.target.value;
 }
 return (
  <>
   <label>
    First name:
    <input
     value={person.firstName}
     onChange={handleFirstNameChange}
    />
   </label>
   <label>
    Last name:
    <input
     value={person.lastName}
     onChange={handleLastNameChange}
    />
   </label>
   <label>
    Email:
    <input
     value={person.email}
     onChange={handleEmailChange}
    />
   </label>
   <p>
    {person.firstName}{' '}
    {person.lastName}{' '}
    ({person.email})
   </p>
  </>
 );
}

```

Show more
For example, this line mutates the state from a past render:
```

person.firstName = e.target.value;

```

The reliable way to get the behavior you’re looking for is to create a new object and pass it to `setPerson`. But here, you want to also **copy the existing data into it** because only one of the fields has changed:
```

setPerson({
 firstName: e.target.value, // New first name from the input
 lastName: person.lastName,
 email: person.email
});

```

You can use the `...` [object spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals) syntax so that you don’t need to copy every property separately.
```

setPerson({
 ...person, // Copy the old fields
 firstName: e.target.value // But override this one
});

```

Now the form works!
Notice how you didn’t declare a separate state variable for each input field. For large forms, keeping all data grouped in an object is very convenient—as long as you update it correctly!
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Form() {
 const [person, setPerson] = useState({
  firstName: 'Barbara',
  lastName: 'Hepworth',
  email: 'bhepworth@sculpture.com'
 });
 function handleFirstNameChange(e) {
  setPerson({
   ...person,
   firstName: e.target.value
  });
 }
 function handleLastNameChange(e) {
  setPerson({
   ...person,
   lastName: e.target.value
  });
 }
 function handleEmailChange(e) {
  setPerson({
   ...person,
   email: e.target.value
  });
 }
 return (
  <>
   <label>
    First name:
    <input
     value={person.firstName}
     onChange={handleFirstNameChange}
    />
   </label>
   <label>
    Last name:
    <input
     value={person.lastName}
     onChange={handleLastNameChange}
    />
   </label>
   <label>
    Email:
    <input
     value={person.email}
     onChange={handleEmailChange}
    />
   </label>
   <p>
    {person.firstName}{' '}
    {person.lastName}{' '}
    ({person.email})
   </p>
  </>
 );
}

```

Show more
Note that the `...` spread syntax is “shallow”—it only copies things one level deep. This makes it fast, but it also means that if you want to update a nested property, you’ll have to use it more than once.
##### Deep Dive
#### Using a single event handler for multiple fields [](https://react.dev/learn/updating-objects-in-state#using-a-single-event-handler-for-multiple-fields "Link for Using a single event handler for multiple fields ")
Show Details
You can also use the `[` and `]` braces inside your object definition to specify a property with a dynamic name. Here is the same example, but with a single event handler instead of three different ones:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Form() {
 const [person, setPerson] = useState({
  firstName: 'Barbara',
  lastName: 'Hepworth',
  email: 'bhepworth@sculpture.com'
 });
 function handleChange(e) {
  setPerson({
   ...person,
   [e.target.name]: e.target.value
  });
 }
 return (
  <>
   <label>
    First name:
    <input
     name="firstName"
     value={person.firstName}
     onChange={handleChange}
    />
   </label>
   <label>
    Last name:
    <input
     name="lastName"
     value={person.lastName}
     onChange={handleChange}
    />
   </label>
   <label>
    Email:
    <input
     name="email"
     value={person.email}
     onChange={handleChange}
    />
   </label>
   <p>
    {person.firstName}{' '}
    {person.lastName}{' '}
    ({person.email})
   </p>
  </>
 );
}

```

Show more
Here, `e.target.name` refers to the `name` property given to the `<input>` DOM element.
## Updating a nested object [](https://react.dev/learn/updating-objects-in-state#updating-a-nested-object "Link for Updating a nested object ")
Consider a nested object structure like this:
```

const [person, setPerson] = useState({
 name: 'Niki de Saint Phalle',
 artwork: {
  title: 'Blue Nana',
  city: 'Hamburg',
  image: 'https://i.imgur.com/Sd1AgUOm.jpg',
 }
});

```

If you wanted to update `person.artwork.city`, it’s clear how to do it with mutation:
```

person.artwork.city = 'New Delhi';

```

But in React, you treat state as immutable! In order to change `city`, you would first need to produce the new `artwork` object (pre-populated with data from the previous one), and then produce the new `person` object which points at the new `artwork`:
```

const nextArtwork = { ...person.artwork, city: 'New Delhi' };
const nextPerson = { ...person, artwork: nextArtwork };
setPerson(nextPerson);

```

Or, written as a single function call:
```

setPerson({
 ...person, // Copy other fields
 artwork: { // but replace the artwork
  ...person.artwork, // with the same one
  city: 'New Delhi' // but in New Delhi!
 }
});

```

This gets a bit wordy, but it works fine for many cases:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Form() {
 const [person, setPerson] = useState({
  name: 'Niki de Saint Phalle',
  artwork: {
   title: 'Blue Nana',
   city: 'Hamburg',
   image: 'https://i.imgur.com/Sd1AgUOm.jpg',
  }
 });
 function handleNameChange(e) {
  setPerson({
   ...person,
   name: e.target.value
  });
 }
 function handleTitleChange(e) {
  setPerson({
   ...person,
   artwork: {
    ...person.artwork,
    title: e.target.value
   }
  });
 }
 function handleCityChange(e) {
  setPerson({
   ...person,
   artwork: {
    ...person.artwork,
    city: e.target.value
   }
  });
 }
 function handleImageChange(e) {
  setPerson({
   ...person,
   artwork: {
    ...person.artwork,
    image: e.target.value
   }
  });
 }
 return (
  <>
   <label>
    Name:
    <input
     value={person.name}
     onChange={handleNameChange}
    />
   </label>
   <label>
    Title:
    <input
     value={person.artwork.title}
     onChange={handleTitleChange}
    />
   </label>
   <label>
    City:
    <input
     value={person.artwork.city}
     onChange={handleCityChange}
    />
   </label>
   <label>
    Image:
    <input
     value={person.artwork.image}
     onChange={handleImageChange}
    />
   </label>
   <p>
    <i>{person.artwork.title}</i>
    {' by '}
    {person.name}
    <br />
    (located in {person.artwork.city})
   </p>
   <img 
    src={person.artwork.image} 
    alt={person.artwork.title}
   />
  </>
 );
}

```

Show more
##### Deep Dive
#### Objects are not really nested [](https://react.dev/learn/updating-objects-in-state#objects-are-not-really-nested "Link for Objects are not really nested ")
Show Details
An object like this appears “nested” in code:
```

let obj = {
 name: 'Niki de Saint Phalle',
 artwork: {
  title: 'Blue Nana',
  city: 'Hamburg',
  image: 'https://i.imgur.com/Sd1AgUOm.jpg',
 }
};

```

However, “nesting” is an inaccurate way to think about how objects behave. When the code executes, there is no such thing as a “nested” object. You are really looking at two different objects:
```

let obj1 = {
 title: 'Blue Nana',
 city: 'Hamburg',
 image: 'https://i.imgur.com/Sd1AgUOm.jpg',
};
let obj2 = {
 name: 'Niki de Saint Phalle',
 artwork: obj1
};

```

The `obj1` object is not “inside” `obj2`. For example, `obj3` could “point” at `obj1` too:
```

let obj1 = {
 title: 'Blue Nana',
 city: 'Hamburg',
 image: 'https://i.imgur.com/Sd1AgUOm.jpg',
};
let obj2 = {
 name: 'Niki de Saint Phalle',
 artwork: obj1
};
let obj3 = {
 name: 'Copycat',
 artwork: obj1
};

```

If you were to mutate `obj3.artwork.city`, it would affect both `obj2.artwork.city` and `obj1.city`. This is because `obj3.artwork`, `obj2.artwork`, and `obj1` are the same object. This is difficult to see when you think of objects as “nested”. Instead, they are separate objects “pointing” at each other with properties.
### Write concise update logic with Immer [](https://react.dev/learn/updating-objects-in-state#write-concise-update-logic-with-immer "Link for Write concise update logic with Immer ")
If your state is deeply nested, you might want to consider [flattening it.](https://react.dev/learn/choosing-the-state-structure#avoid-deeply-nested-state) But, if you don’t want to change your state structure, you might prefer a shortcut to nested spreads. [Immer](https://github.com/immerjs/use-immer) is a popular library that lets you write using the convenient but mutating syntax and takes care of producing the copies for you. With Immer, the code you write looks like you are “breaking the rules” and mutating an object:
```

updatePerson(draft => {
 draft.artwork.city = 'Lagos';
});

```

But unlike a regular mutation, it doesn’t overwrite the past state!
##### Deep Dive
#### How does Immer work? [](https://react.dev/learn/updating-objects-in-state#how-does-immer-work "Link for How does Immer work? ")
Show Details
The `draft` provided by Immer is a special type of object, called a [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy), that “records” what you do with it. This is why you can mutate it freely as much as you like! Under the hood, Immer figures out which parts of the `draft` have been changed, and produces a completely new object that contains your edits.
To try Immer:
  1. Run `npm install use-immer` to add Immer as a dependency
  2. Then replace `import { useState } from 'react'` with `import { useImmer } from 'use-immer'`


Here is the above example converted to Immer:
package.jsonApp.js
package.json
ResetFork
```
{
 "dependencies": {
  "immer": "1.7.3",
  "react": "latest",
  "react-dom": "latest",
  "react-scripts": "latest",
  "use-immer": "0.5.1"
 },
 "scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test --env=jsdom",
  "eject": "react-scripts eject"
 },
 "devDependencies": {}
}
```

Notice how much more concise the event handlers have become. You can mix and match `useState` and `useImmer` in a single component as much as you like. Immer is a great way to keep the update handlers concise, especially if there’s nesting in your state, and copying objects leads to repetitive code.
##### Deep Dive
#### Why is mutating state not recommended in React? [](https://react.dev/learn/updating-objects-in-state#why-is-mutating-state-not-recommended-in-react "Link for Why is mutating state not recommended in React? ")
Show Details
There are a few reasons:
  * **Debugging:** If you use `console.log` and don’t mutate state, your past logs won’t get clobbered by the more recent state changes. So you can clearly see how state has changed between renders.
  * **Optimizations:** Common React [optimization strategies](https://react.dev/reference/react/memo) rely on skipping work if previous props or state are the same as the next ones. If you never mutate state, it is very fast to check whether there were any changes. If `prevObj === obj`, you can be sure that nothing could have changed inside of it.
  * **New Features:** The new React features we’re building rely on state being [treated like a snapshot.](https://react.dev/learn/state-as-a-snapshot) If you’re mutating past versions of state, that may prevent you from using the new features.
  * **Requirement Changes:** Some application features, like implementing Undo/Redo, showing a history of changes, or letting the user reset a form to earlier values, are easier to do when nothing is mutated. This is because you can keep past copies of state in memory, and reuse them when appropriate. If you start with a mutative approach, features like this can be difficult to add later on.
  * **Simpler Implementation:** Because React does not rely on mutation, it does not need to do anything special with your objects. It does not need to hijack their properties, always wrap them into Proxies, or do other work at initialization as many “reactive” solutions do. This is also why React lets you put any object into state—no matter how large—without additional performance or correctness pitfalls.


In practice, you can often “get away” with mutating state in React, but we strongly advise you not to do that so that you can use new React features developed with this approach in mind. Future contributors and perhaps even your future self will thank you!
## Recap[](https://react.dev/learn/updating-objects-in-state#recap "Link for Recap")
  * Treat all state in React as immutable.
  * When you store objects in state, mutating them will not trigger renders and will change the state in previous render “snapshots”.
  * Instead of mutating an object, create a _new_ version of it, and trigger a re-render by setting state to it.
  * You can use the `{...obj, something: 'newValue'}` object spread syntax to create copies of objects.
  * Spread syntax is shallow: it only copies one level deep.
  * To update a nested object, you need to create copies all the way up from the place you’re updating.
  * To reduce repetitive copying code, use Immer.


## Try out some challenges[](https://react.dev/learn/updating-objects-in-state#challenges "Link for Try out some challenges")
1. Fix incorrect state updates 2. Find and fix the mutation 3. Update an object with Immer 
#### 
Challenge 1 of 3: 
Fix incorrect state updates [](https://react.dev/learn/updating-objects-in-state#fix-incorrect-state-updates "Link for this heading")
This form has a few bugs. Click the button that increases the score a few times. Notice that it does not increase. Then edit the first name, and notice that the score has suddenly “caught up” with your changes. Finally, edit the last name, and notice that the score has disappeared completely.
Your task is to fix all of these bugs. As you fix them, explain why each of them happens.
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Scoreboard() {
 const [player, setPlayer] = useState({
  firstName: 'Ranjani',
  lastName: 'Shettar',
  score: 10,
 });
 function handlePlusClick() {
  player.score++;
 }
 function handleFirstNameChange(e) {
  setPlayer({
   ...player,
   firstName: e.target.value,
  });
 }
 function handleLastNameChange(e) {
  setPlayer({
   lastName: e.target.value
  });
 }
 return (
  <>
   <label>
    Score: <b>{player.score}</b>
    {' '}
    <button onClick={handlePlusClick}>
     +1
    </button>
   </label>
   <label>
    First name:
    <input
     value={player.firstName}
     onChange={handleFirstNameChange}
    />
   </label>
   <label>
    Last name:
    <input
     value={player.lastName}
     onChange={handleLastNameChange}
    />
   </label>
  </>
 );
}

```

Show more
Show solutionNext Challenge
[PreviousQueueing a Series of State Updates](https://react.dev/learn/queueing-a-series-of-state-updates)[NextUpdating Arrays in State](https://react.dev/learn/updating-arrays-in-state)
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
  * [Overview](https://react.dev/learn/updating-objects-in-state)
  * [What’s a mutation? ](https://react.dev/learn/updating-objects-in-state#whats-a-mutation)
  * [Treat state as read-only ](https://react.dev/learn/updating-objects-in-state#treat-state-as-read-only)
  * [Copying objects with the spread syntax ](https://react.dev/learn/updating-objects-in-state#copying-objects-with-the-spread-syntax)
  * [Updating a nested object ](https://react.dev/learn/updating-objects-in-state#updating-a-nested-object)
  * [Write concise update logic with Immer ](https://react.dev/learn/updating-objects-in-state#write-concise-update-logic-with-immer)
  * [Recap](https://react.dev/learn/updating-objects-in-state#recap)
  * [Challenges](https://react.dev/learn/updating-objects-in-state#challenges)



