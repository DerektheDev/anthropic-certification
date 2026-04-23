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

def chat(messages, system=None, temperature=1.0, output_config=None, **kwargs):
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": 1000,
        "temperature": temperature,
        **kwargs,
    }

    if system:
        params["system"] = system

    if output_config:
        params["output_config"] = output_config

    message = client.messages.create(**params)
    return message.content[0].text

# %% App
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")

result = chat(messages, output_config={
  "format": {
    "type": "json_schema",
    "schema": {
      "type": "object",
      "properties": {
        "source": {"type": "array", "items": {"type": "string"}},
        "detail-type": {"type": "array", "items": {"type": "string"}},
        "detail": {
          "type": "object",
          "properties": {
            "state": {"type": "string"}
          },
          "required": ["state"],
          "additionalProperties": False
        }
      },
      "required": ["source", "detail-type"],
      "additionalProperties": False
    }
  }
})
print(result)
