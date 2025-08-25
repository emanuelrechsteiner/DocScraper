# 🔐 Security Guide - API Keys & Environment Variables

## 🚨 CRITICAL: Never Commit API Keys!

### ❌ **What NOT to do:**
- Never put real API keys in `.env.example` or `.env.template`
- Never commit `.env` files to version control
- Never hardcode API keys in source code
- Never share API keys in documentation or screenshots

### ✅ **What TO do:**
- Use placeholder values in example files
- Keep real API keys in `.env` (which is gitignored)
- Use environment variables for all secrets
- Rotate API keys regularly

## 📁 File Security

### **Safe Files (can be committed):**
- `.env.template` - Contains placeholder values only
- `.env.example` - Contains placeholder values only
- `.gitignore` - Protects sensitive files

### **Dangerous Files (NEVER commit):**
- `.env` - Contains real API keys
- `.env.local` - Contains real secrets
- Any file with actual API keys

## 🛡️ Current Protection

### **`.gitignore` Protection:**
```gitignore
# Environment files - NEVER commit API keys!
.env
.env.local
.env.*.local
*.env

# API Keys and secrets
*api_key*
*secret*
*token*
```

### **Template Structure:**
```bash
# .env.template (safe to commit)
OPENAI_API_KEY=your-openai-api-key-here

# .env (NEVER commit)
OPENAI_API_KEY=sk-proj-[ACTUAL-KEY-REDACTED]
```

## 🔧 Setup Process

### **For Developers:**
1. **Copy template**: `cp .env.template .env`
2. **Add real keys**: Edit `.env` with actual API keys
3. **Never commit**: `.env` is automatically ignored

### **For Repository Maintainers:**
1. **Check templates**: Ensure no real keys in example files
2. **Review commits**: Never merge commits with API keys
3. **Update .gitignore**: Keep protection rules current

## 🧪 Security Validation

### **Before Committing:**
```bash
# Check for API keys in staged files
git diff --cached | grep -i "sk-proj\|api.*key"

# Verify .env is ignored
git status --ignored | grep .env

# Check template files are safe
grep -r "sk-proj" *.template *.example
```

### **Automated Checks:**
```bash
# Run security scan
./security_check.sh

# Validate no secrets in repo
git log --all -p | grep -i "sk-proj\|api.*key" || echo "✅ No API keys found"
```

## 🚨 If API Key is Exposed

### **Immediate Actions:**
1. **Revoke the key** at https://platform.openai.com/api-keys
2. **Generate new key** 
3. **Update local .env** with new key
4. **Remove from git history** if committed:
   ```bash
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch .env' \
   --prune-empty --tag-name-filter cat -- --all
   ```

### **Prevention:**
- Set up pre-commit hooks to scan for API keys
- Use git-secrets or similar tools
- Regular security audits

## 📋 Security Checklist

- [ ] `.env` is in `.gitignore`
- [ ] No real API keys in template files
- [ ] No real API keys in documentation
- [ ] No real API keys in commit history
- [ ] API keys are rotated regularly
- [ ] Team knows security practices

## 🔗 Resources

- [OpenAI API Key Management](https://platform.openai.com/api-keys)
- [Git Secrets Tool](https://github.com/awslabs/git-secrets)
- [Environment Variable Best Practices](https://12factor.net/config)

---

**Remember: Security is everyone's responsibility! 🛡️**
