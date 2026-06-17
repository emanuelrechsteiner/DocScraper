import {
  isRouteErrorResponse,
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "react-router";

import { ClerkProvider } from "@clerk/react-router";
import { rootAuthLoader } from "@clerk/react-router/ssr.server";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import type { Route } from "./+types/root";
import "./app.css";
import { Analytics } from "@vercel/analytics/react";
import { validateEnvironment } from "./lib/env-validation";

if (typeof window === "undefined") {
  validateEnvironment();
}

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30_000,
      retry: 1,
    },
  },
});

export async function loader(args: Route.LoaderArgs) {
  return rootAuthLoader(args);
}

export const links: Route.LinksFunction = () => [
  { rel: "dns-prefetch", href: "https://fonts.googleapis.com" },
  { rel: "dns-prefetch", href: "https://fonts.gstatic.com" },
  { rel: "dns-prefetch", href: "https://clerk.dev" },
  { rel: "preconnect", href: "https://fonts.googleapis.com" },
  {
    rel: "preconnect",
    href: "https://fonts.gstatic.com",
    crossOrigin: "anonymous",
  },
  {
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
  },
  {
    rel: "icon",
    type: "image/png",
    href: "/favicon.png",
  },
];

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta
          httpEquiv="Content-Security-Policy"
          content="
          default-src 'self';
          script-src 'self' 'unsafe-inline' https://clerk.dev https://*.clerk.accounts.dev https://vercel.live https://va.vercel-scripts.com;
          worker-src 'self' blob:;
          style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
          font-src 'self' https://fonts.gstatic.com;
          img-src 'self' data: https: blob:;
          connect-src 'self' https://clerk.dev https://*.clerk.accounts.dev https://vitals.vercel-analytics.com https://va.vercel-scripts.com;
          frame-src 'self' https://clerk.dev https://*.clerk.accounts.dev;
          object-src 'none';
          base-uri 'self';
          form-action 'self' https://clerk.dev;
        "
        />
        <meta httpEquiv="X-Content-Type-Options" content="nosniff" />
        <meta httpEquiv="X-XSS-Protection" content="1; mode=block" />
        <meta name="referrer" content="strict-origin-when-cross-origin" />
        <meta
          httpEquiv="Permissions-Policy"
          content="camera=(), microphone=(), geolocation=(), payment=()"
        />
        <Meta />
        <Links />
      </head>
      <body>
        <Analytics />
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App({ loaderData }: Route.ComponentProps) {
  return (
    <ClerkProvider
      loaderData={loaderData}
      signUpFallbackRedirectUrl="/"
      signInFallbackRedirectUrl="/"
    >
      <QueryClientProvider client={queryClient}>
        <Outlet />
      </QueryClientProvider>
    </ClerkProvider>
  );
}

export function ErrorBoundary({ error }: Route.ErrorBoundaryProps) {
  const isDev = import.meta.env.DEV;

  let message = "Oops!";
  let details = "An unexpected error occurred.";
  let stack: string | undefined;

  if (isRouteErrorResponse(error)) {
    message = error.status === 404 ? "404" : "Error";
    details =
      error.status === 404
        ? "The requested page could not be found."
        : "Something went wrong. Please try again.";
  } else if (isDev && error && error instanceof Error) {
    details = error.message;
    stack = error.stack;
  }

  if (error instanceof Error) {
    console.error("Application error:", {
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString(),
    });
  }

  return (
    <main className="pt-16 p-4 container mx-auto">
      <h1 className="text-2xl font-bold mb-4">{message}</h1>
      <p className="text-gray-600 mb-4">{details}</p>
      {isDev && stack && (
        <details className="mt-4">
          <summary className="cursor-pointer text-sm text-gray-500 mb-2">
            Debug Information (Development Only)
          </summary>
          <pre className="w-full p-4 overflow-x-auto bg-gray-100 rounded text-xs">
            <code>{stack}</code>
          </pre>
        </details>
      )}
      <div className="mt-6">
        <a
          href="/"
          className="inline-block px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
        >
          Return Home
        </a>
      </div>
    </main>
  );
}
