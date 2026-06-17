import { getAuth } from "@clerk/react-router/ssr.server";
import type { Route } from "./+types/home";
import { Link } from "react-router";
import { Button } from "~/components/ui/button";

export function meta({}: Route.MetaArgs) {
  const title = "Parsify — Documentation Scraping API";
  const description =
    "Scrape, clean, and process documentation at scale with the Parsify REST API.";

  return [
    { title },
    { name: "description", content: description },
    { property: "og:type", content: "website" },
    { property: "og:title", content: title },
    { property: "og:description", content: description },
    { name: "twitter:card", content: "summary_large_image" },
    { name: "twitter:title", content: title },
    { name: "twitter:description", content: description },
  ];
}

export async function loader(args: Route.LoaderArgs) {
  const { userId } = await getAuth(args);
  return { isSignedIn: !!userId };
}

export default function Home({ loaderData }: Route.ComponentProps) {
  const { isSignedIn } = loaderData;

  return (
    <div className="min-h-screen flex flex-col">
      <header className="border-b">
        <div className="mx-auto max-w-6xl flex items-center justify-between px-6 py-4">
          <Link to="/" className="text-xl font-semibold">
            Parsify
          </Link>
          <nav className="flex items-center gap-4">
            <Link
              to="/pricing"
              className="text-sm text-muted-foreground hover:text-foreground"
            >
              Pricing
            </Link>
            {isSignedIn ? (
              <Button size="sm" asChild>
                <Link to="/dashboard">Dashboard</Link>
              </Button>
            ) : (
              <div className="flex items-center gap-2">
                <Button variant="ghost" size="sm" asChild>
                  <Link to="/sign-in">Sign In</Link>
                </Button>
                <Button size="sm" asChild>
                  <Link to="/sign-up">Get Started</Link>
                </Button>
              </div>
            )}
          </nav>
        </div>
      </header>

      <main className="flex-1">
        <section className="py-24 md:py-32">
          <div className="mx-auto max-w-4xl px-6 text-center">
            <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
              Documentation Scraping API
            </h1>
            <p className="mt-6 text-lg text-muted-foreground max-w-2xl mx-auto">
              Scrape, clean, and process any documentation site. Get structured
              markdown, semantic chunks, and AI-ready content via a simple REST API.
            </p>
            <div className="mt-10 flex items-center justify-center gap-4">
              <Button size="lg" asChild>
                <Link to={isSignedIn ? "/dashboard" : "/sign-up"}>
                  {isSignedIn ? "Go to Dashboard" : "Start for Free"}
                </Link>
              </Button>
              <Button variant="outline" size="lg" asChild>
                <Link to="/pricing">View Pricing</Link>
              </Button>
            </div>
          </div>
        </section>

        <section className="border-t py-16">
          <div className="mx-auto max-w-6xl px-6">
            <div className="grid gap-8 md:grid-cols-3">
              <div className="space-y-2">
                <h3 className="font-semibold text-lg">Scrape Any Site</h3>
                <p className="text-sm text-muted-foreground">
                  Playwright-powered scraping handles JavaScript-heavy documentation
                  sites with ease.
                </p>
              </div>
              <div className="space-y-2">
                <h3 className="font-semibold text-lg">Clean Content</h3>
                <p className="text-sm text-muted-foreground">
                  25+ cleaning rules strip navigation, ads, and boilerplate — leaving
                  only the documentation content.
                </p>
              </div>
              <div className="space-y-2">
                <h3 className="font-semibold text-lg">AI-Ready Output</h3>
                <p className="text-sm text-muted-foreground">
                  Semantic chunking optimized for embedding models. Get markdown, JSON,
                  or structured data.
                </p>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="border-t py-8">
        <div className="mx-auto max-w-6xl px-6 text-center text-sm text-muted-foreground">
          Parsify
        </div>
      </footer>
    </div>
  );
}
