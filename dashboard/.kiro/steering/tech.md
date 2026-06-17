---
inclusion: always
---

# Technology Stack & Build System

## Frontend Stack

- **Framework**: Next.js 14 with TypeScript for type safety and modern development
- **Styling**: Tailwind CSS v4 for responsive, utility-first styling with modern features
- **UI Components**: shadcn/ui components for consistent, accessible UI components
- **State Management**: Zustand for lightweight state management
- **Data Fetching**: React Query for efficient data fetching and caching
- **Forms**: react-hook-form for form management and validation

## Backend & Services

- **Backend**: Convex for serverless backend functions with TypeScript
- **Authentication**: Convex Auth or integrated authentication provider
- **Database**: Convex database with real-time subscriptions and ACID transactions
- **File Storage**: Convex file storage for application assets
- **Security**: Convex function-level access control and data validation

## Development Tools

- **Language**: TypeScript throughout the entire stack
- **Linting**: ESLint with strict configuration
- **Formatting**: Prettier for consistent code formatting
- **Testing**: Jest with React Testing Library for unit tests, Playwright for E2E tests

## Architecture Patterns

- **Component-First Development**: Build UI components in isolation before application assembly
- **Function-First Backend**: Design Convex functions as pure, testable units
- **Real-time Data Flow**: Leverage Convex subscriptions for live data updates
- **Type-Safe API**: End-to-end TypeScript from database to UI components

## Security Considerations

- Validate and sanitize all user inputs at the function level
- Use Convex function-level access control for data security
- Implement Content Security Policy headers for XSS prevention
- Use HTTPS for all communications
- Implement proper session management with secure authentication

## Performance Requirements

- Components must not exceed 150 lines per file
- Use React.memo, useMemo, and useCallback for optimization
- Implement code splitting and lazy loading
- Optimize bundle size with proper imports