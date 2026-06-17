# Dashboard System Design

## Architecture Overview

The dashboard system follows a component-based architecture with real-time data synchronization, responsive design, and modular feature organization.

```
┌─────────────────────────────────────────────────────────────┐
│                    Dashboard Layout                         │
├─────────────────┬───────────────────────────────────────────┤
│   Sidebar       │              Main Content Area           │
│   Navigation    │                                          │
│                 │  ┌─────────────────────────────────────┐ │
│  • Overview     │  │         Route-Specific Content      │ │
│  • Chat         │  │                                     │ │
│  • Settings     │  │  • Dashboard Overview               │ │
│  • Billing      │  │  • AI Chat Interface               │ │
│                 │  │  • Settings Forms                  │ │
│  User Profile   │  │  • Analytics Charts               │ │
│  Subscription   │  │                                     │ │
│  Status         │  └─────────────────────────────────────┘ │
└─────────────────┴───────────────────────────────────────────┘
```

## Component Architecture

### 1. Layout Components

#### Dashboard Layout (`app/routes/dashboard/layout.tsx`)
- **Purpose**: Main layout wrapper for all dashboard pages
- **Responsibilities**:
  - Authentication and subscription verification
  - Sidebar and header layout management
  - User data loading and context provision
  - Route protection and access control

#### App Sidebar (`app/components/dashboard/app-sidebar.tsx`)
- **Purpose**: Navigation sidebar with collapsible design
- **Responsibilities**:
  - Navigation menu rendering
  - User profile display
  - Subscription status indicator
  - Mobile-responsive behavior

#### Site Header (`app/components/dashboard/site-header.tsx`)
- **Purpose**: Top header with breadcrumbs and actions
- **Responsibilities**:
  - Breadcrumb navigation
  - User actions (notifications, settings)
  - Mobile menu toggle
  - Search functionality

### 2. Navigation Components

#### Nav Main (`app/components/dashboard/nav-main.tsx`)
- **Purpose**: Primary navigation menu items
- **Responsibilities**:
  - Main navigation links (Overview, Chat, Settings)
  - Active state management
  - Icon and label rendering
  - Keyboard navigation support

#### Nav Secondary (`app/components/dashboard/nav-secondary.tsx`)
- **Purpose**: Secondary navigation and utility links
- **Responsibilities**:
  - Help and support links
  - Documentation access
  - Feedback mechanisms
  - External resource links

#### Nav User (`app/components/dashboard/nav-user.tsx`)
- **Purpose**: User profile and account management
- **Responsibilities**:
  - User avatar and name display
  - Account dropdown menu
  - Sign-out functionality
  - Profile quick actions

### 3. Dashboard Pages

#### Dashboard Overview (`app/routes/dashboard/index.tsx`)
- **Purpose**: Main dashboard landing page
- **Responsibilities**:
  - Key metrics display
  - Recent activity summary
  - Quick action buttons
  - Status indicators

#### Chat Interface (`app/routes/dashboard/chat.tsx`)
- **Purpose**: AI chat functionality
- **Responsibilities**:
  - Chat message interface
  - Real-time message streaming
  - Chat history management
  - File upload capabilities

#### Settings Page (`app/routes/dashboard/settings.tsx`)
- **Purpose**: User settings and preferences
- **Responsibilities**:
  - Profile information editing
  - Notification preferences
  - Security settings
  - Account management

## Data Flow Architecture

### 1. Real-time Data Synchronization

```typescript
// Convex subscription pattern for real-time updates
function useRealtimeSubscription(userId: string) {
  const subscription = useQuery(api.subscriptions.checkUserSubscriptionStatus, {
    userId,
  });
  
  const user = useQuery(api.users.findUserByToken, {
    tokenIdentifier: userId,
  });
  
  return { subscription, user };
}
```

### 2. State Management Pattern

```typescript
// Dashboard context for shared state
interface DashboardContextType {
  user: User | null;
  subscription: Subscription | null;
  sidebarOpen: boolean;
  setSidebarOpen: (open: boolean) => void;
  theme: 'light' | 'dark';
  setTheme: (theme: 'light' | 'dark') => void;
}

const DashboardContext = createContext<DashboardContextType>();
```

### 3. Loading and Error States

```typescript
// Unified loading state management
interface LoadingState {
  isLoading: boolean;
  error: string | null;
  data: any;
}

function useAsyncData<T>(queryFn: () => Promise<T>) {
  const [state, setState] = useState<LoadingState>({
    isLoading: true,
    error: null,
    data: null,
  });
  
  // Implementation with error handling and loading states
}
```

## UI/UX Design System

### 1. Design Tokens

```css
/* Dashboard-specific design tokens */
:root {
  --sidebar-width: 288px;
  --sidebar-width-collapsed: 64px;
  --header-height: 64px;
  --content-padding: 24px;
  
  /* Dashboard colors */
  --dashboard-bg: hsl(var(--background));
  --sidebar-bg: hsl(var(--card));
  --nav-item-hover: hsl(var(--accent));
  --nav-item-active: hsl(var(--primary));
}
```

