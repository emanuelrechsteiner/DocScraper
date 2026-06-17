"use client";

import { ExternalLink, Loader2, Settings } from "lucide-react";
import { Badge } from "~/components/ui/badge";
import { Button } from "~/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import { Skeleton } from "~/components/ui/skeleton";
import { Link } from "react-router";
import {
  useCreatePortalSession,
  useSubscription,
  useUser,
} from "~/hooks/use-parsify";

export default function SettingsPage() {
  const { data: user, isLoading: userLoading } = useUser();
  const { data: subscription, isLoading: subLoading } = useSubscription();
  const portalSession = useCreatePortalSession();

  const handleManageSubscription = async () => {
    const result = await portalSession.mutateAsync();
    window.open(result.portal_url, "_blank");
  };

  const isLoading = userLoading || subLoading;

  return (
    <div className="flex flex-1 flex-col">
      <div className="@container/main flex flex-1 flex-col gap-2">
        <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
          <div className="px-4 lg:px-6 space-y-6">
            <div>
              <h2 className="text-2xl font-semibold flex items-center gap-2">
                <Settings className="h-6 w-6" />
                Settings
              </h2>
              <p className="text-muted-foreground mt-1">
                Manage your account and subscription.
              </p>
            </div>

            {isLoading ? (
              <div className="space-y-4">
                <Skeleton className="h-40 w-full" />
                <Skeleton className="h-40 w-full" />
              </div>
            ) : (
              <>
                <Card>
                  <CardHeader>
                    <CardTitle>Account</CardTitle>
                    <CardDescription>Your account information</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="grid gap-4 sm:grid-cols-2">
                      <div>
                        <p className="text-sm font-medium">Email</p>
                        <p className="text-sm text-muted-foreground">
                          {user?.email}
                        </p>
                      </div>
                      <div>
                        <p className="text-sm font-medium">Name</p>
                        <p className="text-sm text-muted-foreground">
                          {user?.name ?? "—"}
                        </p>
                      </div>
                      <div>
                        <p className="text-sm font-medium">User ID</p>
                        <p className="text-sm text-muted-foreground font-mono">
                          {user?.user_id}
                        </p>
                      </div>
                      <div>
                        <p className="text-sm font-medium">Member Since</p>
                        <p className="text-sm text-muted-foreground">
                          {user?.created_at
                            ? new Date(user.created_at).toLocaleDateString()
                            : "—"}
                        </p>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <div>
                        <CardTitle>Subscription</CardTitle>
                        <CardDescription>
                          Manage your plan and billing
                        </CardDescription>
                      </div>
                      {subscription?.status && (
                        <Badge
                          variant={
                            subscription.status === "active"
                              ? "default"
                              : "secondary"
                          }
                        >
                          {subscription.status}
                        </Badge>
                      )}
                    </div>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="grid gap-4 sm:grid-cols-2">
                      <div>
                        <p className="text-sm font-medium">Current Plan</p>
                        <p className="text-sm text-muted-foreground capitalize">
                          {user?.tier ?? "free"}
                        </p>
                      </div>
                      {subscription?.current_period_end && (
                        <div>
                          <p className="text-sm font-medium">Next Billing</p>
                          <p className="text-sm text-muted-foreground">
                            {new Date(
                              subscription.current_period_end
                            ).toLocaleDateString()}
                          </p>
                        </div>
                      )}
                    </div>

                    {subscription?.cancel_at_period_end && (
                      <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-md">
                        <p className="text-sm text-yellow-800">
                          Your subscription will be canceled at the end of the
                          current billing period.
                        </p>
                      </div>
                    )}

                    <div className="flex gap-2">
                      {subscription?.stripe_customer_id ? (
                        <Button
                          variant="outline"
                          onClick={handleManageSubscription}
                          disabled={portalSession.isPending}
                        >
                          {portalSession.isPending ? (
                            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                          ) : (
                            <ExternalLink className="mr-2 h-4 w-4" />
                          )}
                          Manage Subscription
                        </Button>
                      ) : null}
                      <Button asChild>
                        <Link to="/pricing">
                          {user?.tier === "free"
                            ? "Upgrade Plan"
                            : "Change Plan"}
                        </Link>
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
