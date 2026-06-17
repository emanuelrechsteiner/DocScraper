"use client";

import { Briefcase, Loader2 } from "lucide-react";
import { useState } from "react";
import { Badge } from "~/components/ui/badge";
import { Button } from "~/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "~/components/ui/select";
import { Skeleton } from "~/components/ui/skeleton";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "~/components/ui/table";
import { useJobs, type Job } from "~/hooks/use-parsify";

function JobStatusBadge({ status }: { status: string }) {
  const variants: Record<string, "default" | "secondary" | "destructive" | "outline"> = {
    pending: "outline",
    running: "default",
    completed: "secondary",
    failed: "destructive",
    cancelled: "outline",
  };

  return <Badge variant={variants[status] ?? "outline"}>{status}</Badge>;
}

export default function JobsPage() {
  const [statusFilter, setStatusFilter] = useState<string | undefined>();
  const [page, setPage] = useState(1);

  const { data, isLoading, error } = useJobs({
    status: statusFilter,
    page,
    per_page: 20,
  });

  const jobs = data?.jobs ?? [];
  const total = data?.total ?? 0;
  const totalPages = Math.ceil(total / 20);

  return (
    <div className="flex flex-1 flex-col">
      <div className="@container/main flex flex-1 flex-col gap-2">
        <div className="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
          <div className="px-4 lg:px-6">
            <Card>
              <CardHeader className="flex flex-row items-center justify-between">
                <div>
                  <CardTitle className="flex items-center gap-2">
                    <Briefcase className="h-5 w-5" />
                    Jobs
                  </CardTitle>
                  <CardDescription>
                    Track your scraping and processing jobs.
                  </CardDescription>
                </div>
                <Select
                  value={statusFilter ?? "all"}
                  onValueChange={(v) => {
                    setStatusFilter(v === "all" ? undefined : v);
                    setPage(1);
                  }}
                >
                  <SelectTrigger className="w-36">
                    <SelectValue placeholder="All statuses" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="all">All statuses</SelectItem>
                    <SelectItem value="pending">Pending</SelectItem>
                    <SelectItem value="running">Running</SelectItem>
                    <SelectItem value="completed">Completed</SelectItem>
                    <SelectItem value="failed">Failed</SelectItem>
                  </SelectContent>
                </Select>
              </CardHeader>
              <CardContent>
                {isLoading ? (
                  <div className="space-y-3">
                    {Array.from({ length: 5 }).map((_, i) => (
                      <Skeleton key={i} className="h-12 w-full" />
                    ))}
                  </div>
                ) : error ? (
                  <div className="text-center py-8 text-destructive">
                    Failed to load jobs. Please try again.
                  </div>
                ) : jobs.length === 0 ? (
                  <div className="text-center py-12">
                    <Briefcase className="mx-auto h-12 w-12 text-muted-foreground/50" />
                    <h3 className="mt-4 text-lg font-medium">No jobs yet</h3>
                    <p className="mt-2 text-sm text-muted-foreground">
                      Jobs will appear here when you submit scraping requests
                      via the API.
                    </p>
                  </div>
                ) : (
                  <>
                    <Table>
                      <TableHeader>
                        <TableRow>
                          <TableHead>Job ID</TableHead>
                          <TableHead>Type</TableHead>
                          <TableHead>URL</TableHead>
                          <TableHead>Status</TableHead>
                          <TableHead>Progress</TableHead>
                          <TableHead>Created</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {jobs.map((job: Job) => (
                          <TableRow key={job.job_id}>
                            <TableCell className="font-mono text-xs">
                              {job.job_id}
                            </TableCell>
                            <TableCell className="capitalize">
                              {job.job_type}
                            </TableCell>
                            <TableCell
                              className="max-w-[200px] truncate text-muted-foreground"
                              title={job.url ?? ""}
                            >
                              {job.url ?? "—"}
                            </TableCell>
                            <TableCell>
                              <JobStatusBadge status={job.status} />
                            </TableCell>
                            <TableCell>
                              <div className="flex items-center gap-2">
                                <div className="h-2 w-16 rounded-full bg-muted overflow-hidden">
                                  <div
                                    className="h-full rounded-full bg-primary transition-all"
                                    style={{ width: `${job.progress}%` }}
                                  />
                                </div>
                                <span className="text-xs text-muted-foreground tabular-nums">
                                  {Math.round(job.progress)}%
                                </span>
                              </div>
                            </TableCell>
                            <TableCell className="text-muted-foreground text-sm">
                              {new Date(job.created_at).toLocaleString()}
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>

                    {totalPages > 1 && (
                      <div className="flex items-center justify-between mt-4">
                        <p className="text-sm text-muted-foreground">
                          {total} total jobs
                        </p>
                        <div className="flex gap-2">
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => setPage((p) => Math.max(1, p - 1))}
                            disabled={page <= 1}
                          >
                            Previous
                          </Button>
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() =>
                              setPage((p) => Math.min(totalPages, p + 1))
                            }
                            disabled={page >= totalPages}
                          >
                            Next
                          </Button>
                        </div>
                      </div>
                    )}
                  </>
                )}
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}
