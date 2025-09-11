# filename: a3_model_tokenizer.py
"""  
model_tokenizer.py  
  
Description:  
    This script allows you to:  
    - Enter an OpenAI model name and some text  
    - Automatically select the correct tiktoken encoding for that model  
    - Encode the text into token IDs  
    - Decode tokens back to the original text  
    - Display a token-to-ID mapping table  
  
Requirements:  
    pip install tiktoken  
  
Usage:  
    python model_tokenizer.py  
"""

import tiktoken


def get_encoding_for_model(model_name: str) -> tiktoken.Encoding:
    """  
    Determine and return the correct tiktoken encoding for a given OpenAI model.  

    This function uses tiktoken's internal mapping to look up the correct  
    encoding scheme for the specified model. Encodings define how text is  
    split into tokens and how tokens are mapped to unique IDs.  

    If the provided model name is not recognized, the function falls back  
    to using 'cl100k_base', which is the default encoding for most modern  
    OpenAI models (e.g., GPT-4, GPT-3.5, and latest embeddings).  

    Args:  
        model_name (str):  
            The name of the OpenAI model (e.g., "gpt-4", "text-davinci-003").  
            The name should match an official OpenAI model identifier.  

    Returns:  
        tiktoken.Encoding:  
            The encoding object corresponding to the given model. This object  
            can be used to encode text into token IDs and decode token IDs back  
            into text.  

    Example:  
        >>> enc = get_encoding_for_model("gpt-4")  
        >>> tokens = enc.encode("Hello world!")  
        >>> print(tokens)  
        [9906, 1917, 0]  
        >>> text = enc.decode(tokens)  
        >>> print(text)  
        Hello world!  
    """
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print(
            f"[Warning] Model '{model_name}' not found in tiktoken database. Using 'cl100k_base'.")
        encoding = tiktoken.get_encoding("cl100k_base")
    return encoding


if __name__ == "__main__":
    # Get user input
    model_name = input("Enter the OpenAI model name: ").strip()
    prompt = input("Enter the text to tokenize: ").strip()

    # Get correct encoding for this model
    encoding = get_encoding_for_model(model_name)

    # Encode the text
    tokens = encoding.encode(prompt)
    print("\n--- Tokenization ---")
    print(f"Model: {model_name}")
    print(f"Encoding used: {encoding.name}")
    print(f"Token count: {len(tokens)}")
    print(f"Token IDs: {tokens}")

    # Decode back to string
    decoded_text = encoding.decode(tokens)
    print("\n--- Decoded Text ---")
    print(decoded_text)

    # Token-to-ID mapping
    print("\n--- Token to ID Mapping ---")
    print(f"{'Token':<20} | {'Token ID'}")
    print("-" * 35)
    for token_str, token_id in zip([encoding.decode([t]) for t in tokens], tokens):
        print(f"{repr(token_str):<20} | {token_id}")

##### Examples #####
# Enter the OpenAI model name: gpt-4
# Enter the text to tokenize: I have a white dog named Champ.

# Enter the OpenAI model name: text-davinci-003
# Enter the text to tokenize: I have a white dog named Champ.

# Enter the OpenAI model name: davinci
# Enter the text to tokenize: I have a white dog named Champ.

# Enter the OpenAI model name: text-embedding-ada-002
# Enter the text to tokenize: The quick brown fox jumps over the lazy dog.

# Enter the OpenAI model name: my-custom-model
# Enter the text to tokenize: This is a test.
