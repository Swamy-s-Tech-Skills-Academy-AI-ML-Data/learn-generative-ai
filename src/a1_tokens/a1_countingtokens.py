# filename: a1_countingtokens.py
"""
🔤 Token Discovery Laboratory: Understanding AI Text Processing

This educational exploration reveals how language models perceive and process text
through tokenization - the fundamental bridge between human language and machine understanding.

🎯 Learning Objectives:
    - Discover how text becomes numerical representations
    - Explore boundary detection in subword tokenization  
    - Investigate encoding efficiency across different text types
    - Understand the relationship between tokens and model context windows

🧪 Discovery Features:
    - Interactive token counting with detailed breakdown
    - Visual mapping between text fragments and token IDs
    - Educational insights about tokenization patterns
    - Comparative analysis across text complexity levels

📋 Prerequisites:
    pip install tiktoken

💡 Educational Focus: Original implementation designed for systematic AI concept mastery
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


def discover_tokenization_patterns():
    """
    Educational exploration of tokenization behavior across different text types.
    Reveals how encoding efficiency varies with language complexity.
    """

    # Discovery samples designed to reveal tokenization insights
    exploration_texts = {
        "🔤 Basic English": "Hello world! How are you today?",
        "🎯 Technical Terms": "Python tokenization algorithms process linguistic patterns efficiently",
        "🌍 Mixed Languages": "Hello 你好 Bonjour Hola こんにちは",
        "🔢 Numbers & Symbols": "Cost: $123.45 (15% tax) = Total $141.97",
        "📝 Repeated Patterns": "The the the quick quick brown brown fox fox jumps jumps",
    }

    print("🔬 TOKENIZATION DISCOVERY LABORATORY")
    print("=" * 50)

    encoding = tiktoken.get_encoding("cl100k_base")

    for category, text in exploration_texts.items():
        print(f"\n{category}")
        print(f"📋 Text: '{text}'")

        tokens = encoding.encode(text)
        decoded = [encoding.decode([t]) for t in tokens]

        print(f"🔢 Token count: {len(tokens)}")
        print(f"📊 Efficiency: {len(text)/len(tokens):.2f} chars/token")
        print("🧩 Token breakdown:")

        for i, (token_id, token_text) in enumerate(zip(tokens, decoded)):
            print(f"   {i+1:2d}. '{token_text}' → {token_id}")


def interactive_tokenization_explorer():
    """
    Guided exploration allowing users to discover tokenization patterns
    through hands-on experimentation with their own text samples.
    """

    print("\n🎓 INTERACTIVE TOKENIZATION EXPLORER")
    print("=" * 45)
    print("💡 Experiment with different text types to discover patterns!")
    print("🔍 Try: technical terms, other languages, repeated words, symbols\n")

    encoding = tiktoken.get_encoding("cl100k_base")

    while True:
        user_text = input(
            "🔤 Enter text to analyze (or 'quit' to exit): ").strip()

        if user_text.lower() in ['quit', 'exit', 'q']:
            break

        if not user_text:
            continue

        # Perform tokenization analysis
        token_ids = encoding.encode(user_text)
        decoded_tokens = [encoding.decode([token]) for token in token_ids]

        print(f"\n📊 ANALYSIS RESULTS")
        print(f"📝 Original text: '{user_text}'")
        print(f"📏 Character count: {len(user_text)}")
        print(f"🔢 Token count: {len(token_ids)}")
        print(
            f"⚡ Efficiency ratio: {len(user_text)/len(token_ids):.2f} chars/token")

        # Detailed token mapping
        print(f"\n🗺️ TOKEN MAPPING")
        print(f"{'#':<3} | {'Token Text':<15} | {'Token ID':<8} | {'Length'}")
        print("-" * 50)

        for i, (token_text, token_id) in enumerate(zip(decoded_tokens, token_ids), 1):
            print(
                f"{i:<3} | {repr(token_text):<15} | {token_id:<8} | {len(token_text)}")

        # Educational insights
        print(f"\n💡 LEARNING INSIGHTS:")
        if len(token_ids) == len(user_text.split()):
            print("   🎯 Each word became one token - excellent efficiency!")
        elif len(token_ids) > len(user_text.split()):
            print(
                "   🔍 Some words split into multiple tokens - subword tokenization in action!")
        else:
            print(
                "   ⚡ Multiple words combined into tokens - compound tokenization detected!")

        print("   📚 Notice how punctuation, spaces, and special characters affect tokenization")
        print()


if __name__ == "__main__":
    print("🚀 Welcome to the Token Discovery Laboratory!")
    print("📖 Choose your learning adventure:\n")
    print("1. 🔬 Discover Patterns - See tokenization across different text types")
    print("2. 🎓 Interactive Explorer - Experiment with your own text")
    print("3. 🧪 Single Analysis - Analyze one specific text sample")

    choice = input("\nSelect option (1, 2, or 3): ").strip()

    if choice == "1":
        discover_tokenization_patterns()
    elif choice == "2":
        discover_tokenization_patterns()  # Show patterns first
        interactive_tokenization_explorer()
    elif choice == "3":
        # Original single analysis functionality
        prompt = input("\n🔤 Enter the text you want to tokenize: ").strip()
        encoding_scheme = "cl100k_base"

        token_count, token_ids, decoded_tokens = count_tokens(
            prompt, encoding_scheme)

        print("\n📊 TOKENIZATION ANALYSIS")
        print("=" * 30)
        print(f"📝 Text: {prompt}")
        print(f"🔧 Encoding: {encoding_scheme}")
        print(f"🔢 Token count: {token_count}")
        print(f"🆔 Token IDs: {token_ids}")
        print(f"🧩 Decoded tokens: {decoded_tokens}")

        print(f"\n🗺️ DETAILED TOKEN MAPPING")
        print(f"{'Token':<20} | {'ID':<8} | {'Position'}")
        print("-" * 40)
        for i, (token, token_id) in enumerate(zip(decoded_tokens, token_ids)):
            print(f"{repr(token):<20} | {token_id:<8} | {i+1}")
    else:
        print("🤔 Invalid choice. Running pattern discovery as default...")
        discover_tokenization_patterns()


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
