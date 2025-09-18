# Azure OpenAI utilities: Q&A, summarization, image generation

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2024-02-15-preview"

gpt_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1")
dalle_deployment = os.getenv("AZURE_OPENAI_DALLE_DEPLOYMENT", "dall-e-3")

def ask_question(prompt):
    response = openai.chat.completions.create(
        model=gpt_deployment,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7,
        stream=False,
        extra_headers={"api-key": openai.api_key}
    )
    return response.choices[0].message.content.strip()

def ask_question_with_history(history):
    """Ask a question using the full chat history for context."""
    response = openai.chat.completions.create(
        model=gpt_deployment,
        messages=history,
        max_tokens=300,
        temperature=0.7,
        stream=False,
        extra_headers={"api-key": openai.api_key}
    )
    return response.choices[0].message.content.strip()

def summarize_text(text):
    prompt = f"Summarize the following text:\n{text}"
    return ask_question(prompt)

def generate_image(prompt):
    response = openai.images.generate(
        model=dalle_deployment,
        prompt=prompt,
        n=1,
        size="1024x1024",
        extra_headers={"api-key": openai.api_key}
    )
    return response.data[0].url
