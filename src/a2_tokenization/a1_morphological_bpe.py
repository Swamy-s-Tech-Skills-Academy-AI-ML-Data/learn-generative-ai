"""
🧬 BPE Morphological Pattern Analyzer

Educational tool for discovering how BPE tokenization recognizes and preserves
linguistic morphological structures. This original implementation demonstrates
the intelligent pattern recognition capabilities of Byte-Pair Encoding.

🎯 Learning Objectives:
    - Observe morphological consistency across word families
    - Discover prefix and suffix pattern recognition
    - Analyze compression vs. semantic preservation trade-offs
    - Explore cross-linguistic morphological patterns

🔬 Discovery Features:
    - Morphological family analysis (same root, different forms)
    - Prefix/suffix pattern detection and visualization
    - Cross-domain vocabulary comparison
    - Efficiency metrics with morphological insights

📋 Prerequisites:
    pip install tiktoken

💡 Educational Focus: Original implementation demonstrating BPE's linguistic intelligence
"""

import tiktoken
from collections import defaultdict
from typing import Dict, List, Tuple


class MorphologicalAnalyzer:
    """
    Educational analyzer for exploring BPE morphological patterns.
    Designed to reveal how frequency-based tokenization discovers linguistic structure.
    """

    def __init__(self, encoding_name: str = "cl100k_base"):
        """Initialize with specified tokenization encoding."""
        self.encoding = tiktoken.get_encoding(encoding_name)
        self.encoding_name = encoding_name

    def analyze_word_family(self, word_family: List[str]) -> Dict:
        """
        Analyze how BPE tokenizes related words (same root, different forms).
        Educational insight: Reveals morphological consistency patterns.
        """
        analysis = {
            'family_pattern': {},
            'common_tokens': set(),
            'morphological_boundaries': {},
            'efficiency_metrics': {}
        }

        print(f"🧬 MORPHOLOGICAL FAMILY ANALYSIS")
        print(f"📊 Encoding: {self.encoding_name}")
        print("=" * 50)

        all_tokens = []

        for word in word_family:
            tokens = self.encoding.encode(word)
            decoded = [self.encoding.decode([t]) for t in tokens]

            analysis['family_pattern'][word] = {
                'tokens': decoded,
                'token_ids': tokens,
                'count': len(tokens),
                'efficiency': len(word) / len(tokens)
            }

            all_tokens.extend(decoded)

            print(f"📝 '{word}' → {decoded}")
            print(
                f"   🔢 {len(tokens)} tokens | ⚡ {len(word)/len(tokens):.2f} chars/token")

        # Find common morphological components
        token_frequency = defaultdict(int)
        for token in all_tokens:
            token_frequency[token] += 1

        # Identify shared morphological components
        shared_components = {token: freq for token, freq in token_frequency.items()
                             if freq > 1 and len(token.strip()) > 1}

        if shared_components:
            print(f"\n🧩 SHARED MORPHOLOGICAL COMPONENTS:")
            for component, frequency in sorted(shared_components.items(),
                                               key=lambda x: x[1], reverse=True):
                print(f"   '{component}' appears in {frequency} words")

        analysis['common_tokens'] = shared_components
        return analysis

    def analyze_prefix_patterns(self, prefix_examples: Dict[str, List[str]]) -> Dict:
        """
        Analyze how BPE handles different prefixes across various root words.
        Educational focus: Prefix consistency and boundary detection.
        """
        print(f"\n🔍 PREFIX PATTERN ANALYSIS")
        print("=" * 40)

        prefix_analysis = {}

        for prefix, words in prefix_examples.items():
            print(f"\n📌 Prefix: '{prefix}'")

            prefix_tokens = []
            consistency_score = 0

            for word in words:
                tokens = self.encoding.encode(word)
                decoded = [self.encoding.decode([t]) for t in tokens]

                print(f"   '{word}' → {decoded}")

                # Check if prefix is preserved as a token
                first_token = decoded[0] if decoded else ""
                if prefix in first_token or first_token.strip() == prefix:
                    consistency_score += 1

                prefix_tokens.append(decoded)

            consistency_percentage = (consistency_score / len(words)) * 100
            prefix_analysis[prefix] = {
                'words': words,
                'tokenizations': prefix_tokens,
                'consistency': consistency_percentage
            }

            print(f"   🎯 Prefix consistency: {consistency_percentage:.1f}%")

            if consistency_percentage > 70:
                print(f"   ✅ Strong morphological recognition!")
            elif consistency_percentage > 40:
                print(f"   ⚠️ Moderate morphological recognition")
            else:
                print(f"   ❌ Weak morphological recognition")

        return prefix_analysis

    def analyze_suffix_patterns(self, suffix_examples: Dict[str, List[str]]) -> Dict:
        """
        Analyze how BPE handles different suffixes across various root words.
        Educational focus: Suffix consistency and productive morphology.
        """
        print(f"\n🔍 SUFFIX PATTERN ANALYSIS")
        print("=" * 40)

        suffix_analysis = {}

        for suffix, words in suffix_examples.items():
            print(f"\n📌 Suffix: '{suffix}'")

            suffix_tokens = []
            consistency_score = 0

            for word in words:
                tokens = self.encoding.encode(word)
                decoded = [self.encoding.decode([t]) for t in tokens]

                print(f"   '{word}' → {decoded}")

                # Check if suffix is preserved as a token
                last_token = decoded[-1] if decoded else ""
                if suffix in last_token or last_token.strip() == suffix:
                    consistency_score += 1

                suffix_tokens.append(decoded)

            consistency_percentage = (consistency_score / len(words)) * 100
            suffix_analysis[suffix] = {
                'words': words,
                'tokenizations': suffix_tokens,
                'consistency': consistency_percentage
            }

            print(f"   🎯 Suffix consistency: {consistency_percentage:.1f}%")

            # Educational insights based on consistency
            if consistency_percentage > 70:
                print(f"   ✅ Productive morphological pattern recognized!")
            elif consistency_percentage > 40:
                print(f"   ⚠️ Partially recognized morphological pattern")
            else:
                print(f"   ❌ Morphological pattern not consistently recognized")

        return suffix_analysis

    def compare_morphological_efficiency(self, word_groups: Dict[str, List[str]]) -> Dict:
        """
        Compare tokenization efficiency across different morphological complexity levels.
        Educational insight: How morphological structure affects compression.
        """
        print(f"\n📊 MORPHOLOGICAL EFFICIENCY COMPARISON")
        print("=" * 50)

        efficiency_results = {}

        for group_name, words in word_groups.items():
            efficiencies = []
            token_counts = []

            print(f"\n🏷️ {group_name.upper()}")

            for word in words:
                tokens = self.encoding.encode(word)
                efficiency = len(word) / len(tokens)
                efficiencies.append(efficiency)
                token_counts.append(len(tokens))

                decoded = [self.encoding.decode([t]) for t in tokens]
                print(f"   '{word}' → {decoded} | {efficiency:.2f} chars/token")

            avg_efficiency = sum(efficiencies) / len(efficiencies)
            avg_tokens = sum(token_counts) / len(token_counts)

            efficiency_results[group_name] = {
                'average_efficiency': avg_efficiency,
                'average_tokens': avg_tokens,
                'words': words,
                'individual_efficiencies': efficiencies
            }

            print(f"   📈 Average efficiency: {avg_efficiency:.2f} chars/token")
            print(f"   🔢 Average tokens: {avg_tokens:.1f}")

        # Identify most efficient morphological patterns
        print(f"\n🏆 EFFICIENCY RANKINGS:")
        sorted_groups = sorted(efficiency_results.items(),
                               key=lambda x: x[1]['average_efficiency'], reverse=True)

        for rank, (group, stats) in enumerate(sorted_groups, 1):
            print(
                f"   {rank}. {group}: {stats['average_efficiency']:.2f} chars/token")

        return efficiency_results


