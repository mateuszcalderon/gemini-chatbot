## Code Walkthrough:
#### Libraries:
```python
  import os
  from google.colab import userdata
  from google import genai
  from google.genai import types
```

  - ` os `: Interact with the operating system, specifically to set an environment variable.
  - ` google.colab ` and ` userdata `: Allow for securely access sensitive data (like API keys) stored in Colab environment, without embedding it directly in code.
  - ` google.genai `: The main library for interacting with the Google Gemini API.
  - ` google.genai.types `: Provides specific data types and configurations for the Gemini API, such as ` GenerateContentConfig `.

#### Configuring the Gemini chatbot:
` os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY') `: This line fetches my ` GOOGLE_API_KEY ` from my Colab user data and sets it as an environment variable. The ` genai ` library automatically picks up the API key from this environment variable.

` client = genai.Client() `: It creates an instance of the Gemini client, which is the main point of interaction with the Gemini API.

` MODEL_ID = 'gemini-2.0-flash' `: This sets the Gemini model to be used.

` chat_config = types.GenerateContentConfig(system_instruction=...) `: The 'system_instruction' argument is a powerful feature that allows users to "customize" the chatbot with specific instructions about its persona or purpose.

` chat = client.chats.create(model=MODEL_ID, config=chat_config) `: This line initiates a chat session with the specified ` MODEL_ID ` and applies the ` chat_config ` (our system instruction). The chat object will maintain the conversation history.

#### Chat Loop:
```python
prompt = input("What do you have in mind? Ask Gemini: ")
while prompt.lower() != "exit":
    response = chat.send_message(prompt)
    print(response.text)
    prompt = input("Ask Gemini (type 'exit' to quit): ")
```

  - First, the code prompts the user to start the conversation.
  - The while loop continues as long as the user does not type "exit".
  - The ` chat.send_message(prompt) ` sends the user's input to the Gemini model. Because ` chat ` maintains the conversation history, the model remembers previous turns.
  - ` print(response.text) ` displays the chatbot's reply.
  - Then, the loop prompts the user for their next question, keeping the conversation going.

## Development Environment:
This project was built on Google Colab.
The main dependency,` google-genai `, was installed using the following command: ` !pip install google-genai `
