import os
from huggingface_hub import InferenceClient

TOKEN_LIMIT = 5000
EXIT_KEYWORDS = {"exit", "quit"}
MODELS_DICT = {"sarvamai": "sarvamai/sarvam-m", 
               "llama": "meta-llama/Llama-3.1-8B-Instruct"}

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["COG_AI_TEXT_COMP_TOKEN"],
    timeout=75 # time in seconds before timeout
)

def prompt_user():
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    help_text()
    
    curr_model = ["llama", MODELS_DICT["llama"]]
    settings = [0.5, 0.4]
    while True:
        response = input(f"You (to {curr_model[0]}): ").strip()
        response_split = response.split()
        print("")

        if response.lower() in EXIT_KEYWORDS:
            break
        if response.lower() == "help":
            help_text()
            continue
        if response in MODELS_DICT:
            curr_model = [response, MODELS_DICT[response]]
            continue
        if len(response_split) == 2 and (response_split[0] == "temperature" or response_split[0] == "top-p"):
            try:
                option = 0 if response_split[0] == "temperature" else 1
                val = float(response_split[1])

                if val < 0 or val > 1:
                    raise ValueError("The float must be between 0 and 1. Please try again.\n")
                settings[option] = val

            except ValueError as err:
                print(err)
            except TypeError:
                print("The float provided is not a number. Please try again.\n")
            except Exception:
                print("An unexpected error has occured. It is recommended you quit/exit out of this app and re-execute it to get it working properly.\n")
            finally:
                continue

        if len(response) > 0:
            get_ai_response(response, curr_model, settings)
        else:
            print("Please respond with some text. Pretty please?\n")
    
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

def help_text():
    print("If you want to leave, just type the word \"exit\" or \"quit\" when prompted.")
    print("Type \"sarvamai\" or \"llama\" to access those respective models.")
    print("Set the creativity and ideation of the AI to a float between 0 and 1 with:\n\t\"temperature float\" and \"top-p float\" respectively.")
    print("If you need these messages again, just type \"help\" when prompted.\n")

def get_ai_response(person_response, selected_model, settings):
    try:
        completion = client.chat.completions.create(
            model=selected_model[1],
            messages=[
                {
                    "role": "user",
                    "content": person_response
                }
            ],
            temperature= settings[0],
            max_tokens=TOKEN_LIMIT,
            top_p= settings[1]
        )

        print(f"AI ({selected_model[0]}): ", completion.choices[0].message.content, "\n")
    except Exception:
        print("The model wasn't able to respond to your prompt in time. Try using the other model or making future prompts shorter. \n")

if __name__ == "__main__":
    prompt_user()
