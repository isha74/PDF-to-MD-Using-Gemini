import os
import inquirer
from converter import extract_text_from_pdf
from gemini_helper import convert_text_to_markdown

INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "Input-files_pdfs")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "Converted_md")

os.makedirs(OUTPUT_DIR, exist_ok=True) 

def get_pdf_files():
    files = [f for f in os.listdir(INPUT_FILE) if f.endswith(".pdf")]
    return files

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
            markdown = convert_text_to_markdown(textbook)
            output_path = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".md"))

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"✅ Markdown saved to: {output_path}")
