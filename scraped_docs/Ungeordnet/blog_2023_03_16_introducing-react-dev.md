---
url: https://react.dev/blog/2023/03/16/introducing-react-dev
scraped_at: 2025-05-25T08:33:59.005879
title: Introducing react.dev – React
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
[Blog](https://react.dev/blog)
# Introducing react.dev[](https://react.dev/blog/2023/03/16/introducing-react-dev#undefined "Link for this heading")
March 16, 2023 by [Dan Abramov](https://bsky.app/profile/danabra.mov) and [Rachel Nabors](https://twitter.com/rachelnabors)
Today we are thrilled to launch [react.dev](https://react.dev), the new home for React and its documentation. In this post, we would like to give you a tour of the new site.
## tl;dr [](https://react.dev/blog/2023/03/16/introducing-react-dev#tldr "Link for tl;dr ")
  * The new React site ([react.dev](https://react.dev)) teaches modern React with function components and Hooks.
  * We’ve included diagrams, illustrations, challenges, and over 600 new interactive examples.
  * The previous React documentation site has now moved to [legacy.reactjs.org](https://legacy.reactjs.org).


## New site, new domain, new homepage [](https://react.dev/blog/2023/03/16/introducing-react-dev#new-site-new-domain-new-homepage "Link for New site, new domain, new homepage ")
First, a little bit of housekeeping.
To celebrate the launch of the new docs and, more importantly, to clearly separate the old and the new content, we’ve moved to the shorter [react.dev](https://react.dev) domain. The old [reactjs.org](https://reactjs.org) domain will now redirect here.
The old React docs are now archived at [legacy.reactjs.org](https://legacy.reactjs.org). All existing links to the old content will automatically redirect there to avoid “breaking the web”, but the legacy site will not get many more updates.
Believe it or not, React will soon be ten years old. In JavaScript years, it’s like a whole century! We’ve [refreshed the React homepage](https://react.dev) to reflect why we think React is a great way to create user interfaces today, and updated the getting started guides to more prominently mention modern React-based frameworks.
If you haven’t seen the new homepage yet, check it out!
## Going all-in on modern React with Hooks [](https://react.dev/blog/2023/03/16/introducing-react-dev#going-all-in-on-modern-react-with-hooks "Link for Going all-in on modern React with Hooks ")
When we released React Hooks in 2018, the Hooks docs assumed the reader is familiar with class components. This helped the community adopt Hooks very swiftly, but after a while the old docs failed to serve the new readers. New readers had to learn React twice: once with class components and then once again with Hooks.
**The new docs teach React with Hooks from the beginning.** The docs are divided in two main sections:
  * **[Learn React](https://react.dev/learn)** is a self-paced course that teaches React from scratch.
  * **[API Reference](https://react.dev/reference)** provides the details and usage examples for every React API.


Let’s have a closer look at what you can find in each section.
### Note
There are still a few rare class component use cases that do not yet have a Hook-based equivalent. Class components remain supported, and are documented in the [Legacy API](https://react.dev/reference/react/legacy) section of the new site.
## Quick start [](https://react.dev/blog/2023/03/16/introducing-react-dev#quick-start "Link for Quick start ")
The Learn section begins with the [Quick Start](https://react.dev/learn) page. It is a short introductory tour of React. It introduces the syntax for concepts like components, props, and state, but doesn’t go into much detail on how to use them.
If you like to learn by doing, we recommend checking out the [Tic-Tac-Toe Tutorial](https://react.dev/learn/tutorial-tic-tac-toe) next. It walks you through building a little game with React, while teaching the skills you’ll use every day. Here’s what you’ll build:
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
function Square({ value, onSquareClick }) {
 return (
  <button className="square" onClick={onSquareClick}>
   {value}
  </button>
 );
}
function Board({ xIsNext, squares, onPlay }) {
 function handleClick(i) {
  if (calculateWinner(squares) || squares[i]) {
   return;
  }
  const nextSquares = squares.slice();
  if (xIsNext) {
   nextSquares[i] = 'X';
  } else {
   nextSquares[i] = 'O';
  }
  onPlay(nextSquares);
 }
 const winner = calculateWinner(squares);
 let status;
 if (winner) {
  status = 'Winner: ' + winner;
 } else {
  status = 'Next player: ' + (xIsNext ? 'X' : 'O');
 }
 return (
  <>
   <div className="status">{status}</div>
   <div className="board-row">
    <Square value={squares[0]} onSquareClick={() => handleClick(0)} />
    <Square value={squares[1]} onSquareClick={() => handleClick(1)} />
    <Square value={squares[2]} onSquareClick={() => handleClick(2)} />
   </div>
   <div className="board-row">
    <Square value={squares[3]} onSquareClick={() => handleClick(3)} />
    <Square value={squares[4]} onSquareClick={() => handleClick(4)} />
    <Square value={squares[5]} onSquareClick={() => handleClick(5)} />
   </div>
   <div className="board-row">
    <Square value={squares[6]} onSquareClick={() => handleClick(6)} />
    <Square value={squares[7]} onSquareClick={() => handleClick(7)} />
    <Square value={squares[8]} onSquareClick={() => handleClick(8)} />
   </div>
  </>
 );
}
export default function Game() {
 const [history, setHistory] = useState([Array(9).fill(null)]);
 const [currentMove, setCurrentMove] = useState(0);
 const xIsNext = currentMove % 2 === 0;
 const currentSquares = history[currentMove];
 function handlePlay(nextSquares) {
  const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
  setHistory(nextHistory);
  setCurrentMove(nextHistory.length - 1);
 }
 function jumpTo(nextMove) {
  setCurrentMove(nextMove);
 }
 const moves = history.map((squares, move) => {
  let description;
  if (move > 0) {
   description = 'Go to move #' + move;
  } else {
   description = 'Go to game start';
  }
  return (
   <li key={move}>
    <button onClick={() => jumpTo(move)}>{description}</button>
   </li>
  );
 });
 return (
  <div className="game">
   <div className="game-board">
    <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
   </div>
   <div className="game-info">
    <ol>{moves}</ol>
   </div>
  </div>
 );
}
function calculateWinner(squares) {
 const lines = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
 ];
 for (let i = 0; i < lines.length; i++) {
  const [a, b, c] = lines[i];
  if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
   return squares[a];
  }
 }
 return null;
}

```

Show more
We’d also like to highlight [Thinking in React](https://react.dev/learn/thinking-in-react)—that’s the tutorial that made React “click” for many of us. **We’ve updated both of these classic tutorials to use function components and Hooks,** so they’re as good as new.
### Note
The example above is a _sandbox_. We’ve added a lot of sandboxes—over 600!—everywhere throughout the site. You can edit any sandbox, or press “Fork” in the upper right corner to open it in a separate tab. Sandboxes let you quickly play with the React APIs, explore your ideas, and check your understanding.
## Learn React step by step [](https://react.dev/blog/2023/03/16/introducing-react-dev#learn-react-step-by-step "Link for Learn React step by step ")
We’d like everyone in the world to have an equal opportunity to learn React for free on their own.
This is why the Learn section is organized like a self-paced course split into chapters. The first two chapters describe the fundamentals of React. If you’re new to React, or want to refresh it in your memory, start here:
  * **[Describing the UI](https://react.dev/learn/describing-the-ui)** teaches how to display information with components.
  * **[Adding Interactivity](https://react.dev/learn/adding-interactivity)** teaches how to update the screen in response to user input.


The next two chapters are more advanced, and will give you a deeper insight into the trickier parts:
  * **[Managing State](https://react.dev/learn/managing-state)** teaches how to organize your logic as your app grows in complexity.
  * **[Escape Hatches](https://react.dev/learn/escape-hatches)** teaches how you can “step outside” React, and when it makes most sense to do so.


Every chapter consists of several related pages. Most of these pages teach a specific skill or a technique—for example, [Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx), [Updating Objects in State](https://react.dev/learn/updating-objects-in-state), or [Sharing State Between Components](https://react.dev/learn/sharing-state-between-components). Some of the pages focus on explaining an idea—like [Render and Commit](https://react.dev/learn/render-and-commit), or [State as a Snapshot](https://react.dev/learn/state-as-a-snapshot). And there are a few, like [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect), that share our suggestions based on what we’ve learned over these years.
You don’t have to read these chapters as a sequence. Who has the time for this?! But you could. Pages in the Learn section only rely on concepts introduced by the earlier pages. If you want to read it like a book, go for it!
### Check your understanding with challenges [](https://react.dev/blog/2023/03/16/introducing-react-dev#check-your-understanding-with-challenges "Link for Check your understanding with challenges ")
Most pages in the Learn section end with a few challenges to check your understanding. For example, here are a few challenges from the page about [Conditional Rendering](https://react.dev/learn/conditional-rendering#challenges).
You don’t have to solve them right now! Unless you _really_ want to.
1. Show an icon for incomplete items with `? :` 2. Show the item importance with `&&`
#### 
Challenge 1 of 2: 
Show an icon for incomplete items with `? :` [](https://react.dev/blog/2023/03/16/introducing-react-dev#show-an-icon-for-incomplete-items-with-- "Link for this heading")
Use the conditional operator (`cond ? a : b`) to render a ❌ if `isPacked` isn’t `true`.
App.js
App.js
Download ResetFork
```
function Item({ name, isPacked }) {
 return (
  <li className="item">
   {name} {isPacked && '✅'}
  </li>
 );
}
export default function PackingList() {
 return (
  <section>
   <h1>Sally Ride's Packing List</h1>
   <ul>
    <Item 
     isPacked={true} 
     name="Space suit" 
    />
    <Item 
     isPacked={true} 
     name="Helmet with a golden leaf" 
    />
    <Item 
     isPacked={false} 
     name="Photo of Tam" 
    />
   </ul>
  </section>
 );
}

```

Show more
Show solutionNext Challenge
Notice the “Show solution” button in the left bottom corner. It’s handy if you want to check yourself!
### Build an intuition with diagrams and illustrations [](https://react.dev/blog/2023/03/16/introducing-react-dev#build-an-intuition-with-diagrams-and-illustrations "Link for Build an intuition with diagrams and illustrations ")
When we couldn’t figure out how to explain something with code and words alone, we’ve added diagrams that help provide some intuition. For example, here is one of the diagrams from [Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state):
![Diagram with three sections, with an arrow transitioning each section in between. The first section contains a React component labeled 'div' with a single child labeled 'section', which has a single child labeled 'Counter' containing a state bubble labeled 'count' with value 3. The middle section has the same 'div' parent, but the child components have now been deleted, indicated by a yellow 'proof' image. The third section has the same 'div' parent again, now with a new child labeled 'div', highlighted in yellow, also with a new child labeled 'Counter' containing a state bubble labeled 'count' with value 0, all highlighted in yellow.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpreserving_state_diff_same_pt1.dark.png&w=1920&q=75)
![Diagram with three sections, with an arrow transitioning each section in between. The first section contains a React component labeled 'div' with a single child labeled 'section', which has a single child labeled 'Counter' containing a state bubble labeled 'count' with value 3. The middle section has the same 'div' parent, but the child components have now been deleted, indicated by a yellow 'proof' image. The third section has the same 'div' parent again, now with a new child labeled 'div', highlighted in yellow, also with a new child labeled 'Counter' containing a state bubble labeled 'count' with value 0, all highlighted in yellow.](https://react.dev/_next/image?url=%2Fimages%2Fdocs%2Fdiagrams%2Fpreserving_state_diff_same_pt1.png&w=1920&q=75)
When `section` changes to `div`, the `section` is deleted and the new `div` is added
You’ll also see some illustrations throughout the docs—here’s one of the [browser painting the screen](https://react.dev/learn/render-and-commit#epilogue-browser-paint):
![A browser painting 'still life with card element'.](https://react.dev/images/docs/illustrations/i_browser-paint.png)
Illustrated by [Rachel Lee Nabors](https://nearestnabors.com/)
We’ve confirmed with the browser vendors that this depiction is 100% scientifically accurate.
## A new, detailed API Reference [](https://react.dev/blog/2023/03/16/introducing-react-dev#a-new-detailed-api-reference "Link for A new, detailed API Reference ")
In the [API Reference](https://react.dev/reference/react), every React API now has a dedicated page. This includes all kinds of APIs:
  * Built-in Hooks like [`useState`](https://react.dev/reference/react/useState).
  * Built-in components like [`<Suspense>`](https://react.dev/reference/react/Suspense).
  * Built-in browser components like [`<input>`](https://react.dev/reference/react-dom/components/input).
  * Framework-oriented APIs like [`renderToPipeableStream`](https://react.dev/reference/react-dom/server/renderToReadableStream).
  * Other React APIs like [`memo`](https://react.dev/reference/react/memo).


You’ll notice that every API page is split into at least two segments: _Reference_ and _Usage_.
[Reference](https://react.dev/reference/react/useState#reference) describes the formal API signature by listing its arguments and return values. It’s concise, but it can feel a bit abstract if you’re not familiar with that API. It describes what an API does, but not how to use it.
[Usage](https://react.dev/reference/react/useState#usage) shows why and how you would use this API in practice, like a colleague or a friend might explain. It shows the **canonical scenarios for how each API was meant to be used by the React team.** We’ve added color-coded snippets, examples of using different APIs together, and recipes that you can copy and paste from:
#### Basic useState examples[](https://react.dev/blog/2023/03/16/introducing-react-dev#examples-basic "Link for Basic useState examples")
1. Counter (number) 2. Text field (string) 3. Checkbox (boolean) 4. Form (two variables) 
#### 
Example 1 of 4: 
Counter (number) [](https://react.dev/blog/2023/03/16/introducing-react-dev#counter-number "Link for this heading")
In this example, the `count` state variable holds a number. Clicking the button increments it.
App.js
App.js
Download ResetFork
```
import { useState } from 'react';
export default function Counter() {
 const [count, setCount] = useState(0);
 function handleClick() {
  setCount(count + 1);
 }
 return (
  <button onClick={handleClick}>
   You pressed me {count} times
  </button>
 );
}

```

Next Example
Some API pages also include [Troubleshooting](https://react.dev/reference/react/useEffect#troubleshooting) (for common problems) and [Alternatives](https://react.dev/reference/react-dom/findDOMNode#alternatives) (for deprecated APIs).
We hope that this approach will make the API reference useful not only as a way to look up an argument, but as a way to see all the different things you can do with any given API—and how it connects to the other ones.
## What’s next? [](https://react.dev/blog/2023/03/16/introducing-react-dev#whats-next "Link for What’s next? ")
That’s a wrap for our little tour! Have a look around the new website, see what you like or don’t like, and keep the feedback coming in our [issue tracker](https://github.com/reactjs/react.dev/issues).
We acknowledge this project has taken a long time to ship. We wanted to maintain a high quality bar that the React community deserves. While writing these docs and creating all of the examples, we found mistakes in some of our own explanations, bugs in React, and even gaps in the React design that we are now working to address. We hope that the new documentation will help us hold React itself to a higher bar in the future.
We’ve heard many of your requests to expand the content and functionality of the website, for example:
  * Providing a TypeScript version for all examples;
  * Creating the updated performance, testing, and accessibility guides;
  * Documenting React Server Components independently from the frameworks that support them;
  * Working with our international community to get the new docs translated;
  * Adding missing features to the new website (for example, RSS for this blog).


Now that [react.dev](https://react.dev/) is out, we will be able to shift our focus from “catching up” with the third-party React educational resources to adding new information and further improving our new website.
We think there’s never been a better time to learn React.
## Who worked on this? [](https://react.dev/blog/2023/03/16/introducing-react-dev#who-worked-on-this "Link for Who worked on this? ")
On the React team, [Rachel Nabors](https://twitter.com/rachelnabors/) led the project (and provided the illustrations), and [Dan Abramov](https://bsky.app/profile/danabra.mov) designed the curriculum. They co-authored most of the content together as well.
Of course, no project this large happens in isolation. We have a lot of people to thank!
[Sylwia Vargas](https://twitter.com/SylwiaVargas) overhauled our examples to go beyond “foo/bar/baz” and kittens, and feature scientists, artists and cities from around the world. [Maggie Appleton](https://twitter.com/Mappletons) turned our doodles into a clear diagram system.
Thanks to [David McCabe](https://twitter.com/mcc_abe), [Sophie Alpert](https://twitter.com/sophiebits), [Rick Hanlon](https://twitter.com/rickhanlonii), [Andrew Clark](https://twitter.com/acdlite), and [Matt Carroll](https://twitter.com/mattcarrollcode) for additional writing contributions. We’d also like to thank [Natalia Tepluhina](https://twitter.com/n_tepluhina) and [Sebastian Markbåge](https://twitter.com/sebmarkbage) for their ideas and feedback.
Thanks to [Dan Lebowitz](https://twitter.com/lebo) for the site design and [Razvan Gradinar](https://dribbble.com/GradinarRazvan) for the sandbox design.
On the development front, thanks to [Jared Palmer](https://twitter.com/jaredpalmer) for prototype development. Thanks to [Dane Grant](https://twitter.com/danecando) and [Dustin Goodman](https://twitter.com/dustinsgoodman) from [ThisDotLabs](https://www.thisdot.co/) for their support on UI development. Thanks to [Ives van Hoorne](https://twitter.com/CompuIves), [Alex Moldovan](https://twitter.com/alexnmoldovan), [Jasper De Moor](https://twitter.com/JasperDeMoor), and [Danilo Woznica](https://twitter.com/danilowoz) from [CodeSandbox](https://codesandbox.io/) for their work with sandbox integration. Thanks to [Rick Hanlon](https://twitter.com/rickhanlonii) for spot development and design work, finessing our colors and finer details. Thanks to [Harish Kumar](https://www.strek.in/) and [Luna Ruan](https://twitter.com/lunaruan) for adding new features to the site and helping maintain it.
Huge thanks to the folks who volunteered their time to participate in the alpha and beta testing program. Your enthusiasm and invaluable feedback helped us shape these docs. A special shout out to our beta tester, [Debbie O’Brien](https://twitter.com/debs_obrien), who gave a talk about her experience using the React docs at React Conf 2021.
Finally, thanks to the React community for being the inspiration behind this effort. You are the reason we do this, and we hope that the new docs will help you use React to build any user interface that you want.
[PreviousReact Labs: What We've Been Working On – March 2023](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023)[NextReact Labs: What We've Been Working On – June 2022](https://react.dev/blog/2022/06/15/react-labs-what-we-have-been-working-on-june-2022)
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

