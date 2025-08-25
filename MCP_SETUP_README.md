# 📦 MCP Vector Database Setup Package

Complete documentation and automation tools for setting up the DocScraper vector database with MCP (Model Context Protocol) integration.

## 📋 Package Contents

| File | Description |
|------|-------------|
| `VECTOR_DATABASE_SETUP_GUIDE.md` | **📖 Complete setup guide** - Comprehensive documentation |
| `setup_mcp_vector.sh` | **🚀 Automated setup script** - One-command installation |
| `mcp-config-template.json` | **⚙️ Configuration template** - Copy-paste MCP config |
| `QUICK_REFERENCE.md` | **⚡ Quick reference** - Commands and troubleshooting |
| `test_mcp_setup.py` | **🧪 Test script** - Verify installation |

## 🚀 Quick Start (30 seconds)

```bash
# 1. Run automated setup
./setup_mcp_vector.sh

# 2. Test installation  
python3 test_mcp_setup.py

# 3. Restart Claude Code/Cursor

# 4. Test in Claude Code
# Say: "Search vectordb for documentation about X"
```

## 📖 For New Developers

### If you're setting this up on a new system:

1. **Read first**: `VECTOR_DATABASE_SETUP_GUIDE.md`
2. **Run setup**: `./setup_mcp_vector.sh`
3. **Quick reference**: `QUICK_REFERENCE.md`
4. **Test**: `python3 test_mcp_setup.py`

### If you have an existing vector database:

1. **Copy your database** to the new system
2. **Run**: `./setup_mcp_vector.sh`
3. **Point to your database** when prompted
4. **Test connection** in Claude Code

### If you need to create a new database:

1. **Use DocScraper** to process your documentation:
   ```bash
   python DocPostProcessorGUI.py  # GUI version
   # OR
   python DocPostProcessor.py /path/to/docs /path/to/output --use-llm
   ```
2. **Follow setup guide** for MCP integration

## 🔧 System Requirements

- **Python 3.11+** (recommended 3.13+)
- **8GB+ RAM** (16GB+ recommended for large databases)
- **5GB+ free storage**
- **Claude Code** or **Cursor.ai**

## 🎯 What This Package Provides

### ✅ **Automated Setup**
- MCP server configuration
- Environment variable setup  
- Python virtual environment
- Shell aliases and shortcuts

### ✅ **Cross-Platform Support**
- macOS, Windows, Linux
- Automatic path detection
- Platform-specific configurations

### ✅ **Complete Documentation**
- Step-by-step instructions
- Troubleshooting guides
- Usage examples
- Best practices

### ✅ **Testing & Validation**
- Automated test scripts
- Configuration validation
- Database integrity checks
- Connection testing

## 🔍 Usage Examples

Once set up, you can use these commands in Claude Code:

```
"Search vectordb for crawl4ai session management"
"What documentation does vectordb have about async programming?"
"Find vectordb content related to web scraping"
"Show me vectordb docs about Python asyncio"
```

## 📞 Support

### 🔧 **Troubleshooting**
1. Check `QUICK_REFERENCE.md` for common issues
2. Run `python3 test_mcp_setup.py` for diagnostics
3. Verify paths in `~/.cursor/mcp.json`

### 📚 **Documentation**
- **Complete guide**: `VECTOR_DATABASE_SETUP_GUIDE.md`
- **Quick commands**: `QUICK_REFERENCE.md`
- **Configuration**: `mcp-config-template.json`

### 🧪 **Testing**
```bash
# Test database
python3 test_mcp_setup.py

# Test MCP server
mcp-vector  # (after setup)

# Validate config
python3 -c "import json; json.load(open('~/.cursor/mcp.json'))"
```

## 🚀 Advanced Features

### **Multiple Databases**
Configure multiple vector databases for different projects

### **Custom Search Parameters**
Adjust similarity thresholds and result limits

### **Performance Tuning**
Optimize for large databases and fast searches

### **Integration Examples**
Ready-to-use configurations for common setups

---

## 🎉 Success Indicators

You'll know the setup is working when:

- ✅ `python3 test_mcp_setup.py` passes all tests
- ✅ MCP server starts without errors
- ✅ Claude Code shows MCP tools in use
- ✅ Vector searches return relevant results
- ✅ No error messages in Claude Code

**Ready to search your documentation with AI! 🚀**

---

*Package Version: 1.0*  
*Last Updated: January 2025*  
*Compatible with: Claude Code, Cursor.ai, MCP Protocol*
