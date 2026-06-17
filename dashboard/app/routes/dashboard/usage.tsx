"use client";

import { BarChart3 } from "lucide-react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import { Skeleton } from "~/components/ui/skeleton";
import { useDailyUsage, useUsageSummary } from "~/hooks/use-parsify";
import { Area, AreaChart, CartesianGrid, XAxis, YAxis } from "recharts";
import {
  type ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "~/components/ui/chart";

const chartConfig = {
  requests: {
    label: "Requests",
    color: "var(--primary)",
  },
  pages: {
    label: "Pages",
    color: "var(--chart-2)",
  },
} satisfies ChartConfig;

function RateLimitCard() {
  const { data, isLoading } = useUsageSummary();

  if (isLoading) {
    return (
      <Card>
        <CardHeader>
          <Skeleton className="h-4 w-32" />
        </CardHeader>
        <CardContent>
          <Skeleton className="h-4 w-full" />
        </CardContent>
      </Card>
    );
  }

  const limit = data?.rate_limit?.limit ?? 100;
  const used = data?.rate_limit?.used ?? 0;
  const pct = Math.min(100, (used / limit) * 100);
  const color =
    pct >= 90 ? "bg-destructive" : pct >= 70 ? "bg-yellow-500" : "bg-primary";

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-sm font-medium">Rate Limit Status</CardTitle>
        <CardDescription>Current hour usage</CardDescription>
      </CardHeader>
      <CardContent className="space-y-3">
        <div className="flex justify-between text-sm">
          <span className="text-muted-foreground">
            {used} / {limit} requests
          </span>
          <span className="font-medium tabular-nums">{Math.round(pct)}%</span>
        </div>
        <div className="h-3 rounded-full bg-muted overflow-hidden">
          <div
            className={`h-full rounded-full transition-all ${color}`}
            style={{ width: `${pct}%` }}
          />
        </div>
        <p className="text-xs text-muted-foreground">
          {data?.rate_limit?.remaining ?? 0} requests remaining this hour
        </p>
      </CardContent>
    </Card>
  );
}

function UsageChart() {
  const { data, isLoading } = useDailyUsage(30);

  if (isLoading) {
    return (
      <Card>
        <CardHeader>
          <Skeleton className="h-4 w-40" />
        </CardHeader>
        <CardContent>
          <Skeleton className="h-[250px] w-full" />
        </CardContent>
      </Card>
    );
  }

  const chartData = (data ?? [])
    .slice()
    .reverse()
    .map((d) => ({
      date: d.date,
      requests: d.request_count,
      pages: d.pages_scraped,
    }));

  return (
    <Card>
      <CardHeader>
        <CardTitle>Daily Usage</CardTitle>
        <CardDescription>API requests and pages scraped (last 30 days)</CardDescription>
      </CardHeader>
      <CardContent>
        {chartData.length === 0 ? (
          <div className="flex items-center justify-center h-[250px] text-muted-foreground">
            No usage data yet
          </div>
        ) : (
          <ChartContainer config={chartConfig} className="h-[250px] w-full">
            <AreaChart data={chartData}>
              <defs>
                <linearGradient id="fillRequests" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="var(--color-requests)" stopOpacity={0.8} />
                  <stop offset="95%" stopColor="var(--color-requests)" stopOpacity={0.1} />
                </linearGradient>
                <linearGradient id="fillPages" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="var(--color-pages)" stopOpacity={0.8} />
                  <stop offset="95%" stopColor="var(--color-pages)" stopOpacity={0.1} />
                </linearGradient>
              </defs>
              <CartesianGrid vertical={false} />
              <XAxis
                dataKey="date"
                tickLine={false}
                axisLine={false}
                tickMargin={8}
                minTickGap={32}
                tickFormatter={(value) =>
                  new Date(value).toLocaleDateString("en-US", {
                    month: "short",
                    day: "numeric",
                  })
                }
              />
              <YAxis tickLine={false} axisLine={false} width={40} />
              <ChartTooltip
                content={
                  <ChartTooltipContent
                    labelFormatter={(value) =>
                      new Date(value).toLocaleDateString("en-US", {
                        month: "short",
                        day: "numeric",
                      })
                    }
                    indicator="dot"
                  />
                }
              />
              <Area
                dataKey="requests"
                type="monotone"
                fill="url(#fillRequests)"
                stroke="var(--color-requests)"
              />
              <Area
                dataKey="pages"
                type="monotone"
                fill="url(#fillPages)"
                stroke="var(--color-pages)"
              />
            </AreaChart>
          </ChartContainer>
        )}
      </CardContent>
    </Card>
  );
}

export default function UsagePage() {
  const { data: summary } = useUsageSummary();

  return (
    <div className="flex flex-1 flex-col">
      <div className="@container/main flex flex-1 flex-col gap-2">
        <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
          <div className="px-4 lg:px-6 space-y-6">
            <div>
              <h2 className="text-2xl font-semibold flex items-center gap-2">
                <BarChart3 className="h-6 w-6" />
                Usage
              </h2>
              <p className="text-muted-foreground mt-1">
                Monitor your API usage and rate limits.
              </p>
            </div>

            <div className="grid gap-4 md:grid-cols-3">
              <RateLimitCard />
              <Card>
                <CardHeader>
                  <CardTitle className="text-sm font-medium">
                    Total Requests
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-3xl font-bold tabular-nums">
                    {summary?.total_requests ?? 0}
                  </p>
                  <p className="text-xs text-muted-foreground mt-1">All time</p>
                </CardContent>
              </Card>
              <Card>
                <CardHeader>
                  <CardTitle className="text-sm font-medium">
                    Pages Scraped
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-3xl font-bold tabular-nums">
                    {summary?.total_pages ?? 0}
                  </p>
                  <p className="text-xs text-muted-foreground mt-1">All time</p>
                </CardContent>
              </Card>
            </div>

            <UsageChart />
          </div>
        </div>
      </div>
    </div>
  );
}
