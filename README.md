# PDF to MarkDown Using LLM (Gemini)

This project is based on converting small PDFs to Markdown file format using LLM with custom formatting options.

## What is in this repo?

This repository contains basic project structure, requirements, and this README.

## How to setup?

1. Clone the Repo
   
```bash
git clone https://github.com/isha74/PDF-to-MD-Using-Gemini.git
cd PDF-to-MD-Using-Gemini
```

2. First create a virtual environment. If you don't know how to do that, below are the basic commands: \
   _Use Python 3.13 or greater_. \
   _Do not use CMD.exe on Windows. Use Powershell_

```bash
python -m venv .venv
```

3. Then activate the virtual environment using:

```bash
.\.venv\Scripts\Activate.ps1    # For Windows Powershell.

source .venv/bin/activate       # For Linux and macOS.
```

Read more about virtual environments here: https://docs.python.org/3/library/venv.html

4. Next install the requirements from `requirements.txt` file:

```bash
pip install -r requirements.txt
```

5. Set up .env file
   
```bash
GEMINI_API_KEY=your_gemini_api_key
```

The stepwise process of how the application will work is:

1. New directory is created.
2. User will select files using inquirer.
3. The application will take those files and send them to gemini one by one.
4. The response is to be stored in a file with .md extension with same name as the .pdf file.
5. The .md files will be stored in the created directory.
   
## Technologies Used
   1. Python 3.10+
   2. PyPDF2
   3. Inquirer
   4. google-generativeai
   5. dotenv

## Features Implemented

   1. ✅ CLI-based PDF selection (via `inquirer`)
   2. ✅ Text extraction using `PyPDF2`
   3. ✅ Gemini API integration for markdown formatting
   4. ✅ Output `.md` files saved with original PDF names
   5. ✅ Directory creation handled with `os.makedirs(..., exist_ok=True)`
   6. ✅ Docstrings added for each file
   7. ✅ Final testing completed and project is stable
      
## Things to keep in mind:

- _NO AI CODE SHALL BE USED._ Any plagarised or code given by LLMs can be detected. Anyone found using these tactics will be barred from receiving the completion certificate.
- _NO CODE SHARING_. Every intern must have their own unique code and project style. Same rules as above for violation of this rule.
- Any number of files can be created depending on the neccesity and use.
- Do not clutter the main.py file, try and create multiple files for different logic sections (Eg: converter.py handle the conversion using gemini, filesystem_update.py creates and updated directories and files in filesystem).
