import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';

export function activate(context: vscode.ExtensionContext) {

    let fetchTestCases = vscode.commands.registerCommand('leetcode-cph.fetchTestCases', () => {
        vscode.window.showInformationMessage('Fetching test cases from leetcode-cph by DHRUV SONI');
        runPythonScript('index.py');
    });

    let runTestCases = vscode.commands.registerCommand('leetcode-cph.runTestCases', () => {
        vscode.window.showInformationMessage('Running test cases from leetcode-cph by DHRUV SONI');
        runPythonScript('testrunner.py');
    });

    context.subscriptions.push(fetchTestCases, runTestCases);
}

function runPythonScript(scriptName: string) {
    const terminal = vscode.window.createTerminal(`Python: ${scriptName}`);

    const outDirectory = path.join(__dirname, '..', 'out'); 
    const scriptPath = path.join(outDirectory, scriptName); 

    console.log(`Looking for script at: ${scriptPath}`);

    if (fs.existsSync(scriptPath)) {
        terminal.sendText(`python "${scriptPath}"`);
        terminal.show();
    } else {
        vscode.window.showErrorMessage(`File ${scriptName} not found at ${scriptPath}.`);
    }
}

export function deactivate() {}
