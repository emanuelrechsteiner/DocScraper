---
url: https://react.dev/warnings/react-dom-test-utils
scraped_at: 2025-05-25T08:50:49.408589
title: react-dom/test-utils Deprecation Warnings – React
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
  * [Installation ](https://react.dev/learn/installation "Installation")
### LEARN REACT
  * [Describing the UI ](https://react.dev/learn/describing-the-ui "Describing the UI")
  * [Adding Interactivity ](https://react.dev/learn/adding-interactivity "Adding Interactivity")
  * [Managing State ](https://react.dev/learn/managing-state "Managing State")
  * [Escape Hatches ](https://react.dev/learn/escape-hatches "Escape Hatches")
### REACT API
  * [Hooks ](https://react.dev/reference/react "Hooks")
  * [Components ](https://react.dev/reference/react/components "Components")
  * [APIs ](https://react.dev/reference/react/apis "APIs")
  * [Legacy APIs ](https://react.dev/reference/react/legacy "Legacy APIs")
### REACT DOM API
  * [Components ](https://react.dev/reference/react-dom/components "Components")
  * [APIs ](https://react.dev/reference/react-dom "APIs")
  * [Client APIs ](https://react.dev/reference/react-dom/client "Client APIs")
  * [Server APIs ](https://react.dev/reference/react-dom/server "Server APIs")
### GET INVOLVED
  * [React Community ](https://react.dev/community "React Community")
### STAY INFORMED
  * [React Blog ](https://react.dev/blog "React Blog")


Is this page useful?
[React Docs](https://react.dev/)
# react-dom/test-utils Deprecation Warnings[](https://react.dev/warnings/react-dom-test-utils#undefined "Link for this heading")
## ReactDOMTestUtils.act() warning [](https://react.dev/warnings/react-dom-test-utils#reactdomtestutilsact-warning "Link for ReactDOMTestUtils.act\(\) warning ")
`act` from `react-dom/test-utils` has been deprecated in favor of `act` from `react`.
Before:
```

import {act} from 'react-dom/test-utils';

```

After:
```

import {act} from 'react';

```

## Rest of ReactDOMTestUtils APIS [](https://react.dev/warnings/react-dom-test-utils#rest-of-reactdomtestutils-apis "Link for Rest of ReactDOMTestUtils APIS ")
All APIs except `act` have been removed.
The React Team recommends migrating your tests to [@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) for a modern and well supported testing experience.
### ReactDOMTestUtils.renderIntoDocument [](https://react.dev/warnings/react-dom-test-utils#reactdomtestutilsrenderintodocument "Link for ReactDOMTestUtils.renderIntoDocument ")
`renderIntoDocument` can be replaced with `render` from `@testing-library/react`.
Before:
```

import {renderIntoDocument} from 'react-dom/test-utils';
renderIntoDocument(<Component />);

```

After:
```

import {render} from '@testing-library/react';
render(<Component />);

```

### ReactDOMTestUtils.Simulate [](https://react.dev/warnings/react-dom-test-utils#reactdomtestutilssimulate "Link for ReactDOMTestUtils.Simulate ")
`Simulate` can be replaced with `fireEvent` from `@testing-library/react`.
Before:
```

import {Simulate} from 'react-dom/test-utils';
const element = document.querySelector('button');
Simulate.click(element);

```

After:
```

import {fireEvent} from '@testing-library/react';
const element = document.querySelector('button');
fireEvent.click(element);

```

Be aware that `fireEvent` dispatches an actual event on the element and doesn’t just synthetically call the event handler.
### List of all removed APIs [](https://react.dev/warnings/react-dom-test-utils#list-of-all-removed-apis-list-of-all-removed-apis "Link for List of all removed APIs ")
  * `mockComponent()`
  * `isElement()`
  * `isElementOfType()`
  * `isDOMComponent()`
  * `isCompositeComponent()`
  * `isCompositeComponentWithType()`
  * `findAllInRenderedTree()`
  * `scryRenderedDOMComponentsWithClass()`
  * `findRenderedDOMComponentWithClass()`
  * `scryRenderedDOMComponentsWithTag()`
  * `findRenderedDOMComponentWithTag()`
  * `scryRenderedComponentsWithType()`
  * `findRenderedComponentWithType()`
  * `renderIntoDocument`
  * `Simulate`


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
  * [Overview](https://react.dev/warnings/react-dom-test-utils)
  * [ReactDOMTestUtils.act() warning ](https://react.dev/warnings/react-dom-test-utils#reactdomtestutilsact-warning)
  * [Rest of ReactDOMTestUtils APIS ](https://react.dev/warnings/react-dom-test-utils#rest-of-reactdomtestutils-apis)
  * [ReactDOMTestUtils.renderIntoDocument ](https://react.dev/warnings/react-dom-test-utils#reactdomtestutilsrenderintodocument)
  * [ReactDOMTestUtils.Simulate ](https://react.dev/warnings/react-dom-test-utils#reactdomtestutilssimulate)
  * [List of all removed APIs ](https://react.dev/warnings/react-dom-test-utils#list-of-all-removed-apis-list-of-all-removed-apis)



