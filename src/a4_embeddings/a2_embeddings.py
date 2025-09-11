# filename: a2_embeddings.py
"""  
a2_embeddings.py  
  
Embedding Utility Script:  
- Loads OpenAI API key securely from environment  
- Determines correct tokenizer for a given model  
- Counts tokens before embedding  
- Generates embeddings using OpenAI API  
"""

import os
from typing import List
import tiktoken
from openai import OpenAI

# ==============================
#  API Key Setup
# ==============================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "Missing OpenAI API key. Please set the environment variable 'OPENAI_API_KEY'."
    )

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


# ==============================
#  Tokenizer Helper
# ==============================
def get_encoding_for_model(model_name: str) -> tiktoken.Encoding:
    """  
    Get the correct tokenizer encoding for a given OpenAI model.  
    Falls back to 'cl100k_base' if the model is unknown.  
    """
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print(
            f"[Warning] Model '{model_name}' not found in tiktoken database. Using 'cl100k_base'."
        )
        encoding = tiktoken.get_encoding("cl100k_base")
    return encoding


def count_tokens(text: str, model_name: str) -> int:
    """  
    Count tokens in a given text for a specific model's tokenizer.  
    """
    encoding = get_encoding_for_model(model_name)
    return len(encoding.encode(text))


# ==============================
#  Embedding Helper
# ==============================
def get_embedding(
    text: str,
    model: str = "text-embedding-3-small"
) -> List[float]:
    """  
    Generate an embedding vector for the given text using the specified OpenAI embedding model.  
    """
    # Count tokens for info
    token_count = count_tokens(text, model)
    print(f"[Info] Token count for input: {token_count}")

    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding


# ==============================
#  Example Usage
# ==============================
if __name__ == "__main__":
    # Example text
    sample_text = "I have a white dog named Champ."

    # Choose embedding model
    embedding_model = "text-embedding-3-small"

    # Generate embedding
    embedding_vector = get_embedding(sample_text, model=embedding_model)

    # Output results
    print(f"Model: {embedding_model}")
    print(f"Embedding Length: {len(embedding_vector)}")
    print(f"Embedding (first 5 values): {embedding_vector[:5]}")
