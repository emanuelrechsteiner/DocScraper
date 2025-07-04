---
url: https://react.dev/learn/passing-props-to-a-component
scraped_at: 2025-05-25T08:37:17.161547
title: Passing Props to a Component – React
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
# Passing Props to a Component[](https://react.dev/learn/passing-props-to-a-component#undefined "Link for this heading")
React components use _props_ to communicate with each other. Every parent component can pass some information to its child components by giving them props. Props might remind you of HTML attributes, but you can pass any JavaScript value through them, including objects, arrays, and functions.
### You will learn
  * How to pass props to a component
  * How to read props from a component
  * How to specify default values for props
  * How to pass some JSX to a component
  * How props change over time


## Familiar props [](https://react.dev/learn/passing-props-to-a-component#familiar-props "Link for Familiar props ")
Props are the information that you pass to a JSX tag. For example, `className`, `src`, `alt`, `width`, and `height` are some of the props you can pass to an `<img>`:
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
function Avatar() {
return (
<img
className="avatar"
src="https://i.imgur.com/1bX5QH6.jpg"
alt="Lin Lanying"
width={100}
height={100}
/>
);
}
export default function Profile() {
return (
<Avatar />
);
}
Show more
The props you can pass to an `<img>` tag are predefined (ReactDOM conforms to [the HTML standard](https://www.w3.org/TR/html52/semantics-embedded-content.html#the-img-element)). But you can pass any props to _your own_ components, such as `<Avatar>`, to customize them. Here’s how!
## Passing props to a component [](https://react.dev/learn/passing-props-to-a-component#passing-props-to-a-component "Link for Passing props to a component ")
In this code, the `Profile` component isn’t passing any props to its child component, `Avatar`:
```

export default function Profile() {
 return (
  <Avatar />
 );
}

```

You can give `Avatar` some props in two steps.
### Step 1: Pass props to the child component [](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component "Link for Step 1: Pass props to the child component ")
First, pass some props to `Avatar`. For example, let’s pass two props: `person` (an object), and `size` (a number):
```

export default function Profile() {
 return (
  <Avatar
   person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}
   size={100}
  />
 );
}

```

### Note
If double curly braces after `person=` confuse you, recall [they’re merely an object](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx) inside the JSX curlies.
Now you can read these props inside the `Avatar` component.
### Step 2: Read props inside the child component [](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component "Link for Step 2: Read props inside the child component ")
You can read these props by listing their names `person, size` separated by the commas inside `({` and `})` directly after `function Avatar`. This lets you use them inside the `Avatar` code, like you would with a variable.
```

function Avatar({ person, size }) {
 // person and size are available here
}

```

Add some logic to `Avatar` that uses the `person` and `size` props for rendering, and you’re done.
Now you can configure `Avatar` to render in many different ways with different props. Try tweaking the values!
App.jsutils.js
App.js
ResetFork
```
import { getImageUrl } from './utils.js';
function Avatar({ person, size }) {
 return (
  <img
   className="avatar"
   src={getImageUrl(person)}
   alt={person.name}
   width={size}
   height={size}
  />
 );
}
export default function Profile() {
 return (
  <div>
   <Avatar
    size={100}
    person={{ 
     name: 'Katsuko Saruhashi', 
     imageId: 'YfeOqp2'
    }}
   />
   <Avatar
    size={80}
    person={{
     name: 'Aklilu Lemma', 
     imageId: 'OKS67lh'
    }}
   />
   <Avatar
    size={50}
    person={{ 
     name: 'Lin Lanying',
     imageId: '1bX5QH6'
    }}
   />
  </div>
 );
}

```

Show more
Props let you think about parent and child components independently. For example, you can change the `person` or the `size` props inside `Profile` without having to think about how `Avatar` uses them. Similarly, you can change how the `Avatar` uses these props, without looking at the `Profile`.
You can think of props like “knobs” that you can adjust. They serve the same role as arguments serve for functions—in fact, props _are_ the only argument to your component! React component functions accept a single argument, a `props` object:
```

function Avatar(props) {
 let person = props.person;
 let size = props.size;
 // ...
}

```

Usually you don’t need the whole `props` object itself, so you destructure it into individual props.
### Pitfall
**Don’t miss the pair of`{` and `}` curlies** inside of `(` and `)` when declaring props:
```

function Avatar({ person, size }) {
 // ...
}

```

This syntax is called [“destructuring”](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Unpacking_fields_from_objects_passed_as_a_function_parameter) and is equivalent to reading properties from a function parameter:
```

function Avatar(props) {
 let person = props.person;
 let size = props.size;
 // ...
}

```

## Specifying a default value for a prop [](https://react.dev/learn/passing-props-to-a-component#specifying-a-default-value-for-a-prop "Link for Specifying a default value for a prop ")
If you want to give a prop a default value to fall back on when no value is specified, you can do it with the destructuring by putting `=` and the default value right after the parameter:
```

function Avatar({ person, size = 100 }) {
 // ...
}

```

Now, if `<Avatar person={...} />` is rendered with no `size` prop, the `size` will be set to `100`.
The default value is only used if the `size` prop is missing or if you pass `size={undefined}`. But if you pass `size={null}` or `size={0}`, the default value will **not** be used.
## Forwarding props with the JSX spread syntax [](https://react.dev/learn/passing-props-to-a-component#forwarding-props-with-the-jsx-spread-syntax "Link for Forwarding props with the JSX spread syntax ")
Sometimes, passing props gets very repetitive:
```

function Profile({ person, size, isSepia, thickBorder }) {
 return (
  <div className="card">
   <Avatar
    person={person}
    size={size}
    isSepia={isSepia}
    thickBorder={thickBorder}
   />
  </div>
 );
}

```

There’s nothing wrong with repetitive code—it can be more legible. But at times you may value conciseness. Some components forward all of their props to their children, like how this `Profile` does with `Avatar`. Because they don’t use any of their props directly, it can make sense to use a more concise “spread” syntax:
```

function Profile(props) {
 return (
  <div className="card">
   <Avatar {...props} />
  </div>
 );
}

```

This forwards all of `Profile`’s props to the `Avatar` without listing each of their names.
**Use spread syntax with restraint.** If you’re using it in every other component, something is wrong. Often, it indicates that you should split your components and pass children as JSX. More on that next!
## Passing JSX as children [](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children "Link for Passing JSX as children ")
It is common to nest built-in browser tags:
```

<div>
 <img />
</div>

```

Sometimes you’ll want to nest your own components the same way:
```

<Card>
 <Avatar />
</Card>

```

When you nest content inside a JSX tag, the parent component will receive that content in a prop called `children`. For example, the `Card` component below will receive a `children` prop set to `<Avatar />` and render it in a wrapper div:
App.jsAvatar.jsutils.js
App.js
ResetFork
```
import Avatar from './Avatar.js';
function Card({ children }) {
 return (
  <div className="card">
   {children}
  </div>
 );
}
export default function Profile() {
 return (
  <Card>
   <Avatar
    size={100}
    person={{ 
     name: 'Katsuko Saruhashi',
     imageId: 'YfeOqp2'
    }}
   />
  </Card>
 );
}

```

Show more
Try replacing the `<Avatar>` inside `<Card>` with some text to see how the `Card` component can wrap any nested content. It doesn’t need to “know” what’s being rendered inside of it. You will see this flexible pattern in many places.
You can think of a component with a `children` prop as having a “hole” that can be “filled in” by its parent components with arbitrary JSX. You will often use the `children` prop for visual wrappers: panels, grids, etc.
![A puzzle-like Card tile with a slot for "children" pieces like text and Avatar](https://react.dev/images/docs/illustrations/i_children-prop.png)
Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)
## How props change over time [](https://react.dev/learn/passing-props-to-a-component#how-props-change-over-time "Link for How props change over time ")
The `Clock` component below receives two props from its parent component: `color` and `time`. (The parent component’s code is omitted because it uses [state](https://react.dev/learn/state-a-components-memory), which we won’t dive into just yet.)
Try changing the color in the select box below:
Clock.js
Clock.js
ResetFork
```
export default function Clock({ color, time }) {
 return (
  <h1 style={{ color: color }}>
   {time}
  </h1>
 );
}

```

This example illustrates that **a component may receive different props over time.** Props are not always static! Here, the `time` prop changes every second, and the `color` prop changes when you select another color. Props reflect a component’s data at any point in time, rather than only in the beginning.
However, props are [immutable](https://en.wikipedia.org/wiki/Immutable_object)—a term from computer science meaning “unchangeable”. When a component needs to change its props (for example, in response to a user interaction or new data), it will have to “ask” its parent component to pass it _different props_ —a new object! Its old props will then be cast aside, and eventually the JavaScript engine will reclaim the memory taken by them.
**Don’t try to “change props”.** When you need to respond to the user input (like changing the selected color), you will need to “set state”, which you can learn about in [State: A Component’s Memory.](https://react.dev/learn/state-a-components-memory)
## Recap[](https://react.dev/learn/passing-props-to-a-component#recap "Link for Recap")
  * To pass props, add them to the JSX, just like you would with HTML attributes.
  * To read props, use the `function Avatar({ person, size })` destructuring syntax.
  * You can specify a default value like `size = 100`, which is used for missing and `undefined` props.
  * You can forward all props with `<Avatar {...props} />` JSX spread syntax, but don’t overuse it!
  * Nested JSX like `<Card><Avatar /></Card>` will appear as `Card` component’s `children` prop.
  * Props are read-only snapshots in time: every render receives a new version of props.
  * You can’t change props. When you need interactivity, you’ll need to set state.


## Try out some challenges[](https://react.dev/learn/passing-props-to-a-component#challenges "Link for Try out some challenges")
1. Extract a component 2. Adjust the image size based on a prop 3. Passing JSX in a `children` prop 
#### 
Challenge 1 of 3: 
Extract a component [](https://react.dev/learn/passing-props-to-a-component#extract-a-component "Link for this heading")
This `Gallery` component contains some very similar markup for two profiles. Extract a `Profile` component out of it to reduce the duplication. You’ll need to choose what props to pass to it.
App.jsutils.js
App.js
ResetFork
```
import { getImageUrl } from './utils.js';
export default function Gallery() {
 return (
  <div>
   <h1>Notable Scientists</h1>
   <section className="profile">
    <h2>Maria Skłodowska-Curie</h2>
    <img
     className="avatar"
     src={getImageUrl('szV5sdG')}
     alt="Maria Skłodowska-Curie"
     width={70}
     height={70}
    />
    <ul>
     <li>
      <b>Profession: </b> 
      physicist and chemist
     </li>
     <li>
      <b>Awards: 4 </b> 
      (Nobel Prize in Physics, Nobel Prize in Chemistry, Davy Medal, Matteucci Medal)
     </li>
     <li>
      <b>Discovered: </b>
      polonium (chemical element)
     </li>
    </ul>
   </section>
   <section className="profile">
    <h2>Katsuko Saruhashi</h2>
    <img
     className="avatar"
     src={getImageUrl('YfeOqp2')}
     alt="Katsuko Saruhashi"
     width={70}
     height={70}
    />
    <ul>
     <li>
      <b>Profession: </b> 
      geochemist
     </li>
     <li>
      <b>Awards: 2 </b> 
      (Miyake Prize for geochemistry, Tanaka Prize)
     </li>
     <li>
      <b>Discovered: </b>
      a method for measuring carbon dioxide in seawater
     </li>
    </ul>
   </section>
  </div>
 );
}

```

Show more
Show hint Show solution
Next Challenge
[PreviousJavaScript in JSX with Curly Braces](https://react.dev/learn/javascript-in-jsx-with-curly-braces)[NextConditional Rendering](https://react.dev/learn/conditional-rendering)
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
  * [Overview](https://react.dev/learn/passing-props-to-a-component)
  * [Familiar props ](https://react.dev/learn/passing-props-to-a-component#familiar-props)
  * [Passing props to a component ](https://react.dev/learn/passing-props-to-a-component#passing-props-to-a-component)
  * [Step 1: Pass props to the child component ](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component)
  * [Step 2: Read props inside the child component ](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component)
  * [Specifying a default value for a prop ](https://react.dev/learn/passing-props-to-a-component#specifying-a-default-value-for-a-prop)
  * [Forwarding props with the JSX spread syntax ](https://react.dev/learn/passing-props-to-a-component#forwarding-props-with-the-jsx-spread-syntax)
  * [Passing JSX as children ](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children)
  * [How props change over time ](https://react.dev/learn/passing-props-to-a-component#how-props-change-over-time)
  * [Recap](https://react.dev/learn/passing-props-to-a-component#recap)
  * [Challenges](https://react.dev/learn/passing-props-to-a-component#challenges)



