# Subscription Management Design

## Architecture Overview

The subscription management system integrates Polar.sh for payment processing with Convex for real-time data synchronization and application state management.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Router  │    │    Polar.sh     │    │     Convex      │
│   Application   │◄──►│   Payment API   │◄──►│   Database      │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       │
         │              ┌─────────────────┐              │
         └─────────────►│    Webhooks     │◄─────────────┘
                        │   Processing    │
                        └─────────────────┘
```

## Data Model Design

### Convex Schema

#### Subscriptions Table
```typescript
subscriptions: defineTable({
  userId: v.optional(v.string()),           // Clerk user ID
  polarId: v.optional(v.string()),          // Polar subscription ID
  polarPriceId: v.optional(v.string()),     // Polar price ID
  currency: v.optional(v.string()),         // Billing currency
  interval: v.optional(v.string()),         // Billing interval (month/year)
  status: v.optional(v.string()),           // Subscription status
  currentPeriodStart: v.optional(v.number()), // Current period start timestamp
  currentPeriodEnd: v.optional(v.number()),   // Current period end timestamp
  cancelAtPeriodEnd: v.optional(v.boolean()), // Cancel at period end flag
  amount: v.optional(v.number()),           // Subscription amount
  startedAt: v.optional(v.number()),        // Subscription start timestamp
  endsAt: v.optional(v.number()),           // Subscription end timestamp
  endedAt: v.optional(v.number()),          // Actual end timestamp
  canceledAt: v.optional(v.number()),       // Cancellation timestamp
  customerCancellationReason: v.optional(v.string()),
  customerCancellationComment: v.optional(v.string()),
  metadata: v.optional(v.any()),            // Additional metadata
  customFieldData: v.optional(v.any()),     // Custom field data
  customerId: v.optional(v.string()),       // Polar customer ID
})
.index("userId", ["userId"])
.index("polarId", ["polarId"])
```

#### Webhook Events Table
```typescript
webhookEvents: defineTable({
  type: v.string(),                         // Event type
  polarEventId: v.string(),                 // Polar event ID
  createdAt: v.string(),                    // Event creation timestamp
  modifiedAt: v.string(),                   // Event modification timestamp
  data: v.any(),                           // Event payload data
})
.index("type", ["type"])
.index("polarEventId", ["polarEventId"])
```

## Component Architecture

### 1. Pricing Display Components

#### Pricing Page (`app/routes/pricing.tsx`)
- **Purpose**: Display available subscription plans
- **Responsibilities**:
  - Fetch plans from Polar.sh API
  - Render pricing cards with features
  - Handle plan selection and checkout initiation
  - Show loading states and error handling

#### Pricing Cards (`app/components/homepage/pricing.tsx`)
- **Purpose**: Reusable pricing display component
- **Responsibilities**:
  - Display plan details (price, features, billing interval)
  - Handle subscribe button interactions
  - Show current user's subscription status
  - Adapt UI based on authentication state

### 2. Subscription Management Components

#### Subscription Status (`app/components/subscription-status.tsx`)
- **Purpose**: Display current subscription information
- **Responsibilities**:
  - Show subscription status and details
  - Display billing information and next payment
  - Provide links to customer portal
  - Handle subscription status updates

#### Dashboard Integration
- **Purpose**: Integrate subscription status into dashboard
- **Responsibilities**:
  - Check subscription requirements for route access
  - Display subscription information in navigation
  - Handle subscription-required redirects
  - Show feature availability based on plan

### 3. Webhook Processing System

#### Webhook Handler (`app/routes/webhook/polar.tsx`)
- **Purpose**: Process Polar.sh webhook events
- **Responsibilities**:
  - Validate webhook signatures
  - Parse webhook payloads
  - Update subscription data in Convex
  - Handle idempotency and retry logic

## API Integration Design

### 1. Polar.sh SDK Integration

#### Configuration
```typescript
// Polar.sh client configuration
const polar = new Polar({
  accessToken: process.env.POLAR_ACCESS_TOKEN,
  server: "production", // or "sandbox"
});
```

#### Plan Fetching
```typescript
// Fetch available plans
export const getAvailablePlans = action({
  handler: async () => {
    try {
      const response = await polar.products.list({
        organizationId: process.env.POLAR_ORGANIZATION_ID,
        isArchived: false,
      });
      return response.result?.items || [];
    } catch (error) {
      console.error("Failed to fetch plans:", error);
      return mockPlans; // Fallback to mock data
    }
  },
});
```

#### Checkout Creation
```typescript
// Create checkout session
export const createCheckoutSession = action({
  args: { priceId: v.string(), userId: v.string() },
  handler: async (ctx, { priceId, userId }) => {
    const checkoutSession = await polar.checkouts.create({
      priceId,
      successUrl: `${process.env.FRONTEND_URL}/success`,
      customerEmail: userEmail,
    });
    
    return checkoutSession.url;
  },
});
```

### 2. Convex Functions Design

#### Subscription Status Check
```typescript
export const checkUserSubscriptionStatus = query({
  args: { userId: v.string() },
  handler: async (ctx, { userId }) => {
    const subscription = await ctx.db
      .query("subscriptions")
      .withIndex("userId", (q) => q.eq("userId", userId))
      .filter((q) => q.eq(q.field("status"), "active"))
      .first();

    return {
      hasActiveSubscription: !!subscription,
      subscription,
      planFeatures: subscription ? getPlanFeatures(subscription.polarPriceId) : null,
    };
  },
});
```

#### Subscription Update
```typescript
export const updateSubscription = mutation({
  args: { 
    polarId: v.string(),
    subscriptionData: v.any(),
  },
  handler: async (ctx, { polarId, subscriptionData }) => {
    const existingSubscription = await ctx.db
      .query("subscriptions")
      .withIndex("polarId", (q) => q.eq("polarId", polarId))
      .first();

    if (existingSubscription) {
      await ctx.db.patch(existingSubscription._id, subscriptionData);
    } else {
      await ctx.db.insert("subscriptions", subscriptionData);
    }
  },
});
```

## Webhook Processing Design

### 1. Webhook Validation
```typescript
// Validate webhook signature
function validateWebhookSignature(payload: string, signature: string): boolean {
  const expectedSignature = crypto
    .createHmac('sha256', process.env.POLAR_WEBHOOK_SECRET!)
    .update(payload)
    .digest('hex');
    
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

### 2. Event Processing
```typescript
// Process webhook events
export async function processWebhookEvent(event: PolarWebhookEvent) {
  // Store webhook event for idempotency
  await storeWebhookEvent(event);
  
  switch (event.type) {
    case 'subscription.created':
      await handleSubscriptionCreated(event.data);
      break;
    case 'subscription.updated':
      await handleSubscriptionUpdated(event.data);
      break;
    case 'subscription.cancelled':
      await handleSubscriptionCancelled(event.data);
      break;
    default:
      console.log(`Unhandled webhook event type: ${event.type}`);
  }
}
```

## Security Design

### 1. API Key Management
- Store Polar.sh API keys in environment variables
- Use different keys for development and production
- Implement key rotation procedures
- Monitor API key usage and access

### 2. Webhook Security
- Validate all webhook signatures using HMAC
- Implement replay attack protection
- Use HTTPS for all webhook endpoints
- Log webhook events for audit purposes

### 3. Data Protection
- Encrypt sensitive subscription data at rest
- Implement proper access controls for subscription data
- Audit subscription data access and modifications
- Handle PII according to privacy regulations

## Error Handling Strategy

### 1. API Failures
```typescript
// Graceful API failure handling
async function fetchPlansWithFallback() {
  try {
    return await polar.products.list(params);
  } catch (error) {
    console.error("Polar API error:", error);
    
    // Return cached data or mock data
    return getCachedPlans() || getMockPlans();
  }
}
```

### 2. Webhook Failures
- Implement exponential backoff for webhook retries
- Store failed webhook events for manual processing
- Alert on repeated webhook failures
- Provide webhook replay functionality

### 3. Payment Failures
- Handle declined payments gracefully
- Provide clear error messages to users
- Implement retry logic for temporary failures
- Guide users to update payment methods

## Performance Optimization

### 1. Caching Strategy
- Cache plan data to reduce API calls
- Implement subscription status caching
- Use Convex subscriptions for real-time updates
- Cache customer portal URLs

### 2. Loading States
- Show skeleton screens during data loading
- Implement optimistic updates for UI interactions
- Use React Suspense for component loading
- Provide progress indicators for long operations

### 3. Bundle Optimization
- Code split subscription-related components
- Lazy load Polar.sh SDK
- Optimize webhook processing performance
- Minimize client-side subscription logic

## Integration Patterns

### 1. Authentication Integration
```typescript
// Check subscription in protected routes
export async function loader(args: Route.LoaderArgs) {
  const { userId } = await getAuth(args);
  
  if (!userId) {
    throw redirect("/sign-in");
  }
  
  const subscriptionStatus = await fetchQuery(
    api.subscriptions.checkUserSubscriptionStatus,
    { userId }
  );
  
  if (!subscriptionStatus.hasActiveSubscription) {
    throw redirect("/subscription-required");
  }
  
  return { subscriptionStatus };
}
```

### 2. Feature Flag Integration
```typescript
// Feature availability based on subscription
function useFeatureAccess(feature: string) {
  const { subscription } = useSubscription();
  
  return useMemo(() => {
    if (!subscription) return false;
    
    const planFeatures = getPlanFeatures(subscription.polarPriceId);
    return planFeatures.includes(feature);
  }, [subscription, feature]);
}
```

## Monitoring and Analytics

### 1. Subscription Metrics
- Track subscription conversion rates
- Monitor churn and retention rates
- Measure revenue and growth metrics
- Alert on payment failures and issues

### 2. Technical Metrics
- Monitor API response times and errors
- Track webhook processing success rates
- Measure subscription data sync accuracy
- Alert on system failures and outages

### 3. User Experience Metrics
- Track checkout completion rates
- Monitor customer portal usage
- Measure support ticket volume
- Track user satisfaction scores