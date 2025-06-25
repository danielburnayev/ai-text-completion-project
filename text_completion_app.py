import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["COG_AI_TEXT_COMP_TOKEN"],
)

def prompt_user():
    while True:
        response = input("Welcome to the free AI Text Companion!")
        get_ai_response(response)

def get_ai_response(person_response):
    completion = client.chat.completions.create(
        model="sarvamai/sarvam-m",
        #model="meta-llama/Meta-Llama-3-8B",
        messages=[
            {
                "role": "user",
                "content": person_response
            }
        ],
    )

    print(completion.choices[0].message.content)

if __name__ == "__main__":
    prompt_user()
