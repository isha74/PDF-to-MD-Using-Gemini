import PyPDF2

pdf_path = 'C:/Users/HP/OneDrive/Desktop/PDF-to-MD-Using-Gemini/Input-files_pdfs/Ikigai.pdf'
read = PyPDF2.PdfReader(pdf_path)

print("PDF Metadata:")
print(read.metadata)

full_text = ""
for page in read.pages:
    textbook = page.extract_text()
    if textbook:
        full_text += textbook + "\n"

print("\nExtracted Text:\n")
print(full_text)
