# filename: a6_embeddings.py
"""  
a6_embeddings.py  
  
Persistent FAISS Semantic Search with Metadata Filtering  
- Each record has: doc_id, title, category, content  
- Stores FAISS index + metadata to disk  
- Supports adding new entries without losing old ones  
- Allows filtering search results by category or doc_id  
"""

import os
import argparse
import pickle
import json
import uuid
from typing import List, Dict
import numpy as np
import tiktoken
import faiss
from openai import OpenAI

# ==============================
#  Configuration
# ==============================
INDEX_FILE = "faiss_index.bin"
META_FILE = "faiss_metadata.json"

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
#  Persistence Helpers
# ==============================


def save_index_and_metadata(index: faiss.IndexFlatL2, metadata: List[Dict]):
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print(f"[Saved] Index -> {INDEX_FILE}, Metadata -> {META_FILE}")


def load_index_and_metadata():
    if not os.path.exists(INDEX_FILE) or not os.path.exists(META_FILE):
        return None, []
    index = faiss.read_index(INDEX_FILE)
    with open(META_FILE, "r", encoding="utf-8") as f:
        metadata = json.load(f)
    print(f"[Loaded] Index with {len(metadata)} entries.")
    return index, metadata

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
        description="Persistent FAISS search with metadata.")
    parser.add_argument("--add", action="store_true",
                        help="Flag to add new entries.")
    parser.add_argument("--title", type=str, help="Title of the document.")
    parser.add_argument("--category", type=str,
                        help="Category of the document.")
    parser.add_argument("--content", type=str,
                        help="Content text of the document.")
    parser.add_argument("--file", type=str,
                        help="File with JSON list of metadata+content to add.")
    parser.add_argument("--query", type=str,
                        help="Search query for semantic search.")
    parser.add_argument("--filter_category", type=str,
                        help="Filter search results by category.")
    parser.add_argument("--filter_doc_id", type=str,
                        help="Filter search results by doc_id.")
    parser.add_argument("--model", type=str, default="text-embedding-3-small",
                        help="Embedding model to use.")
    parser.add_argument("--top_k", type=int, default=3,
                        help="Number of search results.")
    args = parser.parse_args()

    # Load or create index
    index, metadata = load_index_and_metadata()
    if index is None:
        index = faiss.IndexFlatL2(1536)
        print("[Info] Created new FAISS index.")

    # Add new entries
    if args.add:
        new_entries = []
        if args.content and args.title and args.category:
            new_entries.append({
                "doc_id": str(uuid.uuid4()),
                "title": args.title,
                "category": args.category,
                "content": args.content
            })
        elif args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                loaded_entries = json.load(f)
                for entry in loaded_entries:
                    if all(k in entry for k in ("title", "category", "content")):
                        entry["doc_id"] = str(uuid.uuid4())
                        new_entries.append(entry)
        else:
            print("[Error] To add, provide --title --category --content OR --file")
            return

        print(f"[Adding] {len(new_entries)} new entries...")
        embeddings = [get_embedding(e["content"], model=args.model)
                      for e in new_entries]
        vectors = np.array(embeddings).astype("float32")
        index.add(vectors)
        metadata.extend(new_entries)
        save_index_and_metadata(index, metadata)

    # Search
    if args.query:
        if len(metadata) == 0:
            print("[Error] No data in index to search.")
            return
        print(f"[Query] {args.query}")
        query_embedding = get_embedding(args.query, model=args.model)
        distances, indices = search_faiss(
            index, query_embedding, k=args.top_k * 2)  # search wider, filter later

        results = []
        for rank, idx in enumerate(indices):
            if idx < len(metadata):
                entry = metadata[idx]
                if args.filter_category and entry["category"] != args.filter_category:
                    continue
                if args.filter_doc_id and entry["doc_id"] != args.filter_doc_id:
                    continue
                results.append((entry, distances[rank]))
            if len(results) >= args.top_k:
                break

        print("\n[Results]")
        for rank, (entry, dist) in enumerate(results):
            print(
                f"{rank+1}. [{entry['category']}] {entry['title']} (doc_id={entry['doc_id']})")
            print(f"    Content: {entry['content']}")
            print(f"    Distance: {dist:.4f}")


if __name__ == "__main__":
    main()

# # **How to Use**

# # 1️⃣ Install dependencies
# ```bash
# pip install openai tiktoken faiss-cpu numpy
# ```

# ---

# # 2️⃣ Set your API key
# ```bash
# export OPENAI_API_KEY = "your-key"   # Mac/Linux
# setx OPENAI_API_KEY "your-key"     # Windows
# ```

# ---

# # 3️⃣ Add a single entry
# ```bash
# python a6_embeddings.py - -add - -title "AI News" - -category "technology" - -content "Artificial Intelligence is transforming the world."
# ```

# ---

# # 4️⃣ Add multiple entries from a JSON file
# **`entries.json`**
# ```json
# [
#     {
#         "title": "Eiffel Tower",
#         "category": "travel",
#         "content": "The Eiffel Tower is located in Paris, France."
#     },
#     {
#         "title": "Python Language",
#         "category": "technology",
#         "content": "Python is a popular programming language."
#     }
# ]
# ```
# Add them:
# ```bash
# python a6_embeddings.py - -add - -file entries.json
# ```

# ---

# # 5️⃣ Search without filter
# ```bash
# python a6_embeddings.py - -query "AI advancements"
# ```

# ---

# # 6️⃣ Search with category filter
# ```bash
# python a6_embeddings.py - -query "France" - -filter_category "travel"
# ```

# ---

# # 7️⃣ Search with doc_id filter
# ```bash
# python a6_embeddings.py - -query "Python" - -filter_doc_id "your-doc-id-here"
# ```

# ---

# # Benefits of `a6_embeddings.py`:
# ✅ Persistent FAISS index
# ✅ Metadata(title, category, doc_id, content)
# ✅ Filtering by category or ID
# ✅ Batch add via JSON file

# ---

# If you want, the ** next step(`a7_embeddings.py`) ** could allow:
# - **Updating ** existing entries by `doc_id`
# - **Deleting ** entries
# - **Rebuilding ** the FAISS index automatically

# Do you want me to make `a7_embeddings.py` with **update & delete support**? That would make it a full CRUD vector database tool.
