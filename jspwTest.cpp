{
  "name": "leetcode-cph",
  "displayName": "Leetcode CPH",
  "description": "A VS Code extension to fetch and run LeetCode test cases by DHRUV SONI.",
  "version": "0.0.1",
  "publisher": "DHRUV SONI", 
  "engines": {
    "vscode": "^1.56.0"
  },
  "activationEvents": [
    "onCommand:leetcode-cph.fetchTestCases",
    "onCommand:leetcode-cph.runTestCases"
  ],
  "main": "./out/extension.js", 
  "scripts": {
    "vscode:prepublish": "npm run compile", 
    "compile": "tsc -p ./", 
    "watch": "tsc -watch -p ./", 
    "postinstall": "node ./node_modules/vscode/bin/compile"
  },
  "dependencies": {
    "vscode": "^1.1.37" 
  },
  "devDependencies": {
    "@types/node": "^14.0.0",
    "typescript": "^4.0.0"
  },
  "scripts": {
    "build": "tsc"
  },
  "contributes": {
    "commands": [
      {
        "command": "leetcode-cph.fetchTestCases",
        "title": "CPH:Fetch Test Cases"
      },
      {
        "command": "leetcode-cph.runTestCases",
        "title": "CPH:Run Test Cases"
      }
    ]
  }
}
