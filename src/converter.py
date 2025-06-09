import os
import PyPDF2

PDF_FOLDER = os.path.join(os.path.dirname(__file__), "..", "Input-files_pdfs")

def extract_text_from_pdf( filename ):
    full_path = os.path.join( PDF_FOLDER, filename )
    reader = PyPDF2.PdfReader( full_path )

    full_text = ""
    for page in reader.pages:
        textbook = page.extract_text()
        if textbook:
            full_text += textbook + "\n"
    return full_text
