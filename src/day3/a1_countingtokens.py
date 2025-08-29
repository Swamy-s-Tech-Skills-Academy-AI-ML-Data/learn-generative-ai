"""  
File: countingtokens.py  
Author: Your Name  
Description:  
    This script demonstrates how to count the number of tokens   
    in a given text string using the `tiktoken` library.  
  
    The script can accept user input and display:  
        - Token count  
        - Token IDs  
        - Decoded tokens  
        - A table mapping each token to its ID  
  
Requirements:  
    pip install tiktoken  
"""

import tiktoken


def count_tokens(text: str, encoding_name: str) -> tuple:
    """  
    Count the number of tokens in the given text using the specified encoding.  

    Args:  
        text (str): The input string to tokenize.  
        encoding_name (str): The encoding scheme to use (e.g., 'cl100k_base').  

    Returns:  
        tuple: (token_count, token_ids, decoded_tokens)  
    """
    # Get encoding object
    encoding = tiktoken.get_encoding(encoding_name)

    # Encode text to tokens
    token_ids = encoding.encode(text)

    # Decode each token ID back to text for clarity
    decoded_tokens = [encoding.decode([token]) for token in token_ids]

    return len(token_ids), token_ids, decoded_tokens


if __name__ == "__main__":
    # Ask the user for a prompt
    prompt = input("Enter the text you want to tokenize: ").strip()
    encoding_scheme = "cl100k_base"  # Encoding scheme used by GPT-4 / GPT-3.5

    token_count, token_ids, decoded_tokens = count_tokens(
        prompt, encoding_scheme)

    print("\n--- Tokenization Results ---")
    print(f"Text: {prompt}")
    print(f"Encoding scheme: {encoding_scheme}")
    print(f"Number of tokens: {token_count}")

    # Print token IDs and tokens
    print("\nToken IDs:", token_ids)
    print("Decoded tokens:", decoded_tokens)

    # Pretty table mapping
    print("\n--- Token to ID Mapping ---")
    print(f"{'Token':<20} | {'Token ID'}")
    print("-" * 35)
    for token, token_id in zip(decoded_tokens, token_ids):
        print(f"{repr(token):<20} | {token_id}")


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
