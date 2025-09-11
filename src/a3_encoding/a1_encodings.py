# filename: a1_encodings.py
"""  
File: token_encodings.py  
Description:  
    Demonstrates how to encode and decode text into tokens  
    using different tokenization schemes with the `tiktoken` library.  
  
    It:  
    - Accepts user text input  
    - Encodes it with multiple encodings (cl100k_base, p50k_base, r50k_base)  
    - Displays token counts and token IDs in a table  
    - Demonstrates decoding tokens back into text  
"""

import tiktoken as tk


def get_tokens(text: str, encoding_name: str) -> list:
    """  
    Encode text into token IDs using the given encoding scheme.  
    """
    encoding = tk.get_encoding(encoding_name)
    return encoding.encode(text)


def get_string(tokens: list, encoding_name: str) -> str:
    """  
    Decode token IDs back into text using the given encoding scheme.  
    """
    encoding = tk.get_encoding(encoding_name)
    return encoding.decode(tokens)


if __name__ == "__main__":
    # Prompt user for input text
    prompt = input("Enter the text to tokenize: ").strip()

    # List of encoding schemes to test
    encodings = ["cl100k_base", "p50k_base", "r50k_base"]

    print("\n--- Tokenization Results ---")
    for enc in encodings:
        tokens = get_tokens(prompt, enc)
        print(f"\nEncoding: {enc}")
        print(f"Token count: {len(tokens)}")
        print(f"Token IDs: {tokens}")

    # Example decoding demonstration
    print("\n--- Decoding Example (cl100k_base) ---")
    sample_tokens = get_tokens(prompt, "cl100k_base")
    decoded_text = get_string(sample_tokens, "cl100k_base")
    print(f"Tokens: {sample_tokens}")
    print(f"Decoded text: {decoded_text}")

    # Optional: show token-to-ID mapping for cl100k_base
    print("\n--- Token to ID Mapping (cl100k_base) ---")
    encoding = tk.get_encoding("cl100k_base")
    decoded_tokens = [encoding.decode([t]) for t in sample_tokens]
    print(f"{'Token':<20} | {'Token ID'}")
    print("-" * 35)
    for token_str, token_id in zip(decoded_tokens, sample_tokens):
        print(f"{repr(token_str):<20} | {token_id}")

# Short sentences
# The sky is clear and blue today.
# Cats love to sleep on warm sunny afternoons.
# AI is changing the world.

# Medium sentences
# Learning Python opens the door to endless programming possibilities.
# Space exploration has inspired generations to dream beyond our planet.
# The quick brown fox jumps over the lazy dog.

# Longer sentences
# In the near future, artificial intelligence will be integrated into almost every aspect of human life, from healthcare and education to transportation and entertainment.
# Climate change remains one of the most pressing challenges of our time, requiring global cooperation and innovative solutions to ensure a sustainable future.
# The human brain is an incredibly complex organ, capable of processing vast amounts of information while also enabling creativity, emotion, and problem-solving.
