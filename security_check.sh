#!/bin/bash
# 🔐 Security Check Script
# Scans for API keys and sensitive information before commits

set -e

echo "🔐 Security Check - Scanning for API Keys and Secrets"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }

# Check for common API key patterns
echo "🔍 Scanning for API keys..."

# OpenAI API keys (exclude .env since it's gitignored and SECURITY_GUIDE.md which has redacted examples)
if grep -r "sk-proj-" . --exclude-dir=.git --exclude="security_check.sh" --exclude=".env" --exclude="SECURITY_GUIDE.md" 2>/dev/null; then
    print_error "OpenAI API key found in tracked files!"
    exit 1
else
    print_success "No OpenAI API keys found in tracked files"
fi

# Generic API key patterns (exclude venv and common directories)
if grep -r -E "(api[_-]?key|secret[_-]?key|access[_-]?token)" . --exclude-dir=.git --exclude-dir=venv --exclude-dir=__pycache__ --exclude="security_check.sh" --exclude="SECURITY_GUIDE.md" --exclude=".env" 2>/dev/null | grep -v "your-.*-key-here\|placeholder\|example"; then
    print_warning "Potential API keys or secrets found - please review"
else
    print_success "No suspicious API key patterns found"
fi

# Check .env files are properly ignored
echo ""
echo "🔍 Checking .env file protection..."

if [ -f ".env" ]; then
    if git check-ignore .env >/dev/null 2>&1; then
        print_success ".env file is properly ignored by git"
    else
        print_error ".env file is NOT ignored by git!"
        echo "Add '.env' to your .gitignore file"
        exit 1
    fi
else
    print_warning ".env file not found (this is OK if using environment variables)"
fi

# Check for staged files with secrets
echo ""
echo "🔍 Checking staged files..."

staged_files=$(git diff --cached --name-only 2>/dev/null | grep -v "\.env$" | head -10)
if [ -n "$staged_files" ]; then
    if echo "$staged_files" | xargs grep -l "sk-proj-" 2>/dev/null; then
        print_error "Staged files contain API keys!"
        echo "Remove API keys before committing"
        exit 1
    else
        print_success "No API keys found in staged files"
    fi
else
    print_success "No staged files to check"
fi

# Check template files are safe
echo ""
echo "🔍 Checking template files..."

template_files=$(find . -name "*.template" -o -name "*.example" 2>/dev/null)
if [ -n "$template_files" ]; then
    if echo "$template_files" | xargs grep -l "sk-proj-" 2>/dev/null; then
        print_error "Template files contain real API keys!"
        exit 1
    else
        print_success "Template files are safe"
    fi
else
    print_warning "No template files found"
fi

# Check for common secret file patterns
echo ""
echo "🔍 Checking for secret files..."

secret_patterns=("*.pem" "*.key" "*.p12" "*.pfx" "id_rsa" "id_dsa")
found_secrets=false

for pattern in "${secret_patterns[@]}"; do
    if find . -name "$pattern" -not -path "./.git/*" 2>/dev/null | grep -q .; then
        print_warning "Found potential secret files: $pattern"
        found_secrets=true
    fi
done

if [ "$found_secrets" = false ]; then
    print_success "No secret files found"
fi

# Final summary
echo ""
echo "=================================================="
print_success "Security check completed!"
echo ""
echo "💡 Tips:"
echo "   - Always use .env for local secrets"
echo "   - Keep .env in .gitignore"
echo "   - Use placeholders in template files"
echo "   - Rotate API keys regularly"
echo ""
echo "🔗 See SECURITY_GUIDE.md for more information"
