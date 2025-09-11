# filename: a4_embeddings.py
"""  
a4_embeddings.py  
  
Embedding + FAISS Search Utility:  
- Secure API key loading  
- Token counting per model  
- Accepts text from arguments or file  
- Stores embeddings in FAISS vector database  
- Allows semantic search queries  
"""

import os
import argparse
from typing import List
import tiktoken
import faiss
import numpy as np
from openai import OpenAI

# ==============================
#  API Key Setup
# ==============================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "Missing OpenAI API key. Please set the environment variable 'OPENAI_API_KEY'."
    )

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
            f"[Warning] Model '{model_name}' not found. Using 'cl100k_base'.")
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
    print(f"[Info] Token count: {token_count}")
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding


# ==============================
#  FAISS Helper Functions
# ==============================
def create_faiss_index(embeddings: List[List[float]]) -> faiss.IndexFlatL2:
    """Create a FAISS index from embeddings."""
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)  # L2 distance
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)
    return index


def search_faiss(index: faiss.IndexFlatL2, query_embedding: List[float], k: int = 3):
    """Search FAISS index for the k most similar embeddings."""
    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, k)
    return distances[0], indices[0]


# ==============================
#  Main Script
# ==============================
def main():
    parser = argparse.ArgumentParser(
        description="Generate embeddings and store in FAISS.")
    parser.add_argument("--text", type=str, help="Single text input to embed.")
    parser.add_argument("--file", type=str,
                        help="Path to file with one text per line.")
    parser.add_argument("--model", type=str, default="text-embedding-3-small",
                        help="Embedding model to use.")
    parser.add_argument("--query", type=str,
                        help="Search query for semantic search.")
    parser.add_argument("--top_k", type=int, default=3,
                        help="Number of search results to return.")
    args = parser.parse_args()

    # Collect input texts
    if args.text:
        texts = [args.text]
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f if line.strip()]
    else:
        texts = [
            "I have a white dog named Champ.",
            "Artificial Intelligence is transforming the world.",
            "The Eiffel Tower is located in Paris, France.",
            "Python is a popular programming language.",
            "OpenAI develops advanced AI models."
        ]
        print("[Info] No input provided. Using default sample texts.")

    # Generate embeddings for dataset
    embeddings = [get_embedding(t, model=args.model) for t in texts]

    # Create FAISS index
    index = create_faiss_index(embeddings)
    print(f"[Info] FAISS index created with {len(texts)} entries.")

    # If query is provided, perform search
    if args.query:
        print(f"\n[Query] {args.query}")
        query_embedding = get_embedding(args.query, model=args.model)
        distances, indices = search_faiss(index, query_embedding, k=args.top_k)
        print("\n[Results]")
        for rank, idx in enumerate(indices):
            print(f"{rank+1}. {texts[idx]} (distance: {distances[rank]:.4f})")


if __name__ == "__main__":
    main()


# ## **How to Use `a4_embeddings.py`**

# ### 1️⃣ Install dependencies
# ```bash
# pip install openai tiktoken faiss-cpu numpy
# ```

# ### 2️⃣ Set your API key
# ```bash
# export OPENAI_API_KEY="your-api-key"   # macOS/Linux
# setx OPENAI_API_KEY "your-api-key"     # Windows PowerShell
# ```

# ---

# ### 3️⃣ Example Usages

# #### **Default sample texts + search**
# ```bash
# python a4_embeddings.py --query "Tell me about AI"
# ```
# **Example Output:**
# ```
# [Info] No input provided. Using default sample texts.
# [Info] Token count: 7
# ...
# [Query] Tell me about AI
# [Info] Token count: 4

# [Results]
# 1. Artificial Intelligence is transforming the world. (distance: 0.2371)
# 2. OpenAI develops advanced AI models. (distance: 0.3895)
# 3. Python is a popular programming language. (distance: 0.8120)
# ```

# ---

# #### **Custom text dataset from file**
# **`dataset.txt`**
# ```
# Bananas are yellow.
# Apples are red or green.
# Grapes are small and sweet.
# ```
# Run:
# ```bash
# python a4_embeddings.py --file dataset.txt --query "Which fruit is green?"
# ```

# ---

# #### **Single text list**
# ```bash
# python a4_embeddings.py --text "The Pacific Ocean is the largest ocean." --query "largest ocean"
# ```

# ---

# ✅ This script now:
# - **Generates embeddings**
# - **Stores them in FAISS**
# - **Performs semantic search**

# ---

# If you want, I can make **`a5_embeddings.py`** where:
# - FAISS index is **saved to disk** and **loaded later** without re-generating embeddings every time
# - You can **incrementally add new texts** to your vector store

# Do you want me to make that persistent FAISS version? That way your search database survives between runs.
