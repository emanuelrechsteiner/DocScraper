---
inclusion: fileMatch
fileMatchPattern: "**/*.{test,spec}.{ts,tsx,js,jsx}"
---

# Testing Standards & Patterns

## Component Testing

### React Testing Library Best Practices
- Test user interactions, not implementation details
- Use semantic queries (getByRole, getByLabelText) over test IDs
- Test components as users would interact with them
- Focus on behavior rather than internal state

### Component Test Structure
```tsx
describe('ComponentName', () => {
  it('should render with required props', () => {
    // Arrange
    const props = { /* minimal required props */ };
    
    // Act
    render(<ComponentName {...props} />);
    
    // Assert
    expect(screen.getByRole('button')).toBeInTheDocument();
  });

  it('should handle user interactions correctly', async () => {
    const mockHandler = jest.fn();
    render(<ComponentName onAction={mockHandler} />);
    
    await user.click(screen.getByRole('button'));
    
    expect(mockHandler).toHaveBeenCalledWith(expectedArgs);
  });
});
```

### Convex Function Mocking
- Mock Convex API calls consistently across tests
- Use __mocks__ directory for Convex mocks
- Test both success and error scenarios
- Isolate components from external dependencies

```tsx
// __mocks__/convex/_generated/api.ts
export const api = {
  users: {
    get: jest.fn(),
    create: jest.fn(),
    update: jest.fn(),
  },
};
```

## Integration Testing

### User Workflow Testing
- Test complete user journeys end-to-end
- Use Playwright for browser automation
- Test authentication flows thoroughly
- Validate multi-tenant data isolation

### API Integration Tests
```tsx
describe('API Integration', () => {
  beforeEach(() => {
    // Setup test data and authentication
  });

  it('should fetch data for authenticated user', async () => {
    const result = await convex.query(api.users.list);
    
    expect(result).toHaveLength(expectedCount);
    expect(result[0]).toMatchObject({
      _id: expect.any(String),
      name: expect.any(String),
      email: expect.any(String),
    });
  });
});
```

## Security Testing

### Authentication Testing
- Test unauthorized access attempts
- Validate role-based access controls
- Test session expiration handling
- Verify proper error messages without information leakage

### Input Validation Testing
```tsx
describe('Input Validation', () => {
  it('should sanitize HTML input', () => {
    const maliciousInput = '<script>alert("xss")</script>';
    const sanitized = sanitizeHtml(maliciousInput);
    
    expect(sanitized).not.toContain('<script>');
    expect(sanitized).toBe('');
  });

  it('should validate file uploads', () => {
    const invalidFile = new File(['content'], 'test.exe', { type: 'application/exe' });
    
    expect(() => validateDashboardFile(invalidFile)).toThrow('Invalid file type');
  });
});
```

## Performance Testing

### Component Performance
- Test component rendering performance with large datasets
- Validate memoization effectiveness
- Test lazy loading behavior
- Monitor bundle size impact

### Load Testing
```tsx
describe('Performance Tests', () => {
  it('should handle large dashboard lists efficiently', () => {
    const largeDashboardList = generateMockDashboards(1000);
    
    const startTime = performance.now();
    render(<DashboardGrid dashboards={largeDashboardList} />);
    const endTime = performance.now();
    
    expect(endTime - startTime).toBeLessThan(100); // 100ms threshold
  });
});
```

## Test Organization

### File Structure
- Place test files adjacent to source files
- Use descriptive test file names: `ComponentName.test.tsx`
- Group related tests in describe blocks
- Use clear, descriptive test names

### Test Data Management
- Use factories for generating test data
- Keep test data minimal and focused
- Use realistic but safe test data
- Avoid hardcoded values in assertions

### Mock Management
```tsx
// tests/utils/mockFactories.ts
export const createMockUser = (overrides = {}) => ({
  _id: 'user-123' as Id<'users'>,
  email: 'test@example.com',
  name: 'Test User',
  _creationTime: Date.now(),
  ...overrides,
});

export const createMockPost = (overrides = {}) => ({
  _id: 'post-789' as Id<'posts'>,
  title: 'Test Post',
  content: 'Test content',
  authorId: 'user-123' as Id<'users'>,
  _creationTime: Date.now(),
  ...overrides,
});
```

## Coverage Requirements

### Minimum Coverage Targets
- Unit tests: 80% line coverage minimum
- Integration tests: Cover all critical user paths
- Security tests: 100% coverage for auth and validation logic
- Performance tests: Cover high-traffic components

### Coverage Exclusions
- Configuration files
- Type definitions
- Test utilities
- Third-party library wrappers

## Continuous Integration

### Test Automation
- Run all tests on every pull request
- Block merges if tests fail
- Generate coverage reports automatically
- Run security scans with tests

### Test Environment
- Use Convex's testing utilities for consistent testing
- Reset test data between test runs
- Use environment-specific configurations
- Maintain test database isolation with proper cleanup