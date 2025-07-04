---
url: https://react.dev/learn/rendering-lists
scraped_at: 2025-05-25T08:42:44.085461
title: Rendering Lists – React
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
# Rendering Lists[](https://react.dev/learn/rendering-lists#undefined "Link for this heading")
You will often want to display multiple similar components from a collection of data. You can use the [JavaScript array methods](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) to manipulate an array of data. On this page, you’ll use [`filter()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) and [`map()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array/map) with React to filter and transform your array of data into an array of components.
### You will learn
  * How to render components from an array using JavaScript’s `map()`
  * How to render only specific components using JavaScript’s `filter()`
  * When and why to use React keys


## Rendering data from arrays [](https://react.dev/learn/rendering-lists#rendering-data-from-arrays "Link for Rendering data from arrays ")
Say that you have a list of content.
```

<ul>
 <li>Creola Katherine Johnson: mathematician</li>
 <li>Mario José Molina-Pasquel Henríquez: chemist</li>
 <li>Mohammad Abdus Salam: physicist</li>
 <li>Percy Lavon Julian: chemist</li>
 <li>Subrahmanyan Chandrasekhar: astrophysicist</li>
</ul>

```

The only difference among those list items is their contents, their data. You will often need to show several instances of the same component using different data when building interfaces: from lists of comments to galleries of profile images. In these situations, you can store that data in JavaScript objects and arrays and use methods like [`map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) and [`filter()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) to render lists of components from them.
Here’s a short example of how to generate a list of items from an array:
  1. **Move** the data into an array:


```

const people = [
 'Creola Katherine Johnson: mathematician',
 'Mario José Molina-Pasquel Henríquez: chemist',
 'Mohammad Abdus Salam: physicist',
 'Percy Lavon Julian: chemist',
 'Subrahmanyan Chandrasekhar: astrophysicist'
];

```

  1. **Map** the `people` members into a new array of JSX nodes, `listItems`:


```

const listItems = people.map(person => <li>{person}</li>);

```

  1. **Return** `listItems` from your component wrapped in a `<ul>`:


```

return <ul>{listItems}</ul>;

```

Here is the result:
App.js
App.js
Download ResetFork
```
const people = [
 'Creola Katherine Johnson: mathematician',
 'Mario José Molina-Pasquel Henríquez: chemist',
 'Mohammad Abdus Salam: physicist',
 'Percy Lavon Julian: chemist',
 'Subrahmanyan Chandrasekhar: astrophysicist'
];
export default function List() {
 const listItems = people.map(person =>
  <li>{person}</li>
 );
 return <ul>{listItems}</ul>;
}

```

Console (1)
Each child in a list should have a unique "key" prop. Check the render method of `List`. See https://react.dev/link/warning-keys for more information.
Notice the sandbox above displays a console error:
Console
Warning: Each child in a list should have a unique “key” prop.
You’ll learn how to fix this error later on this page. Before we get to that, let’s add some structure to your data.
## Filtering arrays of items [](https://react.dev/learn/rendering-lists#filtering-arrays-of-items "Link for Filtering arrays of items ")
This data can be structured even more.
```

const people = [{
 id: 0,
 name: 'Creola Katherine Johnson',
 profession: 'mathematician',
}, {
 id: 1,
 name: 'Mario José Molina-Pasquel Henríquez',
 profession: 'chemist',
}, {
 id: 2,
 name: 'Mohammad Abdus Salam',
 profession: 'physicist',
}, {
 id: 3,
 name: 'Percy Lavon Julian',
 profession: 'chemist', 
}, {
 id: 4,
 name: 'Subrahmanyan Chandrasekhar',
 profession: 'astrophysicist',
}];

```

Let’s say you want a way to only show people whose profession is `'chemist'`. You can use JavaScript’s `filter()` method to return just those people. This method takes an array of items, passes them through a “test” (a function that returns `true` or `false`), and returns a new array of only those items that passed the test (returned `true`).
You only want the items where `profession` is `'chemist'`. The “test” function for this looks like `(person) => person.profession === 'chemist'`. Here’s how to put it together:
  1. **Create** a new array of just “chemist” people, `chemists`, by calling `filter()` on the `people` filtering by `person.profession === 'chemist'`:


```

const chemists = people.filter(person =>
 person.profession === 'chemist'
);

```

  1. Now **map** over `chemists`:


