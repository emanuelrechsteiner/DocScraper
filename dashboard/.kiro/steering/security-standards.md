---
inclusion: fileMatch
fileMatchPattern: "**/*.{ts,tsx,js,jsx,json,rules}"
---

# Security Standards & Guidelines

## Authentication & Authorization

### Authentication Implementation
- Always verify authentication state before accessing protected resources
- Use Convex Auth or integrated auth provider with proper error handling
- Implement role-based access control (RBAC) appropriate to your application
- Validate user permissions in Convex functions before data operations

### Session Management
- Implement proper token refresh mechanisms
- Use secure session storage practices
- Handle authentication state changes gracefully
- Implement automatic logout on token expiration

## Data Protection

### Input Validation & Sanitization
- Validate all user inputs in Convex functions using validators
- Sanitize any HTML or rich content before storage and rendering
- Use TypeScript interfaces and Convex validators for type safety
- Implement proper form validation with react-hook-form on the client

### XSS Prevention
- Use Content Security Policy headers for enhanced security
- Sanitize any user-generated HTML content before display
- Avoid dangerouslySetInnerHTML unless absolutely necessary
- Implement proper escaping for all user-generated content

### Data Access Control
- Implement proper data access validation in Convex functions
- Use Convex's built-in authentication context for user verification
- Validate user permissions before any database operations
- Implement data filtering based on user roles and ownership

## API Security

### Convex Functions Security
- Use Convex's built-in authentication context in all functions
- Validate user permissions before executing any operations
- Implement rate limiting where appropriate
- Avoid information disclosure in error messages

### Environment Variables
- Use NEXT_PUBLIC_ prefix only for client-side variables
- Never commit .env files with real values to version control
- Validate required environment variables on application startup
- Use secure secrets management for sensitive data

## File Security

### File Upload Security
- Validate file types and sizes before upload
- Scan uploaded content for malicious content
- Use Convex file storage with proper access controls
- Implement virus scanning for user uploads where necessary

### Storage Access Controls
- Use Convex's file storage with function-level access control
- Validate file ownership before serving content
- Implement proper file access permissions
- Use Convex's built-in file serving with authentication

## Infrastructure Security

### HTTPS & Transport Security
- Enforce HTTPS for all communications
- Implement proper security headers
- Use secure cookie settings
- Implement HSTS headers

### Database Security
- Implement access control in Convex functions for all operations
- Use Convex validators to ensure data structure integrity
- Validate user permissions before any database mutations
- Implement audit logging for sensitive operations

## Security Best Practices

### Code Review Requirements
- All authentication and authorization code must be reviewed
- Security-sensitive changes require additional review
- Test security controls with both positive and negative cases
- Document security decisions and rationale

### Vulnerability Prevention
- Regularly update dependencies to patch security vulnerabilities
- Use automated security scanning tools
- Implement proper error handling without information leakage
- Follow OWASP security guidelines

### Audit & Monitoring
- Log all authentication and authorization events
- Monitor for suspicious activity patterns
- Implement proper error tracking and alerting
- Maintain audit trails for compliance requirements