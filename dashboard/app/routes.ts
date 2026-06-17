import {
  type RouteConfig,
  index,
  layout,
  route,
} from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("sign-in/*", "routes/sign-in.tsx"),
  route("sign-up/*", "routes/sign-up.tsx"),
  route("pricing", "routes/pricing.tsx"),
  route("success", "routes/success.tsx"),
  layout("routes/dashboard/layout.tsx", [
    route("dashboard", "routes/dashboard/index.tsx"),
    route("dashboard/api-keys", "routes/dashboard/api-keys.tsx"),
    route("dashboard/jobs", "routes/dashboard/jobs.tsx"),
    route("dashboard/usage", "routes/dashboard/usage.tsx"),
    route("dashboard/settings", "routes/dashboard/settings.tsx"),
  ]),
] satisfies RouteConfig;
