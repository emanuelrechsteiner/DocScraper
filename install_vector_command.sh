#!/bin/bash
# Install /vector as a system-wide command

echo "🔧 Installing /vector command system-wide..."

# Create the command script
sudo tee /usr/local/bin/vector > /dev/null << 'EOF'
#!/bin/bash
# Vector Database Quick Access Command

VECTOR_DB_PATH="/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB"
MCP_SERVER_PATH="/Volumes/NvME-Satechi/VectorDatabase/mcp-vector-server"

case "$1" in
    "start"|"")
        echo "🚀 Starting Vector Database Server..."
        cd "$MCP_SERVER_PATH"
        export VECTOR_DB_PATH="$VECTOR_DB_PATH"
        ./.venv/bin/python src/mcp_vector_server/simple_server.py
        ;;
    "status")
        echo "📊 Vector Database Status:"
        if [ -d "$VECTOR_DB_PATH" ]; then
            echo "✅ Database found: $VECTOR_DB_PATH"
            if [ -f "$VECTOR_DB_PATH/vector_db_index.json" ]; then
                size=$(du -h "$VECTOR_DB_PATH/vector_db_index.json" | cut -f1)
                echo "✅ Vector index: $size"
            fi
        else
            echo "❌ Database not found!"
        fi
        ;;
    "help"|"-h"|"--help")
        echo "🔍 Vector Database Commands:"
        echo "  vector start   # Start MCP server"
        echo "  vector status  # Check database status"
        echo "  vector help    # Show this help"
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo "Use 'vector help' for available commands"
        ;;
esac
EOF

# Make it executable
sudo chmod +x /usr/local/bin/vector

echo "✅ Installed /usr/local/bin/vector"
echo ""
echo "🎯 Usage:"
echo "  vector start   # Start vector database server"
echo "  vector status  # Check database status"
echo "  vector help    # Show help"
echo ""
echo "🔄 You can now use 'vector' from anywhere in your terminal!"