### 2. Responsive Breakpoints

```typescript
// Responsive design breakpoints
const breakpoints = {
  mobile: '640px',
  tablet: '768px',
  desktop: '1024px',
  wide: '1280px',
} as const;

// Sidebar behavior by breakpoint
const sidebarBehavior = {
  mobile: 'overlay',     // Overlay on mobile
  tablet: 'collapsible', // Collapsible on tablet
  desktop: 'persistent', // Always visible on desktop
} as const;
```

### 3. Animation System

```typescript
// Motion variants for dashboard animations
const sidebarVariants = {
  open: {
    width: 'var(--sidebar-width)',
    transition: { duration: 0.2, ease: 'easeOut' },
  },
  closed: {
    width: 'var(--sidebar-width-collapsed)',
    transition: { duration: 0.2, ease: 'easeOut' },
  },
};

const contentVariants = {
  enter: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.3, ease: 'easeOut' },
  },
  exit: {
    opacity: 0,
    y: 20,
    transition: { duration: 0.2, ease: 'easeIn' },
  },
};
```

## Component Design Patterns

### 1. Compound Component Pattern

```typescript
// Dashboard card compound component
interface DashboardCardProps {
  children: React.ReactNode;
  className?: string;
}

function DashboardCard({ children, className }: DashboardCardProps) {
  return (
    <Card className={cn('dashboard-card', className)}>
      {children}
    </Card>
  );
}

DashboardCard.Header = function CardHeader({ children }: { children: React.ReactNode }) {
  return <CardHeader className="dashboard-card-header">{children}</CardHeader>;
};

DashboardCard.Content = function CardContent({ children }: { children: React.ReactNode }) {
  return <CardContent className="dashboard-card-content">{children}</CardContent>;
};
```

### 2. Hook-based Data Management

```typescript
// Custom hooks for dashboard functionality
function useDashboardData(userId: string) {
  const user = useQuery(api.users.findUserByToken, { tokenIdentifier: userId });
  const subscription = useQuery(api.subscriptions.checkUserSubscriptionStatus, { userId });
  const analytics = useQuery(api.analytics.getUserAnalytics, { userId });
  
  return {
    user,
    subscription,
    analytics,
    isLoading: user === undefined || subscription === undefined,
    hasError: user === null || subscription === null,
  };
}

function useSidebarState() {
  const [isOpen, setIsOpen] = useState(true);
  const [isMobile, setIsMobile] = useState(false);
  
  useEffect(() => {
    const checkMobile = () => setIsMobile(window.innerWidth < 768);
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);
  
  return { isOpen, setIsOpen, isMobile };
}
```

### 3. Error Boundary Pattern

```typescript
// Dashboard-specific error boundary
class DashboardErrorBoundary extends Component<
  { children: React.ReactNode },
  { hasError: boolean; error: Error | null }
> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  
  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Dashboard error:', error, errorInfo);
    // Log to monitoring service
  }
  
  render() {
    if (this.state.hasError) {
      return <DashboardErrorFallback error={this.state.error} />;
    }
    
    return this.props.children;
  }
}
```

## Performance Optimization

### 1. Code Splitting Strategy

```typescript
// Lazy loading for dashboard routes
const DashboardOverview = lazy(() => import('./routes/dashboard/index'));
const ChatInterface = lazy(() => import('./routes/dashboard/chat'));
const SettingsPage = lazy(() => import('./routes/dashboard/settings'));

// Route configuration with lazy loading
export const dashboardRoutes = [
  {
    path: 'dashboard',
    element: <DashboardLayout />,
    children: [
      {
        index: true,
        element: (
          <Suspense fallback={<DashboardSkeleton />}>
            <DashboardOverview />
          </Suspense>
        ),
      },
      // ... other routes
    ],
  },
];
```

### 2. Memoization Strategy

```typescript
// Memoized components for performance
const MemoizedSidebar = memo(AppSidebar, (prevProps, nextProps) => {
  return (
    prevProps.user?.id === nextProps.user?.id &&
    prevProps.isOpen === nextProps.isOpen
  );
});

const MemoizedChart = memo(ChartComponent, (prevProps, nextProps) => {
  return JSON.stringify(prevProps.data) === JSON.stringify(nextProps.data);
});
```

### 3. Virtual Scrolling for Large Lists

```typescript
// Virtual scrolling for chat history or large data sets
function VirtualizedChatHistory({ messages }: { messages: Message[] }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [visibleRange, setVisibleRange] = useState({ start: 0, end: 50 });
  
  const visibleMessages = useMemo(() => {
    return messages.slice(visibleRange.start, visibleRange.end);
  }, [messages, visibleRange]);
  
  // Virtual scrolling implementation
  return (
    <div ref={containerRef} className="chat-history-container">
      {visibleMessages.map((message) => (
        <ChatMessage key={message.id} message={message} />
      ))}
    </div>
  );
}
```

