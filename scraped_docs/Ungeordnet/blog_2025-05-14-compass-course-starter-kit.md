---
url: https://tailwindcss.com/blog/2025-05-14-compass-course-starter-kit
scraped_at: 2025-05-25T08:29:22.655986
title: Compass: A starter kit for online courses - Tailwind CSS
---

[](https://tailwindcss.com/)v4.1
`⌘K``Ctrl K`[Docs](https://tailwindcss.com/docs)[Blog](https://tailwindcss.com/blog)[Showcase](https://tailwindcss.com/showcase)[Plus](https://tailwindcss.com/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)
May 14, 2025
# Compass: A starter kit for online courses
![](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fadamwathan.f69b0b90.jpg&w=96&q=75)
Adam Wathan
[@adamwathan](https://twitter.com/adamwathan)
I've been itching to get back into screencasting and teaching lately, so a couple of months ago I put together this free [Build UIs that don't suck](https://tailwindcss.com/build-uis-that-dont-suck) mini-course. People seemed to like it and now I want to do some bigger video projects, but there was a problem.
I am a software developer.
And as a software developer, much like I need to write my own static site generator before I can build my own personal website, I needed to build my own course platform before I could even think about putting together a video course.
Well fast-forward six weeks later and we just released [Compass](https://tailwindcss.com/plus/templates/compass), a starter kit we designed with Tailwind CSS and Next.js for publishing your own online course.
[![Compass](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpreview-01.20486579.jpg&w=3840&q=75)](https://tailwindcss.com/plus/templates/compass)
Check out the [live preview](https://tailwindcss.com/plus/templates/compass/preview) as always for the full experience.
We had a lot of fun working on this one, and got to play with a bunch of new tools and technologies and solve some interesting problems.
## [Picture-in-picture video](https://tailwindcss.com/blog/2025-05-14-compass-course-starter-kit#picture-in-picture-video)
You might not have seen it before but most modern browsers have [native Picture-in-Picture support](https://developer.mozilla.org/en-US/docs/Web/API/Picture-in-Picture_API). These APIs let you take a video and pop it out into a separate window that the user can move around and resize while still browsing the site.
We had this idea for Compass where if you started to play a course video and scrolled down the page, the video would move to the bottom right of the screen so you could still watch it while reading the page content.
We were hoping to use the Picture-in-Picture APIs for this, but it turns out you can't passively trigger them on scroll _(for privacy/security reasons I guess?)_ — the user has to actually click something, similar to the clipboard APIs.
We ended up rolling our own simple thing instead, using [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API), video events, and a bit of state to detect when the video was playing and offscreen, and added data attributes to the `<video>` element to so we could target them with utility classes:
video-player.tsx
```
<video data-offscreen={isOffscreen ? "" : undefined} data-playing={isPlaying ? "" : undefined} className="data-offscreen:data-playing:fixeddata-offscreen:data-playing:right-4data-offscreen:data-playing:bottom-4"/>
```

I love using data attributes for this sort of thing, find the code reads a lot more like standard Tailwind stuff compared to a bunch of ternaries and conditional logic in JavaScript.
## [Parsing VTT files into transcripts](https://tailwindcss.com/blog/2025-05-14-compass-course-starter-kit#parsing-vtt-files-into-transcripts)
There's a section in Compass for interviews, which each include a video at the top of the page but also a pretty custom transcript UI below:
![Stylized transcript of an interview between Tom Harris and Annie King](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftranscript.f0edcebf.png&w=3840&q=75)
At first we weren't totally sure how we should approach this. Our first idea was to just write some React components for these pieces and throw the content directly into an MDX file, but it felt sort of unrealistic to expect anyone to ever author their transcripts in this totally custom format.
Then I had the idea to use a standard caption file format, like [SRT](https://en.wikipedia.org/wiki/SubRip). The problem was that for our needs, we needed to encode the current speaker (Tom or Annie in the screenshot above), and SRT has no standardized way of encoding that information in the file.
I did some more research and eventually landed on [WebVTT](https://en.wikipedia.org/wiki/WebVTT), which is similar to SRT but does support speaker information, and is conveniently designed for the web.
annie-king.vtt
```
WEBVTT00:00.000 --> 00:20.000<v Tom Harris>Hello fellow passengers, welcome to the Compass podcast. Today, we have a special guest, Annie King. She's the author of The Inevitable You: How to Embrace Your Path and Succeed with Relentless Precision. Annie, welcome to the show.00:20.000 --> 00:35.000<v Annie King>Thank you! I'm so happy to be here. And thanks for sending me the questions in advance — I'm really excited to share some of the ideas from the book with your viewers. I think we're going to have a lot of fun unpacking what it means to truly embrace your path.00:35.000 --> 00:45.000<v Tom Harris>Absolutely! I want to get into your book, but first I have to ask — what was it like growing up in a household that treated organization almost like...a sport?
```

So we wired things up to parse the transcript data from a `.vtt` file, and then map over that data to render it as a custom UI with React:
src/interview/[slug]/page.tsx
```
<div> {transcript.map(({ start, speaker, text }) => (  <div key={start} className="col-span-2 grid grid-cols-subgrid items-baseline">   <TimestampButton start={start} videoId="video" className="justify-self-end" />   <div>    <p className="text-sm/7 font-semibold text-gray-950 dark:text-white">{speaker}</p>    {text.map((p, index) => (     <p key={index} className="mt-2 text-sm/7 whitespace-pre-wrap text-gray-700 dark:text-gray-400">      {p}     </p>    ))}   </div>  </div> ))}</div>
```

Turned out pretty cool — I can imagine someone just generating a transcript in VTT format using AI, throwing it into the project and it'll automatically be rendered in a nice custom UI.
## [Extending Markdown images for dark mode and layout shift](https://tailwindcss.com/blog/2025-05-14-compass-course-starter-kit#extending-markdown-images-for-dark-mode-and-layout-shift)
The example content we came up with for Compass includes a lot of diagrams that we wanted to adapt between light and dark mode.
![Example of a diagram that uses different colors for light and dark mode](https://tailwindcss.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flight-dark-diagram.206982cb.png&w=3840&q=75)
You can do this sort of thing a ton of different ways (the `<picture>` tag supports it natively for example), but we really wanted to keep the content files feeling as much like vanilla Markdown as possible.
So we came up with this idea of a `{scheme}` placeholder in the image URL that we replace with `light` or `dark` dynamically, loading the correct image based on the user's color scheme:
```
## The Myth of Free Will![Neurological Proof](/img/neuro-proof.{scheme}.png)Your brain makes decisions before you are even aware of them.
```

Now the underlying image component will automatically render `neuro-proof.light.png` or `neuro-proof.dark.png` depending on the current color scheme. And if you just want to use the same image in both, just don't include `{scheme}` in the URL at all.
We also wanted to avoid layout shift in the content, which you can do pretty easily these days by ensuring you give your images `width` and `height` attributes so the browser can compute the aspect ratio and reserve space for the image when it loads.
There's no standard way to express this in Markdown's image syntax, but after a bit of research we discovered some precedent in [Obsidian](https://help.obsidian.md/syntax#External+images).
Obsidian tacks the image dimensions on to the alt text, like this:
```
## The Myth of Free Will![Neurological Proof|2000x990](/img/neuro-proof.{scheme}.png)Your brain makes decisions before you are even aware of them.
```

So we used a custom MDX component to pull out the dimensions using the same format, and add those to the image to make sure there's no layout shift as the content loads.
So there you go — that's Compass! As always it's a free update for anyone with a [Tailwind Plus](https://tailwindcss.com/plus) license, so go and [download the codebase](https://tailwindcss.com/plus/templates/compass), poke around, and have fun with it.
If you don't already have a Tailwind Plus license, think about getting one! Picking one up is the best way to support our work on Tailwind CSS and there's a ton of useful stuff in there.
Looking forward to using this template for some upcoming projects myself in the next couple of months!
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

