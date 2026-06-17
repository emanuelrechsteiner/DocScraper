---
inclusion: fileMatch
fileMatchPattern: "src/**/*.{ts,tsx,js,jsx}"
---

# Code Conventions & Patterns

## Component Structure

### React/Next.js Components
- Use functional components with TypeScript interfaces
- Example: `const MyComponent: React.FC<MyComponentProps> = ({ prop1, prop2 }) => { ... }`
- Declare prop interfaces outside component: `interface MyComponentProps { ... }`
- Maximum 150 lines per file - refactor if larger

### Component File Organization
- One component per file
- Name files same as component (PascalCase)
- Group related components in directories
- Follow the established src/ structure

## State Management

### Local State
- Use useState for component-specific state
- Define state at top of component
- Use semantic naming: `const [isLoading, setIsLoading] = useState(false)`

### Global State (Zustand)
- Use for cross-component state (auth, user preferences)
- Define stores in separate files
- Provide descriptive store names

## Data Fetching & Firebase Integration

### Firebase Patterns
- Use service layer functions, don't call Firebase directly in components
- Handle loading states with explicit variables
- Implement proper error handling
- Example:
```tsx
const [isLoading, setIsLoading] = useState(true);
const [error, setError] = useState<Error | null>(null);

useEffect(() => {
  const fetchData = async () => {
    try {
      setIsLoading(true);
      const data = await dashboardService.fetchDashboards();
      setDashboards(data);
    } catch (err) {
      setError(err as Error);
    } finally {
      setIsLoading(false);
    }
  };
  
  fetchData();
}, [dependencies]);
```

### React Query Integration
- Use for server state management
- Implement proper cache invalidation
- Handle loading and error states consistently

## UI Patterns

### Conditional Rendering
- Use ternary operators for simple conditions
- Use guard clauses for early returns
- Use element variables for complex conditions

### Form Handling
- Use react-hook-form for form management
- Implement proper validation with clear error messages
- Display field-specific errors inline

### Lists and Iterations
- Always provide unique `key` prop
- Use array index as last resort only
- Prefer map over forEach/for loops

## Error Handling

### Component Errors
- Use try/catch blocks for async operations
- Display user-friendly error messages
- Log errors for debugging
- Consider implementing error boundaries

### API Error Handling
```tsx
try {
  const data = await apiService.fetchData();
  setData(data);
} catch (error) {
  if (error instanceof NetworkError) {
    setError('Connection issue. Please check your internet.');
  } else {
    setError('Failed to load data. Please try again.');
    console.error('API Error:', error);
  }
  setIsLoading(false);
}
```

## Styling Conventions

### Tailwind CSS Usage
- Use utility classes directly in JSX
- Group related utilities with consistent ordering
- Example: `className="flex items-center justify-between p-4 bg-primary-500 text-white"`

### Responsive Design
- Mobile-first approach using Tailwind breakpoints
- Example: `className="text-sm md:text-base lg:text-lg"`

### Component Styling
```tsx
// Use cn() utility for conditional classes
import { cn } from '@/lib/utils';

<button className={cn(
  "px-4 py-2 rounded-md font-medium transition-colors",
  variant === 'primary' && "bg-blue-600 text-white hover:bg-blue-700",
  variant === 'secondary' && "bg-gray-200 text-gray-900 hover:bg-gray-300",
  disabled && "opacity-50 cursor-not-allowed"
)}>
```

## Security Patterns

### Authentication
- Always check authentication state before accessing protected resources
- Use Firebase Auth with proper error handling
- Implement role-based access control (RBAC)

### Data Sanitization
- Sanitize all HTML content before rendering
- Use Content Security Policy for iframe rendering
- Validate all user inputs

### Environment Variables
- Use NEXT_PUBLIC_ prefix for client-side variables
- Never commit .env files with real values
- Validate required environment variables on startup

## Performance Optimization

### Memoization
- Use React.memo for expensive component renders
- Use useMemo for expensive calculations
- Use useCallback for functions passed as props

### Code Splitting
- Use dynamic imports for large components
- Implement lazy loading for routes
- Optimize bundle size with proper imports