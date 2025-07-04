---
url: https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber
scraped_at: 2025-05-25T09:01:32.496520
title: Coding the stars - an interactive constellation with Three.js and React Three Fiber
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
# Coding the stars - an interactive constellation with Three.js and React Three Fiber
04 Aug 2023
•
16 minute read
[![Francesco Sansalvadore avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffsansalvadore.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Francesco SansalvadoreEngineering](https://github.com/fsansalvadore)
![Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-constellation-breakdown-og.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Every Launch Week is an opportunity for Supabase to experiment, try some spicy new designs, and dogfood our own technology. During our previous Launch Week we [took Generative AI for a spin](https://supabase.com/blog/designing-with-ai-midjourney). This time we decided to shoot for the stars.
For [Launch Week 8](https://supabase.com/launch-week/), we wanted to make the user-generated tickets a central piece of the launch week theme. To do this, we built a “constellation” of stars - an animated night sky where every user signup was represented as a star, in the form of an “8” shape.
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-early-design.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Early design
We could approach this animation in a few ways.
For example, animating the `stroke-dashoffset` on an SVG path, similar to [this ](https://css-tricks.com/svg-line-animation-works/) example, was a good option, but it would have been difficult to randomize and change the shape at a later stage. Other approaches included 2D animation libraries, like [Framer Motion ](https://www.framer.com/motion/animation/), [gsap ](https://greensock.com/gsap/) or [PixiJS ](https://pixijs.com/).
Ultimately we decided to take [Three.js ](https://threejs.org/) for a spin using [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/getting-started/introduction) (R3F) giving us a more powerful toolset to enable us to achieve the best possible result.
Learning Three.js is not a walk in the park but R3F abstracted many of its complexities such as cameras and renderers, to name a few. If you're new to R3F, some of the core primitives they provide for a basic scene include:
  * `Geometries`: used to create and define shapes
  * `Materials`: manage the texture and color of objects
  * `Mesh`: used to instantiate polygonal objects by combining a Geometry with a Material
  * `Lights`: to shine bright like a diamond 💎🎵
  * `Canvas`: where you define your R3F Scene


If you want to dive a little deeper, here are a few good resources we found to get a solid grasp on the topic:
  * [I wish I knew this before using React Three Fiber ](https://www.youtube.com/watch?v=DPl34H2ISsk) - from our very own [Greg ](https://twitter.com/ggrdson)
  * [Three.js Journey ](https://threejs-journey.com/) - by [Bruno Simon ](https://bruno-simon.com/)


## Setting up the scene[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#setting-up-the-scene)
In this article, we’re going to break down the steps to reproduce the Launch Week 8 animation using React Three Fiber in NextJs.
These are the dependencies we’ll need:
`
1
npm install three @react-three/fiber
`
If you’re using React 17, we’ll spare you the trouble of finding the last compatible R3F version:
`
1
npm install three @react-three/fiber@7.0.29
`
All we need for each particle is a circle geometry with a minimal amount of sides to minimize complexity.
`
1
import { useMemo } from 'react'
23
const Geometry = useMemo(() => () => <circleGeometry args={[1.5, 5]} />, [])
`
A basic standard material with a white color will do just fine. Using the AdditiveBlending module from `three` provides a more interesting touch when particles happen to overlap, making them shine brighter:
`
1
import { AdditiveBlending } from 'three'
23
const Material = () =>
4
 useMemo(() => <meshStandardMaterial color="#ffffff" blending={AdditiveBlending} />, [])
`
Let’s put it together in an R3F `Canvas` element and wrap up the initial setup with an `ambientLight`, which will make objects visible, just as real light does:
`
1
import { useMemo } from 'react'
2
import { Canvas } from '@react-three/fiber'
3
import { AdditiveBlending } from 'three'
45
const Geometry = useMemo(
6
  () => () => <circleGeometry args={[1.5, 5]} />,
7
  []
8
 )
910
const Material = () =>
11
  useMemo(
12
   () => (
13
    <meshStandardMaterial
14
     color="#ffffff"
15
     blending={AdditiveBlending}
16
    />
17
   ),
18
   []
19
  )
2021
return (
22
 <div style={{ width: 100vw, height: 100vh, background: "#000000" }}>
23
  <Canvas
24
   dpr={[1, 2]}
25
   camera={{ fov: 75, position: [0, 0, 500] }}
26
  >
27
   <ambientLight intensity={0.3} />
28
   <group>
29
    {particles?.map((particle, index) => (
30
     <mesh
31
      key={particle.username}
32
     >
33
      <Geometry />
34
      <Material />
35
     </mesh>
36
    ))}
37
   </group>
38
  </Canvas>
39
 </div>
40
)
`
For more context, the `dpr` values help with pixelation issues and the `camera` [0, 0, 500] position means that the camera is moved 500 units back in the z-axis to actually see the center [0,0,0] of the scene.
One thing to note is that the R3F Canvas renders a transparent background, so in order to see the white particle, we need to set the background of the parent html element to a dark color.
We created a separate component for the Particle, which will later encapsulate the animation logic.
`
1
import React, { useRef } from 'react'
23
const Particle = ({ children }) => {
4
 const particle = useRef(null)
56
 return <mesh ref={particle}>{children}</mesh>
7
}
89
export default Particle
`
## Load users from Supabase[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#load-users-from-supabase)
You might have noticed we haven’t instantiated the particles yet. As we mentioned earlier, we wanted each particle to represent a ticket generated by a user and stored in the database. Let’s fetch the signups from the `tickets` table in our Supabase project (you might need to start your own Launch Week to fill your table):
`
1
const [particles, setParticles] = useState([])
23
const loadUsers = async () => {
4
 return await supabase.from('lw8_tickets').select('*')
5
}
67
useEffect(() => {
8
 const { data: users } = loadUsers()
9
 setParticles(users)
10
}, [])
`
We updated the constellation in [realtime](https://supabase.com/realtime) whenever a new ticket was generated, but we’ll skip over this part to keep the article shorter. Since it’s all open-source, you can dive deeper [here ](https://github.com/supabase/supabase/pull/16022/files#diff-e3298724d8ca571c732651658e388d70cafd90c4ceea99be8e5e7529ebb73a56R17-R52) if you wish.
## Animating the particles[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#animating-the-particles)
To move the particle around the screen we are going to leverage a few different concepts: _useFrame_ and _trigonometry_ 🤯
### useFrame[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#useframe)
Generally, the most optimal way to animate things in a browser viewport, using javascript, is by leveraging a method called [requestAnimationFrame ](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame), which _“tells the browser that you wish to perform an animation and requests that the browser calls a specified function to update an animation right before the next repaint.”_. R3F has a similar hook called [useFrame ](https://docs.pmnd.rs/react-three-fiber/tutorials/basic-animations) that lets you execute code on every frame of Fiber's render loop. We’ll use this to change the position of the particles over time in a few moments.
### Using time as an animation variable[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#using-time-as-an-animation-variable)
We can extract time information from the useFrame `clock` parameter, to know how much time has elapsed in our application, and use that time to animate a value. Updating the `x` position with Math.sin() generates a horizontal oscillating movement. Multiply it with a `widthRadius` variable to customize the amplitude of the movement.
`
1
const particle = useRef(null)
23
const widthRadius = 100
4
const heightRadius = 100
56
useFrame(({ clock }) => {
7
  const timer = clock.getElapsedTime()
89
  particle.current.position.x = Math.sin(timer) * widthRadius
10
 }
11
})
1213
return <mesh ref={particle}>{children}</mesh>
`
![01-x-sine.gif](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2F01-x-sine.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Combine the previous horizontal movement with a `Math.cos()` on the `y` position to [draw a circle](https://en.wikipedia.org/wiki/Sine_and_cosine):
`
1
particle.current.position.y = Math.cos(timer) * heightRadius
`
![02-circle.gif](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2F02-circle.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Calculating the circumference we can get the time the x position takes to complete a full circle.
`
1
const circumference = (config.widthRadius * Math.PI * 2) / 100
`
When that happens, we can invert the cos sign on every other loop to obtain a basic 8 shape.
`
1
const isEven = Math.floor(timer / circumference) % 2 == 0
23
particle.current.position.x = Math.sin(timer) * widthRadius
4
particle.current.position.y = isEven
5
 ? Math.cos(timer) * heightRadius - heightRadius
6
 : -Math.cos(timer) * heightRadius + heightRadius
`
![03-eight.gif](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2F03-eight.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
At this point, we played around with a number of parameters that made the animation more randomized and interesting.
For example, we randomized the speed and the delay of each particle:
`
1
const minSpeed = -0.3
2
const maxSpeed = 0.4
3
const speed = Math.random() * (minSpeed - maxSpeed) + maxSpeed
45
const delayOffsetFactor = 100
6
const delayOffset = Math.random() * delayOffsetFactor
78
[...]
910
const timer = clock.getElapsedTime() *** speed + delayOffset**
`
We offset the shape on the x-axis, to concentrate most of the particles in the core of the 8 shape and leave a smaller amount externally, by playing around with exponentials using Math.pow() in combination with some more randomization.
`
1
const xThickness = 7
2
const xRandomnessShape = 2.2
3
const xRandomness = 5
45
const pathOffset =
6
  Math.pow(
7
   Math.random() * xRandomnessShape,
8
   xRandomness - xRandomness / 2
9
  ) * xThickness
1011
...
1213
particle.current.position.x = Math.sin(timer) * widthRadius + pathOffset
`
Honestly, this was the result of a lot of playing and tweaking around, and we certainly didn’t hit the best possible result on the first try. Perhaps you want to take some time to experiment with the math - you might find even better and more configurable results.
## GUI playground[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#gui-playground)
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-constellation-gui-demo.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
What really helped to visualize the shape, gather feedback, and decide on a final design was adding a GUI to play around with the values. You can try for yourself by appending `#debug` to the [supabase.com/launch-week#debu](http://supabase.com/launch-week#debug)[g](http://supabase.com/launch-weekdebug) url. Go crazy with it.
We used the [dat.gui ](https://github.com/dataarts/dat.gui) library:
`
1
npm install dat.gui@0.7.9
`
Which needs to be loaded asynchronously, otherwise it raises a `window is not defined` error.
`
1
const init = async () => {
2
 const dat = await import('dat.gui')
3
 const gui = new dat.GUI()
4
}
56
useEffect(() => {
7
 init()
8
}, [])
`
Then we prepared a `useParticlesConfig` hook with all the configuration wired up to the GUI. Whenever the GUI updated, we also updated react state.
`
1
import { useEffect, useState } from 'react'
2
import { range } from 'lodash'
34
let defaultConfig = {
5
 particles: 1500,
6
 widthRadius: 100,
7
 topHeightRadius: 80,
8
 bottomHeightRadius: 100,
9
 xThickness: 7,
10
 xRandomnessFactor: 2.2,
11
 xRandomnessShape: 2.2,
12
 xRandomness: 5,
13
 yThickness: 20,
14
 max_speed: 0.1,
15
 min_speed: -0.1,
16
}
1718
const useParticlesConfig = (): any => {
19
 if (typeof window === 'undefined') return null
20
 const hash = window.location.hash
21
 const isDebugMode = hash.includes('#debug')
22
 const [particles, setParticles] = useState(range(0, defaultConfig.particles))
2324
 const [config, setConfig] = useState(defaultConfig)
2526
 const handleSetConfig = (name, value) => {
27
  setConfig((prevConfig) => ({ ...prevConfig, [name]: value }))
28
 }
2930
 const init = async () => {
31
  if (!isDebugMode) return
32
  const dat = await import('dat.gui')
33
  const gui = new dat.GUI()
34
  const particlesFolder = gui.addFolder('Particles')
35
  const shapeFolder = gui.addFolder('Shape')
3637
  particlesFolder
38
   .add(config, 'particles')
39
   .min(1)
40
   .max(5000)
41
   .step(1)
42
   .onChange((value) => {
43
    handleSetConfig('particles', value)
44
    setParticles(range(0, value))
45
   })
46
  shapeFolder
47
   .add(config, 'widthRadius')
48
   .min(1)
49
   .max(200)
50
   .step(1)
51
   .onChange((value) => handleSetConfig('widthRadius', value))
5253
  // add desired folders and parameters
5455
  particlesFolder.open()
56
  shapeFolder.open()
57
 }
5859
 useEffect(() => {
60
  init()
61
 }, [])
6263
 return { config, handleSetConfig, particles, setParticles, isDebugMode }
64
}
6566
export default useParticlesConfig
`
Here is the final code:
`
1
import React, { useMemo, useEffect, useState } from 'react'
2
import { Canvas, useFrame } from '@react-three/fiber'
3
import { AdditiveBlending } from 'three'
4
import useParticlesConfig from './hooks/useParticlesConfig'
56
const ParticlesCanvas = () => {
7
 if (typeof window === 'undefined') return null
8
 const { config, particles } = useParticlesConfig()
910
 const Geometry = useMemo(
11
  () => () => <circleGeometry args={[config.particlesSize, config.particlesSides]} />,
12
  []
13
 )
1415
 const Material = () =>
16
  useMemo(
17
   () => (
18
    <meshStandardMaterial
19
     color={config.color}
20
     blending={config.particlesBlending ? AdditiveBlending : undefined}
21
    />
22
   ),
23
   []
24
  )
2526
 return (
27
  <div style={{ width: 100vw, height: 100vh, background: "#000000" }}>
28
   <Canvas
29
    dpr={[1, 2]}
30
    camera={{ fov: 75, position: [0, 0, 500] }}
31
   >
32
    <ambientLight intensity={config.lightIntensity} />
33
    <group>
34
     {particles?.map((particle, index) => (
35
      <Particle
36
       key={particle.username}
37
      >
38
       <Geometry />
39
       <Material />
40
      </Particle>
41
     ))}
42
    </group>
43
   </Canvas>
44
  </div>
45
 )
46
}
4748
const Particle = ({ children }: Props) => {
49
 const particle = useRef(null)
5051
 const pathOffset =
52
  Math.pow(
53
   Math.random() * config.xRandomnessShape,
54
   config.xRandomness - config.xRandomness / 2
55
  ) * config.xThickness
5657
 const verticalRandomness = Math.random() * (config.yThickness - 1) + 1 - config.yThickness / 2
5859
 const speed = Math.random() * (config.min_speed - config.max_speed) + config.max_speed
6061
 const circumference = (config.widthRadius * Math.PI * 2) / 100
62
 const delayOffsetFactor = 100
63
 const delayOffset = Math.random() * delayOffsetFactor
6465
 useFrame(({ clock }) => {
66
  const timer = clock.getElapsedTime() * speed + delayOffset
67
  const isEven = Math.floor(timer / circumference) % 2 == 0
6869
		// When the loop count is even, draw bottom 8 shape
70
  // if odd, draw top 8 shape
71
  particle.current.position.x = isEven
72
   ? Math.sin(timer) * config.widthRadius * config.widthRatio + pathOffset
73
   : Math.sin(timer) * config.widthRadius + pathOffset
74
  particle.current.position.y = isEven
75
   ? Math.cos(timer) * config.bottomHeightRadius -
76
    config.bottomHeightRadius +
77
    verticalRandomness
78
   : -Math.cos(timer) * config.topHeightRadius + config.topHeightRadius + verticalRandomness
79
 })
8081
 return <mesh ref={particle}>{children}</mesh>
82
}
8384
export default Particle
`
Now **_THAT’S_** how you create a new constellation ✨. Feel free to use the code and learnings to build your own.
## Conclusion[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#conclusion)
In this journey, you saw how to use Three.js and harness the power of React Three Fiber and creative experimentation to craft an animation. We leveraged trigonometry, animation hooks, and GUI playgrounds to build a "8" shape formed by user-generated stars.
If you loved this and the new [Launch Week 8](https://supabase.com/launch-week) branding, make sure to tune in on Monday at 09 AM PT as we unveil the full landing 💥
## More Supabase Design[#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#more-supabase-design)
  * [Designing with AI: Generating unique artwork for every user](https://supabase.com/blog/designing-with-ai-midjourney)
  * **[Infinite scroll with Next.js, Framer Motion, and Supabase](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion)**


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&t=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)
[Last postWhy we'll stay remote5 August 2023](https://supabase.com/blog/why-supabase-remote)
[Next postpgvector: Fewer dimensions are better3 August 2023](https://supabase.com/blog/fewer-dimensions-are-better-pgvector)
[launch-week](https://supabase.com/blog/tags/launch-week)
On this page
  * [Setting up the scene](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#setting-up-the-scene)
  * [Load users from Supabase](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#load-users-from-supabase)
  * [Animating the particles](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#animating-the-particles)
    * [useFrame](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#useframe)
    * [Using time as an animation variable](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#using-time-as-an-animation-variable)
  * [GUI playground](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#gui-playground)
  * [Conclusion](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#conclusion)
  * [More Supabase Design](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#more-supabase-design)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&t=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)
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
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-early-design.png&w=1920&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)

