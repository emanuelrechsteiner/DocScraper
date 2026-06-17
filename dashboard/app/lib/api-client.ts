const API_BASE_URL =
  typeof window !== "undefined"
    ? (window as any).__PARSIFY_API_URL || import.meta.env.VITE_PARSIFY_API_URL
    : import.meta.env.VITE_PARSIFY_API_URL;

interface ApiResponse<T> {
  data: T;
  error?: never;
}

interface ApiError {
  data?: never;
  error: {
    code: string;
    message: string;
  };
}

type ApiResult<T> = ApiResponse<T> | ApiError;

interface PaginatedResponse<T> {
  data: T[];
  meta: {
    page: number;
    per_page: number;
    total: number;
    total_pages: number;
  };
}

export type { ApiResult, PaginatedResponse };

async function fetchApi<T>(
  path: string,
  options: {
    method?: string;
    body?: unknown;
    token?: string | null;
    params?: Record<string, string | number | undefined>;
  } = {}
): Promise<ApiResult<T>> {
  const { method = "GET", body, token, params } = options;

  let url = `${API_BASE_URL}/api/v1${path}`;

  if (params) {
    const searchParams = new URLSearchParams();
    for (const [key, value] of Object.entries(params)) {
      if (value !== undefined) {
        searchParams.set(key, String(value));
      }
    }
    const qs = searchParams.toString();
    if (qs) {
      url += `?${qs}`;
    }
  }

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  try {
    const response = await fetch(url, {
      method,
      headers,
      body: body ? JSON.stringify(body) : undefined,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => null);
      return {
        error: {
          code: errorData?.detail?.code || `HTTP_${response.status}`,
          message:
            errorData?.detail?.message ||
            errorData?.detail ||
            `Request failed with status ${response.status}`,
        },
      };
    }

    const data = await response.json();
    return { data: data.data ?? data };
  } catch (err) {
    return {
      error: {
        code: "NETWORK_ERROR",
        message:
          err instanceof Error ? err.message : "Network request failed",
      },
    };
  }
}

export const apiClient = {
  get<T>(
    path: string,
    token?: string | null,
    params?: Record<string, string | number | undefined>
  ) {
    return fetchApi<T>(path, { token, params });
  },

  post<T>(path: string, body: unknown, token?: string | null) {
    return fetchApi<T>(path, { method: "POST", body, token });
  },

  delete<T>(path: string, token?: string | null) {
    return fetchApi<T>(path, { method: "DELETE", token });
  },
};
