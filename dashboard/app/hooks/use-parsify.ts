import { useAuth } from "@clerk/react-router";
import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { apiClient } from "~/lib/api-client";

function useToken() {
  const { getToken } = useAuth();
  return async () => getToken();
}

// ── User ──────────────────────────────────────────────

interface UserProfile {
  user_id: string;
  email: string;
  name: string | null;
  tier: string;
  clerk_user_id: string;
  stripe_customer_id: string | null;
  created_at: string;
}

export function useUser() {
  const getToken = useToken();

  return useQuery({
    queryKey: ["user", "me"],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<UserProfile>("/dashboard/me", token);
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

// ── API Keys ──────────────────────────────────────────

interface ApiKey {
  key_id: string;
  name: string;
  prefix: string;
  is_active: boolean;
  created_at: string;
}

interface CreateKeyResponse {
  key: ApiKey;
  raw_key: string;
}

export function useApiKeys() {
  const getToken = useToken();

  return useQuery({
    queryKey: ["dashboard", "keys"],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<ApiKey[]>("/dashboard/keys", token);
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

export function useCreateApiKey() {
  const getToken = useToken();
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (name: string) => {
      const token = await getToken();
      const result = await apiClient.post<CreateKeyResponse>(
        "/dashboard/keys",
        { name },
        token
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["dashboard", "keys"] });
    },
  });
}

export function useRevokeApiKey() {
  const getToken = useToken();
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (keyId: string) => {
      const token = await getToken();
      const result = await apiClient.delete(`/dashboard/keys/${keyId}`, token);
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["dashboard", "keys"] });
    },
  });
}

// ── Usage ─────────────────────────────────────────────

interface UsageSummary {
  total_requests: number;
  total_pages: number;
  total_errors: number;
  rate_limit: {
    limit: number;
    used: number;
    remaining: number;
  };
}

interface DailyUsage {
  date: string;
  request_count: number;
  pages_scraped: number;
  errors: number;
}

export function useUsageSummary() {
  const getToken = useToken();

  return useQuery({
    queryKey: ["dashboard", "usage"],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<UsageSummary>(
        "/dashboard/usage",
        token
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

export function useDailyUsage(days = 30) {
  const getToken = useToken();

  return useQuery({
    queryKey: ["dashboard", "usage", "daily", days],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<DailyUsage[]>(
        "/dashboard/usage/daily",
        token,
        { days }
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

// ── Jobs ──────────────────────────────────────────────

interface Job {
  job_id: string;
  status: string;
  url: string | null;
  job_type: string;
  max_pages: number | null;
  created_at: string;
  started_at: string | null;
  completed_at: string | null;
  pages_scraped: number;
  pages_failed: number;
  progress: number;
  error_message: string | null;
  output_files: unknown[] | null;
  summary: Record<string, unknown> | null;
}

interface JobsResponse {
  jobs: Job[];
  total: number;
  page: number;
  per_page: number;
}

export function useJobs(params?: {
  status?: string;
  page?: number;
  per_page?: number;
}) {
  const getToken = useToken();

  return useQuery({
    queryKey: ["dashboard", "jobs", params],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<JobsResponse>(
        "/dashboard/jobs",
        token,
        params as Record<string, string | number | undefined>
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
    refetchInterval: (query) => {
      const data = query.state.data;
      if (!data) return false;
      const hasActive = data.jobs.some(
        (j: Job) => j.status === "pending" || j.status === "running"
      );
      return hasActive ? 5000 : false;
    },
  });
}

export function useJob(jobId: string) {
  const getToken = useToken();

  return useQuery({
    queryKey: ["dashboard", "jobs", jobId],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<Job>(
        `/dashboard/jobs/${jobId}`,
        token
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
    enabled: !!jobId,
    refetchInterval: (query) => {
      const data = query.state.data;
      if (!data) return false;
      return data.status === "pending" || data.status === "running"
        ? 3000
        : false;
    },
  });
}

// ── Subscription ──────────────────────────────────────

interface Subscription {
  tier: string;
  status: string;
  stripe_customer_id: string | null;
  current_period_end: string | null;
  cancel_at_period_end: boolean;
}

export function useSubscription() {
  const getToken = useToken();

  return useQuery({
    queryKey: ["dashboard", "subscription"],
    queryFn: async () => {
      const token = await getToken();
      const result = await apiClient.get<Subscription>(
        "/dashboard/subscription",
        token
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

export function useCreateCheckout() {
  const getToken = useToken();

  return useMutation({
    mutationFn: async (priceId: string) => {
      const token = await getToken();
      const result = await apiClient.post<{ checkout_url: string }>(
        "/dashboard/billing/checkout",
        { price_id: priceId },
        token
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

export function useCreatePortalSession() {
  const getToken = useToken();

  return useMutation({
    mutationFn: async () => {
      const token = await getToken();
      const result = await apiClient.post<{ portal_url: string }>(
        "/dashboard/billing/portal",
        {},
        token
      );
      if (result.error) throw new Error(result.error.message);
      return result.data;
    },
  });
}

export type { UserProfile, ApiKey, CreateKeyResponse, UsageSummary, DailyUsage, Job, JobsResponse, Subscription };