```

const listItems = chemists.map(person =>
 <li>
   <img
    src={getImageUrl(person)}
    alt={person.name}
   />
   <p>
    <b>{person.name}:</b>
    {' ' + person.profession + ' '}
    known for {person.accomplishment}
   </p>
 </li>
);

```

  1. Lastly, **return** the `listItems` from your component:


```

return <ul>{listItems}</ul>;

```

App.jsdata.jsutils.js
App.js
ResetFork
```
import { people } from './data.js';
import { getImageUrl } from './utils.js';
export default function List() {
 const chemists = people.filter(person =>
  person.profession === 'chemist'
 );
 const listItems = chemists.map(person =>
  <li>
   <img
    src={getImageUrl(person)}
    alt={person.name}
   />
   <p>
    <b>{person.name}:</b>
    {' ' + person.profession + ' '}
    known for {person.accomplishment}
   </p>
  </li>
 );
 return <ul>{listItems}</ul>;
}

```

Show more
### Pitfall
Arrow functions implicitly return the expression right after `=>`, so you didn’t need a `return` statement:
```

const listItems = chemists.map(person =>
 <li>...</li> // Implicit return!
);

```

However, **you must write`return` explicitly if your `=>` is followed by a `{` curly brace!**
```

const listItems = chemists.map(person => { // Curly brace
 return <li>...</li>;
});

```

