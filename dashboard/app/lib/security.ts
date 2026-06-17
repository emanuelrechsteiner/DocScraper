// Security utilities for the application

import DOMPurify from 'isomorphic-dompurify';

/**
 * Sanitize user input to prevent XSS attacks
 */
export function sanitizeInput(input: string | undefined | null): string | undefined {
  if (!input) return undefined;
  
  return DOMPurify.sanitize(input, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p'],
    ALLOWED_ATTR: [],
  });
}

/**
 * Validate file uploads for security
 */
export function validateFileUpload(file: File): { valid: boolean; error?: string } {
  const maxSize = 10 * 1024 * 1024; // 10MB
  const allowedTypes = [
    'image/jpeg',
    'image/png', 
    'image/webp',
    'text/plain',
    'text/markdown',
    'application/pdf',
  ];
  
  if (file.size > maxSize) {
    return { valid: false, error: 'File size exceeds 10MB limit' };
  }
  
  if (!allowedTypes.includes(file.type)) {
    return { valid: false, error: 'File type not supported' };
  }
  
  return { valid: true };
}

/**
 * Security headers for enhanced protection
 */
export const securityHeaders = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY', 
  'X-XSS-Protection': '1; mode=block',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=()',
} as const;

/**
 * Rate limiting configuration
 */
export const rateLimits = {
  // API calls per minute
  api: 100,
  // Authentication attempts per minute
  auth: 10,
  // File uploads per hour
  upload: 20,
} as const;

/**
 * Validate webhook signatures for security
 */
export function validateWebhookSignature(
  payload: string,
  signature: string,
  secret: string
): boolean {
  if (!signature || !secret) return false;
  
  try {
    const crypto = require('crypto');
    const expectedSignature = crypto
      .createHmac('sha256', secret)
      .update(payload)
      .digest('hex');
      
    return crypto.timingSafeEqual(
      Buffer.from(signature),
      Buffer.from(expectedSignature)
    );
  } catch (error) {
    console.error('Webhook signature validation failed:', error);
    return false;
  }
}

/**
 * Log security events for audit purposes
 */
export function logSecurityEvent(event: {
  userId: string;
  action: string;
  resource: string;
  success: boolean;
  details?: Record<string, any>;
}) {
  console.log('Security Event:', {
    ...event,
    timestamp: new Date().toISOString(),
  });
}