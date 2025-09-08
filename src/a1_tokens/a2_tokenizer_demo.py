#!/usr/bin/env python3
"""  
🎯 Tokenizer Demo  
User inputs text and sees:  
  - Tokens  
  - Token IDs  
  - Token count  
  - Cost estimate for a given model  
"""

import tiktoken

# === Configuration ===
MODEL = "gpt-3.5-turbo"  # Change as needed
# USD per 1K tokens (example for gpt-3.5-turbo input)
COST_PER_1K_TOKENS = 0.0015


def main():
    print("🔤 TOKENIZER DEMO")
    print(f"Using model: {MODEL}")
    print("=" * 40)

    encoding = tiktoken.encoding_for_model(MODEL)

    while True:
        text = input("\nEnter text (or 'quit' to exit): ").strip()
        if text.lower() == "quit":
            break

        tokens = encoding.encode(text)
        token_strings = [encoding.decode([t]) for t in tokens]
        token_count = len(tokens)
        cost_estimate = (token_count / 1000) * COST_PER_1K_TOKENS

        print("\n📊 Tokenization Results")
        print("-" * 40)
        print(f"Token count: {token_count}")
        print(f"Token IDs: {tokens}")
        print(f"Tokens: {token_strings}")
        print(
            f"💰 Estimated cost: ${cost_estimate:.6f} (at ${COST_PER_1K_TOKENS}/1K tokens)")


if __name__ == "__main__":
    main()
