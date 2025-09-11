# filename: a2_compare_tokenizers.py
#!/usr/bin/env python3
"""  
🔍 Compare Tokenizers Across Models  
Given a text input, show how different models tokenize it:  
  - Token count  
  - Token IDs  
  - Token strings  
"""

import tiktoken

MODELS = [
    "gpt-3.5-turbo",
    "gpt-4",
    "text-embedding-3-small",
    "text-embedding-3-large"
]


def compare_tokenizers(text: str):
    print("\n📊 TOKENIZER COMPARISON")
    print("=" * 50)

    for model in MODELS:
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print(f"⚠️ Model '{model}' not found, skipping.")
            continue

        tokens = encoding.encode(text)
        token_strings = [encoding.decode([t]) for t in tokens]

        print(f"\nModel: {model}")
        print(f"Token count: {len(tokens)}")
        print(f"Token IDs: {tokens}")
        print(f"Tokens: {token_strings}")


def main():
    print("🔍 TOKENIZER COMPARISON TOOL")
    print("=" * 40)

    while True:
        text = input("\nEnter text to compare (or 'quit' to exit): ").strip()
        if text.lower() == "quit":
            break
        compare_tokenizers(text)


if __name__ == "__main__":
    main()
