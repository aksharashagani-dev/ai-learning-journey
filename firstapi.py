import anthropic
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

# Create the Claude client using your API key
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Send a message to Claude and get a response
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Recommend 5 songs for a late night coding session"}
    ]
)

# Print Claude's response
print(message.content[0].text)