def demonstrate_morphological_intelligence():
    """
    Educational demonstration of BPE's morphological pattern recognition.
    Original examples designed to reveal linguistic intelligence in tokenization.
    """

    analyzer = MorphologicalAnalyzer()

    print("🧬 BPE MORPHOLOGICAL INTELLIGENCE LABORATORY")
    print("Educational exploration of linguistic pattern recognition in tokenization")
    print("=" * 70)

    # Demonstrate word family analysis
    print("\n🎯 EXPERIMENT 1: WORD FAMILY MORPHOLOGY")
    gerund_family = ["swimming", "running",
                     "debugging", "preprocessing", "tokenizing"]
    analyzer.analyze_word_family(gerund_family)

    # Demonstrate prefix pattern recognition
    print(f"\n🎯 EXPERIMENT 2: PREFIX PATTERN RECOGNITION")
    prefix_examples = {
        "un-": ["unhappy", "unknown", "unusual", "unprocessed"],
        "pre-": ["preprocessing", "prebuilt", "preview", "preload"],
        "multi-": ["multimodal", "multilingual", "multiply", "multitask"],
        "hyper-": ["hyperparameter", "hyperlink", "hyperbole", "hyperactive"]
    }
    analyzer.analyze_prefix_patterns(prefix_examples)

    # Demonstrate suffix pattern recognition
    print(f"\n🎯 EXPERIMENT 3: SUFFIX PATTERN RECOGNITION")
    suffix_examples = {
        "-ing": ["swimming", "running", "debugging", "processing"],
        "-tion": ["tokenization", "classification", "optimization", "generation"],
        "-ly": ["efficiently", "automatically", "systematically", "linguistically"],
        "-ness": ["happiness", "darkness", "usefulness", "effectiveness"]
    }
    analyzer.analyze_suffix_patterns(suffix_examples)

    # Demonstrate efficiency comparison
    print(f"\n🎯 EXPERIMENT 4: MORPHOLOGICAL COMPLEXITY vs EFFICIENCY")
    complexity_groups = {
        "Simple words": ["cat", "dog", "run", "eat", "blue"],
        "Compound words": ["sunshine", "rainbow", "keyboard", "software"],
        "Prefixed words": ["unhappy", "preview", "multimodal", "hyperlink"],
        "Suffixed words": ["running", "happiness", "systematic", "tokenization"],
        "Complex technical": ["preprocessing", "tokenization", "hyperparameter", "optimization"]
    }
    analyzer.compare_morphological_efficiency(complexity_groups)


