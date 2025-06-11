
from converter import extract_text_from_pdf

# Replace this with the name of your PDF file
filename = "Ikigai.pdf"

print(f"\nExtracting text from: {filename}")
textbook = extract_text_from_pdf(filename)

print("\nExtracted Text:\n")
print(textbook)