#!/usr/bin/env python3
"""
Complete MCP Vector Database Setup Validation
Comprehensive test to ensure everything is working correctly
"""

import os
import json
import sys
import subprocess
from pathlib import Path
import platform

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"🔍 {title}")
    print('='*60)

def print_success(message):
    """Print success message"""
    print(f"✅ {message}")

def print_error(message):
    """Print error message"""
    print(f"❌ {message}")

def print_warning(message):
    """Print warning message"""
    print(f"⚠️  {message}")

def print_info(message):
    """Print info message"""
    print(f"ℹ️  {message}")

def check_system_requirements():
    """Check system requirements"""
    print_header("System Requirements Check")
    
    # Check Python version
    python_version = sys.version_info
    if python_version >= (3, 11):
        print_success(f"Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print_error(f"Python {python_version.major}.{python_version.minor} (3.11+ required)")
        return False
    
    # Check platform
    system = platform.system()
    print_success(f"Platform: {system} {platform.release()}")
    
    # Check available memory (basic check)
    try:
        if system == "Darwin":  # macOS
            result = subprocess.run(['sysctl', 'hw.memsize'], capture_output=True, text=True)
            if result.returncode == 0:
                memory_bytes = int(result.stdout.split(':')[1].strip())
                memory_gb = memory_bytes / (1024**3)
                if memory_gb >= 8:
                    print_success(f"Memory: {memory_gb:.1f} GB")
                else:
                    print_warning(f"Memory: {memory_gb:.1f} GB (8GB+ recommended)")
        else:
            print_info("Memory check skipped for this platform")
    except:
        print_info("Could not check memory")
    
    return True

def check_environment_setup():
    """Check environment variables and files"""
    print_header("Environment Setup Check")
    
    # Check for .env file
    env_file = Path('.env')
    if env_file.exists():
        print_success(f".env file found: {env_file.absolute()}")
        
        # Load and check environment variables
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
                    if key == 'VECTOR_DB_PATH':
                        print_success(f"VECTOR_DB_PATH loaded: {value}")
                    elif key == 'MCP_SERVER_PATH':
                        print_success(f"MCP_SERVER_PATH loaded: {value}")
    else:
        print_warning(".env file not found")
    
    # Check environment variables
    vector_db_path = os.getenv('VECTOR_DB_PATH')
    mcp_server_path = os.getenv('MCP_SERVER_PATH')
    
    if vector_db_path:
        print_success(f"VECTOR_DB_PATH set: {vector_db_path}")
    else:
        print_error("VECTOR_DB_PATH not set")
        return False
    
    if mcp_server_path:
        print_success(f"MCP_SERVER_PATH set: {mcp_server_path}")
    else:
        print_warning("MCP_SERVER_PATH not set")
    
    return True

def check_vector_database():
    """Check vector database integrity"""
    print_header("Vector Database Check")
    
    vector_db_path = os.getenv('VECTOR_DB_PATH')
    if not vector_db_path:
        print_error("VECTOR_DB_PATH not set")
        return False
    
    db_path = Path(vector_db_path)
    if not db_path.exists():
        print_error(f"Database directory not found: {vector_db_path}")
        return False
    
    print_success(f"Database directory found: {vector_db_path}")
    
    # Check required files
    required_files = {
        'vector_db_index.json': 'Main vector index',
        'processing_summary.json': 'Database statistics'
    }
    
    for file_name, description in required_files.items():
        file_path = db_path / file_name
        if file_path.exists():
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print_success(f"{description}: {size_mb:.1f} MB")
        else:
            print_error(f"{description} not found: {file_name}")
            return False
    
    # Check database statistics
    try:
        summary_file = db_path / 'processing_summary.json'
        with open(summary_file) as f:
            summary = json.load(f)
        
        total_docs = summary.get('total_documents', 0)
        total_chunks = summary.get('total_chunks', 0)
        processed_at = summary.get('processed_at', 'Unknown')
        
        print_success(f"Documents: {total_docs:,}")
        print_success(f"Chunks: {total_chunks:,}")
        print_success(f"Processed: {processed_at}")
        
        if total_docs == 0:
            print_warning("Database appears to be empty")
        
    except Exception as e:
        print_error(f"Could not read database statistics: {e}")
        return False
    
    return True

def check_mcp_server():
    """Check MCP server setup"""
    print_header("MCP Server Check")
    
    mcp_server_path = os.getenv('MCP_SERVER_PATH')
    if not mcp_server_path:
        print_warning("MCP_SERVER_PATH not set, checking default locations")
        
        # Check common locations
        possible_paths = [
            Path.home() / 'mcp-vector-server',
            Path('/Volumes/NvME-Satechi/VectorDatabase/mcp-vector-server'),
            Path('./mcp-vector-server')
        ]
        
        for path in possible_paths:
            if path.exists():
                mcp_server_path = str(path)
                print_info(f"Found MCP server at: {mcp_server_path}")
                break
    
    if not mcp_server_path:
        print_error("MCP server not found")
        return False
    
    server_path = Path(mcp_server_path)
    if not server_path.exists():
        print_error(f"MCP server directory not found: {mcp_server_path}")
        return False
    
    print_success(f"MCP server directory found: {mcp_server_path}")
    
    # Check for server script
    server_script = server_path / 'mcp-vector-server.py'
    if server_script.exists():
        print_success("MCP server script found")
    else:
        # Check alternative locations
        alt_script = server_path / 'src' / 'mcp_vector_server' / 'simple_server.py'
        if alt_script.exists():
            print_success("MCP server script found (alternative location)")
        else:
            print_error("MCP server script not found")
            return False
    
    # Check Python environment
    venv_path = server_path / '.venv'
    if venv_path.exists():
        print_success("Python virtual environment found")
    else:
        print_warning("Python virtual environment not found")
    
    return True

def check_mcp_configuration():
    """Check MCP configuration file"""
    print_header("MCP Configuration Check")
    
    # Determine config file location based on platform
    system = platform.system()
    if system == "Darwin":  # macOS
        config_paths = [
            Path.home() / '.cursor' / 'mcp.json',
            Path.home() / '.claude-code' / 'mcp.json'
        ]
    elif system == "Windows":
        appdata = os.getenv('APPDATA', '')
        config_paths = [
            Path(appdata) / 'Cursor' / 'mcp.json',
            Path(appdata) / 'Claude Code' / 'mcp.json'
        ]
    else:  # Linux
        config_paths = [
            Path.home() / '.config' / 'cursor' / 'mcp.json',
            Path.home() / '.config' / 'claude-code' / 'mcp.json'
        ]
    
    config_file = None
    for path in config_paths:
        if path.exists():
            config_file = path
            break
    
    if not config_file:
        print_error("MCP configuration file not found")
        print_info("Expected locations:")
        for path in config_paths:
            print_info(f"  - {path}")
        return False
    
    print_success(f"MCP config found: {config_file}")
    
    # Validate JSON syntax
    try:
        with open(config_file) as f:
            config = json.load(f)
        print_success("MCP configuration JSON is valid")
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in MCP config: {e}")
        return False
    
    # Check for vector-db server configuration
    mcp_servers = config.get('mcpServers', {})
    if 'vector-db' in mcp_servers:
        print_success("vector-db server configured")
        
        vector_config = mcp_servers['vector-db']
        
        # Check command
        command = vector_config.get('command', '')
        if command:
            print_success(f"Command: {command}")
        else:
            print_error("No command specified for vector-db server")
        
        # Check args
        args = vector_config.get('args', [])
        if args:
            print_success(f"Args: {args}")
        else:
            print_error("No args specified for vector-db server")
        
        # Check environment
        env = vector_config.get('env', {})
        if 'VECTOR_DB_PATH' in env:
            print_success(f"VECTOR_DB_PATH configured: {env['VECTOR_DB_PATH']}")
        else:
            print_error("VECTOR_DB_PATH not configured in MCP")
        
    else:
        print_error("vector-db server not configured in MCP")
        return False
    
    return True

def check_documentation_files():
    """Check if documentation files are present"""
    print_header("Documentation Files Check")
    
    doc_files = {
        'VECTOR_DATABASE_SETUP_GUIDE.md': 'Complete setup guide',
        'QUICK_REFERENCE.md': 'Quick reference',
        'mcp-config-template.json': 'Configuration template',
        'setup_mcp_vector.sh': 'Setup script'
    }
    
    for file_name, description in doc_files.items():
        file_path = Path(file_name)
        if file_path.exists():
            print_success(f"{description}: {file_name}")
        else:
            print_warning(f"{description} not found: {file_name}")
    
    return True

def run_comprehensive_test():
    """Run all validation tests"""
    print("🚀 MCP Vector Database - Complete Setup Validation")
    print("=" * 60)
    
    tests = [
        ("System Requirements", check_system_requirements),
        ("Environment Setup", check_environment_setup),
        ("Vector Database", check_vector_database),
        ("MCP Server", check_mcp_server),
        ("MCP Configuration", check_mcp_configuration),
        ("Documentation Files", check_documentation_files)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print_error(f"{test_name} test failed")
        except Exception as e:
            print_error(f"{test_name} test error: {e}")
    
    # Final summary
    print_header("Validation Summary")
    
    if passed == total:
        print_success(f"All {total} tests passed! 🎉")
        print_success("Your MCP Vector Database setup is ready to use!")
        print_info("Next steps:")
        print_info("1. Restart Claude Code/Cursor")
        print_info("2. Test with: 'Search vectordb for documentation about X'")
    else:
        print_error(f"Only {passed}/{total} tests passed")
        print_error("Please check the failed tests above and fix the issues")
        print_info("Refer to VECTOR_DATABASE_SETUP_GUIDE.md for help")
    
    return passed == total

if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)
