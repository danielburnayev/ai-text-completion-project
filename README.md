# ai-text-completion-project

## Setup
Make sure you make the following installations in your command line interface before running the following code:
`pip install os
pip install huggingface_hub`
This would install the os and huggingface_hub packages for you, which will be used in this text_completion_app.py file

Also, in your ~/.bashrc (for Bash), ~/.zshrc (for ZShell), or $PROFILE (for Powershell) files, make sure to include your HuggingFace fine-grained token inside it like so:
export COG_AI_TEXT_COMP_TOKEN=[your fine-grained token's hash] (for Bash & ZShell)
OR
$env:COG_AI_TEXT_COMP_TOKEN = "[your fine-grained token's hash]" (for Powershell)

To the best of my knowledge, that's all you should need.

## Usage
This is a general purpose AI, effectively serving as an AI chatbot, but it does specialize primarily in text generation. One can run the program with the following command: `python3 text_completion_app.py`


## Dependencies
As mentioned before, this relies on the os and huggingface_hub Python libraries, available for Python versions >= 3.12. It also requires a fine-grained access token to be set up on your personal HuggingFace account.
