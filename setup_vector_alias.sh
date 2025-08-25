#!/bin/bash
# Vector Database Quick Access Setup

echo "Setting up /vector command alias..."

# Add to .zshrc (for zsh users)
if [ -f ~/.zshrc ]; then
    echo "" >> ~/.zshrc
    echo "# Vector Database Quick Access" >> ~/.zshrc
    echo 'alias /vector="cd /Volumes/NvME-Satechi/VectorDatabase/mcp-vector-server && export VECTOR_DB_PATH=\"/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB\" && ./.venv/bin/python src/mcp_vector_server/simple_server.py"' >> ~/.zshrc
    echo "✅ Added /vector alias to ~/.zshrc"
fi

# Add to .bash_profile (for bash users)
if [ -f ~/.bash_profile ]; then
    echo "" >> ~/.bash_profile
    echo "# Vector Database Quick Access" >> ~/.bash_profile
    echo 'alias /vector="cd /Volumes/NvME-Satechi/VectorDatabase/mcp-vector-server && export VECTOR_DB_PATH=\"/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB\" && ./.venv/bin/python src/mcp_vector_server/simple_server.py"' >> ~/.bash_profile
    echo "✅ Added /vector alias to ~/.bash_profile"
fi

echo ""
echo "🎯 Usage after restart or 'source ~/.zshrc':"
echo "   /vector    # Start vector database server"
echo ""
echo "🔄 To apply now, run: source ~/.zshrc"
