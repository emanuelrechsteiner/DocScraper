import { memo } from "react";
import { Link } from "react-router";
import {
  ReactIcon,
  ReactRouter,
  TailwindIcon,
  Typescript,
} from "~/components/logos";
import { Button } from "~/components/ui/button";
import { cn } from "~/lib/utils";

export default function IntegrationsSection({
  loaderData,
}: {
  loaderData?: { isSignedIn: boolean };
}) {
  return (
    <section id="hero">
      <div className="bg-muted dark:bg-background py-24 md:py-32">
        <div className="mx-auto max-w-5xl px-6 mt-[2rem]">
          <div className="grid items-center sm:grid-cols-2">
            <div className="dark:bg-muted/50 relative mx-auto w-fit">
              <div className="bg-radial to-muted dark:to-background absolute inset-0 z-10 from-transparent to-75%" />
              <div className="mx-auto mb-2 flex w-fit justify-center gap-2">
                <IntegrationCard>
                  <ReactRouter />
                </IntegrationCard>
                <IntegrationCard>
                  <ReactIcon />
                </IntegrationCard>
              </div>
              <div className="mx-auto my-2 flex w-fit justify-center gap-2">
                <IntegrationCard>
                  <TailwindIcon />
                </IntegrationCard>
                <IntegrationCard>
                  <Typescript />
                </IntegrationCard>
              </div>
            </div>
            <div className="mx-auto mt-6 max-w-lg space-y-6 text-center sm:mt-0 sm:text-left">
              <h2 className="text-balance text-3xl font-semibold md:text-4xl">
                Parsify API
              </h2>
              <p className="text-muted-foreground">
                Documentation scraping and processing as a service. Built with
                Python, FastAPI, and Playwright.
              </p>

              <div className="flex gap-3">
                <Button size="sm" asChild>
                  <Link
                    to={loaderData?.isSignedIn ? "/dashboard" : "/sign-up"}
                    prefetch="viewport"
                  >
                    {loaderData?.isSignedIn
                      ? "Go to Dashboard"
                      : "Get Started"}
                  </Link>
                </Button>
                <Button variant="outline" size="sm" asChild>
                  <Link to="/pricing">View Pricing</Link>
                </Button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

const IntegrationCard = memo(
  ({
    children,
    className,
    borderClassName,
  }: {
    children: React.ReactNode;
    className?: string;
    borderClassName?: string;
  }) => {
    return (
      <div
        className={cn(
          "bg-background relative flex size-20 rounded-xl dark:bg-transparent",
          className
        )}
      >
        <div
          role="presentation"
          className={cn(
            "absolute inset-0 rounded-xl border border-black/20 dark:border-white/25",
            borderClassName
          )}
        />
        <div className="relative z-20 m-auto size-fit *:size-8">{children}</div>
      </div>
    );
  }
);
