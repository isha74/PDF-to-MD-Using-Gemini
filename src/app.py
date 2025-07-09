import streamlit as st
import os
from converter import extract_text_from_pdf
from gemini_helper import transform_to_markdown

# App UI config
st.set_page_config(page_title="PDF to Markdown with Gemini", layout="centered")
st.title("📄 PDF to Markdown Converter using Gemini AI")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "Converted_md")
os.makedirs(OUTPUT_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    temp_path = os.path.join("src", "temp_uploaded.pdf")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    if st.button("Convert to Markdown"):
        text = extract_text_from_pdf(temp_path, from_full_path=True)
        st.info("Extracted text... Sending to Gemini")
        markdown = transform_to_markdown(text)

        st.subheader("📝 Markdown Output")
        st.code(markdown, language="markdown")

        md_filename = uploaded_file.name.replace(".pdf", ".md")
        output_path = os.path.join(OUTPUT_DIR, md_filename)
        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown)

        st.success(f"✅ Markdown saved to: Converted_md/{md_filename}")
        
        st.download_button(
            label="📥 Download .md file",
            data=markdown,
            file_name=md_filename,
            mime="text/markdown"
        )
        os.remove(temp_path) 
