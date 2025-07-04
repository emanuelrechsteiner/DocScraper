---
url: https://react.dev/learn/extracting-state-logic-into-a-reducer
scraped_at: 2025-05-25T08:31:33.383833
title: Extracting State Logic into a Reducer – React
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
# Extracting State Logic into a Reducer[](https://react.dev/learn/extracting-state-logic-into-a-reducer#undefined "Link for this heading")
Components with many state updates spread across many event handlers can get overwhelming. For these cases, you can consolidate all the state update logic outside your component in a single function, called a _reducer._
### You will learn
  * What a reducer function is
  * How to refactor `useState` to `useReducer`
  * When to use a reducer
  * How to write one well


## Consolidate state logic with a reducer [](https://react.dev/learn/extracting-state-logic-into-a-reducer#consolidate-state-logic-with-a-reducer "Link for Consolidate state logic with a reducer ")
As your components grow in complexity, it can get harder to see at a glance all the different ways in which a component’s state gets updated. For example, the `TaskApp` component below holds an array of `tasks` in state and uses three different event handlers to add, remove, and edit tasks:
App.js
App.js
ResetFork
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
33
34
35
36
import { useState } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
export default function TaskApp() {
const [tasks, setTasks] = useState(initialTasks);
function handleAddTask(text) {
setTasks([
...tasks,
{
id: nextId++,
text: text,
done: false,
},
]);
}
function handleChangeTask(task) {
setTasks(
tasks.map((t) => {
if (t.id === task.id) {
return task;
} else {
return t;
}
})
);
}
function handleDeleteTask(taskId) {
setTasks(tasks.filter((t) => t.id !== taskId));
}
return (
<>
Show more
Each of its event handlers calls `setTasks` in order to update the state. As this component grows, so does the amount of state logic sprinkled throughout it. To reduce this complexity and keep all your logic in one easy-to-access place, you can move that state logic into a single function outside your component, **called a “reducer”.**
Reducers are a different way to handle state. You can migrate from `useState` to `useReducer` in three steps:
  1. **Move** from setting state to dispatching actions.
  2. **Write** a reducer function.
  3. **Use** the reducer from your component.


### Step 1: Move from setting state to dispatching actions [](https://react.dev/learn/extracting-state-logic-into-a-reducer#step-1-move-from-setting-state-to-dispatching-actions "Link for Step 1: Move from setting state to dispatching actions ")
Your event handlers currently specify _what to do_ by setting state:
```

function handleAddTask(text) {
 setTasks([
  ...tasks,
  {
   id: nextId++,
   text: text,
   done: false,
  },
 ]);
}
function handleChangeTask(task) {
 setTasks(
  tasks.map((t) => {
   if (t.id === task.id) {
    return task;
   } else {
    return t;
   }
  })
 );
}
function handleDeleteTask(taskId) {
 setTasks(tasks.filter((t) => t.id !== taskId));
}

```

Remove all the state setting logic. What you are left with are three event handlers:
  * `handleAddTask(text)` is called when the user presses “Add”.
  * `handleChangeTask(task)` is called when the user toggles a task or presses “Save”.
  * `handleDeleteTask(taskId)` is called when the user presses “Delete”.


Managing state with reducers is slightly different from directly setting state. Instead of telling React “what to do” by setting state, you specify “what the user just did” by dispatching “actions” from your event handlers. (The state update logic will live elsewhere!) So instead of “setting `tasks`” via an event handler, you’re dispatching an “added/changed/deleted a task” action. This is more descriptive of the user’s intent.
```

function handleAddTask(text) {
 dispatch({
  type: 'added',
  id: nextId++,
  text: text,
 });
}
function handleChangeTask(task) {
 dispatch({
  type: 'changed',
  task: task,
 });
}
function handleDeleteTask(taskId) {
 dispatch({
  type: 'deleted',
  id: taskId,
 });
}

```

The object you pass to `dispatch` is called an “action”:
```

function handleDeleteTask(taskId) {
 dispatch(
  // "action" object:
  {
   type: 'deleted',
   id: taskId,
  }
 );
}

```

It is a regular JavaScript object. You decide what to put in it, but generally it should contain the minimal information about _what happened_. (You will add the `dispatch` function itself in a later step.)
### Note
An action object can have any shape.
By convention, it is common to give it a string `type` that describes what happened, and pass any additional information in other fields. The `type` is specific to a component, so in this example either `'added'` or `'added_task'` would be fine. Choose a name that says what happened!
```

dispatch({
 // specific to component
 type: 'what_happened',
 // other fields go here
});

```

### Step 2: Write a reducer function [](https://react.dev/learn/extracting-state-logic-into-a-reducer#step-2-write-a-reducer-function "Link for Step 2: Write a reducer function ")
A reducer function is where you will put your state logic. It takes two arguments, the current state and the action object, and it returns the next state:
```

function yourReducer(state, action) {
 // return next state for React to set
}

```

React will set the state to what you return from the reducer.
To move your state setting logic from your event handlers to a reducer function in this example, you will:
  1. Declare the current state (`tasks`) as the first argument.
  2. Declare the `action` object as the second argument.
  3. Return the _next_ state from the reducer (which React will set the state to).


Here is all the state setting logic migrated to a reducer function:
```

function tasksReducer(tasks, action) {
 if (action.type === 'added') {
  return [
   ...tasks,
   {
    id: action.id,
    text: action.text,
    done: false,
   },
  ];
 } else if (action.type === 'changed') {
  return tasks.map((t) => {
   if (t.id === action.task.id) {
    return action.task;
   } else {
    return t;
   }
  });
 } else if (action.type === 'deleted') {
  return tasks.filter((t) => t.id !== action.id);
 } else {
  throw Error('Unknown action: ' + action.type);
 }
}

```

Because the reducer function takes state (`tasks`) as an argument, you can **declare it outside of your component.** This decreases the indentation level and can make your code easier to read.
### Note
The code above uses if/else statements, but it’s a convention to use [switch statements](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/switch) inside reducers. The result is the same, but it can be easier to read switch statements at a glance.
We’ll be using them throughout the rest of this documentation like so:
```

function tasksReducer(tasks, action) {
 switch (action.type) {
  case 'added': {
   return [
    ...tasks,
    {
     id: action.id,
     text: action.text,
     done: false,
    },
   ];
  }
  case 'changed': {
   return tasks.map((t) => {
    if (t.id === action.task.id) {
     return action.task;
    } else {
     return t;
    }
   });
  }
  case 'deleted': {
   return tasks.filter((t) => t.id !== action.id);
  }
  default: {
   throw Error('Unknown action: ' + action.type);
  }
 }
}

```

We recommend wrapping each `case` block into the `{` and `}` curly braces so that variables declared inside of different `case`s don’t clash with each other. Also, a `case` should usually end with a `return`. If you forget to `return`, the code will “fall through” to the next `case`, which can lead to mistakes!
If you’re not yet comfortable with switch statements, using if/else is completely fine.
##### Deep Dive
#### Why are reducers called this way? [](https://react.dev/learn/extracting-state-logic-into-a-reducer#why-are-reducers-called-this-way "Link for Why are reducers called this way? ")
Show Details
Although reducers can “reduce” the amount of code inside your component, they are actually named after the [`reduce()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) operation that you can perform on arrays.
The `reduce()` operation lets you take an array and “accumulate” a single value out of many:
```

const arr = [1, 2, 3, 4, 5];
const sum = arr.reduce(
 (result, number) => result + number
); // 1 + 2 + 3 + 4 + 5

```

The function you pass to `reduce` is known as a “reducer”. It takes the _result so far_ and the _current item,_ then it returns the _next result._ React reducers are an example of the same idea: they take the _state so far_ and the _action_ , and return the _next state._ In this way, they accumulate actions over time into state.
You could even use the `reduce()` method with an `initialState` and an array of `actions` to calculate the final state by passing your reducer function to it:
index.jsindex.htmltasksReducer.js
index.js
ResetFork
```
import tasksReducer from './tasksReducer.js';
let initialState = [];
let actions = [
 {type: 'added', id: 1, text: 'Visit Kafka Museum'},
 {type: 'added', id: 2, text: 'Watch a puppet show'},
 {type: 'deleted', id: 1},
 {type: 'added', id: 3, text: 'Lennon Wall pic'},
];
let finalState = actions.reduce(tasksReducer, initialState);
const output = document.getElementById('output');
output.textContent = JSON.stringify(finalState, null, 2);

```

You probably won’t need to do this yourself, but this is similar to what React does!
### Step 3: Use the reducer from your component [](https://react.dev/learn/extracting-state-logic-into-a-reducer#step-3-use-the-reducer-from-your-component "Link for Step 3: Use the reducer from your component ")
Finally, you need to hook up the `tasksReducer` to your component. Import the `useReducer` Hook from React:
```

import { useReducer } from 'react';

```

Then you can replace `useState`:
```

const [tasks, setTasks] = useState(initialTasks);

```

with `useReducer` like so:
```

const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);

```

The `useReducer` Hook is similar to `useState`—you must pass it an initial state and it returns a stateful value and a way to set state (in this case, the dispatch function). But it’s a little different.
The `useReducer` Hook takes two arguments:
  1. A reducer function
  2. An initial state


And it returns:
  1. A stateful value
  2. A dispatch function (to “dispatch” user actions to the reducer)


Now it’s fully wired up! Here, the reducer is declared at the bottom of the component file:
App.js
App.js
ResetFork
```
import { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
export default function TaskApp() {
 const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
 function handleAddTask(text) {
  dispatch({
   type: 'added',
   id: nextId++,
   text: text,
  });
 }
 function handleChangeTask(task) {
  dispatch({
   type: 'changed',
   task: task,
  });
 }
 function handleDeleteTask(taskId) {
  dispatch({
   type: 'deleted',
   id: taskId,
  });
 }
 return (
  <>
   <h1>Prague itinerary</h1>
   <AddTask onAddTask={handleAddTask} />
   <TaskList
    tasks={tasks}
    onChangeTask={handleChangeTask}
    onDeleteTask={handleDeleteTask}
   />
  </>
 );
}
function tasksReducer(tasks, action) {
 switch (action.type) {
  case 'added': {
   return [
    ...tasks,
    {
     id: action.id,
     text: action.text,
     done: false,
    },
   ];
  }
  case 'changed': {
   return tasks.map((t) => {
    if (t.id === action.task.id) {
     return action.task;
    } else {
     return t;
    }
   });
  }
  case 'deleted': {
   return tasks.filter((t) => t.id !== action.id);
  }
  default: {
   throw Error('Unknown action: ' + action.type);
  }
 }
}
let nextId = 3;
const initialTasks = [
 {id: 0, text: 'Visit Kafka Museum', done: true},
 {id: 1, text: 'Watch a puppet show', done: false},
 {id: 2, text: 'Lennon Wall pic', done: false},
];

```

Show more
If you want, you can even move the reducer to a different file:
App.jstasksReducer.js
App.js
ResetFork
```
import { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
import tasksReducer from './tasksReducer.js';
export default function TaskApp() {
 const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
 function handleAddTask(text) {
  dispatch({
   type: 'added',
   id: nextId++,
   text: text,
  });
 }
 function handleChangeTask(task) {
  dispatch({
   type: 'changed',
   task: task,
  });
 }
 function handleDeleteTask(taskId) {
  dispatch({
   type: 'deleted',
   id: taskId,
  });
 }
 return (
  <>
   <h1>Prague itinerary</h1>
   <AddTask onAddTask={handleAddTask} />
   <TaskList
    tasks={tasks}
    onChangeTask={handleChangeTask}
    onDeleteTask={handleDeleteTask}
   />
  </>
 );
}
let nextId = 3;
const initialTasks = [
 {id: 0, text: 'Visit Kafka Museum', done: true},
 {id: 1, text: 'Watch a puppet show', done: false},
 {id: 2, text: 'Lennon Wall pic', done: false},
];

```

Show more
Component logic can be easier to read when you separate concerns like this. Now the event handlers only specify _what happened_ by dispatching actions, and the reducer function determines _how the state updates_ in response to them.
## Comparing `useState` and `useReducer` [](https://react.dev/learn/extracting-state-logic-into-a-reducer#comparing-usestate-and-usereducer "Link for this heading")
Reducers are not without downsides! Here’s a few ways you can compare them:
  * **Code size:** Generally, with `useState` you have to write less code upfront. With `useReducer`, you have to write both a reducer function _and_ dispatch actions. However, `useReducer` can help cut down on the code if many event handlers modify state in a similar way.
  * **Readability:** `useState` is very easy to read when the state updates are simple. When they get more complex, they can bloat your component’s code and make it difficult to scan. In this case, `useReducer` lets you cleanly separate the _how_ of update logic from the _what happened_ of event handlers.
  * **Debugging:** When you have a bug with `useState`, it can be difficult to tell _where_ the state was set incorrectly, and _why_. With `useReducer`, you can add a console log into your reducer to see every state update, and _why_ it happened (due to which `action`). If each `action` is correct, you’ll know that the mistake is in the reducer logic itself. However, you have to step through more code than with `useState`.
  * **Testing:** A reducer is a pure function that doesn’t depend on your component. This means that you can export and test it separately in isolation. While generally it’s best to test components in a more realistic environment, for complex state update logic it can be useful to assert that your reducer returns a particular state for a particular initial state and action.
  * **Personal preference:** Some people like reducers, others don’t. That’s okay. It’s a matter of preference. You can always convert between `useState` and `useReducer` back and forth: they are equivalent!


We recommend using a reducer if you often encounter bugs due to incorrect state updates in some component, and want to introduce more structure to its code. You don’t have to use reducers for everything: feel free to mix and match! You can even `useState` and `useReducer` in the same component.
## Writing reducers well [](https://react.dev/learn/extracting-state-logic-into-a-reducer#writing-reducers-well "Link for Writing reducers well ")
Keep these two tips in mind when writing reducers:
  * **Reducers must be pure.** Similar to [state updater functions](https://react.dev/learn/queueing-a-series-of-state-updates), reducers run during rendering! (Actions are queued until the next render.) This means that reducers [must be pure](https://react.dev/learn/keeping-components-pure)—same inputs always result in the same output. They should not send requests, schedule timeouts, or perform any side effects (operations that impact things outside the component). They should update [objects](https://react.dev/learn/updating-objects-in-state) and [arrays](https://react.dev/learn/updating-arrays-in-state) without mutations.
  * **Each action describes a single user interaction, even if that leads to multiple changes in the data.** For example, if a user presses “Reset” on a form with five fields managed by a reducer, it makes more sense to dispatch one `reset_form` action rather than five separate `set_field` actions. If you log every action in a reducer, that log should be clear enough for you to reconstruct what interactions or responses happened in what order. This helps with debugging!


## Writing concise reducers with Immer [](https://react.dev/learn/extracting-state-logic-into-a-reducer#writing-concise-reducers-with-immer "Link for Writing concise reducers with Immer ")
Just like with [updating objects](https://react.dev/learn/updating-objects-in-state#write-concise-update-logic-with-immer) and [arrays](https://react.dev/learn/updating-arrays-in-state#write-concise-update-logic-with-immer) in regular state, you can use the Immer library to make reducers more concise. Here, [`useImmerReducer`](https://github.com/immerjs/use-immer#useimmerreducer) lets you mutate the state with `push` or `arr[i] =` assignment:
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

Reducers must be pure, so they shouldn’t mutate state. But Immer provides you with a special `draft` object which is safe to mutate. Under the hood, Immer will create a copy of your state with the changes you made to the `draft`. This is why reducers managed by `useImmerReducer` can mutate their first argument and don’t need to return state.
## Recap[](https://react.dev/learn/extracting-state-logic-into-a-reducer#recap "Link for Recap")
  * To convert from `useState` to `useReducer`: 
    1. Dispatch actions from event handlers.
    2. Write a reducer function that returns the next state for a given state and action.
    3. Replace `useState` with `useReducer`.
  * Reducers require you to write a bit more code, but they help with debugging and testing.
  * Reducers must be pure.
  * Each action describes a single user interaction.
  * Use Immer if you want to write reducers in a mutating style.


## Try out some challenges[](https://react.dev/learn/extracting-state-logic-into-a-reducer#challenges "Link for Try out some challenges")
1. Dispatch actions from event handlers 2. Clear the input on sending a message 3. Restore input values when switching between tabs 4. Implement `useReducer` from scratch 
#### 
Challenge 1 of 4: 
Dispatch actions from event handlers [](https://react.dev/learn/extracting-state-logic-into-a-reducer#dispatch-actions-from-event-handlers "Link for this heading")
Currently, the event handlers in `ContactList.js` and `Chat.js` have `// TODO` comments. This is why typing into the input doesn’t work, and clicking on the buttons doesn’t change the selected recipient.
Replace these two `// TODO`s with the code to `dispatch` the corresponding actions. To see the expected shape and the type of the actions, check the reducer in `messengerReducer.js`. The reducer is already written so you won’t need to change it. You only need to dispatch the actions in `ContactList.js` and `Chat.js`.
App.jsmessengerReducer.jsContactList.jsChat.js
App.js
ResetFork
```
import { useReducer } from 'react';
import Chat from './Chat.js';
import ContactList from './ContactList.js';
import { initialState, messengerReducer } from './messengerReducer';
export default function Messenger() {
 const [state, dispatch] = useReducer(messengerReducer, initialState);
 const message = state.message;
 const contact = contacts.find((c) => c.id === state.selectedId);
 return (
  <div>
   <ContactList
    contacts={contacts}
    selectedId={state.selectedId}
    dispatch={dispatch}
   />
   <Chat
    key={contact.id}
    message={message}
    contact={contact}
    dispatch={dispatch}
   />
  </div>
 );
}
const contacts = [
 {id: 0, name: 'Taylor', email: 'taylor@mail.com'},
 {id: 1, name: 'Alice', email: 'alice@mail.com'},
 {id: 2, name: 'Bob', email: 'bob@mail.com'},
];

```

Show more
Show hint Show solution
Next Challenge
[PreviousPreserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state)[NextPassing Data Deeply with Context](https://react.dev/learn/passing-data-deeply-with-context)
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
  * [Overview](https://react.dev/learn/extracting-state-logic-into-a-reducer)
  * [Consolidate state logic with a reducer ](https://react.dev/learn/extracting-state-logic-into-a-reducer#consolidate-state-logic-with-a-reducer)
  * [Step 1: Move from setting state to dispatching actions ](https://react.dev/learn/extracting-state-logic-into-a-reducer#step-1-move-from-setting-state-to-dispatching-actions)
  * [Step 2: Write a reducer function ](https://react.dev/learn/extracting-state-logic-into-a-reducer#step-2-write-a-reducer-function)
  * [Step 3: Use the reducer from your component ](https://react.dev/learn/extracting-state-logic-into-a-reducer#step-3-use-the-reducer-from-your-component)
  * [Comparing `useState` and `useReducer` ](https://react.dev/learn/extracting-state-logic-into-a-reducer#comparing-usestate-and-usereducer)
  * [Writing reducers well ](https://react.dev/learn/extracting-state-logic-into-a-reducer#writing-reducers-well)
  * [Writing concise reducers with Immer ](https://react.dev/learn/extracting-state-logic-into-a-reducer#writing-concise-reducers-with-immer)
  * [Recap](https://react.dev/learn/extracting-state-logic-into-a-reducer#recap)
  * [Challenges](https://react.dev/learn/extracting-state-logic-into-a-reducer#challenges)



