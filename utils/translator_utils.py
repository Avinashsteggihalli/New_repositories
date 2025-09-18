# Azure Translator utilities: translation

import os
import requests
from dotenv import load_dotenv

load_dotenv()
TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
TRANSLATOR_REGION = os.getenv("AZURE_TRANSLATOR_REGION")
TRANSLATOR_ENDPOINT = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"

def translate_text(text, to_lang="hi"):
    """Translate text to the target language (default: Hindi)."""
    headers = {
        'Ocp-Apim-Subscription-Key': TRANSLATOR_KEY,
        'Ocp-Apim-Subscription-Region': TRANSLATOR_REGION,
        'Content-type': 'application/json'
    }
    params = {'to': to_lang}
    body = [{ 'text': text }]
    response = requests.post(TRANSLATOR_ENDPOINT, params=params, headers=headers, json=body)
    response.raise_for_status()
    return response.json()[0]['translations'][0]['text']
