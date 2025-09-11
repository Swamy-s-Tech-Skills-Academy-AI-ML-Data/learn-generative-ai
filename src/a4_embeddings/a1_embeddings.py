# filename: a1_embeddings.py
"""  
Embedding Helper Script  
  
This script securely connects to the OpenAI API, generates embeddings for a given text,  
and prints the embedding length and first few values for inspection.  
"""

import os
from openai import OpenAI
from typing import List

# Load API key from environment variable for security
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "Missing OpenAI API key. Please set the environment variable 'OPENAI_API_KEY'."
    )

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def get_embedding(
    text: str,
    model: str = "text-embedding-3-small"
) -> List[float]:
    """  
    Generate an embedding vector for the given text using the specified OpenAI embedding model.  

    Args:  
        text (str): The input string to embed.  
        model (str): The OpenAI embedding model to use.  
                     Options: "text-embedding-3-small", "text-embedding-3-large", etc.  

    Returns:  
        List[float]: The embedding vector as a list of floating-point numbers.  

    Example:  
        >>> embedding = get_embedding("I have a white dog named Champ.")  
        >>> print(len(embedding))  
        1536  
    """
    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding


if __name__ == "__main__":
    sample_text = "I have a white dog named Champ."
    embedding_vector = get_embedding(sample_text)

    print(f"Text: {sample_text}")
    print(f"Embedding Length: {len(embedding_vector)}")
    print(f"Embedding (first 5 values): {embedding_vector[:5]}")
