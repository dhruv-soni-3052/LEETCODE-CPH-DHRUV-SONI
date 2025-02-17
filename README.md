## LeetCode-CPH Visual Studio Code Extension

Enhance your problem-solving experience on LeetCode with the LeetCode-CPH Visual Studio Code Extension! Tailored for competitive programmers and DSA learners.

## Features

🚀 Auto-fetch LeetCode Problems: Fetch problem statements and test cases directly into your editor.
🧪 Local Testing: Run and validate your solutions locally with sample inputs.
🔍 Integrated Debugging: Use VS Code’s debugging tools to troubleshoot your solutions easily.

## Usage

1.Fetching Problems

Use the command palette (Ctrl+Shift+P) and select CPH:Fetch Testcases.
Enter the problem URL to load it into your editor (You can also verify the name of the problem statement).You will then see 3 files, input.txt
which contains your inputs, output.txt which contains the expected output and solution file
where you can code up your solution.

!! ONE IMPORTANT THING TO ENSURE IS THAT IN YOUR SOLUTION FILE YOU SHOULD CODE 
YOUR SOLUTION IN A FUNCTION WHICH SHOULD NAME BE NAMED "Solve" ONLY !!

2.Running Testcases

Once you are ready with your solution file which contains your logic coded up 
in the "Solve" function, use the command palette (Ctrl+Shift+P) again and select the
feature CPH:Run Testcases.

Now you have to enter the number of arguments to the "Solve" function and their data-types
in "correct order". Reverify these things from input.txt file.

After that as you hit Enter you will see a new file myoutput.txt which contains the output generated 
by your code in solution file against the input in input.txt.

## ANALYZING VERDICTS

You will see verdict on the terminal:

"All test cases passed":--> If your code has generated the exact same output as expected by output.txt.

If the outputs don’t match, you’ll receive a detailed verdict for each test case. The expected output and the actual output will be displayed side by side, making it easy for you to debug and trace errors.

Additionally, you can open myoutput.txt at any time to view the output generated by your code in a clean and structured format.

## REUSAGE

You can easily use the Command Palette (Ctrl+Shift+P) and select "CPH: Fetch Testcases" to fetch test cases for a new problem. Simply enter the URL of the LeetCode problem, and the following will happen automatically:

input.txt and output.txt: These files will be overwritten with the new set of inputs and expected outputs for the problem.
Solution File: The solution file will be cleared, providing a clean slate for you to code your solution.
There’s no need to manually delete or worry about the contents of any files.

When you're ready to test your solution, use the "CPH: Run Testcases" feature from the Command Palette. This will update the myoutput.txt file with the actual outputs of your code for the new provided inputs.

## ENDING NOTE
Thank you for taking the time to explore LeetCode-CPH!. I hope this extension becomes a valuable part of your problem-solving journey.

Your feedback and contributions are always welcome to keep improving this project. Keep coding and growing! 🚀

-- Dhruv Soni
-- EE'27

**Enjoy!**
