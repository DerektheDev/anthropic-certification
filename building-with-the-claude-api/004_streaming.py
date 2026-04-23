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

# %% Setup
# Make an initial list of messages
messages = []

# %% Print events
# add_user_message(messages, "Write a 1 sentence description of a fake database")

# stream = client.messages.create(
#   model=model,
#   max_tokens=1000,
#   messages=messages,
#   stream=True
# )

# for event in stream:
#   print(event)


add_user_message(messages, "Write a 1 sentence description of a fake database")

# Streaming method!
with client.messages.stream(
  model=model,
  max_tokens=1000,
  messages=messages
) as stream:
  for text in stream.text_stream:
    pass
    # print(text, end="")
# Store the final response to some variable
final = stream.get_final_message()

print(final.content)