## Accessibility Design

### 1. Keyboard Navigation

```typescript
// Keyboard navigation for sidebar
function useSidebarKeyboardNavigation() {
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.ctrlKey || event.metaKey) {
        switch (event.key) {
          case 'b':
            event.preventDefault();
            toggleSidebar();
            break;
          case '1':
            event.preventDefault();
            navigateTo('/dashboard');
            break;
          case '2':
            event.preventDefault();
            navigateTo('/dashboard/chat');
            break;
          // ... other shortcuts
        }
      }
    };
    
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);
}
```

### 2. Screen Reader Support

```typescript
// ARIA labels and descriptions for dashboard components
function AccessibleNavItem({ 
  href, 
  icon: Icon, 
  label, 
  isActive, 
  badge 
}: NavItemProps) {
  return (
    <Link
      to={href}
      className={cn('nav-item', { 'nav-item-active': isActive })}
      aria-current={isActive ? 'page' : undefined}
      aria-describedby={badge ? `${label}-badge` : undefined}
    >
      <Icon className="nav-item-icon" aria-hidden="true" />
      <span className="nav-item-label">{label}</span>
      {badge && (
        <Badge 
          id={`${label}-badge`}
          className="nav-item-badge"
          aria-label={`${badge} notifications`}
        >
          {badge}
        </Badge>
      )}
    </Link>
  );
}
```

### 3. Focus Management

```typescript
// Focus management for modal and drawer components
function useFocusManagement(isOpen: boolean) {
  const previousFocusRef = useRef<HTMLElement | null>(null);
  const containerRef = useRef<HTMLElement>(null);
  
  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement as HTMLElement;
      
      // Focus first focusable element in container
      const firstFocusable = containerRef.current?.querySelector(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      ) as HTMLElement;
      
      firstFocusable?.focus();
    } else {
      // Restore focus to previous element
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);
  
  return containerRef;
}
```

## Security Considerations

### 1. Data Sanitization

```typescript
// Sanitize user input in dashboard forms
function sanitizeUserInput(input: string): string {
  return DOMPurify.sanitize(input, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong'],
    ALLOWED_ATTR: [],
  });
}

// Validate and sanitize form data
function validateProfileForm(data: ProfileFormData): ValidationResult {
  const sanitized = {
    name: sanitizeUserInput(data.name),
    bio: sanitizeUserInput(data.bio),
    email: validator.isEmail(data.email) ? data.email : '',
  };
  
  return { isValid: true, data: sanitized, errors: [] };
}
```

### 2. Route Protection

```typescript
// Enhanced route protection with feature flags
async function protectDashboardRoute(
  userId: string,
  requiredFeatures: string[] = []
) {
  const [user, subscription] = await Promise.all([
    fetchQuery(api.users.findUserByToken, { tokenIdentifier: userId }),
    fetchQuery(api.subscriptions.checkUserSubscriptionStatus, { userId }),
  ]);
  
  if (!user) {
    throw redirect('/sign-in');
  }
  
  if (!subscription?.hasActiveSubscription) {
    throw redirect('/subscription-required');
  }
  
  // Check feature access
  for (const feature of requiredFeatures) {
    if (!hasFeatureAccess(subscription, feature)) {
      throw redirect('/upgrade-required');
    }
  }
  
  return { user, subscription };
}
```

## Testing Strategy

### 1. Component Testing

```typescript
// Dashboard component testing utilities
function renderDashboardComponent(
  component: React.ReactElement,
  options: {
    user?: User;
    subscription?: Subscription;
    initialRoute?: string;
  } = {}
) {
  const mockUser = options.user || createMockUser();
  const mockSubscription = options.subscription || createMockSubscription();
  
  return render(
    <MemoryRouter initialEntries={[options.initialRoute || '/dashboard']}>
      <DashboardContext.Provider value={{
        user: mockUser,
        subscription: mockSubscription,
        sidebarOpen: true,
        setSidebarOpen: jest.fn(),
        theme: 'light',
        setTheme: jest.fn(),
      }}>
        {component}
      </DashboardContext.Provider>
    </MemoryRouter>
  );
}
```

### 2. Integration Testing

```typescript
// Dashboard integration tests
describe('Dashboard Integration', () => {
  it('should load user data and display dashboard', async () => {
    const { getByText, getByRole } = renderDashboardComponent(<DashboardLayout />);
    
    await waitFor(() => {
      expect(getByText('Welcome back')).toBeInTheDocument();
      expect(getByRole('navigation')).toBeInTheDocument();
    });
  });
  
  it('should handle subscription status changes', async () => {
    const { rerender } = renderDashboardComponent(<DashboardLayout />, {
      subscription: createMockSubscription({ status: 'active' }),
    });
    
    // Test subscription status update
    rerender(<DashboardLayout />);
    
    await waitFor(() => {
      expect(screen.getByText('Pro Plan')).toBeInTheDocument();
    });
  });
});
```