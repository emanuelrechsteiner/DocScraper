# 🚀 MCP Vector Database - Quick Reference

## 📁 Essential Files & Paths

| Component | Path | Purpose |
|-----------|------|---------|
| **MCP Config** | `~/.cursor/mcp.json` | Claude Code MCP server configuration |
| **Vector Database** | `/path/to/VectorDatabase/YYYYMMDD_*_VectorDB/` | Your processed documentation |
| **MCP Server** | `/path/to/mcp-vector-server/` | Vector search server code |
| **Environment** | `.env` | API keys and paths |

## ⚡ Quick Commands

```bash
# Start vector database server
mcp-vector

# Test setup
python3 test_mcp_setup.py

# Check database status  
ls -la $VECTOR_DB_PATH

# Validate MCP config
python3 -c "import json; print('✅ Valid JSON' if json.load(open('~/.cursor/mcp.json')) else '❌ Invalid')"
```

## 🔧 MCP Configuration Template

```json
{
  "mcpServers": {
    "vector-db": {
      "command": "python3",
      "args": ["/path/to/mcp-vector-server/mcp-vector-server.py"],
      "env": {
        "VECTOR_DB_PATH": "/path/to/VectorDatabase/YYYYMMDD_*_VectorDB"
      }
    }
  }
}
```

## 🧪 Testing Checklist

- [ ] Python 3.11+ installed
- [ ] Vector database exists and has `vector_db_index.json`
- [ ] MCP server starts without errors
- [ ] MCP config JSON is valid
- [ ] Claude Code connects to MCP (restart required)
- [ ] Vector search works: "Search vectordb for X"

## 🔍 Usage in Claude Code

| Command | Description |
|---------|-------------|
| `"Search vectordb for crawl4ai"` | Search documentation |
| `"What's in vectordb about async?"` | Content queries |
| `"Find vectordb docs on Python"` | Specific topic search |

## 🚨 Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| **"Vector database not found"** | Check `VECTOR_DB_PATH` in MCP config |
| **"MCP server won't start"** | Verify Python path and permissions |
| **"Claude Code not connecting"** | Restart Claude Code after config changes |
| **"Permission denied"** | Run `chmod +x mcp-vector-server.py` |

## 📊 Database Structure

```
VectorDatabase/
├── YYYYMMDD_HHMMSS_YourDocs_VectorDB/
│   ├── vector_db_index.json      # Main search index (large)
│   ├── processing_summary.json   # Database statistics
│   ├── chunks/                   # Document chunks
│   ├── cleaned/                  # Processed files
│   └── metadata/                 # Document metadata
```

## 🔄 Setup Process

1. **Install** → `./setup_mcp_vector.sh`
2. **Configure** → Update `~/.cursor/mcp.json`
3. **Test** → `python3 test_mcp_setup.py`
4. **Restart** → Claude Code/Cursor
5. **Use** → "Search vectordb for X"

## 📞 Emergency Commands

```bash
# Reset MCP config
cp mcp-config-template.json ~/.cursor/mcp.json

# Restart MCP server
pkill -f mcp-vector-server && mcp-vector

# Check logs
tail -f ~/.cursor/logs/mcp.log  # If available

# Verify database integrity
python3 -c "
import json
from pathlib import Path
db = Path('$VECTOR_DB_PATH')
summary = db / 'processing_summary.json'
if summary.exists():
    data = json.load(open(summary))
    print(f'✅ {data[\"total_documents\"]} docs, {data[\"total_chunks\"]} chunks')
else:
    print('❌ Database summary not found')
"
```

---

**💡 Remember**: Always restart Claude Code after changing MCP configuration!
