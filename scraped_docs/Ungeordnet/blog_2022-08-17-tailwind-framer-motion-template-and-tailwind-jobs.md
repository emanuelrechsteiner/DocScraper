---
url: https://tailwindcss.com/blog/2022-08-17-tailwind-framer-motion-template-and-tailwind-jobs
scraped_at: 2025-05-25T08:32:01.122211
title: New Tailwind CSS + Framer Motion template and Tailwind Jobs - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
August 19, 2022
# New Tailwind CSS + Framer Motion template and Tailwind Jobs
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
Got another update for you today on some cool things we've shipped, and some other things that are in the works but shipping soon!
Since the [Tailwind UI site templates and all-access](https://tailwindcss.com/blog/2022-06-23-tailwind-templates-and-all-access) release back in June we've been doing a lot of maintenance-focused stuff, like processing [over 350 GitHub issues and pull requests](https://github.com/search?q=is%3Aclosed+org%3Atailwindlabs+archived%3Afalse+sort%3Acreated-desc+is%3Apublic+closed%3A%3E%3D2022-06-23+-author%3Aapp%2Fdependabot+-author%3Aapp%2Fgithub-actions+-author%3Aapp%2Fdepfu&type=Issues) and updating all of the new templates we released to use [Next.js 12.2](https://nextjs.org/blog/next-12-2) and the new [`next/future/image`](https://nextjs.org/docs/app/api-reference/next-config-js/images) component.
We did find time to ship a few new things in there too though!
## [Tailwind + Framer Motion = Pocket](https://tailwindcss.com/blog/2022-08-17-tailwind-framer-motion-template-and-tailwind-jobs#tailwind-framer-motion-pocket)
About a week ago we shipped a brand new Tailwind UI template, built with Next.js and (of course) Tailwind CSS.
We're calling it [Pocket](https://tailwindui.com/templates/pocket), and it's a mobile app landing page loaded with tons of fun animations and interactions, powered by [Framer Motion](https://www.framer.com/motion/) which is basically the coolest library anyone has ever made.
[![Learn about the Pocket template](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpocket-preview.0125ad4d.png&w=3840&q=75)](https://tailwindui.com/templates/pocket)
Be sure to check out [the live preview](https://pocket.tailwindui.com/) for the full experience — screenshots miss all the coolest parts, like the graph that draws in on page load, the animated mobile device UI in the features section, and the Frogger-inspired testimonials animation.
Funny story about this template — when we initially designed it and built it we actually didn't plan to do anything in terms of animations or interactions. We put together a static design in Figma that we were all really excited about, then built the whole thing out with a plan to ship it like three and a half weeks ago.
But once we had the finished template in the browser it just kinda felt stiff. It looked great in Figma where you sort of expect everything to be still and static, but once we could see it in real life it felt more like a screenshot or something instead of a real, interactive website.
Take a look at [this earlier version of the template](https://tailwindui-template-wip-saas-02-7i25puvq2-tailwindlabs.vercel.app/) and maybe you'll see what I mean.
We decided to delay the release for a couple of weeks while we experimented with some things we could do to breathe some life into it, and after trying a bunch of different ideas ended up with what we have today.
I'm super stoked about how this one turned out, and I think the codebase is a really interesting case study to pour over if you want to learn how to use Framer Motion to pull off some of the cool effects we landed on.
And like all of our templates, if you've got a [Tailwind UI all-access](https://tailwindui.com/all-access) license, it's included alongside all of our other components and templates at no extra cost.
## [Tailwind Jobs](https://tailwindcss.com/blog/2022-08-17-tailwind-framer-motion-template-and-tailwind-jobs#tailwind-jobs)
We've tossed around the idea of building an official Tailwind CSS job board for about two years, and finally made the decision in the last few weeks to give it a shot and see what happens.
If you're a company that uses Tailwind and are looking for front-end engineers or you're a developer who wants to work at a company that uses Tailwind, [check out Tailwind Jobs](https://jobs.tailwindcss.com/) to learn more about it.
[![Tailwind Jobs](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftailwind-jobs.3539bfbe.jpg&w=3840&q=75)](https://jobs.tailwindcss.com)
We broke ground on the codebase on July 14th, and launched the site to companies on August 2nd. We built it with [Laravel](https://laravel.com/), [Inertia](https://inertiajs.com/), [React](https://reactjs.org/), and of course Tailwind CSS. Pretty amazing what you can build with tools like these in just 20 days!
We're still figuring out the positioning and what we can do to make it _the best_ place for companies using Tailwind to find front-end talent, so if you do any hiring at your company and have any feedback or ideas, shoot Peter an email — he's taking the lead on this project and is looking for people to talk to about it.
One thing we're trying to figure out for example is how to make it clear that jobs don't have to be strictly "styling things with Tailwind CSS all day" to be a good fit — there's really not a lot of jobs like that in the world, we don't even have any jobs like that here at the company that actually _makes_ Tailwind CSS itself!
But man a lot of people hate wrestling with CSS, even if they're not writing it every single day.
There's ton of developers out there who would be ecstatic to know that whenever they _do_ have to do some styling, they'll get do it with Tailwind instead of some custom CSS spaghetti.
We want the job board to be a place to find React developers, Vue developers, Laravel developers, Rails developers, whatever — as long as the person would get to use Tailwind when it's time to style something, it's a good fit for Tailwind Jobs.
## [Work in progress...](https://tailwindcss.com/blog/2022-08-17-tailwind-framer-motion-template-and-tailwind-jobs#work-in-progress)
We've got a bunch of cool stuff in the works that will be coming out in the next few weeks:
  * We've almost finished [Heroicons v2.0](https://twitter.com/steveschoger/status/1559622409136873473), with a [new website](https://twitter.com/jamesm/status/1556957434194829314) to go along with it
  * There's a damn beautiful [personal website template](https://twitter.com/jamesm/status/1560289211424595973) coming soon to Tailwind UI
  * [Headless UI v1.7](https://github.com/tailwindlabs/headlessui/blob/main/packages/@headlessui-react/CHANGELOG.md#unreleased) is almost ready for release
  * We've got a bunch of new components designed for Tailwind UI that we're going to start building next week


So look for another update in a couple weeks with a bunch more stuff! With the big templates/all-access release behind us I'm excited to switch gears from creating brand new products and spend the rest of the year focused on making Tailwind CSS and Headless UI even better, and adding tons of awesome new stuff to Tailwind UI.
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

