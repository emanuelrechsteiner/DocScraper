---
url: https://supabase.com/blog/supabase-dashboard-performance
scraped_at: 2025-05-25T09:46:08.426153
title: Making the Supabase Dashboard Supa-fast
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Making the Supabase Dashboard Supa-fast
13 Dec 2020
•
8 minute read
[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)
The Supabase dashboard has become more feature-rich in the last month. We have a powerful SQL editor backed by [Monaco](https://microsoft.github.io/monaco-editor/). We built an Airtable-like view of your database, making editing a breeze.
> Features, performance, DX - choose three
Performance can quickly regress when adding new features, especially in a Single Page Application. Here are the steps we took to guarantee a good baseline performance within our application, without compromising on the developer experience (DX).
## Establishing a baseline and setting targets[#](https://supabase.com/blog/supabase-dashboard-performance#establishing-a-baseline-and-setting-targets)
> You can't fix what you can't measure
There was some low-hanging fruit to improve performance, but we had one important thing to do before that - establish a baseline.
Our dashboard is JavaScript heavy, so we started by setting up analytics to track our bundle sizes. [Next-bundle-analyzer](https://www.npmjs.com/package/@next/bundle-analyzer) (or [webpack-bundle-analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer)) provides an interactive treemap of your generated JavaScript bundles. This is our treemap when we started. It gave us a clear indication what changes we needed to achieve the most impact.
![Nextjs tree analyzer](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fnextjs-tree-analyzer.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
There are some great tools when it comes to Real User Monitoring (RUM). We chose the newly-launched [Sentry performance monitoring](https://sentry.io/for/performance/) product since we already use Sentry for error tracking and we wanted to minimize new tools in our stack. It also supports reporting [Core Web Vitals](https://web.dev/vitals/), the performance metrics created by Google to track initial loading performance, responsiveness and visual stability. Core Web Vitals come with recommended target values, giving us clear goals to hit.
![Core Web Vitals](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fcore-web-vitals.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Improving our JavaScript bundle size[#](https://supabase.com/blog/supabase-dashboard-performance#improving-our-javascript-bundle-size)
> How to not load the entire npm registry into our user's browsers
### Choosing smaller modules[#](https://supabase.com/blog/supabase-dashboard-performance#choosing-smaller-modules)
We used [Bundlephobia](https://bundlephobia.com/) on our largest modules. This is a great website to have in your JS-performance arsenal. It gives the size of npm modules across different versions and recommends alternate modules with similar functionality which are smaller.
`Moment.js` is notorious for its large bundle size and we don't need complex date processing for our dashboard. It was straightforward to switch to [day-js](https://day.js.org/) which is largely API-compatible with `Moment.js`. This change reduced our gzipped bundle size by 68 KB.
We migrated from `Joi` to `ajv` for our schema validation which was 32% smaller. `ajv` was already bundled as a transitive dependency of other modules, making it a no-brainer.
![NPM dependencies](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fnpm-dependencies.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We reverted our [crypto-js](https://github.com/brix/crypto-js) module from version 4.0 to 3.3.0. Version 4.0 [injects more than 400kb code](https://github.com/brix/crypto-js/issues/276) when used in a browser context. The newer version replaces `Math.random` with node's implementation, injecting the entire node crypto module into the browser context. We use `crypto-js` for decrypting user's API keys and so we're not reliant on the randomness of the PRNG. We might move to a dedicated module like [aes-js](https://www.npmjs.com/package/aes-js) in the future since it has a much smaller surface area than `crypto-js` (in terms of security and performance).
### Using partial imports[#](https://supabase.com/blog/supabase-dashboard-performance#using-partial-imports)
By selectively importing functions from modules like `lodash`, we cut the gzipped size by another 40kb across all our bundles.
`
1
// before
2
import _ from 'lodash'\n
3
// maunally cherry picking modules
4
import find from 'lodash/find'
5
import debounce from 'lodash/debounce'\n
6
// using babel-plugin-lodash
7
import { find, debounce } from 'lodash'
`
In the above example, we added [babel-plugin-lodash](https://github.com/lodash/babel-plugin-lodash) to our babel configuration which cherry picks the exact `lodash` functions we import. This makes it easier to import from `lodash` without cluttering the code with selective import statements.
### Moving complex logic to the server[#](https://supabase.com/blog/supabase-dashboard-performance#moving-complex-logic-to-the-server)
Thanks to some skilled haxors (well, weak passwords mainly) we had crypto miners running on some of our customer's databases. To prevent this, we enforce password strength with the [zxcvbn](https://github.com/dropbox/zxcvbn) module. Though it improved our overall security, the module is [pretty big](https://bundlephobia.com/result?p=zxcvbn@4.4.2), weighing in at 388kb gzipped. To get around this, we moved the password-strength checking logic to an API. Now, the frontend queries a server with a user-supplied password and the server computes its strength. This eliminates the module from the frontend.
### Lazy loading code[#](https://supabase.com/blog/supabase-dashboard-performance#lazy-loading-code)
[xlsx](https://github.com/SheetJS/sheetjs) is another complex and large module, which is used to import spreadsheets into tables. We contemplated moving this logic to the backend, but we found another solution: lazy loading it.
The spreadsheet import is triggered when the user is creating a new table. However the code was previously loaded every time the page was visited - even when a new table was not being created. This made it a good candidate for lazy loading. Using [Next.js dynamic imports](https://nextjs.org/docs/advanced-features/dynamic-import) we are able to load this component (313 kb brotlied) dynamically, whenever the user clicks the "Add content" button.
We use the same technique to lazy load some Lottie animations which are relatively large.
### Using native browser APIs[#](https://supabase.com/blog/supabase-dashboard-performance#using-native-browser-apis)
We decided against supporting IE11, opening up more avenues for optimization. Using native browser APIs enabled us to drop even more dependencies. For example, since the [fetch API is available](https://caniuse.com/fetch) in all the browsers we care about, we removed [axios](https://github.com/axios/axios) and built a simple wrapper using the native fetch API.
## Improving Vercel's default caching[#](https://supabase.com/blog/supabase-dashboard-performance#improving-vercels-default-caching)
> The fastest request is the request not made
We noticed that Vercel was sending a `Cache-Control` header of `public, max-age=0, must-revalidate` , preventing some of our SVG, CSS and font files from being cached in the browser.
We updated our `next.config.js` , adding a long `max-age` to the caching header that Vercel sends. Our assets are versioned properly, so we were able to safely do this.
## Enabling Next.js Automatic Static Optimization[#](https://supabase.com/blog/supabase-dashboard-performance#enabling-nextjs-automatic-static-optimization)
Next.js is able to automatically pre-render a page to HTML, whenever a page meets some pre-conditions. This mode is called [Automatic Static Optimization](https://nextjs.org/docs/advanced-features/automatic-static-optimization). Pre-rendered pages can be cached on a CDN for extremely fast page loads. We removed calls to `getServerSideProps` and `getInitialProps` to take advantage of this mode.
## Developing a performance culture[#](https://supabase.com/blog/supabase-dashboard-performance#developing-a-performance-culture)
> Always in sight, always in mind
Our performance optimization journey will never be complete. It requires constant vigilance to maintain a baseline across our users. To instill this within our team, we took a few actions.
We developed a Slack bot which sends our Sentry performance dashboard every week, containing our slowest transactions and our Core Web Vitals summary. This shows which pages need improvement and where our [users are the most miserable](https://docs.sentry.io/product/performance/metrics/#user-misery).
During our transition from Alpha to Beta, performance was one of the important features, along with stability and security. We considered performance implications while choosing libraries and tools. Having a "seat at the table" in these discussions ensures that performance is not considered as an after-thought.
## Results[#](https://supabase.com/blog/supabase-dashboard-performance#results)
With these changes, we have a respectable Core Web Vitals score. This is a snapshot from Sentry with RUM data from the last week. We are within the recommended threshold for all the 3 Web Vitals.
![Sentry results](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fsentry-results.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Our Next.js build output also shows that users download < 200 kb of JavaScript between any two page transitions. We're still improving too - even though we provide a lot of functionality in our dashboard, we will continue to reduce our bundle sizes.
## Things that did not work[#](https://supabase.com/blog/supabase-dashboard-performance#things-that-did-not-work)
> You win some, you lose some
We tried a VSCode plugin called [Import cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) which shows the size of JavaScript modules when you import it in your editor. However, the plugin did not work on our codebase since it doesn't support some JavaScript features, like optional chaining.
We also passed on using [lodash-webpack-plugin](https://www.npmjs.com/package/lodash-webpack-plugin) even though it had the potential to reduce our JavaScript sizes, because it could potentially break our code if not used carefully. This plugin would require our frontend team to understand the Webpack configuration, updating it whenever they use a new lodash feature set.
## The road ahead[#](https://supabase.com/blog/supabase-dashboard-performance#the-road-ahead)
Our broad goal is to implement best practices for frontend performance, and make it exciting to all of our team. These are some ideas we have on our roadmap -
  * Set up [Lighthouse](https://developers.google.com/web/tools/lighthouse) in a GitHub Action to catch performance regression earlier in the development life cycle.
  * Continue reducing our initial JavaScript payload size, to improve our LCP time
  * Explore `cloud-mode` in [Segment](https://segment.com/docs/connections/destinations/) which makes API calls from the server instead of loading third-party library on the browser.


Reach out to us on [Twitter](https://twitter.com/supabase) if you have more ideas to speed up our website ⚡
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-dashboard-performance&text=Making%20the%20Supabase%20Dashboard%20Supa-fast)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-dashboard-performance&text=Making%20the%20Supabase%20Dashboard%20Supa-fast)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-dashboard-performance&t=Making%20the%20Supabase%20Dashboard%20Supa-fast)
[Last postSupabase Beta December 20202 January 2021](https://supabase.com/blog/supabase-beta-december-2020)
[Next postMonitoro Built a Web Crawler Handling Millions of API Requests2 December 2020](https://supabase.com/blog/case-study-monitoro)
[supabase](https://supabase.com/blog/tags/supabase)
On this page
  * [Establishing a baseline and setting targets](https://supabase.com/blog/supabase-dashboard-performance#establishing-a-baseline-and-setting-targets)
  * [Improving our JavaScript bundle size](https://supabase.com/blog/supabase-dashboard-performance#improving-our-javascript-bundle-size)
  * [Improving Vercel's default caching](https://supabase.com/blog/supabase-dashboard-performance#improving-vercels-default-caching)
  * [Enabling Next.js Automatic Static Optimization](https://supabase.com/blog/supabase-dashboard-performance#enabling-nextjs-automatic-static-optimization)
  * [Developing a performance culture](https://supabase.com/blog/supabase-dashboard-performance#developing-a-performance-culture)
  * [Results](https://supabase.com/blog/supabase-dashboard-performance#results)
  * [Things that did not work](https://supabase.com/blog/supabase-dashboard-performance#things-that-did-not-work)
  * [The road ahead](https://supabase.com/blog/supabase-dashboard-performance#the-road-ahead)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-dashboard-performance&text=Making%20the%20Supabase%20Dashboard%20Supa-fast)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-dashboard-performance&text=Making%20the%20Supabase%20Dashboard%20Supa-fast)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-dashboard-performance&t=Making%20the%20Supabase%20Dashboard%20Supa-fast)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

