# Environment Setup for Intelligent Content Analysis

## Quick Start

1. **Copy the example environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` and add your OpenAI API key:**
   ```bash
   nano .env
   # or
   open .env
   ```

3. **Add your API key:**
   ```
   OPENAI_API_KEY=sk-proj-your-actual-key-here
   ```

4. **Save and close the file**

## Getting Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-proj-...`)
5. Paste it into `.env`

## Security

- ✅ `.env` is in `.gitignore` - your key will NOT be committed to git
- ✅ Never share your `.env` file or commit it to version control
- ✅ Use `.env.example` to show the structure without exposing secrets

## Testing the Setup

Run the test script to verify everything works:

```bash
python3 test_intelligent_cleaning.py
```

If you see an error about the API key, double-check:
1. The file is named exactly `.env` (not `.env.txt` or anything else)
2. The key is on a line like: `OPENAI_API_KEY=sk-proj-...`
3. There are no extra spaces around the `=` sign
4. The key is valid and not expired

## Cost Estimates

The intelligent content analysis uses GPT-4o-mini, which is very cost-effective:

- **Per document:** ~$0.0003 (0.03 cents)
- **1,000 documents:** ~$0.30
- **10,000 documents:** ~$3.00

## Optional Configuration

You can override default settings in `.env`:

```
# Change the LLM model (default: gpt-4o-mini)
LLM_MODEL=gpt-4o-mini

# Adjust temperature for more/less randomness (default: 0.1)
LLM_TEMPERATURE=0.1

# Maximum tokens for LLM response (default: 1500)
LLM_MAX_TOKENS=1500

# Rate limit requests per minute (default: 500)
LLM_RATE_LIMIT_RPM=500
```

## Troubleshooting

### "API key not set" error
- Make sure `.env` exists in the same directory as the scripts
- Check that `OPENAI_API_KEY=` has your actual key after the `=`
- Try printing the env var: `python3 -c "import os; print(os.getenv('OPENAI_API_KEY'))"`

### "Invalid API key" error
- Your key may be expired or invalid
- Generate a new key at https://platform.openai.com/api-keys
- Make sure you copied the entire key (they're long!)

### "Rate limit exceeded" error
- You're making requests too quickly
- Wait a minute and try again
- Or reduce `LLM_RATE_LIMIT_RPM` in `.env`
