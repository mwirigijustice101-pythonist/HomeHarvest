
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_")
if not api_key:
    raise SystemExit("OPENAI_API_KEY not set in environment")

api_key = api_key.strip()  # remove hidden whitespace/newlines

client = OpenAI(api_key=api_key)

query = input("Write a question for GPT Bot:\n")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=query,
    max_tokens=150,
)

print(response.choices[0].text)
