---
url: https://react.dev/learn/scaling-up-with-reducer-and-context
scraped_at: 2025-05-25T08:34:19.318246
title: Scaling Up with Reducer and Context – React
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
# Scaling Up with Reducer and Context[](https://react.dev/learn/scaling-up-with-reducer-and-context#undefined "Link for this heading")
Reducers let you consolidate a component’s state update logic. Context lets you pass information deep down to other components. You can combine reducers and context together to manage state of a complex screen.
### You will learn
  * How to combine a reducer with context
  * How to avoid passing state and dispatch through props
  * How to keep context and state logic in a separate file


## Combining a reducer with context [](https://react.dev/learn/scaling-up-with-reducer-and-context#combining-a-reducer-with-context "Link for Combining a reducer with context ")
In this example from [the introduction to reducers](https://react.dev/learn/extracting-state-logic-into-a-reducer), the state is managed by a reducer. The reducer function contains all of the state update logic and is declared at the bottom of this file:
App.jsAddTask.jsTaskList.js
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
import { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
export default function TaskApp() {
const [tasks, dispatch] = useReducer(
tasksReducer,
initialTasks
);
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
task: task
});
}
function handleDeleteTask(taskId) {
dispatch({
type: 'deleted',
id: taskId
});
}
return (
<>
<h1>Day off in Kyoto</h1>
<AddTask
Show more
A reducer helps keep the event handlers short and concise. However, as your app grows, you might run into another difficulty. **Currently, the`tasks` state and the `dispatch` function are only available in the top-level `TaskApp` component.** To let other components read the list of tasks or change it, you have to explicitly [pass down](https://react.dev/learn/passing-props-to-a-component) the current state and the event handlers that change it as props.
For example, `TaskApp` passes a list of tasks and the event handlers to `TaskList`:
```

<TaskList
 tasks={tasks}
 onChangeTask={handleChangeTask}
 onDeleteTask={handleDeleteTask}
/>

```

And `TaskList` passes the event handlers to `Task`:
```

<Task
 task={task}
 onChange={onChangeTask}
 onDelete={onDeleteTask}
/>

```

In a small example like this, this works well, but if you have tens or hundreds of components in the middle, passing down all state and functions can be quite frustrating!
This is why, as an alternative to passing them through props, you might want to put both the `tasks` state and the `dispatch` function [into context.](https://react.dev/learn/passing-data-deeply-with-context) **This way, any component below`TaskApp` in the tree can read the tasks and dispatch actions without the repetitive “prop drilling”.**
Here is how you can combine a reducer with context:
  1. **Create** the context.
  2. **Put** state and dispatch into context.
  3. **Use** context anywhere in the tree.


### Step 1: Create the context [](https://react.dev/learn/scaling-up-with-reducer-and-context#step-1-create-the-context "Link for Step 1: Create the context ")
The `useReducer` Hook returns the current `tasks` and the `dispatch` function that lets you update them:
```

const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);

```

To pass them down the tree, you will [create](https://react.dev/learn/passing-data-deeply-with-context#step-2-use-the-context) two separate contexts:
  * `TasksContext` provides the current list of tasks.
  * `TasksDispatchContext` provides the function that lets components dispatch actions.


Export them from a separate file so that you can later import them from other files:
App.jsTasksContext.jsAddTask.jsTaskList.js
TasksContext.js
ResetFork
```
import { createContext } from 'react';
export const TasksContext = createContext(null);
export const TasksDispatchContext = createContext(null);

```

Here, you’re passing `null` as the default value to both contexts. The actual values will be provided by the `TaskApp` component.
### Step 2: Put state and dispatch into context [](https://react.dev/learn/scaling-up-with-reducer-and-context#step-2-put-state-and-dispatch-into-context "Link for Step 2: Put state and dispatch into context ")
Now you can import both contexts in your `TaskApp` component. Take the `tasks` and `dispatch` returned by `useReducer()` and [provide them](https://react.dev/learn/passing-data-deeply-with-context#step-3-provide-the-context) to the entire tree below:
```

import { TasksContext, TasksDispatchContext } from './TasksContext.js';
export default function TaskApp() {
 const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
 // ...
 return (
  <TasksContext.Provider value={tasks}>
   <TasksDispatchContext.Provider value={dispatch}>
    ...
   </TasksDispatchContext.Provider>
  </TasksContext.Provider>
 );
}

```

For now, you pass the information both via props and in context:
App.jsTasksContext.jsAddTask.jsTaskList.js
App.js
ResetFork
```
import { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
import { TasksContext, TasksDispatchContext } from './TasksContext.js';
export default function TaskApp() {
 const [tasks, dispatch] = useReducer(
  tasksReducer,
  initialTasks
 );
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
   task: task
  });
 }
 function handleDeleteTask(taskId) {
  dispatch({
   type: 'deleted',
   id: taskId
  });
 }
 return (
  <TasksContext.Provider value={tasks}>
   <TasksDispatchContext.Provider value={dispatch}>
    <h1>Day off in Kyoto</h1>
    <AddTask
     onAddTask={handleAddTask}
    />
    <TaskList
     tasks={tasks}
     onChangeTask={handleChangeTask}
     onDeleteTask={handleDeleteTask}
    />
   </TasksDispatchContext.Provider>
  </TasksContext.Provider>
 );
}
function tasksReducer(tasks, action) {
 switch (action.type) {
  case 'added': {
   return [...tasks, {
    id: action.id,
    text: action.text,
    done: false
   }];
  }
  case 'changed': {
   return tasks.map(t => {
    if (t.id === action.task.id) {
     return action.task;
    } else {
     return t;
    }
   });
  }
  case 'deleted': {
   return tasks.filter(t => t.id !== action.id);
  }
  default: {
   throw Error('Unknown action: ' + action.type);
  }
 }
}
let nextId = 3;
const initialTasks = [
 { id: 0, text: 'Philosopher’s Path', done: true },
 { id: 1, text: 'Visit the temple', done: false },
 { id: 2, text: 'Drink matcha', done: false }
];

```

Show more
In the next step, you will remove prop passing.
### Step 3: Use context anywhere in the tree [](https://react.dev/learn/scaling-up-with-reducer-and-context#step-3-use-context-anywhere-in-the-tree "Link for Step 3: Use context anywhere in the tree ")
Now you don’t need to pass the list of tasks or the event handlers down the tree:
```

<TasksContext.Provider value={tasks}>
 <TasksDispatchContext.Provider value={dispatch}>
  <h1>Day off in Kyoto</h1>
  <AddTask />
  <TaskList />
 </TasksDispatchContext.Provider>
</TasksContext.Provider>

```

Instead, any component that needs the task list can read it from the `TaskContext`:
```

export default function TaskList() {
 const tasks = useContext(TasksContext);
 // ...

```

To update the task list, any component can read the `dispatch` function from context and call it:
```

export default function AddTask() {
 const [text, setText] = useState('');
 const dispatch = useContext(TasksDispatchContext);
 // ...
 return (
  // ...
  <button onClick={() => {
   setText('');
   dispatch({
    type: 'added',
    id: nextId++,
    text: text,
   });
  }}>Add</button>
  // ...

```

**The`TaskApp` component does not pass any event handlers down, and the `TaskList` does not pass any event handlers to the `Task` component either.** Each component reads the context that it needs:
App.jsTasksContext.jsAddTask.jsTaskList.js
TaskList.js
ResetFork
```
import { useState, useContext } from 'react';
import { TasksContext, TasksDispatchContext } from './TasksContext.js';
export default function TaskList() {
 const tasks = useContext(TasksContext);
 return (
  <ul>
   {tasks.map(task => (
    <li key={task.id}>
     <Task task={task} />
    </li>
   ))}
  </ul>
 );
}
function Task({ task }) {
 const [isEditing, setIsEditing] = useState(false);
 const dispatch = useContext(TasksDispatchContext);
 let taskContent;
 if (isEditing) {
  taskContent = (
   <>
    <input
     value={task.text}
     onChange={e => {
      dispatch({
       type: 'changed',
       task: {
        ...task,
        text: e.target.value
       }
      });
     }} />
    <button onClick={() => setIsEditing(false)}>
     Save
    </button>
   </>
  );
 } else {
  taskContent = (
   <>
    {task.text}
    <button onClick={() => setIsEditing(true)}>
     Edit
    </button>
   </>
  );
 }
 return (
  <label>
   <input
    type="checkbox"
    checked={task.done}
    onChange={e => {
     dispatch({
      type: 'changed',
      task: {
       ...task,
       done: e.target.checked
      }
     });
    }}
   />
   {taskContent}
   <button onClick={() => {
    dispatch({
     type: 'deleted',
     id: task.id
    });
   }}>
    Delete
   </button>
  </label>
 );
}

```

Show more
**The state still “lives” in the top-level`TaskApp` component, managed with `useReducer`.** But its `tasks` and `dispatch` are now available to every component below in the tree by importing and using these contexts.
## Moving all wiring into a single file [](https://react.dev/learn/scaling-up-with-reducer-and-context#moving-all-wiring-into-a-single-file "Link for Moving all wiring into a single file ")
You don’t have to do this, but you could further declutter the components by moving both reducer and context into a single file. Currently, `TasksContext.js` contains only two context declarations:
```

import { createContext } from 'react';
export const TasksContext = createContext(null);
export const TasksDispatchContext = createContext(null);

```

This file is about to get crowded! You’ll move the reducer into that same file. Then you’ll declare a new `TasksProvider` component in the same file. This component will tie all the pieces together:
  1. It will manage the state with a reducer.
  2. It will provide both contexts to components below.
  3. It will [take `children` as a prop](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children) so you can pass JSX to it.


```

export function TasksProvider({ children }) {
 const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
 return (
  <TasksContext.Provider value={tasks}>
   <TasksDispatchContext.Provider value={dispatch}>
    {children}
   </TasksDispatchContext.Provider>
  </TasksContext.Provider>
 );
}

```

**This removes all the complexity and wiring from your`TaskApp` component:**
App.jsTasksContext.jsAddTask.jsTaskList.js
App.js
ResetFork
```
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
import { TasksProvider } from './TasksContext.js';
export default function TaskApp() {
 return (
  <TasksProvider>
   <h1>Day off in Kyoto</h1>
   <AddTask />
   <TaskList />
  </TasksProvider>
 );
}

```

You can also export functions that _use_ the context from `TasksContext.js`:
```

export function useTasks() {
 return useContext(TasksContext);
}
export function useTasksDispatch() {
 return useContext(TasksDispatchContext);
}

```

When a component needs to read context, it can do it through these functions:
```

const tasks = useTasks();
const dispatch = useTasksDispatch();

```

This doesn’t change the behavior in any way, but it lets you later split these contexts further or add some logic to these functions. **Now all of the context and reducer wiring is in`TasksContext.js`. This keeps the components clean and uncluttered, focused on what they display rather than where they get the data:**
App.jsTasksContext.jsAddTask.jsTaskList.js
TaskList.js
ResetFork
```
import { useState } from 'react';
import { useTasks, useTasksDispatch } from './TasksContext.js';
export default function TaskList() {
 const tasks = useTasks();
 return (
  <ul>
   {tasks.map(task => (
    <li key={task.id}>
     <Task task={task} />
    </li>
   ))}
  </ul>
 );
}
function Task({ task }) {
 const [isEditing, setIsEditing] = useState(false);
 const dispatch = useTasksDispatch();
 let taskContent;
 if (isEditing) {
  taskContent = (
   <>
    <input
     value={task.text}
     onChange={e => {
      dispatch({
       type: 'changed',
       task: {
        ...task,
        text: e.target.value
       }
      });
     }} />
    <button onClick={() => setIsEditing(false)}>
     Save
    </button>
   </>
  );
 } else {
  taskContent = (
   <>
    {task.text}
    <button onClick={() => setIsEditing(true)}>
     Edit
    </button>
   </>
  );
 }
 return (
  <label>
   <input
    type="checkbox"
    checked={task.done}
    onChange={e => {
     dispatch({
      type: 'changed',
      task: {
       ...task,
       done: e.target.checked
      }
     });
    }}
   />
   {taskContent}
   <button onClick={() => {
    dispatch({
     type: 'deleted',
     id: task.id
    });
   }}>
    Delete
   </button>
  </label>
 );
}

```

Show more
You can think of `TasksProvider` as a part of the screen that knows how to deal with tasks, `useTasks` as a way to read them, and `useTasksDispatch` as a way to update them from any component below in the tree.
### Note
Functions like `useTasks` and `useTasksDispatch` are called _[Custom Hooks.](https://react.dev/learn/reusing-logic-with-custom-hooks)_ Your function is considered a custom Hook if its name starts with `use`. This lets you use other Hooks, like `useContext`, inside it.
As your app grows, you may have many context-reducer pairs like this. This is a powerful way to scale your app and [lift state up](https://react.dev/learn/sharing-state-between-components) without too much work whenever you want to access the data deep in the tree.
## Recap[](https://react.dev/learn/scaling-up-with-reducer-and-context#recap "Link for Recap")
  * You can combine reducer with context to let any component read and update state above it.
  * To provide state and the dispatch function to components below: 
    1. Create two contexts (for state and for dispatch functions).
    2. Provide both contexts from the component that uses the reducer.
    3. Use either context from components that need to read them.
  * You can further declutter the components by moving all wiring into one file. 
    * You can export a component like `TasksProvider` that provides context.
    * You can also export custom Hooks like `useTasks` and `useTasksDispatch` to read it.
  * You can have many context-reducer pairs like this in your app.


[PreviousPassing Data Deeply with Context](https://react.dev/learn/passing-data-deeply-with-context)[NextEscape Hatches](https://react.dev/learn/escape-hatches)
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
  * [Overview](https://react.dev/learn/scaling-up-with-reducer-and-context)
  * [Combining a reducer with context ](https://react.dev/learn/scaling-up-with-reducer-and-context#combining-a-reducer-with-context)
  * [Step 1: Create the context ](https://react.dev/learn/scaling-up-with-reducer-and-context#step-1-create-the-context)
  * [Step 2: Put state and dispatch into context ](https://react.dev/learn/scaling-up-with-reducer-and-context#step-2-put-state-and-dispatch-into-context)
  * [Step 3: Use context anywhere in the tree ](https://react.dev/learn/scaling-up-with-reducer-and-context#step-3-use-context-anywhere-in-the-tree)
  * [Moving all wiring into a single file ](https://react.dev/learn/scaling-up-with-reducer-and-context#moving-all-wiring-into-a-single-file)
  * [Recap](https://react.dev/learn/scaling-up-with-reducer-and-context#recap)



