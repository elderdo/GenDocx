# VS Code Configuration for Python

Yes, extensions.json is an excellent file to include.
It is used to manage Workspace Recommendations. When you share this folder with others (or open it on a brand-new computer), VS Code will read this file and instantly pop up a small notification saying: "This workspace has extension recommendations." It gives the user a one-click button to install all the exact tools needed to work on the project.
It completely eliminates the "it doesn't work on my machine" problem by ensuring everyone uses the same formatters, linters, and python tools.
Here is a great production-ready template for your directory:

The .vscode/extensions.json File

Create a file named .vscode/extensions.json:
json
{
    "recommendations": [
        // The core Python integration tool (linting, debugging, environment switching)
        "ms-python.python",
        
        // Pylance: Language server providing fast auto-complete and type checking
        "ms-python.vscode-pylance",
        
        // The industry-standard tool for auto-formatting Python files on save
        "ms-python.black-formatter",
        
        // Useful if you ever want to preview JSON files (like configurations) cleanly
        "ms-custom.unjson"
    ],
    "unwantedRecommendations": [
        // Prevents VS Code from recommending competing or outdated linting extensions
        "ms-python.flake8"
    ]
}
Use code with caution.

How to View the Recommendations Manually

If you ever want to see what a project recommends without waiting for a pop-up:
1. Open the Extensions tab on the left sidebar (Ctrl+Shift+X or Cmd+Shift+X).
2. Type @recommended into the search bar at the top.
3. You will see a dedicated section labeled Workspace Recommendations listing exactly what you specified in the JSON file.

Summary of Your Complete .vscode Folder Structure

With this added, your workspace directory configuration is now locked down perfectly:
• settings.json: Enforces strict code styling rules (like auto-formatting your script on save).
• launch.json: Saves your command-line arguments (-t, -o, key=value) for easy one-click testing.
• extensions.json: Ensures your environment has the exact extension tools required to run the scripts smoothly.
Would you like to know how to set up a requirements.txt file alongside this so that your team can install docxtpl and the Python dependencies just as easily as they install these extensions?
