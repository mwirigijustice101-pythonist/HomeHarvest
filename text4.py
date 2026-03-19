
import openai

openai.api_key = "sk-Jo954QaSjnowxo3Rxh1MZ_-m59_69Ecn6ajJUkq5pJ3OYvpDYgvr09k8uYimjhJsr0g5JnyOS7T3BlbkFJi52Ip2udyJ6M7RHYG86fQKkigSXrLucH3dyCSAbgTOArUGhWhGFp3PUQCuIR2hvreiizqwUkQA"

query = input("Write a question for GPT Bot:\n")

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=query,
    max_tokens=150,
)

data = response.choices[0].text
print(data)
