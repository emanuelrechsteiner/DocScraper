const requiredEnvVars = [
  "VITE_CLERK_PUBLISHABLE_KEY",
  "CLERK_SECRET_KEY",
  "VITE_PARSIFY_API_URL",
] as const;

export function validateEnvironment() {
  const missing = requiredEnvVars.filter((key) => !process.env[key]);

  if (missing.length > 0) {
    throw new Error(
      `Missing required environment variables: ${missing.join(", ")}`
    );
  }
}
