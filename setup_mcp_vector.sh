#!/bin/bash
# 🚀 Automated MCP Vector Database Setup Script
# This script sets up the complete MCP vector database environment

set -e  # Exit on any error

echo "🚀 MCP Vector Database Setup Script"
echo "=================================="

# Configuration variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_VECTOR_DB_DIR="$HOME/VectorDatabase"
DEFAULT_MCP_SERVER_DIR="$HOME/mcp-vector-server"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

# Check prerequisites
check_prerequisites() {
    print_info "Checking prerequisites..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is required but not installed"
        exit 1
    fi
    
    python_version=$(python3 --version | cut -d' ' -f2)
    print_success "Python $python_version found"
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        print_warning "Node.js not found - some MCP features may not work"
    else
        node_version=$(node --version)
        print_success "Node.js $node_version found"
    fi
    
    # Check Git
    if ! command -v git &> /dev/null; then
        print_error "Git is required but not installed"
        exit 1
    fi
    
    print_success "Prerequisites check passed"
}

# Get user configuration
get_user_config() {
    print_info "Configuration setup..."
    
    # Vector database directory
    read -p "Vector database directory [$DEFAULT_VECTOR_DB_DIR]: " VECTOR_DB_DIR
    VECTOR_DB_DIR=${VECTOR_DB_DIR:-$DEFAULT_VECTOR_DB_DIR}
    
    # MCP server directory
    read -p "MCP server directory [$DEFAULT_MCP_SERVER_DIR]: " MCP_SERVER_DIR
    MCP_SERVER_DIR=${MCP_SERVER_DIR:-$DEFAULT_MCP_SERVER_DIR}
    
    # Check if vector database exists
    if [ -d "$VECTOR_DB_DIR" ]; then
        print_info "Found existing vector database directory"
        
        # List available databases
        echo "Available vector databases:"
        find "$VECTOR_DB_DIR" -maxdepth 1 -type d -name "*VectorDB" | head -5
        
        read -p "Enter the full path to your vector database: " SELECTED_DB_PATH
        
        if [ ! -d "$SELECTED_DB_PATH" ]; then
            print_error "Selected database path does not exist: $SELECTED_DB_PATH"
            exit 1
        fi
    else
        print_warning "Vector database directory not found: $VECTOR_DB_DIR"
        read -p "Do you want to create it? (y/n): " CREATE_DIR
        if [[ $CREATE_DIR =~ ^[Yy]$ ]]; then
            mkdir -p "$VECTOR_DB_DIR"
            print_success "Created directory: $VECTOR_DB_DIR"
            SELECTED_DB_PATH="$VECTOR_DB_DIR/placeholder_VectorDB"
        else
            print_error "Cannot proceed without vector database directory"
            exit 1
        fi
    fi
    
    # OpenAI API Key
    read -s -p "OpenAI API Key (optional, press enter to skip): " OPENAI_API_KEY
    echo
}

# Setup MCP server
setup_mcp_server() {
    print_info "Setting up MCP server..."
    
    if [ ! -d "$MCP_SERVER_DIR" ]; then
        print_info "Cloning MCP vector server..."
        # Note: Replace with actual repository URL
        git clone https://github.com/your-org/mcp-vector-server.git "$MCP_SERVER_DIR" || {
            print_warning "Could not clone MCP server repository"
            print_info "Creating basic MCP server structure..."
            mkdir -p "$MCP_SERVER_DIR/src/mcp_vector_server"
            
            # Create basic server file
            cat > "$MCP_SERVER_DIR/mcp-vector-server.py" << 'EOF'
#!/usr/bin/env python3
"""
Basic MCP Vector Server
"""
import os
import sys
import json
from pathlib import Path

def main():
    vector_db_path = os.getenv('VECTOR_DB_PATH')
    if not vector_db_path:
        print("Error: VECTOR_DB_PATH environment variable not set")
        sys.exit(1)
    
    if not Path(vector_db_path).exists():
        print(f"Error: Vector database not found: {vector_db_path}")
        sys.exit(1)
    
    print(f"MCP Vector Server starting with database: {vector_db_path}")
    print("Server ready for connections...")
    
    # Basic server loop (replace with actual MCP implementation)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nServer stopped")

if __name__ == "__main__":
    main()
EOF
            chmod +x "$MCP_SERVER_DIR/mcp-vector-server.py"
        }
    fi
    
    # Setup Python environment
    cd "$MCP_SERVER_DIR"
    
    if [ ! -d ".venv" ]; then
        print_info "Creating Python virtual environment..."
        python3 -m venv .venv
    fi
    
    source .venv/bin/activate
    
    # Install basic dependencies
    print_info "Installing dependencies..."
    pip install --upgrade pip
    pip install asyncio aiofiles json-rpc requests
    
    print_success "MCP server setup complete"
}

