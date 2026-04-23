# %% Install dependencies
%pip install anthropic python-dotenv
# ------------------------

# %% Load the environment variables
from dotenv import load_dotenv
load_dotenv()
# ------------------------


# %% Create an API client
from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-6"
# ------------------------

# %% Add helper functions
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})
    print("> ", text)

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})
    print("* ", text)

def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": 1000,
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

# %% Make an initial list of messages
messages = []

# %% Provide the system prompt
system = """
You are an expert python developer.
You explain complex concepts in concise terms.
Please answer as concisely as possible.
No examples or code blocks.
"""


add_user_message(messages, "Generate a one-sentence movie idea")

answer = chat(messages, temperature=1.0)

add_assistant_message(messages, answer)
