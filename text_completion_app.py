import os
from huggingface_hub import InferenceClient

EXIT_KEYWORDS = {"exit", "quit"}

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["COG_AI_TEXT_COMP_TOKEN"],
)

def prompt_user():
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    print("Welcome to the free AI Text Companion! Like all free things, however, it's a bit slow, so patience is appreciated.\nIf you want to leave, just type the word \"exit\" or \"quit\" when prompted.\n")
    
    while True:
        response = input("You: ")
        print("")

        if response.lower() in EXIT_KEYWORDS:
            break

        if len(response) > 0:
            get_ai_response(response)
        else:
            print("Please respond with some text. Pretty please?\n")
    
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

#work on getting quicker responses
def get_ai_response(person_response):
    completion = client.chat.completions.create(
        #model="sarvamai/sarvam-m",
        #model="meta-llama/Meta-Llama-3-8B",
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": person_response
            }
        ],
    )

    print("AI: ", completion.choices[0].message.content, "\n")

if __name__ == "__main__":
    prompt_user()
