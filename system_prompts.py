import anthropic
import os
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
def ask_claude(system_prompt, user_message):
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return message.content[0].text
print("=== EXPERIMENT 1: Music Curator ===")

music_prompt = """You are an expert music curator at a top 
streaming platform. You recommend songs based on emotions. 
Always recommend exactly 3 songs with reasons why each fits."""

print(ask_claude(music_prompt, "I feel like coding all night"))
print("\n")

print("=== EXPERIMENT 2: Harsh Web Dev Mentor ===")

webdev_prompt = """You are a brutally honest senior web developer. 
You review ideas critically. Always point out 2 problems 
before saying anything positive. Be direct and short."""

print(ask_claude(webdev_prompt, "I want to build a music recommendation app"))
print("\n")
print("=== EXPERIMENT 3: Simple Explainer ===")

simple_prompt = """You are a teacher who explains everything 
using simple analogies. Never use technical jargon. 
Always use one real world comparison."""

print(ask_claude(simple_prompt, "What is an API?"))