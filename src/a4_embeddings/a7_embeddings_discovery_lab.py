# filename: a7_embeddings_discovery_lab.py
#!/usr/bin/env python3
"""
🎨 Embeddings Discovery Laboratory

Educational tool for exploring semantic vector representations and their mathematical properties.
This original implementation demonstrates how embeddings transform discrete tokens into
continuous semantic spaces where meaning becomes measurable.

🎯 Learning Objectives:
    - Generate and analyze embedding vectors
    - Explore semantic similarity relationships
    - Understand vector arithmetic properties
    - Visualize semantic clustering patterns

🔬 Discovery Features:
    - Interactive similarity analysis
    - Vector arithmetic exploration
    - Semantic clustering visualization
    - Context-dependent embedding comparison

📋 Prerequisites:
    pip install openai tiktoken numpy matplotlib scikit-learn

💡 Educational Focus: Original implementation showcasing embedding intelligence
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import tiktoken
from openai import OpenAI

# Load API key securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("⚠️ Warning: OPENAI_API_KEY not found in environment variables")
    print("Some features will be limited to demo mode")


class EmbeddingDiscoveryLab:
    """
    Educational laboratory for discovering embedding properties and relationships.
    Designed to reveal how semantic meaning emerges from vector mathematics.
    """

    def __init__(self, model: str = "text-embedding-3-small"):
        """Initialize the discovery lab with specified embedding model."""
        self.model = model
        self.client = OpenAI(
            api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
        self.embedding_cache = {}
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def get_embedding(self, text: str) -> Optional[np.ndarray]:
        """
        Generate embedding vector for text with educational caching.
        Returns None if API is not available.
        """
        if not self.client:
            print(f"🔧 Demo mode: Simulating embedding for '{text[:30]}...'")
            # Generate deterministic pseudo-embedding for demo
            np.random.seed(hash(text) % (2**32))
            return np.random.normal(0, 1, 1536)

        if text in self.embedding_cache:
            return self.embedding_cache[text]

        try:
            response = self.client.embeddings.create(
                model=self.model,
                input=text
            )
            embedding = np.array(response.data[0].embedding)
            self.embedding_cache[text] = embedding
            return embedding
        except Exception as e:
            print(f"❌ Error generating embedding: {e}")
            return None

    def analyze_embedding_properties(self, text: str) -> Dict:
        """
        Educational analysis of embedding vector properties.
        Reveals dimensional characteristics and statistical patterns.
        """
        embedding = self.get_embedding(text)
        if embedding is None:
            return {}

        # Count tokens for educational context
        tokens = self.tokenizer.encode(text)
        token_strings = [self.tokenizer.decode([t]) for t in tokens]

        analysis = {
            'text': text,
            'token_count': len(tokens),
            'tokens': token_strings,
            'embedding_dimensions': len(embedding),
            'vector_magnitude': float(np.linalg.norm(embedding)),
            'mean_value': float(np.mean(embedding)),
            'std_deviation': float(np.std(embedding)),
            'min_value': float(np.min(embedding)),
            'max_value': float(np.max(embedding)),
            'zero_dimensions': int(np.sum(embedding == 0)),
            'positive_dimensions': int(np.sum(embedding > 0)),
            'negative_dimensions': int(np.sum(embedding < 0))
        }

        return analysis

    def explore_semantic_similarity(self, text_pairs: List[Tuple[str, str]]) -> Dict:
        """
        Educational exploration of semantic similarity between text pairs.
        Demonstrates how vector mathematics captures meaning relationships.
        """
        print(f"🔍 SEMANTIC SIMILARITY EXPLORATION")
        print("=" * 50)

        results = {}

        for i, (text1, text2) in enumerate(text_pairs, 1):
            embedding1 = self.get_embedding(text1)
            embedding2 = self.get_embedding(text2)

            if embedding1 is None or embedding2 is None:
                continue

            # Calculate similarity metrics
            cosine_sim = float(cosine_similarity(
                [embedding1], [embedding2])[0][0])
            euclidean_dist = float(np.linalg.norm(embedding1 - embedding2))
            dot_product = float(np.dot(embedding1, embedding2))

            results[f"pair_{i}"] = {
                'text1': text1,
                'text2': text2,
                'cosine_similarity': cosine_sim,
                'euclidean_distance': euclidean_dist,
                'dot_product': dot_product
            }

            # Educational output
            print(f"\n📝 Pair {i}: '{text1}' vs '{text2}'")
            print(f"   🎯 Cosine Similarity: {cosine_sim:.3f}")
            print(f"   📏 Euclidean Distance: {euclidean_dist:.3f}")
            print(f"   ⚡ Dot Product: {dot_product:.3f}")

            # Educational insights
            if cosine_sim > 0.8:
                print(f"   💡 High similarity - closely related concepts!")
            elif cosine_sim > 0.5:
                print(f"   🤔 Moderate similarity - some conceptual overlap")
            elif cosine_sim < 0.2:
                print(f"   🔄 Low similarity - different semantic domains")
            else:
                print(f"   📊 Medium similarity - related but distinct")

        return results

    def discover_vector_arithmetic(self, analogies: List[Tuple[str, str, str]]) -> Dict:
        """
        Educational discovery of vector arithmetic properties in semantic space.
        Demonstrates how embeddings capture relational patterns.
        """
        print(f"\n🧮 VECTOR ARITHMETIC DISCOVERY")
        print("=" * 40)

        results = {}

        for i, (word_a, word_b, word_c) in enumerate(analogies, 1):
            # Get embeddings for analogy components
            emb_a = self.get_embedding(word_a)
            emb_b = self.get_embedding(word_b)
            emb_c = self.get_embedding(word_c)

            if any(emb is None for emb in [emb_a, emb_b, emb_c]):
                continue

            # Calculate analogy: A is to B as C is to ?
            # Vector arithmetic: B - A + C = ?
            target_vector = emb_b - emb_a + emb_c

            # Find closest match from a set of candidate words
            candidates = self._get_analogy_candidates(word_a, word_b, word_c)
            best_match, best_similarity = self._find_closest_word(
                target_vector, candidates)

            results[f"analogy_{i}"] = {
                'word_a': word_a,
                'word_b': word_b,
                'word_c': word_c,
                'predicted_word': best_match,
                'similarity_score': best_similarity,
                'relationship': f"{word_a} → {word_b} :: {word_c} → {best_match}"
            }

            # Educational output
            print(f"\n🔤 Analogy {i}: {word_a} → {word_b} :: {word_c} → ?")
            print(f"   🎯 Predicted: {best_match}")
            print(f"   📊 Similarity: {best_similarity:.3f}")
            print(
                f"   💡 Relationship: {word_a} → {word_b} :: {word_c} → {best_match}")

        return results

    def visualize_semantic_clusters(self, word_groups: Dict[str, List[str]]) -> Dict:
        """
        Educational visualization of semantic clustering in embedding space.
        Demonstrates how related concepts cluster together geometrically.
        """
        print(f"\n🎨 SEMANTIC CLUSTERING VISUALIZATION")
        print("=" * 45)

        # Collect all words and their embeddings
        all_words = []
        all_embeddings = []
        group_labels = []

        for group_name, words in word_groups.items():
            for word in words:
                embedding = self.get_embedding(word)
                if embedding is not None:
                    all_words.append(word)
                    all_embeddings.append(embedding)
                    group_labels.append(group_name)

        if len(all_embeddings) < 2:
            print("❌ Insufficient embeddings for clustering analysis")
            return {}

        # Convert to numpy array
        embeddings_matrix = np.array(all_embeddings)

        # Dimensionality reduction for visualization
        pca = PCA(n_components=2)
        embeddings_2d = pca.fit_transform(embeddings_matrix)

        # K-means clustering
        n_clusters = len(word_groups)
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(embeddings_matrix)

        # Visualization
        plt.figure(figsize=(12, 8))
        colors = plt.cm.Set3(np.linspace(0, 1, len(word_groups)))
        group_to_color = {group: colors[i]
                          for i, group in enumerate(word_groups.keys())}

        for i, word in enumerate(all_words):
            x, y = embeddings_2d[i]
            color = group_to_color[group_labels[i]]
            plt.scatter(x, y, c=[color], s=100, alpha=0.7)
            plt.annotate(word, (x, y), xytext=(5, 5), textcoords='offset points',
                         fontsize=9, ha='left')

        # Add cluster centers
        centers_2d = pca.transform(kmeans.cluster_centers_)
        plt.scatter(centers_2d[:, 0], centers_2d[:, 1],
                    marker='x', s=300, linewidths=3, color='black', label='Cluster Centers')

        plt.title('Semantic Clustering in 2D Embedding Space',
                  fontsize=14, fontweight='bold')
        plt.xlabel('First Principal Component', fontsize=12)
        plt.ylabel('Second Principal Component', fontsize=12)
        plt.legend(title='Semantic Groups')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        # Save visualization
        plt.savefig('semantic_clusters_visualization.png',
                    dpi=300, bbox_inches='tight')
        plt.show()

        # Educational analysis
        results = {
            'total_words': len(all_words),
            'total_groups': len(word_groups),
            'pca_explained_variance': pca.explained_variance_ratio_.tolist(),
            'cluster_assignments': {word: int(cluster_labels[i]) for i, word in enumerate(all_words)},
            'visualization_saved': 'semantic_clusters_visualization.png'
        }

        print(f"📊 Clustering Results:")
        print(f"   Words analyzed: {len(all_words)}")
        print(f"   Semantic groups: {len(word_groups)}")
        print(
            f"   PCA variance explained: {sum(pca.explained_variance_ratio_):.1%}")
        print(f"   📁 Visualization saved: semantic_clusters_visualization.png")

        return results

    def _get_analogy_candidates(self, word_a: str, word_b: str, word_c: str) -> List[str]:
        """Generate candidate words for analogy completion."""
        # Educational example candidates - in practice, this would be a larger vocabulary
        candidates = [
            "queen", "woman", "king", "man", "royal", "crown",
            "water", "swimming", "snow", "skiing", "ice", "cold",
            "Paris", "Rome", "France", "Italy", "capital", "city",
            "teacher", "student", "doctor", "patient", "nurse", "hospital",
            "book", "reading", "movie", "watching", "music", "listening"
        ]
        # Remove input words from candidates
        candidates = [c for c in candidates if c not in [
            word_a, word_b, word_c]]
        return candidates

    def _find_closest_word(self, target_vector: np.ndarray, candidates: List[str]) -> Tuple[str, float]:
        """Find the candidate word closest to the target vector."""
        best_word = None
        best_similarity = -1

        for candidate in candidates:
            candidate_embedding = self.get_embedding(candidate)
            if candidate_embedding is not None:
                similarity = float(cosine_similarity(
                    [target_vector], [candidate_embedding])[0][0])
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_word = candidate

        return best_word or "unknown", best_similarity


def demonstrate_embedding_intelligence():
    """
    Comprehensive demonstration of embedding intelligence and discovery capabilities.
    Educational showcase of semantic vector analysis and mathematical properties.
    """
    print("🎨 EMBEDDINGS DISCOVERY LABORATORY")
    print("Educational exploration of semantic vector intelligence")
    print("=" * 60)

    lab = EmbeddingDiscoveryLab()

    # Experiment 1: Basic embedding properties
    print("\n🎯 EXPERIMENT 1: EMBEDDING PROPERTY ANALYSIS")
    test_texts = [
        "The AI model processes natural language efficiently",
        "Machine learning algorithms learn from data patterns",
        "Deep neural networks require substantial computational resources"
    ]

    for text in test_texts:
        analysis = lab.analyze_embedding_properties(text)
        if analysis:
            print(f"\n📝 Text: '{text}'")
            print(f"   🔢 Tokens: {analysis['token_count']}")
            print(f"   📊 Dimensions: {analysis['embedding_dimensions']}")
            print(f"   📏 Magnitude: {analysis['vector_magnitude']:.3f}")
            print(f"   ⚖️ Mean: {analysis['mean_value']:.3f}")
            print(f"   📈 Std Dev: {analysis['std_deviation']:.3f}")
            print(f"   ➕ Positive dims: {analysis['positive_dimensions']}")
            print(f"   ➖ Negative dims: {analysis['negative_dimensions']}")

    # Experiment 2: Semantic similarity exploration
    print(f"\n🎯 EXPERIMENT 2: SEMANTIC SIMILARITY DISCOVERY")
    similarity_pairs = [
        ("dog", "puppy"),
        ("happy", "joyful"),
        ("computer", "laptop"),
        ("car", "airplane"),
        ("programming", "coding"),
        ("hot", "cold")
    ]
    lab.explore_semantic_similarity(similarity_pairs)

    # Experiment 3: Vector arithmetic discovery
    print(f"\n🎯 EXPERIMENT 3: VECTOR ARITHMETIC EXPLORATION")
    analogies = [
        ("king", "queen", "man"),      # man -> woman
        ("Paris", "Rome", "France"),   # France -> Italy
        ("swimming", "skiing", "water")  # water -> snow
    ]
    lab.discover_vector_arithmetic(analogies)

    # Experiment 4: Semantic clustering visualization
    print(f"\n🎯 EXPERIMENT 4: SEMANTIC CLUSTERING ANALYSIS")
    word_groups = {
        "Animals": ["cat", "dog", "elephant", "tiger"],
        "Vehicles": ["car", "truck", "airplane", "boat"],
        "Emotions": ["happy", "sad", "angry", "excited"],
        "Colors": ["red", "blue", "green", "yellow"],
        "Technology": ["computer", "smartphone", "internet", "software"]
    }
    lab.visualize_semantic_clusters(word_groups)


if __name__ == "__main__":
    print("🔬 Choose your embedding discovery mode:\n")
    print("1. 🎨 Full Demonstration - Complete embedding intelligence exploration")
    print("2. 🎯 Custom Analysis - Analyze your own text and concepts")
    print("3. 🔍 Similarity Explorer - Compare semantic relationships")
    print("4. 🧮 Vector Arithmetic - Explore mathematical properties")
    print("5. 🎪 Clustering Visualizer - Analyze semantic organization")

    choice = input("\nSelect option (1, 2, 3, 4, or 5): ").strip()

    lab = EmbeddingDiscoveryLab()

    if choice == "1":
        demonstrate_embedding_intelligence()

    elif choice == "2":
        print("\n🎯 CUSTOM EMBEDDING ANALYSIS")
        text = input("Enter text to analyze: ").strip()
        if text:
            analysis = lab.analyze_embedding_properties(text)
            if analysis:
                print(f"\n📊 Analysis Results:")
                for key, value in analysis.items():
                    if key != 'tokens':  # Skip token list for cleaner output
                        print(f"   {key}: {value}")

    elif choice == "3":
        print("\n🔍 SEMANTIC SIMILARITY EXPLORER")
        text1 = input("Enter first text: ").strip()
        text2 = input("Enter second text: ").strip()
        if text1 and text2:
            lab.explore_semantic_similarity([(text1, text2)])

    elif choice == "4":
        print("\n🧮 VECTOR ARITHMETIC EXPLORER")
        print("Enter three words for analogy: A is to B as C is to ?")
        word_a = input("Word A: ").strip()
        word_b = input("Word B: ").strip()
        word_c = input("Word C: ").strip()
        if word_a and word_b and word_c:
            lab.discover_vector_arithmetic([(word_a, word_b, word_c)])

    elif choice == "5":
        print("\n🎪 SEMANTIC CLUSTERING VISUALIZER")
        print("Using default word groups for demonstration...")
        word_groups = {
            "Programming": ["python", "javascript", "function", "variable"],
            "Science": ["physics", "chemistry", "biology", "mathematics"],
            "Sports": ["football", "basketball", "tennis", "swimming"]
        }
        lab.visualize_semantic_clusters(word_groups)

    else:
        print("🤔 Invalid choice. Running full demonstration...")
        demonstrate_embedding_intelligence()

    print(f"\n🎓 DISCOVERY COMPLETE!")
    print("You've explored the mathematical foundations of semantic meaning!")
    print("These vector representations enable AI systems to understand,")
    print("reason about, and manipulate semantic relationships!")