if __name__ == "__main__":
    print("🔬 Choose your morphological discovery mode:\n")
    print("1. 🧬 Full Demonstration - Complete morphological intelligence exploration")
    print("2. 🎯 Custom Analysis - Analyze your own word patterns")
    print("3. 🔍 Single Family - Focus on one morphological family")

    choice = input("\nSelect option (1, 2, or 3): ").strip()

    analyzer = MorphologicalAnalyzer()

    if choice == "1":
        demonstrate_morphological_intelligence()

    elif choice == "2":
        print("\n🎯 CUSTOM MORPHOLOGICAL ANALYSIS")
        print("Enter words separated by commas to analyze their morphological patterns:")

        user_input = input("Words to analyze: ").strip()
        if user_input:
            words = [word.strip() for word in user_input.split(",")]
            analyzer.analyze_word_family(words)

    elif choice == "3":
        print("\n🔍 SINGLE FAMILY ANALYSIS")
        print("Enter related words (same root, different forms) separated by commas:")

        family_input = input("Word family: ").strip()
        if family_input:
            family = [word.strip() for word in family_input.split(",")]
            result = analyzer.analyze_word_family(family)

            # Provide educational summary
            print(f"\n💡 EDUCATIONAL INSIGHTS:")
            if result['common_tokens']:
                print("   ✅ BPE recognized morphological relationships!")
                print("   📚 This demonstrates BPE's linguistic intelligence")
            else:
                print("   🤔 No shared morphological components detected")
                print("   📚 This might indicate diverse word structures")

    else:
        print("🤔 Invalid choice. Running full demonstration...")
        demonstrate_morphological_intelligence()

    print(f"\n🎓 LEARNING COMPLETE!")
    print("You've explored how BPE tokenization intelligently recognizes")
    print("morphological patterns, balancing compression with semantic preservation!")
