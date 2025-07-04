---
url: https://tailwindcss.com/blog/standalone-cli
scraped_at: 2025-05-25T08:42:06.094213
title: Standalone CLI: Use Tailwind CSS without Node.js - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
December 16, 2021
# Standalone CLI: Use Tailwind CSS without Node.js
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
Tailwind CSS is written in JavaScript and distributed as an npm package, which means you've always had to have Node.js and npm installed to use it.
This has made it harder to integrate into projects where using npm isn't always common, and with tools like [Rails](https://world.hey.com/dhh/rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b) and [Phoenix](https://github.com/phoenixframework/phoenix/pull/4377) both moving away from npm by default, we needed to find a way for people to use Tailwind in these projects without forcing them to adopt an entirely separate ecosystem of tooling.
Today we're announcing a new [standalone CLI build](https://github.com/tailwindlabs/tailwindcss/releases/latest) that gives you the full power of Tailwind CLI in a self-contained executable — no Node.js or npm required.
## [Get started](https://tailwindcss.com/blog/standalone-cli#get-started)
To install it, grab the executable for your platform from the [latest release](https://github.com/tailwindlabs/tailwindcss/releases/latest) on GitHub, making sure to give it executable permissions:
```
# Example for macOS arm64curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64chmod +x tailwindcss-macos-arm64mv tailwindcss-macos-arm64 tailwindcss
```

Now you can use it just like our npm-distributed CLI tool:
```
# Create a tailwind.config.js file./tailwindcss init# Start a watcher./tailwindcss -i input.css -o output.css --watch# Compile and minify your CSS for production./tailwindcss -i input.css -o output.css --minify
```

We've even bundled the latest versions of all of our first-party plugins, so if you want to use them in your project, just `require` them in your `tailwind.config.js` file like you would in a Node-based project:
```
module.exports = { // ... plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],};
```

You get all the power of our standard npm-distributed CLI in a convenient, portable package — no dependencies required.
## [How does it work?](https://tailwindcss.com/blog/standalone-cli#how-does-it-work)
We didn't rewrite Tailwind in Rust or anything ([yet...](https://twitter.com/malfaitrobin/status/1446905317825069063)) — we're actually using [pkg](https://github.com/vercel/pkg), a really cool project by [Vercel](https://vercel.com) that lets you turn a Node.js project into an executable that can be run without installing Node.js by bundling all of the parts your project needs right into the executable itself.
This is what makes it possible for you to still use a `tailwind.config.js` file with the full power of JavaScript, rather than a static format like JSON.
## [Which CLI should I use?](https://tailwindcss.com/blog/standalone-cli#which-cli-should-i-use)
If you are already using npm in your project, use the npm-distributed version of our CLI that we've always provided. It's simpler to update, the file size is smaller, and you're already in the ecosystem anyways — there's no benefit at all to using the standalone build.
If on the other hand you're working on a project where you don't otherwise need Node.js or npm, the standalone build can be a great choice. If Tailwind was the only reason you had a `package.json` file, this is probably going to feel like a nicer solution.
## Get all of our updates directly to your inbox.Sign up for our newsletter.
Subscribe
### Learn
  * [Documentation](https://tailwindcss.com/docs)
  * [Showcase](https://tailwindcss.com/showcase)
  * [Blog](https://tailwindcss.com/blog)
  * [Playground](https://play.tailwindcss.com/)


### Resources
  * [Refactoring UI](https://www.refactoringui.com)
  * [Headless UI](https://headlessui.com)
  * [Heroicons](https://heroicons.com)
  * [Hero Patterns](https://heropatterns.com)


### [Tailwind Plus](https://tailwindcss.com/plus?ref=footer)
  * [UI Blocks](https://tailwindcss.com/plus/ui-blocks?ref=footer)
  * [Templates](https://tailwindcss.com/plus/templates?ref=footer)
  * [UI Kit](https://tailwindcss.com/plus/ui-kit?ref=footer)


### Community
  * [GitHub](https://github.com/tailwindlabs/tailwindcss)
  * [Discord](https://tailwindcss.com/discord)
  * [X](https://x.com/tailwindcss)


### Learn
  * [Documentation](https://tailwindcss.com/docs)
  * [Showcase](https://tailwindcss.com/showcase)
  * [Blog](https://tailwindcss.com/blog)
  * [Playground](https://play.tailwindcss.com/)


### [Tailwind Plus](https://tailwindcss.com/plus?ref=footer)
  * [UI Blocks](https://tailwindcss.com/plus/ui-blocks?ref=footer)
  * [Templates](https://tailwindcss.com/plus/templates?ref=footer)
  * [UI Kit](https://tailwindcss.com/plus/ui-kit?ref=footer)


### Resources
  * [Refactoring UI](https://www.refactoringui.com)
  * [Headless UI](https://headlessui.com)
  * [Heroicons](https://heroicons.com)
  * [Hero Patterns](https://heropatterns.com)


### Community
  * [GitHub](https://github.com/tailwindlabs/tailwindcss)
  * [Discord](https://tailwindcss.com/discord)
  * [X](https://x.com/tailwindcss)


Copyright © 2025 Tailwind Labs Inc.·[Trademark Policy](https://tailwindcss.com/brand)

