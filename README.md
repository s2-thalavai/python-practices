# python-practices

🧰 Method 1: Using Python and pip (lightweight setup)
Install Python

Download the latest version from python.org.

During installation, check “Add Python to PATH”.

Verify pip installation

Open Command Prompt and run:

bash

    python --version
    pip --version
    
Install Jupyter Notebook

Run:

bash

    pip install notebook

Launch Jupyter Notebook

Run:

bash
  
    jupyter notebook

It will open in your default browser.

--------------------------------------------------------------------------

🛠️ Fix 1: Check if Jupyter is installed

Run this in your terminal:

bash

    pip show notebook

If you see output, Jupyter is installed—just not in your PATH.

If nothing appears, install it with:

bash  

    pip install notebook

⚙️ Fix 2: Ensure the install location is in your PATH

Find out where jupyter was installed:

bash

    pip show notebook | grep Location

That gives the base path. Now check for the actual executable:

bash

      ls <location>/Scripts

If you see jupyter.exe, you can run it directly like:

bash

    <location>/Scripts/jupyter notebook

To make it globally available, add that Scripts folder to your system PATH:

Press Win + S, search “Environment Variables”.

Under System variables, edit the Path variable.

Add the full path to the folder containing jupyter.exe.

💡 Alternative: Use Python Launcher

Instead of relying on PATH, try:

bash

    python -m notebook

This runs Jupyter via Python directly.


--------------------------------------------------------------------------