# Create MCP configuration
create_mcp_config() {
    print_info "Creating MCP configuration..."
    
    # Detect OS and set config path
    case "$(uname -s)" in
        Darwin*)    MCP_CONFIG_DIR="$HOME/.cursor" ;;
        Linux*)     MCP_CONFIG_DIR="$HOME/.config/cursor" ;;
        MINGW*)     MCP_CONFIG_DIR="$APPDATA/Cursor" ;;
        *)          MCP_CONFIG_DIR="$HOME/.cursor" ;;
    esac
    
    mkdir -p "$MCP_CONFIG_DIR"
    MCP_CONFIG_FILE="$MCP_CONFIG_DIR/mcp.json"
    
    # Backup existing config
    if [ -f "$MCP_CONFIG_FILE" ]; then
        cp "$MCP_CONFIG_FILE" "$MCP_CONFIG_FILE.backup.$(date +%Y%m%d_%H%M%S)"
        print_info "Backed up existing MCP config"
    fi
    
    # Create new config
    cat > "$MCP_CONFIG_FILE" << EOF
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "$HOME"]
    },
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"]
    },
    "vector-db": {
      "command": "python3",
      "args": ["$MCP_SERVER_DIR/mcp-vector-server.py"],
      "env": {
        "VECTOR_DB_PATH": "$SELECTED_DB_PATH"
      }
    },
    "memory": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-memory"]
    }
  }
}
EOF
    
    print_success "MCP configuration created: $MCP_CONFIG_FILE"
}

# Create environment file
create_env_file() {
    print_info "Creating environment file..."
    
    ENV_FILE="$SCRIPT_DIR/.env"
    
    cat > "$ENV_FILE" << EOF
# Vector Database Configuration
VECTOR_DB_PATH=$SELECTED_DB_PATH
MCP_SERVER_PATH=$MCP_SERVER_DIR

# OpenAI Configuration (optional)
EOF
    
    if [ -n "$OPENAI_API_KEY" ]; then
        echo "OPENAI_API_KEY=$OPENAI_API_KEY" >> "$ENV_FILE"
    else
        echo "# OPENAI_API_KEY=your-api-key-here" >> "$ENV_FILE"
    fi
    
    print_success "Environment file created: $ENV_FILE"
}

# Create test script
create_test_script() {
    print_info "Creating test script..."
    
    cat > "$SCRIPT_DIR/test_mcp_setup.py" << 'EOF'
#!/usr/bin/env python3
"""Test MCP Vector Database Setup"""

import os
import json
import sys
from pathlib import Path

def test_setup():
    """Test the MCP setup"""
    print("🧪 Testing MCP Vector Database Setup")
    print("=" * 40)
    
    # Check environment variables
    vector_db_path = os.getenv('VECTOR_DB_PATH')
    if not vector_db_path:
        print("❌ VECTOR_DB_PATH not set")
        return False
    
    print(f"✅ VECTOR_DB_PATH: {vector_db_path}")
    
    # Check database exists
    if not Path(vector_db_path).exists():
        print(f"❌ Database not found: {vector_db_path}")
        return False
    
    print("✅ Vector database directory found")
    
    # Check required files
    required_files = ["vector_db_index.json", "processing_summary.json"]
    for file_name in required_files:
        file_path = Path(vector_db_path) / file_name
        if file_path.exists():
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print(f"✅ {file_name}: {size_mb:.1f} MB")
        else:
            print(f"⚠️  {file_name}: Not found (may be created later)")
    
    # Test MCP server path
    mcp_server_path = os.getenv('MCP_SERVER_PATH')
    if mcp_server_path and Path(mcp_server_path).exists():
        print(f"✅ MCP server found: {mcp_server_path}")
    else:
        print("⚠️  MCP server path not found")
    
    print("\n🎉 Setup test completed!")
    return True

if __name__ == "__main__":
    # Load environment
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    
    test_setup()
EOF
    
    chmod +x "$SCRIPT_DIR/test_mcp_setup.py"
    print_success "Test script created: $SCRIPT_DIR/test_mcp_setup.py"
}

# Create quick access commands
create_quick_commands() {
    print_info "Creating quick access commands..."
    
    # Shell alias
    SHELL_RC_FILE=""
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_RC_FILE="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_RC_FILE="$HOME/.bashrc"
    fi
    
    if [ -n "$SHELL_RC_FILE" ]; then
        echo "" >> "$SHELL_RC_FILE"
        echo "# MCP Vector Database Quick Access" >> "$SHELL_RC_FILE"
        echo "alias mcp-vector='cd \"$MCP_SERVER_DIR\" && export VECTOR_DB_PATH=\"$SELECTED_DB_PATH\" && ./.venv/bin/python mcp-vector-server.py'" >> "$SHELL_RC_FILE"
        echo "alias test-mcp='cd \"$SCRIPT_DIR\" && python3 test_mcp_setup.py'" >> "$SHELL_RC_FILE"
        
        print_success "Added aliases to $SHELL_RC_FILE"
        print_info "Run 'source $SHELL_RC_FILE' to activate aliases"
    fi
}

# Main setup function
main() {
    echo
    print_info "Starting MCP Vector Database setup..."
    echo
    
    check_prerequisites
    echo
    
    get_user_config
    echo
    
    setup_mcp_server
    echo
    
    create_mcp_config
    echo
    
    create_env_file
    echo
    
    create_test_script
    echo
    
    create_quick_commands
    echo
    
    print_success "🎉 MCP Vector Database setup complete!"
    echo
    print_info "Next steps:"
    echo "1. Restart Claude Code/Cursor"
    echo "2. Run: python3 test_mcp_setup.py"
    echo "3. Test MCP connection in Claude Code"
    echo "4. Use 'mcp-vector' command to start server manually"
    echo
    print_info "Configuration files created:"
    echo "- MCP config: $MCP_CONFIG_FILE"
    echo "- Environment: $SCRIPT_DIR/.env"
    echo "- Test script: $SCRIPT_DIR/test_mcp_setup.py"
    echo
}

# Run main function
main "$@"
