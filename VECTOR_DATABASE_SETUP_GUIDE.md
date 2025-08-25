# 🚀 Vector Database & MCP Server Setup Guide

Complete guide for setting up the DocScraper vector database with MCP (Model Context Protocol) server integration for Claude Code and other AI development environments.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [System Requirements](#system-requirements)
3. [Installation Steps](#installation-steps)
4. [MCP Configuration](#mcp-configuration)
5. [Vector Database Setup](#vector-database-setup)
6. [Testing & Verification](#testing--verification)
7. [Usage Examples](#usage-examples)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Configuration](#advanced-configuration)

---

## 🔧 Prerequisites

### Required Software
- **Python 3.11+** (recommended 3.13+)
- **Node.js 18+** (for MCP server dependencies)
- **Git** (for cloning repositories)
- **Claude Code** or **Cursor.ai** (for MCP integration)

### Required Python Packages
```bash
pip install asyncio aiofiles openai python-dotenv beautifulsoup4 crawl4ai networkx scikit-learn tenacity
```

---

## 💻 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8GB | 16GB+ |
| **Storage** | 5GB free | 10GB+ free |
| **CPU** | 4 cores | 8+ cores |
| **OS** | macOS 10.15+, Ubuntu 20.04+, Windows 10+ | Latest versions |

---

## 🛠️ Installation Steps

### Step 1: Clone the DocScraper Repository

```bash
# Clone the repository
git clone https://github.com/emanuelrechsteiner/DocScraper.git
cd DocScraper

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Set Up MCP Vector Server

```bash
# Clone the MCP Vector Server (if not included)
git clone https://github.com/your-org/mcp-vector-server.git /path/to/mcp-vector-server

# Navigate to MCP server directory
cd /path/to/mcp-vector-server

# Create virtual environment for MCP server
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install MCP server dependencies
pip install -r requirements.txt
# OR if using uv:
uv sync
```

### Step 3: Create Vector Database Directory Structure

```bash
# Create the main vector database directory
mkdir -p /path/to/VectorDatabase

# Example structure:
# /path/to/VectorDatabase/
# ├── mcp-vector-server/          # MCP server code
# ├── YYYYMMDD_HHMMSS_YourDocs_VectorDB/  # Your vector database
# └── other_databases/            # Additional databases
```

---

## ⚙️ MCP Configuration

### Step 1: Configure Claude Code/Cursor MCP Settings

Create or update your MCP configuration file:

**Location**: 
- **macOS**: `~/.cursor/mcp.json` or `~/.claude-code/mcp.json`
- **Windows**: `%APPDATA%\Cursor\mcp.json` or `%APPDATA%\Claude Code\mcp.json`
- **Linux**: `~/.config/cursor/mcp.json` or `~/.config/claude-code/mcp.json`

**Configuration**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/your/home/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"]
    },
    "vector-db": {
      "command": "python3",
      "args": ["/path/to/mcp-vector-server/mcp-vector-server.py"],
      "env": {
        "VECTOR_DB_PATH": "/path/to/VectorDatabase/YYYYMMDD_HHMMSS_YourDocs_VectorDB"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-memory"]
    }
  }
}
```

### Step 2: Environment Variables

Create a `.env` file in your project root:

```bash
# .env file
OPENAI_API_KEY=your-openai-api-key-here
VECTOR_DB_PATH=/path/to/VectorDatabase/YYYYMMDD_HHMMSS_YourDocs_VectorDB
MCP_SERVER_PATH=/path/to/mcp-vector-server
```

---

## 🗃️ Vector Database Setup

### Option 1: Process Your Own Documents

```bash
# Navigate to DocScraper directory
cd /path/to/DocScraper

# Set up environment
source venv/bin/activate
export OPENAI_API_KEY="your-api-key"

# Process documents with GUI
python DocPostProcessorGUI.py

# OR process via CLI
python DocPostProcessor.py "/path/to/your/docs" "/path/to/output" --use-llm
```

### Option 2: Use Pre-built Database

If you have a pre-built vector database:

```bash
# Copy the database to your system
cp -r /source/YYYYMMDD_HHMMSS_YourDocs_VectorDB /path/to/VectorDatabase/

# Update the path in your MCP configuration
# Edit ~/.cursor/mcp.json and update VECTOR_DB_PATH
```

### Database Structure

A properly configured vector database should have:

```
YYYYMMDD_HHMMSS_YourDocs_VectorDB/
├── vector_db_index.json          # Main vector index (large file)
├── processing_summary.json       # Database statistics
├── chunks/                       # Individual document chunks
├── cleaned/                      # Cleaned markdown files
├── metadata/                     # Document metadata
└── checkpoints/                  # Processing checkpoints
```

---

## 🧪 Testing & Verification

### Step 1: Test Vector Database

Create a test script (`test_setup.py`):

```python
#!/usr/bin/env python3
import json
import os
from pathlib import Path

def test_vector_database():
    """Test vector database setup"""
    db_path = os.getenv('VECTOR_DB_PATH')
    
    if not db_path:
        print("❌ VECTOR_DB_PATH not set")
        return False
    
    if not Path(db_path).exists():
        print(f"❌ Database not found: {db_path}")
        return False
    
    # Check required files
    required_files = [
        "vector_db_index.json",
        "processing_summary.json"
    ]
    
    for file_name in required_files:
        file_path = Path(db_path) / file_name
        if not file_path.exists():
            print(f"❌ Missing file: {file_name}")
            return False
        
        size_mb = file_path.stat().st_size / (1024 * 1024)
        print(f"✅ {file_name}: {size_mb:.1f} MB")
    
    # Load summary
    try:
        with open(Path(db_path) / "processing_summary.json", 'r') as f:
            summary = json.load(f)
        
        print(f"📊 Database Statistics:")
        print(f"   Documents: {summary.get('total_documents', 0):,}")
        print(f"   Chunks: {summary.get('total_chunks', 0):,}")
        print(f"   Processed: {summary.get('processed_at', 'Unknown')}")
        
    except Exception as e:
        print(f"❌ Error reading summary: {e}")
        return False
    
    print("✅ Vector database test passed!")
    return True

if __name__ == "__main__":
    test_vector_database()
```

Run the test:
```bash
python test_setup.py
```

### Step 2: Test MCP Server

```bash
# Start MCP server manually
cd /path/to/mcp-vector-server
export VECTOR_DB_PATH="/path/to/VectorDatabase/YYYYMMDD_HHMMSS_YourDocs_VectorDB"
./.venv/bin/python src/mcp_vector_server/simple_server.py

# Should output: Server starting on port XXXX
```

### Step 3: Test Claude Code Integration

1. **Restart Claude Code/Cursor**
2. **Open a project**
3. **Test MCP connection**:
   - In chat, ask: "Can you search the vectordb for documentation about X?"
   - Should see MCP tools being used

---

## 📚 Usage Examples

### Basic Vector Search

```python
# In Claude Code, you can now use:
# "Search vectordb for crawl4ai session management"
# "Find documentation about async web scraping in vectordb"
# "What does vectordb contain about Python asyncio?"
```

### Command Line Access

```bash
# Quick start alias (add to ~/.zshrc or ~/.bashrc)
alias /vector="cd /path/to/mcp-vector-server && export VECTOR_DB_PATH='/path/to/VectorDatabase/YYYYMMDD_HHMMSS_YourDocs_VectorDB' && ./.venv/bin/python src/mcp_vector_server/simple_server.py"

# Usage
/vector  # Starts vector database server
```

### Cursor.ai Integration

Add to `.vscode/tasks.json` in your project:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Start Vector Database",
            "type": "shell",
            "command": "cd /path/to/mcp-vector-server && export VECTOR_DB_PATH='/path/to/VectorDatabase/YYYYMMDD_HHMMSS_YourDocs_VectorDB' && ./.venv/bin/python src/mcp_vector_server/simple_server.py",
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "panel": "new"
            }
        }
    ]
}
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "Vector database not found"
```bash
# Check path
echo $VECTOR_DB_PATH
ls -la $VECTOR_DB_PATH

# Fix: Update path in MCP config
```

#### 2. "MCP server not starting"
```bash
# Check Python environment
which python3
python3 --version

# Check dependencies
pip list | grep -E "(asyncio|aiofiles|json)"

# Fix: Reinstall dependencies
pip install -r requirements.txt
```

#### 3. "Permission denied"
```bash
# Fix permissions
chmod +x /path/to/mcp-vector-server/mcp-vector-server.py
chmod -R 755 /path/to/VectorDatabase/
```

#### 4. "Claude Code not connecting to MCP"
```bash
# Check MCP config syntax
cat ~/.cursor/mcp.json | python -m json.tool

# Restart Claude Code completely
# Check logs in Claude Code developer tools
```

### Debug Commands

```bash
# Test MCP server directly
python3 /path/to/mcp-vector-server/mcp-vector-server.py --debug

# Test vector database access
python3 -c "
import json
from pathlib import Path
db_path = '/path/to/VectorDatabase/YYYYMMDD_HHMMSS_YourDocs_VectorDB'
summary_file = Path(db_path) / 'processing_summary.json'
if summary_file.exists():
    with open(summary_file) as f:
        data = json.load(f)
        print(f'Documents: {data.get(\"total_documents\", 0)}')
else:
    print('Summary file not found')
"
```

---

## 🚀 Advanced Configuration

### Multiple Vector Databases

```json
{
  "mcpServers": {
    "vector-db-main": {
      "command": "python3",
      "args": ["/path/to/mcp-vector-server/mcp-vector-server.py"],
      "env": {
        "VECTOR_DB_PATH": "/path/to/VectorDatabase/main_docs_VectorDB"
      }
    },
    "vector-db-secondary": {
      "command": "python3", 
      "args": ["/path/to/mcp-vector-server/mcp-vector-server.py"],
      "env": {
        "VECTOR_DB_PATH": "/path/to/VectorDatabase/secondary_docs_VectorDB",
        "MCP_SERVER_PORT": "8081"
      }
    }
  }
}
```

### Custom Search Parameters

```python
# In your MCP server configuration, you can customize:
# - Search similarity threshold
# - Maximum results returned
# - Search algorithm (TF-IDF, semantic, etc.)
```

### Performance Tuning

```bash
# For large databases (>1GB), consider:
# 1. Increase system memory
# 2. Use SSD storage
# 3. Adjust search parameters
# 4. Enable caching

# Environment variables for performance
export VECTOR_DB_CACHE_SIZE=1000
export VECTOR_DB_MAX_RESULTS=50
export VECTOR_DB_SIMILARITY_THRESHOLD=0.1
```

---

## 📞 Support & Resources

### Documentation Links
- [DocScraper Repository](https://github.com/emanuelrechsteiner/DocScraper)
- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Claude Code Documentation](https://claude.ai/code)

### Getting Help
1. **Check logs** in Claude Code developer tools
2. **Test components** individually (database → MCP server → Claude Code)
3. **Verify paths** and permissions
4. **Check environment variables**

### Example Working Configuration

```bash
# Verified working paths (adjust for your system):
VECTOR_DB_PATH="/Users/username/VectorDatabase/20250824_135319_TechDocs_VectorDB"
MCP_SERVER_PATH="/Users/username/mcp-vector-server"
DOCSCRAPER_PATH="/Users/username/DocScraper"
```

---

## ✅ Quick Setup Checklist

- [ ] Python 3.11+ installed
- [ ] DocScraper repository cloned
- [ ] MCP vector server set up
- [ ] Vector database created/copied
- [ ] MCP configuration file updated
- [ ] Environment variables set
- [ ] Test script passes
- [ ] MCP server starts successfully
- [ ] Claude Code connects to MCP
- [ ] Vector search works in Claude Code

**🎉 Setup Complete!** Your vector database is now accessible via MCP in Claude Code.

---

*Last updated: January 2025*
*Version: 1.0*