Arrow functions containing `=> {` are said to have a [“block body”.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#function_body) They let you write more than a single line of code, but you _have to_ write a `return` statement yourself. If you forget it, nothing gets returned!
## Keeping list items in order with `key` [](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key "Link for this heading")
Notice that all the sandboxes above show an error in the console:
Console
Warning: Each child in a list should have a unique “key” prop.
You need to give each array item a `key` — a string or a number that uniquely identifies it among other items in that array:
```

<li key={person.id}>...</li>

```

### Note
JSX elements directly inside a `map()` call always need keys!
Keys tell React which array item each component corresponds to, so that it can match them up later. This becomes important if your array items can move (e.g. due to sorting), get inserted, or get deleted. A well-chosen `key` helps React infer what exactly has happened, and make the correct updates to the DOM tree.
Rather than generating keys on the fly, you should include them in your data:
App.jsdata.jsutils.js
data.js
ResetFork
```
export const people = [{
 id: 0, // Used in JSX as a key
 name: 'Creola Katherine Johnson',
 profession: 'mathematician',
 accomplishment: 'spaceflight calculations',
 imageId: 'MK3eW3A'
}, {
 id: 1, // Used in JSX as a key
 name: 'Mario José Molina-Pasquel Henríquez',
 profession: 'chemist',
 accomplishment: 'discovery of Arctic ozone hole',
 imageId: 'mynHUSa'
}, {
 id: 2, // Used in JSX as a key
 name: 'Mohammad Abdus Salam',
 profession: 'physicist',
 accomplishment: 'electromagnetism theory',
 imageId: 'bE7W1ji'
}, {
 id: 3, // Used in JSX as a key
 name: 'Percy Lavon Julian',
 profession: 'chemist',
 accomplishment: 'pioneering cortisone drugs, steroids and birth control pills',
 imageId: 'IOjWm71'
}, {
 id: 4, // Used in JSX as a key
 name: 'Subrahmanyan Chandrasekhar',
 profession: 'astrophysicist',
 accomplishment: 'white dwarf star mass calculations',
 imageId: 'lrWQx8l'
}];

```

Show more
##### Deep Dive
#### Displaying several DOM nodes for each list item [](https://react.dev/learn/rendering-lists#displaying-several-dom-nodes-for-each-list-item "Link for Displaying several DOM nodes for each list item ")
Show Details
What do you do when each item needs to render not one, but several DOM nodes?
The short [`<>...</>` Fragment](https://react.dev/reference/react/Fragment) syntax won’t let you pass a key, so you need to either group them into a single `<div>`, or use the slightly longer and [more explicit `<Fragment>` syntax:](https://react.dev/reference/react/Fragment#rendering-a-list-of-fragments)
```

import { Fragment } from 'react';
// ...
const listItems = people.map(person =>
 <Fragment key={person.id}>
  <h1>{person.name}</h1>
  <p>{person.bio}</p>
 </Fragment>
);

```

Fragments disappear from the DOM, so this will produce a flat list of `<h1>`, `<p>`, `<h1>`, `<p>`, and so on.
### Where to get your `key` [](https://react.dev/learn/rendering-lists#where-to-get-your-key "Link for this heading")
Different sources of data provide different sources of keys:
  * **Data from a database:** If your data is coming from a database, you can use the database keys/IDs, which are unique by nature.
  * **Locally generated data:** If your data is generated and persisted locally (e.g. notes in a note-taking app), use an incrementing counter, [`crypto.randomUUID()`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) or a package like [`uuid`](https://www.npmjs.com/package/uuid) when creating items.


### Rules of keys [](https://react.dev/learn/rendering-lists#rules-of-keys "Link for Rules of keys ")
  * **Keys must be unique among siblings.** However, it’s okay to use the same keys for JSX nodes in _different_ arrays.
  * **Keys must not change** or that defeats their purpose! Don’t generate them while rendering.


### Why does React need keys? [](https://react.dev/learn/rendering-lists#why-does-react-need-keys "Link for Why does React need keys? ")
Imagine that files on your desktop didn’t have names. Instead, you’d refer to them by their order — the first file, the second file, and so on. You could get used to it, but once you delete a file, it would get confusing. The second file would become the first file, the third file would be the second file, and so on.
File names in a folder and JSX keys in an array serve a similar purpose. They let us uniquely identify an item between its siblings. A well-chosen key provides more information than the position within the array. Even if the _position_ changes due to reordering, the `key` lets React identify the item throughout its lifetime.
### Pitfall
You might be tempted to use an item’s index in the array as its key. In fact, that’s what React will use if you don’t specify a `key` at all. But the order in which you render items will change over time if an item is inserted, deleted, or if the array gets reordered. Index as a key often leads to subtle and confusing bugs.
Similarly, do not generate keys on the fly, e.g. with `key={Math.random()}`. This will cause keys to never match up between renders, leading to all your components and DOM being recreated every time. Not only is this slow, but it will also lose any user input inside the list items. Instead, use a stable ID based on the data.
Note that your components won’t receive `key` as a prop. It’s only used as a hint by React itself. If your component needs an ID, you have to pass it as a separate prop: `<Profile key={id} userId={id} />`.
## Recap[](https://react.dev/learn/rendering-lists#recap "Link for Recap")
On this page you learned:
  * How to move data out of components and into data structures like arrays and objects.
  * How to generate sets of similar components with JavaScript’s `map()`.
  * How to create arrays of filtered items with JavaScript’s `filter()`.
  * Why and how to set `key` on each component in a collection so React can keep track of each of them even if their position or data changes.


## Try out some challenges[](https://react.dev/learn/rendering-lists#challenges "Link for Try out some challenges")
1. Splitting a list in two 2. Nested lists in one component 3. Extracting a list item component 4. List with a separator 
#### 
Challenge 1 of 4: 
Splitting a list in two [](https://react.dev/learn/rendering-lists#splitting-a-list-in-two "Link for this heading")
This example shows a list of all people.
Change it to show two separate lists one after another: **Chemists** and **Everyone Else.** Like previously, you can determine whether a person is a chemist by checking if `person.profession === 'chemist'`.
App.jsdata.jsutils.js
App.js
ResetFork
```
import { people } from './data.js';
import { getImageUrl } from './utils.js';
export default function List() {
 const listItems = people.map(person =>
  <li key={person.id}>
   <img
    src={getImageUrl(person)}
    alt={person.name}
   />
   <p>
    <b>{person.name}:</b>
    {' ' + person.profession + ' '}
    known for {person.accomplishment}
   </p>
  </li>
 );
 return (
  <article>
   <h1>Scientists</h1>
   <ul>{listItems}</ul>
  </article>
 );
}

```

Show more
Show solutionNext Challenge
[PreviousConditional Rendering](https://react.dev/learn/conditional-rendering)[NextKeeping Components Pure](https://react.dev/learn/keeping-components-pure)
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
  * [Overview](https://react.dev/learn/rendering-lists)
  * [Rendering data from arrays ](https://react.dev/learn/rendering-lists#rendering-data-from-arrays)
  * [Filtering arrays of items ](https://react.dev/learn/rendering-lists#filtering-arrays-of-items)
  * [Keeping list items in order with `key` ](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key)
  * [Where to get your `key` ](https://react.dev/learn/rendering-lists#where-to-get-your-key)
  * [Rules of keys ](https://react.dev/learn/rendering-lists#rules-of-keys)
  * [Why does React need keys? ](https://react.dev/learn/rendering-lists#why-does-react-need-keys)
  * [Recap](https://react.dev/learn/rendering-lists#recap)
  * [Challenges](https://react.dev/learn/rendering-lists#challenges)



