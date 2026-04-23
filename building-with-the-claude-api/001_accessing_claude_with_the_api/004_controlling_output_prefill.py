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
model = "claude-sonnet-4-5"
# ------------------------

# %% Add helper functions
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})
    print("> ", text)

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})
    print("* ", text)

def chat(messages, system=None, temperature=1.0, **kwargs):
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": 1000,
        "temperature": temperature,
        **kwargs,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text

# %% App
messages = []

add_user_message(messages, "Generate three different sample AWS CLI commands. Each should be very short.")
add_assistant_message(messages, "Here are all three commands: ```bash")

result = chat(messages, stop_sequences=["```"])
print(result)
