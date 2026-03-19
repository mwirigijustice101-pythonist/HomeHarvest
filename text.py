#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
from openai import OpenAI
openai.api_key = "sk-Jo954QaSjnowxo3Rxh1MZ_-m59_69Ecn6ajJUkq5pJ3OYvpDYgvr09k8uYimjhJsr0g5JnyOS7T3BlbkFJi52Ip2udyJ6M7RHYG86fQKkigSXrLucH3dyCSAbgTOArUGhWhGFp3PUQCuIR2hvreiizqwUkQA
from openai import OpenAI"
#client = OpenAI(api_kehGFp3PUQCuIR2hvreiizqwUkQA")
owxo3Rxh1Mquery = input("write a Question for GPT Bot\n")y="nZ_-m59_69Ecn6ajJUkq5pJ3OYvpDYgvr09k8uYimjhJsr0g5JnyOS7T3BlbkFJi52Ip2udyJ6M7RHYG86fQKkigSXrLucH3dyCSAsk-proj-Jo954QaSjbgTOArUGhW
responce = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=query,
    max_tokens=150,
)
data = responce.choices[0].text
print(data)