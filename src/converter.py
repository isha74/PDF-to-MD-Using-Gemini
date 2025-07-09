import os
import PyPDF2

PDF_FOLDER = os.path.join(os.path.dirname(__file__), "..", "Input-files_pdfs")

def extract_text_from_pdf(filename_or_path, from_full_path=False):
    
    """
    Extracts text from a PDF file.
    
    If from_full_path is True, expects absolute or relative path.
    Otherwise, loads file from Input-files_pdfs folder.
    """
    if from_full_path:
        full_path = filename_or_path
    else:
        full_path = os.path.join(PDF_FOLDER, filename_or_path)

    reader = PyPDF2.PdfReader(full_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text
