import os
import inquirer
from converter import extract_text_from_pdf

# Path to the folder containing PDF files
INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "Input-files_pdfs")

# Get list of all PDFs in the folder
def get_pdf_files():
    files = [f for f in os.listdir(INPUT_FILE) if f.endswith(".pdf")]
    return files

# Let user select which PDF files to process
def select_pdf_files(pdf_files):
    questions = [
        inquirer.Checkbox(
            "selected_files",
            message="Select PDF files to convert",
            choices=pdf_files
        )
    ]
    selected = inquirer.prompt(questions)
    return selected["selected_files"]

# Main function
if __name__ == "__main__":
    pdf_files = get_pdf_files()

    if not pdf_files:
        print("No PDF files found in the 'Input-files_pdfs' folder.")
    else:
        selected_files = select_pdf_files(pdf_files)

        for file in selected_files:
            print(f"\nExtracting text from: {file}")
            textbook = extract_text_from_pdf(file)
            print(textbook[:1000])  # Optional: just previewing first 1000 characters