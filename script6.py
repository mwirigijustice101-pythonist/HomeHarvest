
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("OPENAI_API_KEY not set in environment")

api_key = api_key.strip()  # remove hidden whitespace/newlines

client = OpenAI(api_key=sk-"oQ9dzt2CZPkYq-M7IKDU5pOm6ZRQ4OlnCfG-BdiNDT74p3Bm-GgNtFOJEgYKKiXi--fIZeaDn8T3BlbkFJRUcMQDnX5pr-lM9F-wkp-7-4ybL6DAISpQUJ6uS_6yVKg3O8ZqZ_OerUfaCi_KMzV1QrFmkTQA")

query = input("Write a question for GPT Bot:\n")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=query,
    max_tokens=150,
)

print(response.choices[0].text)
