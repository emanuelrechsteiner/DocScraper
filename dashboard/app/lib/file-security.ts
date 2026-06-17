// File security utilities for safe file handling

/**
 * Validate file type and content for security
 */
export function validateFileType(file: File): { valid: boolean; error?: string } {
  const allowedTypes = new Set([
    'image/jpeg',
    'image/png',
    'image/webp',
    'image/gif',
    'text/plain',
    'text/markdown',
    'application/pdf',
    'application/json',
  ]);

  const allowedExtensions = new Set([
    '.jpg', '.jpeg', '.png', '.webp', '.gif',
    '.txt', '.md', '.pdf', '.json'
  ]);

  // Check MIME type
  if (!allowedTypes.has(file.type)) {
    return { 
      valid: false, 
      error: `File type ${file.type} is not allowed` 
    };
  }

  // Check file extension
  const extension = file.name.toLowerCase().split('.').pop();
  if (!extension || !allowedExtensions.has(`.${extension}`)) {
    return { 
      valid: false, 
      error: `File extension .${extension} is not allowed` 
    };
  }

  return { valid: true };
}

/**
 * Validate file size limits
 */
export function validateFileSize(file: File): { valid: boolean; error?: string } {
  const maxSizes = {
    'image/jpeg': 5 * 1024 * 1024,    // 5MB for images
    'image/png': 5 * 1024 * 1024,     // 5MB for images
    'image/webp': 5 * 1024 * 1024,    // 5MB for images
    'image/gif': 2 * 1024 * 1024,     // 2MB for GIFs
    'text/plain': 1 * 1024 * 1024,    // 1MB for text
    'text/markdown': 1 * 1024 * 1024, // 1MB for markdown
    'application/pdf': 10 * 1024 * 1024, // 10MB for PDFs
    'application/json': 1 * 1024 * 1024,  // 1MB for JSON
  };

  const maxSize = maxSizes[file.type as keyof typeof maxSizes] || 1024 * 1024; // 1MB default

  if (file.size > maxSize) {
    return { 
      valid: false, 
      error: `File size ${(file.size / 1024 / 1024).toFixed(2)}MB exceeds limit of ${(maxSize / 1024 / 1024).toFixed(2)}MB` 
    };
  }

  return { valid: true };
}

/**
 * Sanitize filename for safe storage
 */
export function sanitizeFilename(filename: string): string {
  // Remove dangerous characters and limit length
  return filename
    .replace(/[^a-zA-Z0-9.-]/g, '_')
    .replace(/_{2,}/g, '_')
    .slice(0, 100);
}

/**
 * Comprehensive file validation
 */
export function validateFile(file: File): { valid: boolean; error?: string } {
  // Check file type
  const typeValidation = validateFileType(file);
  if (!typeValidation.valid) {
    return typeValidation;
  }

  // Check file size
  const sizeValidation = validateFileSize(file);
  if (!sizeValidation.valid) {
    return sizeValidation;
  }

  // Additional security checks
  if (file.name.includes('..') || file.name.includes('/') || file.name.includes('\\')) {
    return { 
      valid: false, 
      error: 'Filename contains invalid characters' 
    };
  }

  return { valid: true };
}

/**
 * Generate secure file access URL with expiration
 */
export function generateSecureFileUrl(fileId: string, expiresIn: number = 3600): string {
  // This would integrate with Convex file storage
  // For now, return a placeholder that shows the pattern
  const timestamp = Date.now() + (expiresIn * 1000);
  return `/api/files/${fileId}?expires=${timestamp}`;
}