import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
system_prompt = """You are an expert movie and series recommender. 
You remember everything the user tells you in the conversation.
You always ask one follow up question to understand their taste better.
You never recommend the same thing twice.
You suggest both movies and series based on mood and genre."""
# This list stores the entire conversation history
# We add to it every time the user says something and Claude replies
conversation_history = []
# Welcome message
print("=== Tollywood Film Recommender ===")
print("Tell me your mood or what kind of film you want!")
print("Type 'quit' to exit")
print("=" * 35)

# Keep chatting until user types quit
while True:
    # Get user input
    user_input = input("\nYou: ")
    
    # Exit if user types quit
    if user_input.lower() == "quit":
        print("Happy watching! 🎬")
        break
    
    # Add user message to conversation history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Send full conversation history to Claude
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        system=system_prompt,
        messages=conversation_history
    )
    
    # Get Claude's reply
    reply = message.content[0].text
    
    # Add Claude's reply to conversation history
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    # Print Claude's reply
    print(f"\nBot: {reply}")
