const vscode = require('vscode');
const { exec } = require('child_process');

/**
 * Vector Database Extension for Cursor
 */
function activate(context) {
    console.log('Vector Database extension is now active!');

    // Start Vector Database command
    let startCommand = vscode.commands.registerCommand('vectordb.start', () => {
        const terminal = vscode.window.createTerminal('Vector Database');
        terminal.show();
        
        const command = `cd /Volumes/NvME-Satechi/VectorDatabase/mcp-vector-server && export VECTOR_DB_PATH="/Volumes/NvME-Satechi/VectorDatabase/20250824_135319_2025_Emanuels_Tech_Stack_Docs_VectorDB" && ./.venv/bin/python src/mcp_vector_server/simple_server.py`;
        
        terminal.sendText(command);
        vscode.window.showInformationMessage('🚀 Starting Vector Database Server...');
    });

    // Vector Database Status command
    let statusCommand = vscode.commands.registerCommand('vectordb.status', () => {
        const terminal = vscode.window.createTerminal('Vector Status');
        terminal.show();
        
        const command = `cd /Volumes/NvME-Satechi/Development/Claude_Code/DocScraper && python test_vector_db.py`;
        
        terminal.sendText(command);
        vscode.window.showInformationMessage('📊 Checking Vector Database Status...');
    });

    context.subscriptions.push(startCommand);
    context.subscriptions.push(statusCommand);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
