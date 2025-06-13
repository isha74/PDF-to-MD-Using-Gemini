import google.generativeai as genai
import os

# (TEMPORARY) Directly set your API Key here for testing
genai.configure(api_key="API KEY")

# Create model object
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Send simple test prompt
response = model.generate_content("Hello Gemini! Can you convert 'Hello World' into markdown?")

# Print Gemini response
print(response.text)
