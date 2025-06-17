import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


def convert_text_to_markdown(text):
    prompt = f"""
You are a helpful assistant. Convert the following text into well-formatted Markdown.

Text:
{text}
"""
    response = model.generate_content(prompt)
    return response.text.strip()
