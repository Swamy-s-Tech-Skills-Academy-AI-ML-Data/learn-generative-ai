"""  
a3_embeddings.py  
  
Enhanced Embedding Utility:  
- Secure API key loading  
- Get correct tokenizer for a model  
- Count tokens before embedding  
- Accepts text from command line or file  
- Saves embeddings to CSV  
"""

import os
import csv
import argparse
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
    """Get the correct tokenizer encoding for a given OpenAI model."""
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print(
            f"[Warning] Model '{model_name}' not found in tiktoken database. Using 'cl100k_base'."
        )
        encoding = tiktoken.get_encoding("cl100k_base")
    return encoding


def count_tokens(text: str, model_name: str) -> int:
    """Count tokens in a given text for a specific model's tokenizer."""
    encoding = get_encoding_for_model(model_name)
    return len(encoding.encode(text))


# ==============================
#  Embedding Helper
# ==============================
def get_embedding(text: str, model: str = "text-embedding-3-small") -> List[float]:
    """Generate an embedding vector for the given text."""
    token_count = count_tokens(text, model)
    print(f"[Info] Token count for input: {token_count}")
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding


# ==============================
#  Main Script
# ==============================
def main():
    parser = argparse.ArgumentParser(
        description="Generate embeddings for text input.")
    parser.add_argument("--text", type=str, help="Single text input to embed.")
    parser.add_argument("--file", type=str,
                        help="Path to a file with one text per line.")
    parser.add_argument("--model", type=str, default="text-embedding-3-small",
                        help="Embedding model to use.")
    parser.add_argument("--output", type=str, default="embeddings.csv",
                        help="Output CSV file to save embeddings.")
    args = parser.parse_args()

    # Collect inputs
    texts = []
    if args.text:
        texts.append(args.text)
    elif args.file:
        if not os.path.exists(args.file):
            raise FileNotFoundError(f"File not found: {args.file}")
        with open(args.file, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f if line.strip()]
    else:
        # Default sample inputs if none provided
        texts = [
            "I have a white dog named Champ.",
            "Artificial Intelligence is transforming the world.",
            "The Eiffel Tower is located in Paris, France."
        ]
        print("[Info] No input provided. Using default sample texts.")

    # Generate embeddings
    results = []
    for text in texts:
        print(f"\n[Processing] {text}")
        embedding_vector = get_embedding(text, model=args.model)
        results.append({
            "text": text,
            "embedding": embedding_vector
        })
        print(f"Embedding length: {len(embedding_vector)}")

    # Save to CSV
    with open(args.output, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["text", "embedding"])
        for row in results:
            writer.writerow([row["text"], row["embedding"]])

    print(f"\n[Success] Saved embeddings to {args.output}")


if __name__ == "__main__":
    main()

# Without Argument
# python a3_embeddings.py
# I have a white dog named Champ.
# Artificial Intelligence is transforming the world.
# The Eiffel Tower is located in Paris, France.


# python a3_embeddings.py --text "ChatGPT is a powerful AI assistant."

# python a3_embeddings.py --file input.txt
