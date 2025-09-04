#!/usr/bin/env python3
"""
Chapter 01: Generative AI Foundations - Basic Concepts
=====================================================

A simple script version of the key concepts from the notebook.
Run this to get started with Generative AI fundamentals.

Usage: python basic_concepts.py
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def welcome_message():
    """Display welcome message and environment info"""
    print("=" * 60)
    print("🚀 LEARN GENERATIVE AI - CHAPTER 01")
    print("=" * 60)
    print()
    print("📚 Welcome to your Generative AI learning journey!")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python Environment: Ready")
    print()


def explain_generative_ai():
    """Explain the key differences between traditional and generative AI"""
    print("🤖 WHAT IS GENERATIVE AI?")
    print("-" * 30)
    print()
    print("Traditional AI (Discriminative):")
    print("  ❌ Analyzes and classifies existing data")
    print("  ❌ Answers: 'What is this?' or 'Which category?'")
    print("  ❌ Examples: Image classification, spam detection")
    print()
    print("Generative AI (Generative):")
    print("  ✅ Creates new data that resembles training data")
    print("  ✅ Answers: 'What would new data look like?'")
    print("  ✅ Examples: Text generation, image creation, code synthesis")
    print()


def show_evolution():
    """Display the evolution from RNNs to Transformers"""
    print("🚀 THE AI EVOLUTION")
    print("-" * 20)
    print()
    evolution_steps = [
        "1990s-2000s: Statistical Models (N-grams)",
        "2010s: Recurrent Neural Networks (RNNs/LSTMs)",
        "2017: Transformers ('Attention Is All You Need')",
        "2018-2019: BERT, GPT-1, GPT-2",
        "2020: GPT-3 (175B parameters)",
        "2022: ChatGPT & GPT-4",
        "2023-2024: Claude, Gemini, and the LLM explosion",
        "2024+: AI Agents & Agentic AI"
    ]

    for i, step in enumerate(evolution_steps):
        if i < len(evolution_steps) - 1:
            print(f"   {step}")
            print("        ↓")
        else:
            print(f"   {step}")
    print()


def explain_attention():
    """Simple explanation of attention mechanism"""
    print("🔍 ATTENTION MECHANISM (SIMPLIFIED)")
    print("-" * 40)
    print()
    print("🧠 Human Analogy:")
    print("   When you read a sentence, you don't give equal attention")
    print("   to every word - you focus on the important ones.")
    print()
    print("🤖 In AI:")
    print("   Attention allows the model to focus on relevant parts")
    print("   of the input when generating each output token.")
    print()
    print("📝 Example: Translation")
    print("   Input:  'The cat sat on the mat'")
    print("   Output: 'Le chat s'est assis sur le tapis'")
    print("   When generating 'chat', focus on 'cat' in input!")
    print()


def show_learning_path():
    """Display the 4-week learning path"""
    print("🗺️ YOUR 4-WEEK LEARNING PATH")
    print("-" * 35)
    print()

    weeks = [
        ("Week 1: Transformer Fundamentals", [
            "Attention mechanisms deep dive",
            "Multi-head attention implementation",
            "Positional encoding & layer normalization",
            "Complete transformer architecture review"
        ]),
        ("Week 2: Transformer Variants", [
            "Encoder-only models (BERT)",
            "Decoder-only models (GPT)",
            "Encoder-decoder models (T5/BART)",
            "Code complete mini-transformer"
        ]),
        ("Week 3: LLM Training & Fine-tuning", [
            "Pretraining strategies",
            "Fine-tuning methods (LoRA, QLoRA)",
            "Instruction tuning & RLHF",
            "Hands-on fine-tuning project"
        ]),
        ("Week 4: LLM Applications", [
            "Advanced prompting techniques",
            "RAG systems & vector databases",
            "LLM APIs & integration",
            "Production deployment"
        ])
    ]

    for week_title, topics in weeks:
        print(f"📅 {week_title}")
        for topic in topics:
            print(f"     • {topic}")
        print()


def simple_tokenization_demo():
    """Demonstrate basic tokenization"""
    print("🔤 TOKENIZATION DEMO")
    print("-" * 20)
    print()

    text = "Hello, world! How are you today?"
    # Simple tokenization (split by spaces and punctuation)
    import re
    tokens = re.findall(r'\w+|[^\w\s]', text.lower())

    print(f"📝 Original text: '{text}'")
    print(f"🔍 Tokens: {tokens}")
    print(f"📊 Number of tokens: {len(tokens)}")
    print()
    print("💡 Key insight: Models see tokens, not words!")
    print()


def next_steps():
    """Show what to do next"""
    print("🚀 NEXT STEPS")
    print("-" * 15)
    print()
    print("1. 📓 Open the Jupyter notebook for interactive learning:")
    print("   cd ../../notebooks/day1 && jupyter notebook 01_generative_ai_foundations.ipynb")
    print()
    print("2. 📁 Move to Chapter 02 for environment setup:")
    print("   cd ../chapter-02/")
    print()
    print("3. 📚 Read the theory docs in docs/concepts/")
    print()
    print("4. 🎯 Start your 4-week transformer journey!")
    print()
    print("💪 Remember: Code first, theory follows. Let's build!")
    print()


def main():
    """Main function to run all demonstrations"""
    welcome_message()
    explain_generative_ai()
    show_evolution()
    explain_attention()
    simple_tokenization_demo()
    show_learning_path()
    next_steps()

    print("=" * 60)
    print("🎉 Chapter 01 Complete! Ready for the journey ahead?")
    print("=" * 60)


if __name__ == "__main__":
    main()
