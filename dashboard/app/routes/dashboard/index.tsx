"use client";

import { IconTrendingUp } from "@tabler/icons-react";
import { Activity, BarChart3, Key, Zap } from "lucide-react";
import { Badge } from "~/components/ui/badge";
import {
  Card,
  CardAction,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import { Skeleton } from "~/components/ui/skeleton";
import { useApiKeys, useDailyUsage, useUsageSummary, useUser } from "~/hooks/use-parsify";
import { ChartAreaInteractive } from "~/components/dashboard/chart-area-interactive";

function StatCard({
  title,
  value,
  icon: Icon,
  footer,
}: {
  title: string;
  value: string | number;
  icon: React.ElementType;
  footer: string;
}) {
  return (
    <Card className="@container/card">
      <CardHeader>
        <CardDescription className="flex items-center gap-1.5">
          <Icon className="size-4" />
          {title}
        </CardDescription>
        <CardTitle className="text-2xl font-semibold tabular-nums @[250px]/card:text-3xl">
          {value}
        </CardTitle>
        <CardAction>
          <Badge variant="outline">
            <IconTrendingUp />
            Live
          </Badge>
        </CardAction>
      </CardHeader>
      <CardFooter className="flex-col items-start gap-1.5 text-sm">
        <div className="text-muted-foreground">{footer}</div>
      </CardFooter>
    </Card>
  );
}

function SectionCards() {
  const { data: usage, isLoading: usageLoading } = useUsageSummary();
  const { data: keys, isLoading: keysLoading } = useApiKeys();
  const { data: user, isLoading: userLoading } = useUser();

  const isLoading = usageLoading || keysLoading || userLoading;

  if (isLoading) {
    return (
      <div className="grid grid-cols-1 gap-4 px-4 lg:px-6 @xl/main:grid-cols-2 @5xl/main:grid-cols-4">
        {Array.from({ length: 4 }).map((_, i) => (
          <Card key={i} className="@container/card">
            <CardHeader>
              <Skeleton className="h-4 w-24" />
              <Skeleton className="h-8 w-32 mt-2" />
            </CardHeader>
            <CardFooter>
              <Skeleton className="h-3 w-40" />
            </CardFooter>
          </Card>
        ))}
      </div>
    );
  }

  const activeKeys = keys?.filter((k) => k.is_active).length ?? 0;

  return (
    <div className="*:data-[slot=card]:from-primary/5 *:data-[slot=card]:to-card dark:*:data-[slot=card]:bg-card grid grid-cols-1 gap-4 px-4 *:data-[slot=card]:bg-gradient-to-t *:data-[slot=card]:shadow-xs lg:px-6 @xl/main:grid-cols-2 @5xl/main:grid-cols-4">
      <StatCard
        title="API Requests (hour)"
        value={usage?.rate_limit?.used ?? 0}
        icon={Activity}
        footer={`${usage?.rate_limit?.remaining ?? 0} remaining this hour`}
      />
      <StatCard
        title="Pages Scraped"
        value={usage?.total_pages ?? 0}
        icon={Zap}
        footer="Total pages processed"
      />
      <StatCard
        title="Active Keys"
        value={activeKeys}
        icon={Key}
        footer={`${keys?.length ?? 0} total keys created`}
      />
      <StatCard
        title="Current Plan"
        value={(user?.tier ?? "free").charAt(0).toUpperCase() + (user?.tier ?? "free").slice(1)}
        icon={BarChart3}
        footer="Manage in Settings"
      />
    </div>
  );
}

export default function DashboardOverview() {
  return (
    <div className="flex flex-1 flex-col">
      <div className="@container/main flex flex-1 flex-col gap-2">
        <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
          <SectionCards />
          <div className="px-4 lg:px-6">
            <ChartAreaInteractive />
          </div>
        </div>
      </div>
    </div>
  );
}
