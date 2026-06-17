"use client";

import { useAuth } from "@clerk/react-router";
import { Check, Loader2 } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { Button } from "~/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import { useCreateCheckout, useUser } from "~/hooks/use-parsify";

const PLANS = [
  {
    name: "Free",
    priceId: "free",
    price: 0,
    description: "Get started with basic scraping",
    features: [
      "100 requests/hour",
      "10 pages per scrape",
      "1 concurrent job",
      "Markdown output",
    ],
  },
  {
    name: "Pro",
    priceId: "pro",
    price: 49,
    popular: true,
    description: "For teams and production workloads",
    features: [
      "1,000 requests/hour",
      "100 pages per scrape",
      "5 concurrent jobs",
      "All output formats",
      "Priority support",
      "Webhook notifications",
    ],
  },
  {
    name: "Enterprise",
    priceId: "enterprise",
    price: 199,
    description: "Unlimited scraping at scale",
    features: [
      "10,000 requests/hour",
      "Unlimited pages per scrape",
      "20 concurrent jobs",
      "All output formats",
      "Dedicated support",
      "Webhook notifications",
      "Custom rate limits",
    ],
  },
];

export default function PricingPage() {
  const { isSignedIn } = useAuth();
  const { data: user } = useUser();
  const createCheckout = useCreateCheckout();
  const [loadingPriceId, setLoadingPriceId] = useState<string | null>(null);

  const handleSubscribe = async (priceId: string) => {
    if (!isSignedIn) {
      window.location.href = "/sign-in";
      return;
    }

    if (priceId === "free") return;

    setLoadingPriceId(priceId);
    try {
      const result = await createCheckout.mutateAsync(priceId);
      window.location.href = result.checkout_url;
    } catch {
      setLoadingPriceId(null);
    }
  };

  return (
    <div className="min-h-screen">
      <header className="border-b">
        <div className="mx-auto max-w-6xl flex items-center justify-between px-6 py-4">
          <Link to="/" className="text-xl font-semibold">
            Parsify
          </Link>
          <nav className="flex items-center gap-4">
            {isSignedIn ? (
              <Button size="sm" variant="outline" asChild>
                <Link to="/dashboard">Dashboard</Link>
              </Button>
            ) : (
              <Button size="sm" asChild>
                <Link to="/sign-up">Get Started</Link>
              </Button>
            )}
          </nav>
        </div>
      </header>

      <section className="flex flex-col items-center justify-center py-16 px-4">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold tracking-tight mb-4">
            Simple, transparent pricing
          </h1>
          <p className="text-xl text-muted-foreground">
            Choose the plan that fits your scraping needs
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8 max-w-6xl w-full">
          {PLANS.map((plan) => {
            const isCurrentPlan = user?.tier === plan.priceId;

            return (
              <Card
                key={plan.priceId}
                className={`relative h-fit ${
                  plan.popular ? "border-primary" : ""
                } ${isCurrentPlan ? "border-green-500 bg-green-50/50" : ""}`}
              >
                {plan.popular && !isCurrentPlan && (
                  <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                    <span className="bg-primary text-primary-foreground px-3 py-1 rounded-full text-sm font-medium">
                      Most Popular
                    </span>
                  </div>
                )}
                {isCurrentPlan && (
                  <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                    <span className="bg-green-500 text-white px-3 py-1 rounded-full text-sm font-medium">
                      Current Plan
                    </span>
                  </div>
                )}

                <CardHeader>
                  <CardTitle className="text-2xl">{plan.name}</CardTitle>
                  <CardDescription>{plan.description}</CardDescription>
                  <div className="mt-4">
                    <span className="text-4xl font-bold">
                      ${plan.price}
                    </span>
                    <span className="text-muted-foreground">/month</span>
                  </div>
                </CardHeader>

                <CardContent className="space-y-3">
                  {plan.features.map((feature) => (
                    <div key={feature} className="flex items-center gap-3">
                      <Check className="h-4 w-4 text-green-500 shrink-0" />
                      <span className="text-sm">{feature}</span>
                    </div>
                  ))}
                </CardContent>

                <CardFooter>
                  <Button
                    className="w-full"
                    onClick={() => handleSubscribe(plan.priceId)}
                    disabled={
                      isCurrentPlan || loadingPriceId === plan.priceId
                    }
                    variant={isCurrentPlan ? "secondary" : "default"}
                  >
                    {loadingPriceId === plan.priceId ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        Setting up checkout...
                      </>
                    ) : isCurrentPlan ? (
                      "Current Plan"
                    ) : plan.price === 0 ? (
                      isSignedIn ? "Current Plan" : "Get Started"
                    ) : (
                      "Upgrade"
                    )}
                  </Button>
                </CardFooter>
              </Card>
            );
          })}
        </div>

        <div className="mt-12 text-center">
          <p className="text-muted-foreground">
            Need a custom plan?{" "}
            <span className="text-primary cursor-pointer hover:underline">
              Contact us
            </span>
          </p>
        </div>
      </section>
    </div>
  );
}
