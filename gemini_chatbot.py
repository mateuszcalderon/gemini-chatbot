import os
from google.colab import userdata
from google import genai
from google.genai import types

# Fetches my 'GOOGLE_API_KEY' from my Colab user data and sets it as an environment variable.
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

# Interacts with the Gemini API.
client = genai.Client()

"""
# Getting all model names:
for model in client.models.list():
    print(model.name)
"""

# Sets the Gemini model to be used.
MODEL_ID = 'gemini-2.0-flash'

chat_config = types.GenerateContentConfig(system_instruction='You are a capable, efficient AI assistant, providing quick, accurate, and helpful answers across a wide range of topics.')
chat = client.chats.create(model=MODEL_ID, config=chat_config)

# Chat loop interaction:
prompt = input("What do you have in mind? Ask Gemini: ")
while prompt.lower() != "exit":
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input("Ask Gemini (type 'exit' to quit): ")
