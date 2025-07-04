---
url: https://react.dev/learn/separating-events-from-effects
scraped_at: 2025-05-25T08:35:02.241550
title: Separating Events from Effects – React
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
# Separating Events from Effects[](https://react.dev/learn/separating-events-from-effects#undefined "Link for this heading")
Event handlers only re-run when you perform the same interaction again. Unlike event handlers, Effects re-synchronize if some value they read, like a prop or a state variable, is different from what it was during the last render. Sometimes, you also want a mix of both behaviors: an Effect that re-runs in response to some values but not others. This page will teach you how to do that.
### You will learn
  * How to choose between an event handler and an Effect
  * Why Effects are reactive, and event handlers are not
  * What to do when you want a part of your Effect’s code to not be reactive
  * What Effect Events are, and how to extract them from your Effects
  * How to read the latest props and state from Effects using Effect Events


## Choosing between event handlers and Effects [](https://react.dev/learn/separating-events-from-effects#choosing-between-event-handlers-and-effects "Link for Choosing between event handlers and Effects ")
First, let’s recap the difference between event handlers and Effects.
Imagine you’re implementing a chat room component. Your requirements look like this:
  1. Your component should automatically connect to the selected chat room.
  2. When you click the “Send” button, it should send a message to the chat.


Let’s say you’ve already implemented the code for them, but you’re not sure where to put it. Should you use event handlers or Effects? Every time you need to answer this question, consider [_why_ the code needs to run.](https://react.dev/learn/synchronizing-with-effects#what-are-effects-and-how-are-they-different-from-events)
### Event handlers run in response to specific interactions [](https://react.dev/learn/separating-events-from-effects#event-handlers-run-in-response-to-specific-interactions "Link for Event handlers run in response to specific interactions ")
From the user’s perspective, sending a message should happen _because_ the particular “Send” button was clicked. The user will get rather upset if you send their message at any other time or for any other reason. This is why sending a message should be an event handler. Event handlers let you handle specific interactions:
```

function ChatRoom({ roomId }) {
 const [message, setMessage] = useState('');
 // ...
 function handleSendClick() {
  sendMessage(message);
 }
 // ...
 return (
  <>
   <input value={message} onChange={e => setMessage(e.target.value)} />
   <button onClick={handleSendClick}>Send</button>
  </>
 );
}

```

With an event handler, you can be sure that `sendMessage(message)` will _only_ run if the user presses the button.
### Effects run whenever synchronization is needed [](https://react.dev/learn/separating-events-from-effects#effects-run-whenever-synchronization-is-needed "Link for Effects run whenever synchronization is needed ")
Recall that you also need to keep the component connected to the chat room. Where does that code go?
The _reason_ to run this code is not some particular interaction. It doesn’t matter why or how the user navigated to the chat room screen. Now that they’re looking at it and could interact with it, the component needs to stay connected to the selected chat server. Even if the chat room component was the initial screen of your app, and the user has not performed any interactions at all, you would _still_ need to connect. This is why it’s an Effect:
```

function ChatRoom({ roomId }) {
 // ...
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.connect();
  return () => {
   connection.disconnect();
  };
 }, [roomId]);
 // ...
}

```

With this code, you can be sure that there is always an active connection to the currently selected chat server, _regardless_ of the specific interactions performed by the user. Whether the user has only opened your app, selected a different room, or navigated to another screen and back, your Effect ensures that the component will _remain synchronized_ with the currently selected room, and will [re-connect whenever it’s necessary.](https://react.dev/learn/lifecycle-of-reactive-effects#why-synchronization-may-need-to-happen-more-than-once)
App.jschat.js
App.js
ResetFork
```
import { useState, useEffect } from 'react';
import { createConnection, sendMessage } from './chat.js';
const serverUrl = 'https://localhost:1234';
function ChatRoom({ roomId }) {
 const [message, setMessage] = useState('');
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.connect();
  return () => connection.disconnect();
 }, [roomId]);
 function handleSendClick() {
  sendMessage(message);
 }
 return (
  <>
   <h1>Welcome to the {roomId} room!</h1>
   <input value={message} onChange={e => setMessage(e.target.value)} />
   <button onClick={handleSendClick}>Send</button>
  </>
 );
}
export default function App() {
 const [roomId, setRoomId] = useState('general');
 const [show, setShow] = useState(false);
 return (
  <>
   <label>
    Choose the chat room:{' '}
    <select
     value={roomId}
     onChange={e => setRoomId(e.target.value)}
    >
     <option value="general">general</option>
     <option value="travel">travel</option>
     <option value="music">music</option>
    </select>
   </label>
   <button onClick={() => setShow(!show)}>
    {show ? 'Close chat' : 'Open chat'}
   </button>
   {show && <hr />}
   {show && <ChatRoom roomId={roomId} />}
  </>
 );
}

```

Show more
## Reactive values and reactive logic [](https://react.dev/learn/separating-events-from-effects#reactive-values-and-reactive-logic "Link for Reactive values and reactive logic ")
Intuitively, you could say that event handlers are always triggered “manually”, for example by clicking a button. Effects, on the other hand, are “automatic”: they run and re-run as often as it’s needed to stay synchronized.
There is a more precise way to think about this.
Props, state, and variables declared inside your component’s body are called reactive values. In this example, `serverUrl` is not a reactive value, but `roomId` and `message` are. They participate in the rendering data flow:
```

const serverUrl = 'https://localhost:1234';
function ChatRoom({ roomId }) {
 const [message, setMessage] = useState('');
 // ...
}

```

Reactive values like these can change due to a re-render. For example, the user may edit the `message` or choose a different `roomId` in a dropdown. Event handlers and Effects respond to changes differently:
  * **Logic inside event handlers is _not reactive._** It will not run again unless the user performs the same interaction (e.g. a click) again. Event handlers can read reactive values without “reacting” to their changes.
  * **Logic inside Effects is _reactive._** If your Effect reads a reactive value, [you have to specify it as a dependency.](https://react.dev/learn/lifecycle-of-reactive-effects#effects-react-to-reactive-values) Then, if a re-render causes that value to change, React will re-run your Effect’s logic with the new value.


Let’s revisit the previous example to illustrate this difference.
### Logic inside event handlers is not reactive [](https://react.dev/learn/separating-events-from-effects#logic-inside-event-handlers-is-not-reactive "Link for Logic inside event handlers is not reactive ")
Take a look at this line of code. Should this logic be reactive or not?
```

  // ...
  sendMessage(message);
  // ...

```

From the user’s perspective, **a change to the`message` does _not_ mean that they want to send a message.** It only means that the user is typing. In other words, the logic that sends a message should not be reactive. It should not run again only because the reactive value has changed. That’s why it belongs in the event handler:
```

 function handleSendClick() {
  sendMessage(message);
 }

```

Event handlers aren’t reactive, so `sendMessage(message)` will only run when the user clicks the Send button.
### Logic inside Effects is reactive [](https://react.dev/learn/separating-events-from-effects#logic-inside-effects-is-reactive "Link for Logic inside Effects is reactive ")
Now let’s return to these lines:
```

  // ...
  const connection = createConnection(serverUrl, roomId);
  connection.connect();
  // ...

```

From the user’s perspective, **a change to the`roomId` _does_ mean that they want to connect to a different room.** In other words, the logic for connecting to the room should be reactive. You _want_ these lines of code to “keep up” with the reactive value, and to run again if that value is different. That’s why it belongs in an Effect:
```

 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.connect();
  return () => {
   connection.disconnect()
  };
 }, [roomId]);

```

Effects are reactive, so `createConnection(serverUrl, roomId)` and `connection.connect()` will run for every distinct value of `roomId`. Your Effect keeps the chat connection synchronized to the currently selected room.
## Extracting non-reactive logic out of Effects [](https://react.dev/learn/separating-events-from-effects#extracting-non-reactive-logic-out-of-effects "Link for Extracting non-reactive logic out of Effects ")
Things get more tricky when you want to mix reactive logic with non-reactive logic.
For example, imagine that you want to show a notification when the user connects to the chat. You read the current theme (dark or light) from the props so that you can show the notification in the correct color:
```

function ChatRoom({ roomId, theme }) {
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.on('connected', () => {
   showNotification('Connected!', theme);
  });
  connection.connect();
  // ...

```

However, `theme` is a reactive value (it can change as a result of re-rendering), and [every reactive value read by an Effect must be declared as its dependency.](https://react.dev/learn/lifecycle-of-reactive-effects#react-verifies-that-you-specified-every-reactive-value-as-a-dependency) Now you have to specify `theme` as a dependency of your Effect:
```

function ChatRoom({ roomId, theme }) {
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.on('connected', () => {
   showNotification('Connected!', theme);
  });
  connection.connect();
  return () => {
   connection.disconnect()
  };
 }, [roomId, theme]); // ✅ All dependencies declared
 // ...

```

Play with this example and see if you can spot the problem with this user experience:
App.jschat.jsnotifications.js
App.js
ResetFork
```
import { useState, useEffect } from 'react';
import { createConnection, sendMessage } from './chat.js';
import { showNotification } from './notifications.js';
const serverUrl = 'https://localhost:1234';
function ChatRoom({ roomId, theme }) {
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.on('connected', () => {
   showNotification('Connected!', theme);
  });
  connection.connect();
  return () => connection.disconnect();
 }, [roomId, theme]);
 return <h1>Welcome to the {roomId} room!</h1>
}
export default function App() {
 const [roomId, setRoomId] = useState('general');
 const [isDark, setIsDark] = useState(false);
 return (
  <>
   <label>
    Choose the chat room:{' '}
    <select
     value={roomId}
     onChange={e => setRoomId(e.target.value)}
    >
     <option value="general">general</option>
     <option value="travel">travel</option>
     <option value="music">music</option>
    </select>
   </label>
   <label>
    <input
     type="checkbox"
     checked={isDark}
     onChange={e => setIsDark(e.target.checked)}
    />
    Use dark theme
   </label>
   <hr />
   <ChatRoom
    roomId={roomId}
    theme={isDark ? 'dark' : 'light'}
   />
  </>
 );
}

```

Show more
When the `roomId` changes, the chat re-connects as you would expect. But since `theme` is also a dependency, the chat _also_ re-connects every time you switch between the dark and the light theme. That’s not great!
In other words, you _don’t_ want this line to be reactive, even though it is inside an Effect (which is reactive):
```

   // ...
   showNotification('Connected!', theme);
   // ...

```

You need a way to separate this non-reactive logic from the reactive Effect around it.
### Declaring an Effect Event [](https://react.dev/learn/separating-events-from-effects#declaring-an-effect-event "Link for Declaring an Effect Event ")
### Under Construction
This section describes an **experimental API that has not yet been released** in a stable version of React.
Use a special Hook called [`useEffectEvent`](https://react.dev/reference/react/experimental_useEffectEvent) to extract this non-reactive logic out of your Effect:
```

import { useEffect, useEffectEvent } from 'react';
function ChatRoom({ roomId, theme }) {
 const onConnected = useEffectEvent(() => {
  showNotification('Connected!', theme);
 });
 // ...

```

Here, `onConnected` is called an _Effect Event._ It’s a part of your Effect logic, but it behaves a lot more like an event handler. The logic inside it is not reactive, and it always “sees” the latest values of your props and state.
Now you can call the `onConnected` Effect Event from inside your Effect:
```

function ChatRoom({ roomId, theme }) {
 const onConnected = useEffectEvent(() => {
  showNotification('Connected!', theme);
 });
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.on('connected', () => {
   onConnected();
  });
  connection.connect();
  return () => connection.disconnect();
 }, [roomId]); // ✅ All dependencies declared
 // ...

```

This solves the problem. Note that you had to _remove_ `theme` from the list of your Effect’s dependencies, because it’s no longer used in the Effect. You also don’t need to _add_ `onConnected` to it, because **Effect Events are not reactive and must be omitted from dependencies.**
Verify that the new behavior works as you would expect:
App.jschat.js
App.js
ResetFork
```
import { useState, useEffect } from 'react';
import { experimental_useEffectEvent as useEffectEvent } from 'react';
import { createConnection, sendMessage } from './chat.js';
import { showNotification } from './notifications.js';
const serverUrl = 'https://localhost:1234';
function ChatRoom({ roomId, theme }) {
 const onConnected = useEffectEvent(() => {
  showNotification('Connected!', theme);
 });
 useEffect(() => {
  const connection = createConnection(serverUrl, roomId);
  connection.on('connected', () => {
   onConnected();
  });
  connection.connect();
  return () => connection.disconnect();
 }, [roomId]);
 return <h1>Welcome to the {roomId} room!</h1>
}
export default function App() {
 const [roomId, setRoomId] = useState('general');
 const [isDark, setIsDark] = useState(false);
 return (
  <>
   <label>
    Choose the chat room:{' '}
    <select
     value={roomId}
     onChange={e => setRoomId(e.target.value)}
    >
     <option value="general">general</option>
     <option value="travel">travel</option>
     <option value="music">music</option>
    </select>
   </label>
   <label>
    <input
     type="checkbox"
     checked={isDark}
     onChange={e => setIsDark(e.target.checked)}
    />
    Use dark theme
   </label>
   <hr />
   <ChatRoom
    roomId={roomId}
    theme={isDark ? 'dark' : 'light'}
   />
  </>
 );
}

```

Show more
You can think of Effect Events as being very similar to event handlers. The main difference is that event handlers run in response to a user interactions, whereas Effect Events are triggered by you from Effects. Effect Events let you “break the chain” between the reactivity of Effects and code that should not be reactive.
### Reading latest props and state with Effect Events [](https://react.dev/learn/separating-events-from-effects#reading-latest-props-and-state-with-effect-events "Link for Reading latest props and state with Effect Events ")
### Under Construction
This section describes an **experimental API that has not yet been released** in a stable version of React.
Effect Events let you fix many patterns where you might be tempted to suppress the dependency linter.
For example, say you have an Effect to log the page visits:
```

function Page() {
 useEffect(() => {
  logVisit();
 }, []);
 // ...
}

```

Later, you add multiple routes to your site. Now your `Page` component receives a `url` prop with the current path. You want to pass the `url` as a part of your `logVisit` call, but the dependency linter complains:
```

function Page({ url }) {
 useEffect(() => {
  logVisit(url);
 }, []); // 🔴 React Hook useEffect has a missing dependency: 'url'
 // ...
}

```

Think about what you want the code to do. You _want_ to log a separate visit for different URLs since each URL represents a different page. In other words, this `logVisit` call _should_ be reactive with respect to the `url`. This is why, in this case, it makes sense to follow the dependency linter, and add `url` as a dependency:
```

function Page({ url }) {
 useEffect(() => {
  logVisit(url);
 }, [url]); // ✅ All dependencies declared
 // ...
}

```

Now let’s say you want to include the number of items in the shopping cart together with every page visit:
```

function Page({ url }) {
 const { items } = useContext(ShoppingCartContext);
 const numberOfItems = items.length;
 useEffect(() => {
  logVisit(url, numberOfItems);
 }, [url]); // 🔴 React Hook useEffect has a missing dependency: 'numberOfItems'
 // ...
}

```

You used `numberOfItems` inside the Effect, so the linter asks you to add it as a dependency. However, you _don’t_ want the `logVisit` call to be reactive with respect to `numberOfItems`. If the user puts something into the shopping cart, and the `numberOfItems` changes, this _does not mean_ that the user visited the page again. In other words, _visiting the page_ is, in some sense, an “event”. It happens at a precise moment in time.
Split the code in two parts:
```

function Page({ url }) {
 const { items } = useContext(ShoppingCartContext);
 const numberOfItems = items.length;
 const onVisit = useEffectEvent(visitedUrl => {
  logVisit(visitedUrl, numberOfItems);
 });
 useEffect(() => {
  onVisit(url);
 }, [url]); // ✅ All dependencies declared
 // ...
}

```

Here, `onVisit` is an Effect Event. The code inside it isn’t reactive. This is why you can use `numberOfItems` (or any other reactive value!) without worrying that it will cause the surrounding code to re-execute on changes.
On the other hand, the Effect itself remains reactive. Code inside the Effect uses the `url` prop, so the Effect will re-run after every re-render with a different `url`. This, in turn, will call the `onVisit` Effect Event.
As a result, you will call `logVisit` for every change to the `url`, and always read the latest `numberOfItems`. However, if `numberOfItems` changes on its own, this will not cause any of the code to re-run.
### Note
You might be wondering if you could call `onVisit()` with no arguments, and read the `url` inside it:
```

 const onVisit = useEffectEvent(() => {
  logVisit(url, numberOfItems);
 });
 useEffect(() => {
  onVisit();
 }, [url]);

```

This would work, but it’s better to pass this `url` to the Effect Event explicitly. **By passing`url` as an argument to your Effect Event, you are saying that visiting a page with a different `url` constitutes a separate “event” from the user’s perspective.** The `visitedUrl` is a _part_ of the “event” that happened:
```

 const onVisit = useEffectEvent(visitedUrl => {
  logVisit(visitedUrl, numberOfItems);
 });
 useEffect(() => {
  onVisit(url);
 }, [url]);

```

Since your Effect Event explicitly “asks” for the `visitedUrl`, now you can’t accidentally remove `url` from the Effect’s dependencies. If you remove the `url` dependency (causing distinct page visits to be counted as one), the linter will warn you about it. You want `onVisit` to be reactive with regards to the `url`, so instead of reading the `url` inside (where it wouldn’t be reactive), you pass it _from_ your Effect.
This becomes especially important if there is some asynchronous logic inside the Effect:
```

 const onVisit = useEffectEvent(visitedUrl => {
  logVisit(visitedUrl, numberOfItems);
 });
 useEffect(() => {
  setTimeout(() => {
   onVisit(url);
  }, 5000); // Delay logging visits
 }, [url]);

```

Here, `url` inside `onVisit` corresponds to the _latest_ `url` (which could have already changed), but `visitedUrl` corresponds to the `url` that originally caused this Effect (and this `onVisit` call) to run.
##### Deep Dive
#### Is it okay to suppress the dependency linter instead? [](https://react.dev/learn/separating-events-from-effects#is-it-okay-to-suppress-the-dependency-linter-instead "Link for Is it okay to suppress the dependency linter instead? ")
Show Details
In the existing codebases, you may sometimes see the lint rule suppressed like this:
```

function Page({ url }) {
 const { items } = useContext(ShoppingCartContext);
 const numberOfItems = items.length;
 useEffect(() => {
  logVisit(url, numberOfItems);
  // 🔴 Avoid suppressing the linter like this:
  // eslint-disable-next-line react-hooks/exhaustive-deps
 }, [url]);
 // ...
}

```

After `useEffectEvent` becomes a stable part of React, we recommend **never suppressing the linter**.
The first downside of suppressing the rule is that React will no longer warn you when your Effect needs to “react” to a new reactive dependency you’ve introduced to your code. In the earlier example, you added `url` to the dependencies _because_ React reminded you to do it. You will no longer get such reminders for any future edits to that Effect if you disable the linter. This leads to bugs.
Here is an example of a confusing bug caused by suppressing the linter. In this example, the `handleMove` function is supposed to read the current `canMove` state variable value in order to decide whether the dot should follow the cursor. However, `canMove` is always `true` inside `handleMove`.
Can you see why?
App.js
App.js
Download ResetFork
```
import { useState, useEffect } from 'react';
export default function App() {
 const [position, setPosition] = useState({ x: 0, y: 0 });
 const [canMove, setCanMove] = useState(true);
 function handleMove(e) {
  if (canMove) {
   setPosition({ x: e.clientX, y: e.clientY });
  }
 }
 useEffect(() => {
  window.addEventListener('pointermove', handleMove);
  return () => window.removeEventListener('pointermove', handleMove);
  // eslint-disable-next-line react-hooks/exhaustive-deps
 }, []);
 return (
  <>
   <label>
    <input type="checkbox"
     checked={canMove}
     onChange={e => setCanMove(e.target.checked)}
    />
    The dot is allowed to move
   </label>
   <hr />
   <div style={{
    position: 'absolute',
    backgroundColor: 'pink',
    borderRadius: '50%',
    opacity: 0.6,
    transform: `translate(${position.x}px, ${position.y}px)`,
    pointerEvents: 'none',
    left: -20,
    top: -20,
    width: 40,
    height: 40,
   }} />
  </>
 );
}

```

Show more
The problem with this code is in suppressing the dependency linter. If you remove the suppression, you’ll see that this Effect should depend on the `handleMove` function. This makes sense: `handleMove` is declared inside the component body, which makes it a reactive value. Every reactive value must be specified as a dependency, or it can potentially get stale over time!
The author of the original code has “lied” to React by saying that the Effect does not depend (`[]`) on any reactive values. This is why React did not re-synchronize the Effect after `canMove` has changed (and `handleMove` with it). Because React did not re-synchronize the Effect, the `handleMove` attached as a listener is the `handleMove` function created during the initial render. During the initial render, `canMove` was `true`, which is why `handleMove` from the initial render will forever see that value.
**If you never suppress the linter, you will never see problems with stale values.**
With `useEffectEvent`, there is no need to “lie” to the linter, and the code works as you would expect:
App.js
App.js
ResetFork
```
import { useState, useEffect } from 'react';
import { experimental_useEffectEvent as useEffectEvent } from 'react';
export default function App() {
 const [position, setPosition] = useState({ x: 0, y: 0 });
 const [canMove, setCanMove] = useState(true);
 const onMove = useEffectEvent(e => {
  if (canMove) {
   setPosition({ x: e.clientX, y: e.clientY });
  }
 });
 useEffect(() => {
  window.addEventListener('pointermove', onMove);
  return () => window.removeEventListener('pointermove', onMove);
 }, []);
 return (
  <>
   <label>
    <input type="checkbox"
     checked={canMove}
     onChange={e => setCanMove(e.target.checked)}
    />
    The dot is allowed to move
   </label>
   <hr />
   <div style={{
    position: 'absolute',
    backgroundColor: 'pink',
    borderRadius: '50%',
    opacity: 0.6,
    transform: `translate(${position.x}px, ${position.y}px)`,
    pointerEvents: 'none',
    left: -20,
    top: -20,
    width: 40,
    height: 40,
   }} />
  </>
 );
}

```

Show more
This doesn’t mean that `useEffectEvent` is _always_ the correct solution. You should only apply it to the lines of code that you don’t want to be reactive. In the above sandbox, you didn’t want the Effect’s code to be reactive with regards to `canMove`. That’s why it made sense to extract an Effect Event.
Read [Removing Effect Dependencies](https://react.dev/learn/removing-effect-dependencies) for other correct alternatives to suppressing the linter.
### Limitations of Effect Events [](https://react.dev/learn/separating-events-from-effects#limitations-of-effect-events "Link for Limitations of Effect Events ")
### Under Construction
This section describes an **experimental API that has not yet been released** in a stable version of React.
Effect Events are very limited in how you can use them:
  * **Only call them from inside Effects.**
  * **Never pass them to other components or Hooks.**


For example, don’t declare and pass an Effect Event like this:
```

function Timer() {
 const [count, setCount] = useState(0);
 const onTick = useEffectEvent(() => {
  setCount(count + 1);
 });
 useTimer(onTick, 1000); // 🔴 Avoid: Passing Effect Events
 return <h1>{count}</h1>
}
function useTimer(callback, delay) {
 useEffect(() => {
  const id = setInterval(() => {
   callback();
  }, delay);
  return () => {
   clearInterval(id);
  };
 }, [delay, callback]); // Need to specify "callback" in dependencies
}

```

Instead, always declare Effect Events directly next to the Effects that use them:
```

function Timer() {
 const [count, setCount] = useState(0);
 useTimer(() => {
  setCount(count + 1);
 }, 1000);
 return <h1>{count}</h1>
}
function useTimer(callback, delay) {
 const onTick = useEffectEvent(() => {
  callback();
 });
 useEffect(() => {
  const id = setInterval(() => {
   onTick(); // ✅ Good: Only called locally inside an Effect
  }, delay);
  return () => {
   clearInterval(id);
  };
 }, [delay]); // No need to specify "onTick" (an Effect Event) as a dependency
}

```

Effect Events are non-reactive “pieces” of your Effect code. They should be next to the Effect using them.
## Recap[](https://react.dev/learn/separating-events-from-effects#recap "Link for Recap")
  * Event handlers run in response to specific interactions.
  * Effects run whenever synchronization is needed.
  * Logic inside event handlers is not reactive.
  * Logic inside Effects is reactive.
  * You can move non-reactive logic from Effects into Effect Events.
  * Only call Effect Events from inside Effects.
  * Don’t pass Effect Events to other components or Hooks.


## Try out some challenges[](https://react.dev/learn/separating-events-from-effects#challenges "Link for Try out some challenges")
1. Fix a variable that doesn’t update 2. Fix a freezing counter 3. Fix a non-adjustable delay 4. Fix a delayed notification 
#### 
Challenge 1 of 4: 
Fix a variable that doesn’t update [](https://react.dev/learn/separating-events-from-effects#fix-a-variable-that-doesnt-update "Link for this heading")
This `Timer` component keeps a `count` state variable which increases every second. The value by which it’s increasing is stored in the `increment` state variable. You can control the `increment` variable with the plus and minus buttons.
However, no matter how many times you click the plus button, the counter is still incremented by one every second. What’s wrong with this code? Why is `increment` always equal to `1` inside the Effect’s code? Find the mistake and fix it.
App.js
App.js
ResetFork
```
import { useState, useEffect } from 'react';
export default function Timer() {
 const [count, setCount] = useState(0);
 const [increment, setIncrement] = useState(1);
 useEffect(() => {
  const id = setInterval(() => {
   setCount(c => c + increment);
  }, 1000);
  return () => {
   clearInterval(id);
  };
  // eslint-disable-next-line react-hooks/exhaustive-deps
 }, []);
 return (
  <>
   <h1>
    Counter: {count}
    <button onClick={() => setCount(0)}>Reset</button>
   </h1>
   <hr />
   <p>
    Every second, increment by:
    <button disabled={increment === 0} onClick={() => {
     setIncrement(i => i - 1);
    }}>–</button>
    <b>{increment}</b>
    <button onClick={() => {
     setIncrement(i => i + 1);
    }}>+</button>
   </p>
  </>
 );
}

```

Show more
Show hint Show solution
Next Challenge
[PreviousLifecycle of Reactive Effects](https://react.dev/learn/lifecycle-of-reactive-effects)[NextRemoving Effect Dependencies](https://react.dev/learn/removing-effect-dependencies)
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
  * [Overview](https://react.dev/learn/separating-events-from-effects)
  * [Choosing between event handlers and Effects ](https://react.dev/learn/separating-events-from-effects#choosing-between-event-handlers-and-effects)
  * [Event handlers run in response to specific interactions ](https://react.dev/learn/separating-events-from-effects#event-handlers-run-in-response-to-specific-interactions)
  * [Effects run whenever synchronization is needed ](https://react.dev/learn/separating-events-from-effects#effects-run-whenever-synchronization-is-needed)
  * [Reactive values and reactive logic ](https://react.dev/learn/separating-events-from-effects#reactive-values-and-reactive-logic)
  * [Logic inside event handlers is not reactive ](https://react.dev/learn/separating-events-from-effects#logic-inside-event-handlers-is-not-reactive)
  * [Logic inside Effects is reactive ](https://react.dev/learn/separating-events-from-effects#logic-inside-effects-is-reactive)
  * [Extracting non-reactive logic out of Effects ](https://react.dev/learn/separating-events-from-effects#extracting-non-reactive-logic-out-of-effects)
  * [Declaring an Effect Event ](https://react.dev/learn/separating-events-from-effects#declaring-an-effect-event)
  * [Reading latest props and state with Effect Events ](https://react.dev/learn/separating-events-from-effects#reading-latest-props-and-state-with-effect-events)
  * [Limitations of Effect Events ](https://react.dev/learn/separating-events-from-effects#limitations-of-effect-events)
  * [Recap](https://react.dev/learn/separating-events-from-effects#recap)
  * [Challenges](https://react.dev/learn/separating-events-from-effects#challenges)



