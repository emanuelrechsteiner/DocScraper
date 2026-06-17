---
inclusion: always
---

# Project Structure & Organization

## Root Directory Structure

```
/
├── .kiro/                    # Kiro configuration and specs
│   ├── specs/               # Project specifications
│   ├── steering/            # AI steering rules
│   └── hooks/               # Agent hooks for automated workflows
├── src/                     # Frontend source code
│   ├── app/                 # Next.js app router pages
│   ├── components/          # React components (max 150 lines per file)
│   ├── lib/                 # Utility functions and configurations
│   ├── hooks/               # Custom React hooks
│   └── types/               # TypeScript type definitions
├── convex/                  # Convex backend functions and schema
│   ├── _generated/          # Auto-generated Convex files
│   ├── functions/           # Backend function implementations
│   ├── schema.ts            # Database schema definitions
│   └── auth.config.ts       # Authentication configuration
├── public/                  # Static assets
└── tests/                   # Test files
```

## File Size Guidelines

- **Maximum 150 lines per file** - refactor into smaller modules if exceeded
- **One component per file** - maintain clear separation of concerns
- **Semantic file naming** - use descriptive names that reflect functionality

## Component Organization

### Component Categories
- **ui/**: Base shadcn/ui components and custom foundational components
- **auth/**: Authentication-related components
- **layout/**: Navigation, headers, and layout components
- **forms/**: Form components and input handling
- **data/**: Data display and visualization components
- **common/**: Shared utility components

## Naming Conventions

### Files and Directories
- **Components**: PascalCase (e.g., `DashboardCard.tsx`)
- **Pages**: kebab-case directories with `page.tsx` files
- **Convex Functions**: camelCase with descriptive names (e.g., `getUser.ts`, `createPost.ts`)
- **Types**: camelCase with `.ts` extension (e.g., `dashboard.ts`)
- **Hooks**: camelCase starting with "use" (e.g., `useAuth.ts`)

### Code Conventions
- **Interfaces**: PascalCase with descriptive names (e.g., `UserProfile`, `PostMetadata`)
- **Enums**: PascalCase with UPPER_CASE values (e.g., `UserRole.ADMIN`)
- **Functions**: camelCase with verb-noun pattern (e.g., `createUser`, `updatePost`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_FILE_SIZE`, `API_ENDPOINTS`)

## Import Organization

### Import Order
1. React and Next.js imports
2. Third-party library imports
3. Convex imports (api, functions)
4. Internal utility and hook imports
5. Component imports
6. Type imports
7. Relative imports

### Path Aliases
```typescript
// tsconfig.json paths
{
  "@/*": ["./src/*"],
  "@/components/*": ["./src/components/*"],
  "@/lib/*": ["./src/lib/*"],
  "@/hooks/*": ["./src/hooks/*"],
  "@/types/*": ["./src/types/*"]
}
```