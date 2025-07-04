---
url: https://ui.shadcn.com/docs/dark-mode/vite
scraped_at: 2025-05-24T22:30:18.795238
title: Vite - shadcn/ui
---

[shadcn/ui](https://ui.shadcn.com/)[Docs](https://ui.shadcn.com/docs/installation)[Components](https://ui.shadcn.com/docs/components)[Blocks](https://ui.shadcn.com/blocks)[Charts](https://ui.shadcn.com/charts)[Themes](https://ui.shadcn.com/themes)[Colors](https://ui.shadcn.com/colors)
Toggle MenuSearch documentation...
Search documentation...Search...`⌘K`
[GitHub](https://github.com/shadcn-ui/ui)Toggle theme
#### Getting Started 
[Introduction](https://ui.shadcn.com/docs)[Installation](https://ui.shadcn.com/docs/installation)[components.json](https://ui.shadcn.com/docs/components-json)[Theming](https://ui.shadcn.com/docs/theming)[Dark mode](https://ui.shadcn.com/docs/dark-mode)[CLI](https://ui.shadcn.com/docs/cli)[Monorepo](https://ui.shadcn.com/docs/monorepo)[Tailwind v4New](https://ui.shadcn.com/docs/tailwind-v4)[Next.js 15 + React 19](https://ui.shadcn.com/docs/react-19)[Typography](https://ui.shadcn.com/docs/components/typography)[Open in v0](https://ui.shadcn.com/docs/v0)[Blocks](https://ui.shadcn.com/docs/blocks)[Figma](https://ui.shadcn.com/docs/figma)[Changelog](https://ui.shadcn.com/docs/changelog)
#### Installation 
[Next.js](https://ui.shadcn.com/docs/installation/next)[Vite](https://ui.shadcn.com/docs/installation/vite)[Laravel](https://ui.shadcn.com/docs/installation/laravel)[React Router](https://ui.shadcn.com/docs/installation/react-router)[Remix](https://ui.shadcn.com/docs/installation/remix)[Astro](https://ui.shadcn.com/docs/installation/astro)[Tanstack Start](https://ui.shadcn.com/docs/installation/tanstack)[Tanstack Router](https://ui.shadcn.com/docs/installation/tanstack-router)[Manual](https://ui.shadcn.com/docs/installation/manual)
#### Components 
[Accordion](https://ui.shadcn.com/docs/components/accordion)[Alert](https://ui.shadcn.com/docs/components/alert)[Alert Dialog](https://ui.shadcn.com/docs/components/alert-dialog)[Aspect Ratio](https://ui.shadcn.com/docs/components/aspect-ratio)[Avatar](https://ui.shadcn.com/docs/components/avatar)[Badge](https://ui.shadcn.com/docs/components/badge)[Breadcrumb](https://ui.shadcn.com/docs/components/breadcrumb)[Button](https://ui.shadcn.com/docs/components/button)[Calendar](https://ui.shadcn.com/docs/components/calendar)[Card](https://ui.shadcn.com/docs/components/card)[Carousel](https://ui.shadcn.com/docs/components/carousel)[Chart](https://ui.shadcn.com/docs/components/chart)[Checkbox](https://ui.shadcn.com/docs/components/checkbox)[Collapsible](https://ui.shadcn.com/docs/components/collapsible)[Combobox](https://ui.shadcn.com/docs/components/combobox)[Command](https://ui.shadcn.com/docs/components/command)[Context Menu](https://ui.shadcn.com/docs/components/context-menu)[Data Table](https://ui.shadcn.com/docs/components/data-table)[Date Picker](https://ui.shadcn.com/docs/components/date-picker)[Dialog](https://ui.shadcn.com/docs/components/dialog)[Drawer](https://ui.shadcn.com/docs/components/drawer)[Dropdown Menu](https://ui.shadcn.com/docs/components/dropdown-menu)[Form](https://ui.shadcn.com/docs/components/form)[Hover Card](https://ui.shadcn.com/docs/components/hover-card)[Input](https://ui.shadcn.com/docs/components/input)[Input OTP](https://ui.shadcn.com/docs/components/input-otp)[Label](https://ui.shadcn.com/docs/components/label)[Menubar](https://ui.shadcn.com/docs/components/menubar)[Navigation Menu](https://ui.shadcn.com/docs/components/navigation-menu)[Pagination](https://ui.shadcn.com/docs/components/pagination)[Popover](https://ui.shadcn.com/docs/components/popover)[Progress](https://ui.shadcn.com/docs/components/progress)[Radio Group](https://ui.shadcn.com/docs/components/radio-group)[Resizable](https://ui.shadcn.com/docs/components/resizable)[Scroll Area](https://ui.shadcn.com/docs/components/scroll-area)[Select](https://ui.shadcn.com/docs/components/select)[Separator](https://ui.shadcn.com/docs/components/separator)[Sheet](https://ui.shadcn.com/docs/components/sheet)[Sidebar](https://ui.shadcn.com/docs/components/sidebar)[Skeleton](https://ui.shadcn.com/docs/components/skeleton)[Slider](https://ui.shadcn.com/docs/components/slider)[Sonner](https://ui.shadcn.com/docs/components/sonner)[Switch](https://ui.shadcn.com/docs/components/switch)[Table](https://ui.shadcn.com/docs/components/table)[Tabs](https://ui.shadcn.com/docs/components/tabs)[Textarea](https://ui.shadcn.com/docs/components/textarea)[Toast](https://ui.shadcn.com/docs/components/toast)[Toggle](https://ui.shadcn.com/docs/components/toggle)[Toggle Group](https://ui.shadcn.com/docs/components/toggle-group)[Tooltip](https://ui.shadcn.com/docs/components/tooltip)
#### Registry New
[Introduction](https://ui.shadcn.com/docs/registry)[Getting Started](https://ui.shadcn.com/docs/registry/getting-started)[Examples](https://ui.shadcn.com/docs/registry/examples)[Open in v0](https://ui.shadcn.com/docs/registry/open-in-v0)[FAQ](https://ui.shadcn.com/docs/registry/faq)[registry.json](https://ui.shadcn.com/docs/registry/registry-json)[registry-item.json](https://ui.shadcn.com/docs/registry/registry-item-json)
[Docs](https://ui.shadcn.com/docs)
Vite
# Vite
Adding dark mode to your vite app.
## [](https://ui.shadcn.com/docs/dark-mode/vite#dark-mode)Dark mode
### [](https://ui.shadcn.com/docs/dark-mode/vite#create-a-theme-provider)Create a theme provider
components/theme-provider.tsx
```
import { createContext, useContext, useEffect, useState } from "react"
type Theme = "dark" | "light" | "system"
type ThemeProviderProps = {
 children: React.ReactNode
 defaultTheme?: Theme
 storageKey?: string
}
type ThemeProviderState = {
 theme: Theme
 setTheme: (theme: Theme) => void
}
const initialState: ThemeProviderState = {
 theme: "system",
 setTheme: () => null,
}
const ThemeProviderContext = createContext<ThemeProviderState>(initialState)
export function ThemeProvider({
 children,
 defaultTheme = "system",
 storageKey = "vite-ui-theme",
 ...props
}: ThemeProviderProps) {
 const [theme, setTheme] = useState<Theme>(
  () => (localStorage.getItem(storageKey) as Theme) || defaultTheme
 )
 useEffect(() => {
  const root = window.document.documentElement
  root.classList.remove("light", "dark")
  if (theme === "system") {
   const systemTheme = window.matchMedia("(prefers-color-scheme: dark)")
    .matches
    ? "dark"
    : "light"
   root.classList.add(systemTheme)
   return
  }
  root.classList.add(theme)
 }, [theme])
 const value = {
  theme,
  setTheme: (theme: Theme) => {
   localStorage.setItem(storageKey, theme)
   setTheme(theme)
  },
 }
 return (
  <ThemeProviderContext.Provider {...props} value={value}>
   {children}
  </ThemeProviderContext.Provider>
 )
}
export const useTheme = () => {
 const context = useContext(ThemeProviderContext)
 if (context === undefined)
  throw new Error("useTheme must be used within a ThemeProvider")
 return context
}
```
Copy
### [](https://ui.shadcn.com/docs/dark-mode/vite#wrap-your-root-layout)Wrap your root layout
Add the `ThemeProvider` to your root layout.
App.tsx
```
import { ThemeProvider } from "@/components/theme-provider"
function App() {
 return (
  <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
   {children}
  </ThemeProvider>
 )
}
export default App
```
Copy
### [](https://ui.shadcn.com/docs/dark-mode/vite#add-a-mode-toggle)Add a mode toggle
Place a mode toggle on your site to toggle between light and dark mode.
components/mode-toggle.tsx
```
import { Moon, Sun } from "lucide-react"
import { Button } from "@/components/ui/button"
import {
 DropdownMenu,
 DropdownMenuContent,
 DropdownMenuItem,
 DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { useTheme } from "@/components/theme-provider"
export function ModeToggle() {
 const { setTheme } = useTheme()
 return (
  <DropdownMenu>
   <DropdownMenuTrigger asChild>
    <Button variant="outline" size="icon">
     <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
     <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
     <span className="sr-only">Toggle theme</span>
    </Button>
   </DropdownMenuTrigger>
   <DropdownMenuContent align="end">
    <DropdownMenuItem onClick={() => setTheme("light")}>
     Light
    </DropdownMenuItem>
    <DropdownMenuItem onClick={() => setTheme("dark")}>
     Dark
    </DropdownMenuItem>
    <DropdownMenuItem onClick={() => setTheme("system")}>
     System
    </DropdownMenuItem>
   </DropdownMenuContent>
  </DropdownMenu>
 )
}
```
Copy
On This Page
  * [Dark mode](https://ui.shadcn.com/docs/dark-mode/vite#dark-mode)
    * [Create a theme provider](https://ui.shadcn.com/docs/dark-mode/vite#create-a-theme-provider)
    * [Wrap your root layout](https://ui.shadcn.com/docs/dark-mode/vite#wrap-your-root-layout)
    * [Add a mode toggle](https://ui.shadcn.com/docs/dark-mode/vite#add-a-mode-toggle)


Deploy your shadcn/ui app on Vercel
Trusted by OpenAI, Sonos, Chick-fil-A, and more.
Vercel provides tools and infrastructure to deploy apps and features at scale.
Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
Built by [shadcn](https://twitter.com/shadcn). The source code is available on [GitHub](https://github.com/shadcn-ui/ui).

