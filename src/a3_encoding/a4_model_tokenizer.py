# filename: a4_model_tokenizer.py
"""  
model_tokenizer.py  
  
Description:  
    This script allows you to:  
    - Enter an OpenAI model name and some text  
    - Automatically select the correct tiktoken encoding for that model  
    - Encode the text into token IDs  
    - Decode tokens back to the original text  
    - Display a token-to-ID mapping table  
    - Special "compare" mode: run text through all three major encodings to compare results  
  
Requirements:  
    pip install tiktoken  
  
Usage:  
    python model_tokenizer.py  
"""

import tiktoken


def get_encoding_for_model(model_name: str) -> tiktoken.Encoding:
    """  
    Determine and return the correct tiktoken encoding for a given OpenAI model.  

    Uses tiktoken's internal mapping to find the right encoding.  
    Falls back to 'cl100k_base' if the model is unknown.  

    Args:  
        model_name (str): Name of the OpenAI model (e.g., "gpt-4", "text-davinci-003")  

    Returns:  
        tiktoken.Encoding: Encoding object for the model.  
    """
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print(
            f"[Warning] Model '{model_name}' not found in tiktoken database. Using 'cl100k_base'.")
        encoding = tiktoken.get_encoding("cl100k_base")
    return encoding


def display_tokenization(encoding: tiktoken.Encoding, model_label: str, text: str):
    """Tokenize text with given encoding and print results."""
    tokens = encoding.encode(text)
    print("\n--- Tokenization ---")
    print(f"Model/Encoding: {model_label}")
    print(f"Encoding used: {encoding.name}")
    print(f"Token count: {len(tokens)}")
    print(f"Token IDs: {tokens}")

    decoded_text = encoding.decode(tokens)
    print("\n--- Decoded Text ---")
    print(decoded_text)

    print("\n--- Token to ID Mapping ---")
    print(f"{'Token':<20} | {'Token ID'}")
    print("-" * 35)
    for token_str, token_id in zip([encoding.decode([t]) for t in tokens], tokens):
        print(f"{repr(token_str):<20} | {token_id}")


if __name__ == "__main__":
    model_name = input(
        "Enter the OpenAI model name (or 'compare' to test all encodings): ").strip()
    prompt = input("Enter the text to tokenize: ").strip()

    if model_name.lower() == "compare":
        print("\n[Compare Mode] Testing all major encodings...\n")
        encodings_to_test = [
            ("Modern Models (cl100k_base)", tiktoken.get_encoding("cl100k_base")),
            ("Older GPT-3/Codex (p50k_base)", tiktoken.get_encoding("p50k_base")),
            ("Legacy GPT-3 (r50k_base)", tiktoken.get_encoding("r50k_base")),
        ]
        for label, enc in encodings_to_test:
            display_tokenization(enc, label, prompt)
            print("\n" + "=" * 50 + "\n")
    else:
        encoding = get_encoding_for_model(model_name)
        display_tokenization(encoding, model_name, prompt)

# Examples
# Enter the OpenAI model name (or 'compare' to test all encodings): compare
# Enter the text to tokenize: I have a white dog named Champ.
