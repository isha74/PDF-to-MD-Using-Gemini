
import os
import inquirer
from converter import extract_text_from_pdf

INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", " Input-files_pdfs ")

def get_pdf_files():
    files = [f for f in os.listdir( INPUT_FILE ) if f.endswith(".pdf")]
    return files

def select_pdf_files(pdf_files):
    
    # if not pdf_files:
    # return []
    
    questions = [
        inquirer.Checkbox(
            "selected_files",
            message=" Select PDF files to convert ",
            choices=pdf_files
        )
    ]
    selected = inquirer.prompt(questions)
    return selected[ "selected_files" ]

# Main function
if __name__ == "__main__":
    pdf_files = get_pdf_files()

    if not pdf_files:
        print("No PDF files found in the 'Input-files_pdfs' folder.")
    else:
        selected_files = select_pdf_files(pdf_files)

        for file in selected_files:
            print(f"\n Extracting text from: {file} ")
            textbook = extract_text_from_pdf(file)
            print(textbook[:1000])  # Optional
