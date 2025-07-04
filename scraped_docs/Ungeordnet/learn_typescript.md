---
url: https://react.dev/learn/typescript
scraped_at: 2025-05-25T08:40:44.403644
title: Using TypeScript – React
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
[Setup](https://react.dev/learn/setup)
# Using TypeScript[](https://react.dev/learn/typescript#undefined "Link for this heading")
TypeScript is a popular way to add type definitions to JavaScript codebases. Out of the box, TypeScript [supports JSX](https://react.dev/learn/writing-markup-with-jsx) and you can get full React Web support by adding [`@types/react`](https://www.npmjs.com/package/@types/react) and [`@types/react-dom`](https://www.npmjs.com/package/@types/react-dom) to your project.
### You will learn
  * [TypeScript with React Components](https://react.dev/learn/typescript#typescript-with-react-components)
  * [Examples of typing with Hooks](https://react.dev/learn/typescript#example-hooks)
  * [Common types from `@types/react`](https://react.dev/learn/typescript#useful-types)
  * [Further learning locations](https://react.dev/learn/typescript#further-learning)


## Installation [](https://react.dev/learn/typescript#installation "Link for Installation ")
All [production-grade React frameworks](https://react.dev/learn/start-a-new-react-project#production-grade-react-frameworks) offer support for using TypeScript. Follow the framework specific guide for installation:
  * [Next.js](https://nextjs.org/docs/app/building-your-application/configuring/typescript)
  * [Remix](https://remix.run/docs/en/1.19.2/guides/typescript)
  * [Gatsby](https://www.gatsbyjs.com/docs/how-to/custom-configuration/typescript/)
  * [Expo](https://docs.expo.dev/guides/typescript/)


### Adding TypeScript to an existing React project [](https://react.dev/learn/typescript#adding-typescript-to-an-existing-react-project "Link for Adding TypeScript to an existing React project ")
To install the latest version of React’s type definitions:
Terminal
Copy
npm install @types/react @types/react-dom
The following compiler options need to be set in your `tsconfig.json`:
  1. `dom` must be included in [`lib`](https://www.typescriptlang.org/tsconfig/#lib) (Note: If no `lib` option is specified, `dom` is included by default).
  2. [`jsx`](https://www.typescriptlang.org/tsconfig/#jsx) must be set to one of the valid options. `preserve` should suffice for most applications. If you’re publishing a library, consult the [`jsx` documentation](https://www.typescriptlang.org/tsconfig/#jsx) on what value to choose.


## TypeScript with React Components [](https://react.dev/learn/typescript#typescript-with-react-components "Link for TypeScript with React Components ")
### Note
Every file containing JSX must use the `.tsx` file extension. This is a TypeScript-specific extension that tells TypeScript that this file contains JSX.
Writing TypeScript with React is very similar to writing JavaScript with React. The key difference when working with a component is that you can provide types for your component’s props. These types can be used for correctness checking and providing inline documentation in editors.
Taking the [`MyButton` component](https://react.dev/learn#components) from the [Quick Start](https://react.dev/learn) guide, we can add a type describing the `title` for the button:
App.tsx
App.tsx
ResetFork[TypeScript Playground](https://www.typescriptlang.org/play#src=import%20*%20as%20React%20from%20'react'%3B%0A%0Afunction%20MyButton\(%7B%20title%20%7D%3A%20%7B%20title%3A%20string%20%7D\)%20%7B%0A%20%20return%20\(%0A%20%20%20%20%3Cbutton%3E%7Btitle%7D%3C%2Fbutton%3E%0A%20%20\)%3B%0A%7D%0A%0Aexport%20default%20function%20MyApp\(\)%20%7B%0A%20%20return%20\(%0A%20%20%20%20%3Cdiv%3E%0A%20%20%20%20%20%20%3Ch1%3EWelcome%20to%20my%20app%3C%2Fh1%3E%0A%20%20%20%20%20%20%3CMyButton%20title%3D%22I'm%20a%20button%22%20%2F%3E%0A%20%20%20%20%3C%2Fdiv%3E%0A%20%20\)%3B%0A%7D%0A "Open in TypeScript Playground")
```
function MyButton({ title }: { title: string }) {
 return (
  <button>{title}</button>
 );
}
export default function MyApp() {
 return (
  <div>
   <h1>Welcome to my app</h1>
   <MyButton title="I'm a button" />
  </div>
 );
}

```

### Note
These sandboxes can handle TypeScript code, but they do not run the type-checker. This means you can amend the TypeScript sandboxes to learn, but you won’t get any type errors or warnings. To get type-checking, you can use the [TypeScript Playground](https://www.typescriptlang.org/play) or use a more fully-featured online sandbox.
This inline syntax is the simplest way to provide types for a component, though once you start to have a few fields to describe it can become unwieldy. Instead, you can use an `interface` or `type` to describe the component’s props:
App.tsx
App.tsx
ResetFork[TypeScript Playground](https://www.typescriptlang.org/play#src=import%20*%20as%20React%20from%20'react'%3B%0A%0Ainterface%20MyButtonProps%20%7B%0A%20%20%2F**%20The%20text%20to%20display%20inside%20the%20button%20*%2F%0A%20%20title%3A%20string%3B%0A%20%20%2F**%20Whether%20the%20button%20can%20be%20interacted%20with%20*%2F%0A%20%20disabled%3A%20boolean%3B%0A%7D%0A%0Afunction%20MyButton\(%7B%20title%2C%20disabled%20%7D%3A%20MyButtonProps\)%20%7B%0A%20%20return%20\(%0A%20%20%20%20%3Cbutton%20disabled%3D%7Bdisabled%7D%3E%7Btitle%7D%3C%2Fbutton%3E%0A%20%20\)%3B%0A%7D%0A%0Aexport%20default%20function%20MyApp\(\)%20%7B%0A%20%20return%20\(%0A%20%20%20%20%3Cdiv%3E%0A%20%20%20%20%20%20%3Ch1%3EWelcome%20to%20my%20app%3C%2Fh1%3E%0A%20%20%20%20%20%20%3CMyButton%20title%3D%22I'm%20a%20disabled%20button%22%20disabled%3D%7Btrue%7D%2F%3E%0A%20%20%20%20%3C%2Fdiv%3E%0A%20%20\)%3B%0A%7D%0A "Open in TypeScript Playground")
```
interface MyButtonProps {
 /** The text to display inside the button */
 title: string;
 /** Whether the button can be interacted with */
 disabled: boolean;
}
function MyButton({ title, disabled }: MyButtonProps) {
 return (
  <button disabled={disabled}>{title}</button>
 );
}
export default function MyApp() {
 return (
  <div>
   <h1>Welcome to my app</h1>
   <MyButton title="I'm a disabled button" disabled={true}/>
  </div>
 );
}

```

Show more
The type describing your component’s props can be as simple or as complex as you need, though they should be an object type described with either a `type` or `interface`. You can learn about how TypeScript describes objects in [Object Types](https://www.typescriptlang.org/docs/handbook/2/objects.html) but you may also be interested in using [Union Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types) to describe a prop that can be one of a few different types and the [Creating Types from Types](https://www.typescriptlang.org/docs/handbook/2/types-from-types.html) guide for more advanced use cases.
## Example Hooks [](https://react.dev/learn/typescript#example-hooks "Link for Example Hooks ")
The type definitions from `@types/react` include types for the built-in Hooks, so you can use them in your components without any additional setup. They are built to take into account the code you write in your component, so you will get [inferred types](https://www.typescriptlang.org/docs/handbook/type-inference.html) a lot of the time and ideally do not need to handle the minutiae of providing the types.
However, we can look at a few examples of how to provide types for Hooks.
### `useState` [](https://react.dev/learn/typescript#typing-usestate "Link for this heading")
The [`useState` Hook](https://react.dev/reference/react/useState) will re-use the value passed in as the initial state to determine what the type of the value should be. For example:
```

// Infer the type as "boolean"
const [enabled, setEnabled] = useState(false);

```

This will assign the type of `boolean` to `enabled`, and `setEnabled` will be a function accepting either a `boolean` argument, or a function that returns a `boolean`. If you want to explicitly provide a type for the state, you can do so by providing a type argument to the `useState` call:
```

// Explicitly set the type to "boolean"
const [enabled, setEnabled] = useState<boolean>(false);

```

This isn’t very useful in this case, but a common case where you may want to provide a type is when you have a union type. For example, `status` here can be one of a few different strings:
```

type Status = "idle" | "loading" | "success" | "error";
const [status, setStatus] = useState<Status>("idle");

```

Or, as recommended in [Principles for structuring state](https://react.dev/learn/choosing-the-state-structure#principles-for-structuring-state), you can group related state as an object and describe the different possibilities via object types:
```

type RequestState =
 | { status: 'idle' }
 | { status: 'loading' }
 | { status: 'success', data: any }
 | { status: 'error', error: Error };
const [requestState, setRequestState] = useState<RequestState>({ status: 'idle' });

```

### `useReducer` [](https://react.dev/learn/typescript#typing-usereducer "Link for this heading")
The [`useReducer` Hook](https://react.dev/reference/react/useReducer) is a more complex Hook that takes a reducer function and an initial state. The types for the reducer function are inferred from the initial state. You can optionally provide a type argument to the `useReducer` call to provide a type for the state, but it is often better to set the type on the initial state instead:
App.tsx
App.tsx
ResetFork[TypeScript Playground](https://www.typescriptlang.org/play#src=import%20*%20as%20React%20from%20'react'%3B%0A%0Aimport%20%7BuseReducer%7D%20from%20'react'%3B%0A%0Ainterface%20State%20%7B%0A%20%20%20count%3A%20number%20%0A%7D%3B%0A%0Atype%20CounterAction%20%3D%0A%20%20%7C%20%7B%20type%3A%20%22reset%22%20%7D%0A%20%20%7C%20%7B%20type%3A%20%22setCount%22%3B%20value%3A%20State%5B%22count%22%5D%20%7D%0A%0Aconst%20initialState%3A%20State%20%3D%20%7B%20count%3A%200%20%7D%3B%0A%0Afunction%20stateReducer\(state%3A%20State%2C%20action%3A%20CounterAction\)%3A%20State%20%7B%0A%20%20switch%20\(action.type\)%20%7B%0A%20%20%20%20case%20%22reset%22%3A%0A%20%20%20%20%20%20return%20initialState%3B%0A%20%20%20%20case%20%22setCount%22%3A%0A%20%20%20%20%20%20return%20%7B%20...state%2C%20count%3A%20action.value%20%7D%3B%0A%20%20%20%20default%3A%0A%20%20%20%20%20%20throw%20new%20Error\(%22Unknown%20action%22\)%3B%0A%20%20%7D%0A%7D%0A%0Aexport%20default%20function%20App\(\)%20%7B%0A%20%20const%20%5Bstate%2C%20dispatch%5D%20%3D%20useReducer\(stateReducer%2C%20initialState\)%3B%0A%0A%20%20const%20addFive%20%3D%20\(\)%20%3D%3E%20dispatch\(%7B%20type%3A%20%22setCount%22%2C%20value%3A%20state.count%20%2B%205%20%7D\)%3B%0A%20%20const%20reset%20%3D%20\(\)%20%3D%3E%20dispatch\(%7B%20type%3A%20%22reset%22%20%7D\)%3B%0A%0A%20%20return%20\(%0A%20%20%20%20%3Cdiv%3E%0A%20%20%20%20%20%20%3Ch1%3EWelcome%20to%20my%20counter%3C%2Fh1%3E%0A%0A%20%20%20%20%20%20%3Cp%3ECount%3A%20%7Bstate.count%7D%3C%2Fp%3E%0A%20%20%20%20%20%20%3Cbutton%20onClick%3D%7BaddFive%7D%3EAdd%205%3C%2Fbutton%3E%0A%20%20%20%20%20%20%3Cbutton%20onClick%3D%7Breset%7D%3EReset%3C%2Fbutton%3E%0A%20%20%20%20%3C%2Fdiv%3E%0A%20%20\)%3B%0A%7D%0A%0A "Open in TypeScript Playground")
```
import {useReducer} from 'react';
interface State {
  count: number 
};
type CounterAction =
 | { type: "reset" }
 | { type: "setCount"; value: State["count"] }
const initialState: State = { count: 0 };
function stateReducer(state: State, action: CounterAction): State {
 switch (action.type) {
  case "reset":
   return initialState;
  case "setCount":
   return { ...state, count: action.value };
  default:
   throw new Error("Unknown action");
 }
}
export default function App() {
 const [state, dispatch] = useReducer(stateReducer, initialState);
 const addFive = () => dispatch({ type: "setCount", value: state.count + 5 });
 const reset = () => dispatch({ type: "reset" });
 return (
  <div>
   <h1>Welcome to my counter</h1>
   <p>Count: {state.count}</p>
   <button onClick={addFive}>Add 5</button>
   <button onClick={reset}>Reset</button>
  </div>
 );
}

```

Show more
We are using TypeScript in a few key places:
  * `interface State` describes the shape of the reducer’s state.
  * `type CounterAction` describes the different actions which can be dispatched to the reducer.
  * `const initialState: State` provides a type for the initial state, and also the type which is used by `useReducer` by default.
  * `stateReducer(state: State, action: CounterAction): State` sets the types for the reducer function’s arguments and return value.


A more explicit alternative to setting the type on `initialState` is to provide a type argument to `useReducer`:
```

import { stateReducer, State } from './your-reducer-implementation';
const initialState = { count: 0 };
export default function App() {
 const [state, dispatch] = useReducer<State>(stateReducer, initialState);
}

```

### `useContext` [](https://react.dev/learn/typescript#typing-usecontext "Link for this heading")
The [`useContext` Hook](https://react.dev/reference/react/useContext) is a technique for passing data down the component tree without having to pass props through components. It is used by creating a provider component and often by creating a Hook to consume the value in a child component.
The type of the value provided by the context is inferred from the value passed to the `createContext` call:
App.tsx
App.tsx
ResetFork[TypeScript Playground](https://www.typescriptlang.org/play#src=import%20*%20as%20React%20from%20'react'%3B%0A%0Aimport%20%7B%20createContext%2C%20useContext%2C%20useState%20%7D%20from%20'react'%3B%0A%0Atype%20Theme%20%3D%20%22light%22%20%7C%20%22dark%22%20%7C%20%22system%22%3B%0Aconst%20ThemeContext%20%3D%20createContext%3CTheme%3E\(%22system%22\)%3B%0A%0Aconst%20useGetTheme%20%3D%20\(\)%20%3D%3E%20useContext\(ThemeContext\)%3B%0A%0Aexport%20default%20function%20MyApp\(\)%20%7B%0A%20%20const%20%5Btheme%2C%20setTheme%5D%20%3D%20useState%3CTheme%3E\('light'\)%3B%0A%0A%20%20return%20\(%0A%20%20%20%20%3CThemeContext.Provider%20value%3D%7Btheme%7D%3E%0A%20%20%20%20%20%20%3CMyComponent%20%2F%3E%0A%20%20%20%20%3C%2FThemeContext.Provider%3E%0A%20%20\)%0A%7D%0A%0Afunction%20MyComponent\(\)%20%7B%0A%20%20const%20theme%20%3D%20useGetTheme\(\)%3B%0A%0A%20%20return%20\(%0A%20%20%20%20%3Cdiv%3E%0A%20%20%20%20%20%20%3Cp%3ECurrent%20theme%3A%20%7Btheme%7D%3C%2Fp%3E%0A%20%20%20%20%3C%2Fdiv%3E%0A%20%20\)%0A%7D%0A "Open in TypeScript Playground")
```
import { createContext, useContext, useState } from 'react';
type Theme = "light" | "dark" | "system";
const ThemeContext = createContext<Theme>("system");
const useGetTheme = () => useContext(ThemeContext);
export default function MyApp() {
 const [theme, setTheme] = useState<Theme>('light');
 return (
  <ThemeContext.Provider value={theme}>
   <MyComponent />
  </ThemeContext.Provider>
 )
}
function MyComponent() {
 const theme = useGetTheme();
 return (
  <div>
   <p>Current theme: {theme}</p>
  </div>
 )
}

```

Show more
This technique works when you have a default value which makes sense - but there are occasionally cases when you do not, and in those cases `null` can feel reasonable as a default value. However, to allow the type-system to understand your code, you need to explicitly set `ContextShape | null` on the `createContext`.
This causes the issue that you need to eliminate the `| null` in the type for context consumers. Our recommendation is to have the Hook do a runtime check for it’s existence and throw an error when not present:
```

import { createContext, useContext, useState, useMemo } from 'react';
// This is a simpler example, but you can imagine a more complex object here
type ComplexObject = {
 kind: string
};
// The context is created with `| null` in the type, to accurately reflect the default value.
const Context = createContext<ComplexObject | null>(null);
// The `| null` will be removed via the check in the Hook.
const useGetComplexObject = () => {
 const object = useContext(Context);
 if (!object) { throw new Error("useGetComplexObject must be used within a Provider") }
 return object;
}
export default function MyApp() {
 const object = useMemo(() => ({ kind: "complex" }), []);
 return (
  <Context.Provider value={object}>
   <MyComponent />
  </Context.Provider>
 )
}
function MyComponent() {
 const object = useGetComplexObject();
 return (
  <div>
   <p>Current object: {object.kind}</p>
  </div>
 )
}

```

### `useMemo` [](https://react.dev/learn/typescript#typing-usememo "Link for this heading")
The [`useMemo`](https://react.dev/reference/react/useMemo) Hooks will create/re-access a memorized value from a function call, re-running the function only when dependencies passed as the 2nd parameter are changed. The result of calling the Hook is inferred from the return value from the function in the first parameter. You can be more explicit by providing a type argument to the Hook.
```

// The type of visibleTodos is inferred from the return value of filterTodos
const visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]);

```

### `useCallback` [](https://react.dev/learn/typescript#typing-usecallback "Link for this heading")
The [`useCallback`](https://react.dev/reference/react/useCallback) provide a stable reference to a function as long as the dependencies passed into the second parameter are the same. Like `useMemo`, the function’s type is inferred from the return value of the function in the first parameter, and you can be more explicit by providing a type argument to the Hook.
```

const handleClick = useCallback(() => {
 // ...
}, [todos]);

```

When working in TypeScript strict mode `useCallback` requires adding types for the parameters in your callback. This is because the type of the callback is inferred from the return value of the function, and without parameters the type cannot be fully understood.
Depending on your code-style preferences, you could use the `*EventHandler` functions from the React types to provide the type for the event handler at the same time as defining the callback:
```

import { useState, useCallback } from 'react';
export default function Form() {
 const [value, setValue] = useState("Change me");
 const handleChange = useCallback<React.ChangeEventHandler<HTMLInputElement>>((event) => {
  setValue(event.currentTarget.value);
 }, [setValue])
 return (
  <>
   <input value={value} onChange={handleChange} />
   <p>Value: {value}</p>
  </>
 );
}

```

## Useful Types [](https://react.dev/learn/typescript#useful-types "Link for Useful Types ")
There is quite an expansive set of types which come from the `@types/react` package, it is worth a read when you feel comfortable with how React and TypeScript interact. You can find them [in React’s folder in DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/react/index.d.ts). We will cover a few of the more common types here.
### DOM Events [](https://react.dev/learn/typescript#typing-dom-events "Link for DOM Events ")
When working with DOM events in React, the type of the event can often be inferred from the event handler. However, when you want to extract a function to be passed to an event handler, you will need to explicitly set the type of the event.
App.tsx
App.tsx
ResetFork[TypeScript Playground](https://www.typescriptlang.org/play#src=import%20*%20as%20React%20from%20'react'%3B%0A%0Aimport%20%7B%20useState%20%7D%20from%20'react'%3B%0A%0Aexport%20default%20function%20Form\(\)%20%7B%0A%20%20const%20%5Bvalue%2C%20setValue%5D%20%3D%20useState\(%22Change%20me%22\)%3B%0A%0A%20%20function%20handleChange\(event%3A%20React.ChangeEvent%3CHTMLInputElement%3E\)%20%7B%0A%20%20%20%20setValue\(event.currentTarget.value\)%3B%0A%20%20%7D%0A%0A%20%20return%20\(%0A%20%20%20%20%3C%3E%0A%20%20%20%20%20%20%3Cinput%20value%3D%7Bvalue%7D%20onChange%3D%7BhandleChange%7D%20%2F%3E%0A%20%20%20%20%20%20%3Cp%3EValue%3A%20%7Bvalue%7D%3C%2Fp%3E%0A%20%20%20%20%3C%2F%3E%0A%20%20\)%3B%0A%7D%0A "Open in TypeScript Playground")
```
import { useState } from 'react';
export default function Form() {
 const [value, setValue] = useState("Change me");
 function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
  setValue(event.currentTarget.value);
 }
 return (
  <>
   <input value={value} onChange={handleChange} />
   <p>Value: {value}</p>
  </>
 );
}

```

Show more
There are many types of events provided in the React types - the full list can be found [here](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/b580df54c0819ec9df62b0835a315dd48b8594a9/types/react/index.d.ts#L1247C1-L1373) which is based on the [most popular events from the DOM](https://developer.mozilla.org/en-US/docs/Web/Events).
When determining the type you are looking for you can first look at the hover information for the event handler you are using, which will show the type of the event.
If you need to use an event that is not included in this list, you can use the `React.SyntheticEvent` type, which is the base type for all events.
### Children [](https://react.dev/learn/typescript#typing-children "Link for Children ")
There are two common paths to describing the children of a component. The first is to use the `React.ReactNode` type, which is a union of all the possible types that can be passed as children in JSX:
```

interface ModalRendererProps {
 title: string;
 children: React.ReactNode;
}

```

This is a very broad definition of children. The second is to use the `React.ReactElement` type, which is only JSX elements and not JavaScript primitives like strings or numbers:
```

interface ModalRendererProps {
 title: string;
 children: React.ReactElement;
}

```

Note, that you cannot use TypeScript to describe that the children are a certain type of JSX elements, so you cannot use the type-system to describe a component which only accepts `<li>` children.
You can see an example of both `React.ReactNode` and `React.ReactElement` with the type-checker in [this TypeScript playground](https://www.typescriptlang.org/play#code/JYWwDg9gTgLgBAJQKYEMDG8BmUIjgIilQ3wChSB6CxYmAOmXRgDkIATJOdNJMGAZzgwAFpxAR+8YADswAVwGkZMJFEzpOjDKw4AFHGEEBvUnDhphwADZsi0gFw0mDWjqQBuUgF9yaCNMlENzgAXjgACjADfkctFnYkfQhDAEpQgD44AB42YAA3dKMo5P46C2tbJGkvLIpcgt9-QLi3AEEwMFCItJDMrPTTbIQ3dKywdIB5aU4kKyQQKpha8drhhIGzLLWODbNs3b3s8YAxKBQAcwXpAThMaGWDvbH0gFloGbmrgQfBzYpd1YjQZbEYARkB6zMwO2SHSAAlZlYIBCdtCRkZpHIrFYahQYQD8UYYFA5EhcfjyGYqHAXnJAsIUHlOOUbHYhMIIHJzsI0Qk4P9SLUBuRqXEXEwAKKfRZcNA8PiCfxWACecAAUgBlAAacFm80W-CU11U6h4TgwUv11yShjgJjMLMqDnN9Dilq+nh8pD8AXgCHdMrCkWisVoAet0R6fXqhWKhjKllZVVxMcavpd4Zg7U6Qaj+2hmdG4zeRF10uu-Aeq0LBfLMEe-V+T2L7zLVu+FBWLdLeq+lc7DYFf39deFVOotMCACNOCh1dq219a+30uC8YWoZsRyuEdjkevR8uvoVMdjyTWt4WiSSydXD4NqZP4AymeZE072ZzuUeZQKheQgA).
### Style Props [](https://react.dev/learn/typescript#typing-style-props "Link for Style Props ")
When using inline styles in React, you can use `React.CSSProperties` to describe the object passed to the `style` prop. This type is a union of all the possible CSS properties, and is a good way to ensure you are passing valid CSS properties to the `style` prop, and to get auto-complete in your editor.
```

interface MyComponentProps {
 style: React.CSSProperties;
}

```

## Further learning [](https://react.dev/learn/typescript#further-learning "Link for Further learning ")
This guide has covered the basics of using TypeScript with React, but there is a lot more to learn. Individual API pages on the docs may contain more in-depth documentation on how to use them with TypeScript.
We recommend the following resources:
  * [The TypeScript handbook](https://www.typescriptlang.org/docs/handbook/) is the official documentation for TypeScript, and covers most key language features.
  * [The TypeScript release notes](https://devblogs.microsoft.com/typescript/) cover new features in depth.
  * [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/) is a community-maintained cheatsheet for using TypeScript with React, covering a lot of useful edge cases and providing more breadth than this document.
  * [TypeScript Community Discord](https://discord.com/invite/typescript) is a great place to ask questions and get help with TypeScript and React issues.


[PreviousEditor Setup](https://react.dev/learn/editor-setup)[NextReact Developer Tools](https://react.dev/learn/react-developer-tools)
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
  * [Overview](https://react.dev/learn/typescript)
  * [Installation ](https://react.dev/learn/typescript#installation)
  * [Adding TypeScript to an existing React project ](https://react.dev/learn/typescript#adding-typescript-to-an-existing-react-project)
  * [TypeScript with React Components ](https://react.dev/learn/typescript#typescript-with-react-components)
  * [Example Hooks ](https://react.dev/learn/typescript#example-hooks)
  * [`useState` ](https://react.dev/learn/typescript#typing-usestate)
  * [`useReducer` ](https://react.dev/learn/typescript#typing-usereducer)
  * [`useContext` ](https://react.dev/learn/typescript#typing-usecontext)
  * [`useMemo` ](https://react.dev/learn/typescript#typing-usememo)
  * [`useCallback` ](https://react.dev/learn/typescript#typing-usecallback)
  * [Useful Types ](https://react.dev/learn/typescript#useful-types)
  * [DOM Events ](https://react.dev/learn/typescript#typing-dom-events)
  * [Children ](https://react.dev/learn/typescript#typing-children)
  * [Style Props ](https://react.dev/learn/typescript#typing-style-props)
  * [Further learning ](https://react.dev/learn/typescript#further-learning)



