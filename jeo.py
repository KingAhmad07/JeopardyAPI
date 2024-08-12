from secret import *
from openai import AzureOpenAI

ENDPOINT = AZURE_OPENAI_ENDPOINT
KEY = AZURE_OPENAI_API_KEY
MODEL = "gpt-35-turbo"

openai_client = AzureOpenAI(
    api_key=KEY,
    azure_endpoint=ENDPOINT,
    api_version="2024-05-01-preview"
)
advice_prompt = "Hi, respond back"
response = openai_client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a highly skilled teacher that wants to create jeopardry"},
        {"role": "user", "content": advice_prompt}
    ],
    max_tokens=300
)
ai_response = response.choices[0].message.content
print(ai_response)

