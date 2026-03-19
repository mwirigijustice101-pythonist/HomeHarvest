#script4.py

#Import os to read environment variables securely
import os

# Import the OpenAI client class from the installed SDK
from openai import OpenAI

#Read the API key from the environment variable OPEAI_API_KEY
#This avoids hardcoding secret in your file and prevents accidental leaks
api_key = os.environ.get("OPENAI_API_KEY")

#if the key is missing,stop immediately with clear message
#This prevents confusing authentication errors later
if not api_key:
    raise SystemExit("OPENAI_API_KEY is not set in the environment")

#Remove any leading/trailing whitespace or hidden new lines that breaks the key
# script4.py

# Import os to read environment variables securely
import os

# Import the OpenAI client class from the installed SDK
from openai import OpenAI

# Read the API key from the environment variable OPENAI_API_KEY
# This avoids hardcoding secrets in your file and prevents accidental leaks
api_key = os.getenv("OPENAI_API_KEY")

# If the key is missing, stop immediately with a clear message
# This prevents confusing authentication errors later
if not api_key:
    raise SystemExit("OPENAI_API_KEY not set in environment")

# Remove any leading/trailing whitespace or hidden newlines that break the key
# Copy/paste can add invisible characters; .strip() prevents that
api_key = api_key.strip()

# Initialize the OpenAI client with the cleaned API key
# The OpenAI class is the new SDK entry point for requests
client = OpenAI(api_key=api_key)

# Prompt the user for a question to send to the model
# Using input keeps the script interactive for your assignment
query = input("Write a question for GPT Bot:\n")

# Call the completions endpoint using the new client style
# model: gpt-3.5-turbo-instruct is supported in the SDK; max_tokens limits response length
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=query,
    max_tokens=150,
)

# Extract and print the text from the first choice returned by the API
# The SDK returns a list of choices; .choices[0].text is the actual generated text
print(response.choices[0].text)
