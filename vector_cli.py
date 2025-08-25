#!/usr/bin/env python3
"""
Vector Database CLI Tool
Quick access to vector database operations
Usage: /vector [command] [query]
"""

import sys
import os
import subprocess
import json
from pathlib import Path

# Vector database configuration
VECTOR_DB_PATH = "/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB"
MCP_SERVER_PATH = "/Volumes/NvME-Satechi/VectorDatabase/mcp-vector-server"

def show_help():
    """Show available commands"""
    print("🔍 Vector Database CLI")
    print("=" * 30)
    print("Commands:")
    print("  /vector start          # Start MCP vector server")
    print("  /vector status         # Check database status")
    print("  /vector search <query> # Search the database")
    print("  /vector info           # Show database info")
    print("  /vector help           # Show this help")
    print("")
    print("Examples:")
    print("  /vector search crawl4ai")
    print("  /vector search 'async web scraping'")

def start_server():
    """Start the MCP vector server"""
    print("🚀 Starting Vector Database Server...")
    
    try:
        os.chdir(MCP_SERVER_PATH)
        env = os.environ.copy()
        env['VECTOR_DB_PATH'] = VECTOR_DB_PATH
        
        subprocess.run([
            "./.venv/bin/python", 
            "src/mcp_vector_server/simple_server.py"
        ], env=env)
        
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def show_status():
    """Show database status"""
    print("📊 Vector Database Status")
    print("=" * 30)
    
    if Path(VECTOR_DB_PATH).exists():
        print(f"✅ Database found: {VECTOR_DB_PATH}")
        
        # Check key files
        index_file = Path(VECTOR_DB_PATH) / "vector_db_index.json"
        summary_file = Path(VECTOR_DB_PATH) / "processing_summary.json"
        
        if index_file.exists():
            size_mb = index_file.stat().st_size / (1024 * 1024)
            print(f"✅ Vector index: {size_mb:.1f} MB")
        
        if summary_file.exists():
            try:
                with open(summary_file, 'r') as f:
                    summary = json.load(f)
                print(f"📄 Documents: {summary.get('total_documents', 0):,}")
                print(f"🧩 Chunks: {summary.get('total_chunks', 0):,}")
                print(f"📅 Processed: {summary.get('processed_at', 'Unknown')}")
            except:
                print("⚠️  Could not read summary file")
    else:
        print("❌ Database not found!")

def search_database(query):
    """Search the database (placeholder - would integrate with MCP)"""
    print(f"🔍 Searching for: '{query}'")
    print("📝 Note: This would integrate with MCP vector search tools")
    print("💡 For now, use the MCP interface in Claude to search")

def show_info():
    """Show database information"""
    print("ℹ️  Vector Database Information")
    print("=" * 35)
    print(f"📍 Location: {VECTOR_DB_PATH}")
    print(f"🖥️  MCP Server: {MCP_SERVER_PATH}")
    print("🔧 Contains: Tech stack documentation")
    print("📚 Includes: Crawl4ai, Python docs, and more")

def main():
    """Main CLI function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "start":
        start_server()
    elif command == "status":
        show_status()
    elif command == "search":
        if len(sys.argv) < 3:
            print("❌ Please provide a search query")
            print("Usage: /vector search <query>")
        else:
            query = " ".join(sys.argv[2:])
            search_database(query)
    elif command == "info":
        show_info()
    elif command == "help":
        show_help()
    else:
        print(f"❌ Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main()
