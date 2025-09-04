"""  
a5_embeddings.py  
  
Persistent FAISS Embedding Search Tool:  
- Secure API key loading  
- Token counting per model  
- Stores FAISS index & metadata to disk  
- Can add new text data without losing previous embeddings  
- Allows semantic search queries  
"""

import os
import argparse
import pickle
from typing import List
import numpy as np
import tiktoken
import faiss
from openai import OpenAI

# ==============================
#  Configuration
# ==============================
INDEX_FILE = "faiss_index.bin"
META_FILE = "faiss_texts.pkl"

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
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print(
            f"[Warning] Model '{model_name}' not found. Using 'cl100k_base'.")
        encoding = tiktoken.get_encoding("cl100k_base")
    return encoding


def count_tokens(text: str, model_name: str) -> int:
    encoding = get_encoding_for_model(model_name)
    return len(encoding.encode(text))

# ==============================
#  Embedding Helper
# ==============================


def get_embedding(text: str, model: str = "text-embedding-3-small") -> List[float]:
    token_count = count_tokens(text, model)
    print(f"[Info] Token count: {token_count}")
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding

# ==============================
#  FAISS Persistence Helpers
# ==============================


def save_faiss_index(index: faiss.IndexFlatL2, texts: List[str]):
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(texts, f)
    print(f"[Saved] Index -> {INDEX_FILE}, Metadata -> {META_FILE}")


def load_faiss_index():
    if not os.path.exists(INDEX_FILE) or not os.path.exists(META_FILE):
        return None, []
    index = faiss.read_index(INDEX_FILE)
    with open(META_FILE, "rb") as f:
        texts = pickle.load(f)
    print(f"[Loaded] Index with {len(texts)} entries.")
    return index, texts

# ==============================
#  Search Helper
# ==============================


def search_faiss(index: faiss.IndexFlatL2, query_embedding: List[float], k: int = 3):
    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, k)
    return distances[0], indices[0]

# ==============================
#  Main Script
# ==============================


def main():
    parser = argparse.ArgumentParser(
        description="Persistent FAISS embedding search.")
    parser.add_argument("--add", type=str, help="Single text to add to index.")
    parser.add_argument("--file", type=str,
                        help="File with one text per line to add.")
    parser.add_argument("--query", type=str,
                        help="Search query for semantic search.")
    parser.add_argument("--model", type=str, default="text-embedding-3-small",
                        help="Embedding model to use.")
    parser.add_argument("--top_k", type=int, default=3,
                        help="Number of search results.")
    args = parser.parse_args()

    # Load existing index or start new
    index, texts = load_faiss_index()
    if index is None:
        index = faiss.IndexFlatL2(1536)
        print("[Info] Created new FAISS index.")

    # Add new data
    new_texts = []
    if args.add:
        new_texts.append(args.add)
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            new_texts = [line.strip() for line in f if line.strip()]

    if new_texts:
        print(f"[Adding] {len(new_texts)} new texts to index...")
        new_embeddings = [get_embedding(t, model=args.model)
                          for t in new_texts]
        new_vectors = np.array(new_embeddings).astype("float32")
        index.add(new_vectors)
        texts.extend(new_texts)
        save_faiss_index(index, texts)

    # Search
    if args.query:
        if len(texts) == 0:
            print("[Error] No data in index to search.")
            return
        print(f"[Query] {args.query}")
        query_embedding = get_embedding(args.query, model=args.model)
        distances, indices = search_faiss(index, query_embedding, k=args.top_k)
        print("\n[Results]")
        for rank, idx in enumerate(indices):
            print(f"{rank+1}. {texts[idx]} (distance: {distances[rank]:.4f})")


if __name__ == "__main__":
    main()

# ## **How This Works**
# - First run can **add** texts to create a new FAISS index.
# - Future runs **load** the existing index from disk.
# - You can **add more data** without losing old entries.
# - You can **query** the stored database anytime without re-embedding everything.

# ---

# ## **Usage Examples**

# ### 1️⃣ Add some initial data
# ```bash
# python a5_embeddings.py --add "Artificial Intelligence is transforming the world."
# python a5_embeddings.py --add "The Eiffel Tower is located in Paris, France."
# python a5_embeddings.py --add "Python is a popular programming language."
# ```

# ---

# ### 2️⃣ Add multiple entries from a file
# **dataset.txt**
# ```
# Bananas are yellow.
# Apples can be red or green.
# Grapes are small and sweet.
# ```
# ```bash
# python a5_embeddings.py --file dataset.txt
# ```

# ---

# ### 3️⃣ Search the stored FAISS index
# ```bash
# python a5_embeddings.py --query "Which fruit is green?"
# ```
# Example Output:
# ```
# [Loaded] Index with 6 entries.
# [Query] Which fruit is green?
# [Info] Token count: 5

# [Results]
# 1. Apples can be red or green. (distance: 0.1923)
# 2. Bananas are yellow. (distance: 0.7512)
# 3. Grapes are small and sweet. (distance: 0.8321)
# ```

# ---

# ### 4️⃣ Mix adding and searching in one run
# ```bash
# python a5_embeddings.py --add "The Pacific Ocean is the largest ocean." --query "largest ocean"
# ```

# ---

# ✅ Now you have a **persistent FAISS embedding search system** —
# no more re-generating embeddings for the same dataset each time.

# ---

# If you want, I can make **`a6_embeddings.py`** next, where:
# - The FAISS index supports **metadata fields** (title, category, etc.)
# - You can **filter search results** by metadata
# - It can store **document IDs** for retrieval in larger apps

# Do you want me to make `a6_embeddings.py` with metadata support? That would make it ready for production-scale document search.
