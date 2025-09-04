# 18‑Week Generative AI Learning Path (90 days, 5 days/week, ~30 min/day)

This comprehensive plan uses content from this repository's `docs/`, `src/`, and `notebooks/` folders. Study 5 days per week (e.g., Mon–Fri), ~30 minutes per day. Weekends are for rest, catch‑up, or deeper exploration.

Note: Paths below are relative to the repository root.

## Week 1 — Generative AI Introduction (Days 1–5)

- Day 1 — What is Generative AI
  - Read: `docs/archived/concepts/generative-ai-fundamentals.md` (intro + key characteristics)
  - Do: Write 3 concrete outputs you want GenAI to produce in your domain.
  - Reflect: 10 minutes on potential applications

- Day 2 — How GenAI Works (Overview)
  - Read: same file, "How Generative AI Works" (first half)
  - Do: Sketch the high-level training concept
  - Explore: Browse `docs/archived/day1/01_generative_ai_foundations.ipynb` (introduction cells)

- Day 3 — Key Components & Architecture
  - Read: same file, "Key Components" section
  - Do: List 2 quality levers you can control
  - Study: Architecture diagrams in the notebook

- Day 4 — Mathematical Foundations I: Probability Basics
  - Read: same file, "Mathematical Foundation" (probability section only)
  - Do: Explain probability in language modeling (2 sentences)
  - Practice: Simple probability examples

- Day 5 — Mathematical Foundations II: Loss Functions
  - Read: same file, "Mathematical Foundation" (loss functions)
  - Do: Describe what language modeling loss optimizes
  - Code: Run basic example in `src/a1/helloworld.py`

## Week 2 — Generative AI Deep Dive (Days 6–10)

- Day 6 — Sampling Strategies I: Basics
  - Read: same file, "Sampling Strategies" (greedy + random)
  - Do: Compare greedy vs random sampling
  - Experiment: Test basic sampling with `src/a1/basic_concepts.py`

- Day 7 — Sampling Strategies II: Advanced
  - Read: same file, "Sampling Strategies" (top-k + top-p)
  - Do: When would you choose top-k vs top-p?
  - Practice: Experiment with different sampling parameters

- Day 8 — Limitations & Challenges
  - Read: same file, "Current Limitations"
  - Do: Pick one limitation and propose a mitigation
  - Reflect: How limitations affect your use cases

- Day 9 — Ethical Considerations
  - Read: same file, "Ethical Considerations"
  - Do: Document ethical considerations for your planned use cases
  - Discuss: Consider bias and fairness implications

- Day 10 — Applications & Future Directions
  - Read: same file, "Practical Applications" + "Future Directions"
  - Do: List 3 practical ideas you could try
  - Explore: Contact extraction examples in `src/a1/extract_contact_info*.py`

## Week 3 — Language Models Foundations (Days 11–15)

- Day 11 — Language Models Evolution I
  - Read: `docs/archived/concepts/language-models.md` (statistical era)
  - Do: Understand n-gram limitations
  - Study: Historical progression of language modeling

- Day 12 — Language Models Evolution II
  - Read: same file (neural era through transformers)
  - Do: Name 1 transformer advantage over LSTMs
  - Visualize: Study transformer architecture diagrams

- Day 13 — Tokenization Introduction
  - Read: `docs/archived/concepts/tokenization-fundamentals.md` (introduction)
  - Do: Understand why tokenization is needed
  - Practice: Basic text splitting examples

- Day 14 — Embeddings Introduction
  - Read: `docs/archived/concepts/embeddings-fundamentals.md` (introduction + basic concepts)
  - Do: Explain how embeddings enable similarity
  - Concept: Understand discrete → continuous transformation

- Day 15 — Transformer Blocks Overview
  - Read: `docs/archived/concepts/language-models.md`, "Transformer Blocks" (overview)
  - Do: Sketch basic transformer components
  - Study: Attention + FFN + residuals overview

## Week 4 — Tokenization Fundamentals (Days 16–20)

- Day 16 — Tokenization Concepts Deep Dive
  - Read: `docs/archived/concepts/tokenization-fundamentals.md` (complete)
  - Workshop: Begin `docs/archived/tutorials/day3-tokenization-workshop.md` (intro)
  - Do: Understand subword tokenization benefits

- Day 17 — BPE and Subword Tokenization I
  - Read: `docs/archived/reference/tokenization-reference.md` (BPE section)
  - Workshop: Day 3 Workshop Experiment 1
  - Code: Basic tokenization with `src/a2/a1_countingtokens.py`

- Day 18 — BPE and Subword Tokenization II
  - Workshop: Day 3 Workshop Experiment 2
  - Code: Analyze encodings with `src/a2/a2_encodings.py`
  - Do: Compare different tokenizer outputs

- Day 19 — Encoding Strategies I
  - Workshop: Day 3 Workshop Experiment 3
  - Code: Practice with `src/a2/a3_tokenencoding.py`
  - Do: Understand encoding vs decoding

- Day 20 — Encoding Strategies II
  - Workshop: Day 3 Workshop Experiment 4
  - Practice: Test tokenization on your domain text
  - Reflect: Tokenization choices impact on your use case

## Week 5 — Advanced Tokenization (Days 21–25)

- Day 21 — Morphological Analysis I
  - Read: `docs/archived/tutorials/bpe-morphological-discovery.md` (first half)
  - Code: Explore `src/a2/a2_morphological_bpe.py`
  - Study: How BPE handles word formation

- Day 22 — Morphological Analysis II
  - Read: Complete morphological discovery tutorial
  - Do: Analyze compound words in your target language
  - Practice: Morphological pattern recognition

- Day 23 — Model-Specific Tokenizers I
  - Code: Compare tokenizers with `src/a2/a4_model_tokenizer.py`
  - Workshop: Day 3 Workshop Experiment 5
  - Study: Different model tokenization approaches

- Day 24 — Model-Specific Tokenizers II
  - Code: Advanced comparison with `src/a2/a5_model_tokenizer.py`
  - Workshop: Day 3 Workshop Experiment 6
  - Do: Document tokenizer choice impacts

- Day 25 — Tokenization Best Practices
  - Read: `docs/archived/reference/tokenization-reference.md` (troubleshooting)
  - Workshop: Complete Day 3 summary and reflection
  - Project: Design tokenization strategy for custom application

## Week 6 — Embeddings Fundamentals (Days 26–30)

- Day 26 — Embeddings Concepts Deep Dive
  - Read: `docs/archived/concepts/embeddings-fundamentals.md` (complete review)
  - Workshop: Begin `docs/archived/tutorials/day4-embeddings-workshop.md`
  - Understand: Vector space properties

- Day 27 — Embedding Generation I
  - Workshop: Day 4 Workshop Experiment 1
  - Code: Run `src/a3/a1_embeddings.py`
  - Notebook: Begin `docs/archived/day4/04_embeddings_discovery_laboratory.ipynb`

- Day 28 — Embedding Generation II
  - Workshop: Day 4 Workshop Experiment 2
  - Code: Explore properties with `src/a3/a2_embeddings.py`
  - Do: Analyze embedding dimensions and properties

- Day 29 — Semantic Similarity I
  - Workshop: Day 4 Workshop Experiment 3 (first half)
  - Code: Similarity analysis with `src/a3/a3_embeddings.py`
  - Study: Cosine similarity mathematics

- Day 30 — Semantic Similarity II
  - Workshop: Complete Day 4 Workshop Experiment 3
  - Code: Advanced similarity with `src/a3/a4_embeddings.py`
  - Practice: Semantic relationship analysis

## Week 7 — Advanced Embeddings (Days 31–35)

- Day 31 — Vector Arithmetic I
  - Workshop: Day 4 Workshop Experiment 4 (vector arithmetic intro)
  - Lab: Use `src/a3/embeddings_discovery_lab.py` (arithmetic section)
  - Concept: Mathematics of meaning

- Day 32 — Vector Arithmetic II
  - Workshop: Complete Day 4 Workshop Experiment 4
  - Practice: King - Man + Woman = Queen experiments
  - Do: Test analogies in your domain

- Day 33 — Clustering and Visualization I
  - Workshop: Day 4 Workshop Experiment 5
  - Code: Clustering with `src/a3/a5_embeddings.py`
  - Notebook: Clustering experiments in discovery lab

- Day 34 — Clustering and Visualization II
  - Workshop: Day 4 Workshop Experiment 6
  - Code: Advanced visualization with `src/a3/a6_embeddings.py`
  - Practice: Visualize embeddings for your data

- Day 35 — Semantic Search Implementation
  - Code: Build semantic search with discovery lab
  - Project: Create domain-specific semantic search
  - Do: Compare keyword vs semantic search results

## Week 8 — Embeddings in Practice (Days 36–40)

- Day 36 — Advanced Similarity Search
  - Lab: Complete semantic search experiments
  - Practice: Optimize search parameters
  - Test: Search quality evaluation

- Day 37 — Contextual Embeddings
  - Study: Context-dependent meaning representation
  - Experiment: Same word, different contexts
  - Analyze: Polysemy in embeddings

- Day 38 — Embedding Applications
  - Workshop: Complete Day 4 summary and discoveries
  - Project: Embeddings-based recommendation system
  - Plan: Production embedding system design

- Day 39 — Embedding Evaluation
  - Study: Intrinsic vs extrinsic evaluation
  - Practice: Embedding quality metrics
  - Do: Evaluate embeddings for your use case

- Day 40 — Embeddings Best Practices
  - Reflect: When to use embeddings vs alternatives
  - Document: Best practices for your domain
  - Review: Complete embeddings mastery check

## Week 9 — Attention Mechanisms (Days 41–45)

- Day 41 — Attention Fundamentals
  - Read: `docs/archived/concepts/language-models.md`, "Attention Mechanism"
  - Do: Summarize self-attention in your own words
  - Study: Attention as weighted averaging

- Day 42 — Attention Mathematics
  - Study: Query, Key, Value matrices
  - Practice: Manual attention calculations
  - Visualize: Attention pattern examples

- Day 43 — Multi-Head Attention I
  - Study: Multiple attention perspectives
  - Do: Explain why multiple heads help
  - Code: Basic attention scoring examples

- Day 44 — Multi-Head Attention II
  - Practice: Multi-head attention analysis
  - Study: Attention head specialization
  - Implement: Simple attention mechanism

- Day 45 — Attention Patterns
  - Project: Analyze attention in real texts
  - Do: Identify local vs global attention
  - Study: Common attention patterns

## Week 10 — Context and Efficiency (Days 46–50)

- Day 46 — Context Window Fundamentals
  - Read: `docs/archived/concepts/language-models.md`, "Context Window"
  - Do: Understand context limitations
  - Study: Memory and computational constraints

- Day 47 — Context Window Strategies
  - Do: Note 2 tactics for long inputs
  - Practice: Context window management
  - Study: Sliding window techniques

- Day 48 — Positional Encoding I
  - Study: How transformers handle sequence order
  - Understand: Absolute vs relative positioning
  - Code: Basic positional encoding examples

- Day 49 — Positional Encoding II
  - Compare: Sinusoidal vs learned positions
  - Practice: Positional encoding variations
  - Implement: Custom positional encoding

- Day 50 — Attention Efficiency
  - Study: Sparse attention patterns
  - Understand: Linear attention approaches
  - Research: Efficient attention mechanisms

## Week 11 — Training and Model Types (Days 51–55)

- Day 51 — Training Process I: Data Collection
  - Read: `docs/archived/concepts/language-models.md`, "Training Process" (data)
  - Study: Data collection strategies
  - Do: List 3 data quality risks

- Day 52 — Training Process II: Preprocessing
  - Read: same file (cleaning, dedup, filtering)
  - Practice: Data preprocessing pipeline
  - Do: Design data quality mitigations

- Day 53 — Training Process III: Pretraining
  - Read: same file (pretraining objective)
  - Do: Write pseudo-code for pretraining
  - Code: Basic language modeling loss

- Day 54 — Fine-tuning Strategies I
  - Read: same file, "Fine-tuning" (SFT)
  - Study: Supervised fine-tuning approaches
  - Do: Map use case to fine-tuning type

- Day 55 — Fine-tuning Strategies II
  - Read: same file (RLHF, Constitutional AI)
  - Compare: Different fine-tuning approaches
  - Experiment: Fine-tuned vs base models

## Week 12 — Model Families and Evaluation (Days 56–60)

- Day 56 — Model Families I: GPT
  - Read: `docs/archived/concepts/language-models.md`, "Types" (GPT)
  - Study: Decoder-only architecture
  - Do: Identify GPT use cases

- Day 57 — Model Families II: BERT
  - Read: same file (BERT section)
  - Study: Encoder-only architecture
  - Do: Compare BERT vs GPT applications

- Day 58 — Model Families III: Encoder-Decoder
  - Read: same file (Encoder-Decoder)
  - Study: Full transformer architecture
  - Do: Map 3 tasks to appropriate model types

- Day 59 — Evaluation Metrics I
  - Read: same file, "Evaluation Metrics" (Perplexity, BLEU)
  - Practice: Calculate basic metrics
  - Do: Choose metrics for your experiments

- Day 60 — Evaluation Metrics II
  - Read: same file (Human evaluation)
  - Study: Qualitative vs quantitative evaluation
  - Practice: Design evaluation framework

## Week 13 — Prompting Fundamentals (Days 61–65)

- Day 61 — Prompt Engineering Basics I
  - Read: `docs/archived/concepts/language-models.md`, "Prompt Engineering" (principles)
  - Study: Clear task definition principles
  - Practice: Basic prompt structure

- Day 62 — Prompt Engineering Basics II
  - Do: Draft prompts with clear constraints and format
  - Practice: Prompt iteration and refinement
  - Test: Systematic prompt variations

- Day 63 — Zero-shot and Few-shot I
  - Read: same file (zero/few-shot examples)
  - Study: In-context learning principles
  - Practice: Zero-shot prompting techniques

- Day 64 — Zero-shot and Few-shot II
  - Do: Write few-shot prompts for your tasks
  - Practice: Example selection strategies
  - Test: Few-shot vs zero-shot performance

- Day 65 — Chain-of-Thought I
  - Read: same file (CoT examples)
  - Study: Step-by-step reasoning
  - Practice: CoT prompt construction

## Week 14 — Advanced Prompting (Days 66–70)

- Day 66 — Chain-of-Thought II
  - Practice: Complex reasoning tasks
  - Compare: CoT vs direct prompting
  - Experiment: CoT effectiveness analysis

- Day 67 — Prompt Optimization I
  - Study: A/B testing for prompts
  - Practice: Systematic prompt improvement
  - Tools: Prompt evaluation frameworks

- Day 68 — Prompt Optimization II
  - Do: Develop prompt templates
  - Practice: Template-based prompt systems
  - Test: Template effectiveness

- Day 69 — Model Comparison I
  - Read: `docs/archived/concepts/language-models.md`, "Popular Models"
  - Study: Model characteristics and trade-offs
  - Do: Pick model for your use case

- Day 70 — Model Comparison II
  - Practice: Benchmark models on specific tasks
  - Do: Document cost vs performance trade-offs
  - Plan: Model selection strategy

## Week 15 — AI Agents Introduction (Days 71–75)

- Day 71 — AI Agents Overview I
  - Read: `docs/archived/concepts/ai-agents.md` (introduction)
  - Study: Agents vs chatbots distinction
  - Do: List 3 key differences

- Day 72 — AI Agents Overview II
  - Read: same file (relation to GenAI)
  - Study: How LLMs enable agents
  - Explore: Agent architecture examples

- Day 73 — Agent Types I
  - Read: same file, "Types of AI Agents" (first half)
  - Study: Reactive vs deliberative agents
  - Do: Pick agent type for your use case

- Day 74 — Agent Types II
  - Read: same file (remaining agent types)
  - Compare: Different agent architectures
  - Design: Sketch agent for your domain

- Day 75 — Core Agent Components I
  - Read: same file, "Key Components" (perception)
  - Study: How agents perceive environment
  - Do: List signals your agent needs

## Week 16 — Agent Architectures (Days 76–80)

- Day 76 — Core Agent Components II
  - Read: same file (reasoning/planning)
  - Study: Agent decision-making processes
  - Plan: Design reasoning components

- Day 77 — Core Agent Components III
  - Read: same file (action + learning)
  - Study: Agent action mechanisms
  - Design: Plan action components

- Day 78 — ReAct Architecture I
  - Read: same file (ReAct) + `docs/archived/concepts/agentic-ai-patterns.md` (ReAct)
  - Study: Reasoning + Acting cycles
  - Do: Outline 4-loop ReAct cycle

- Day 79 — ReAct Architecture II
  - Study: ReAct pattern details
  - Implement: Basic ReAct loop structure
  - Practice: ReAct for research tasks

- Day 80 — Plan-and-Execute I
  - Read: `docs/archived/concepts/agentic-ai-patterns.md` (Plan-and-Execute)
  - Study: Planning-based agent architecture
  - Do: Draft 5-step plan for complex task

## Week 17 — Advanced Agent Patterns (Days 81–85)

- Day 81 — Plan-and-Execute II
  - Study: Plan monitoring and adaptation
  - Implement: Basic planning logic
  - Practice: Multi-step task planning

- Day 82 — Reflexion I
  - Read: `docs/archived/concepts/agentic-ai-patterns.md` (Reflexion)
  - Study: Self-reflection in agents
  - Do: Design reflection workflow

- Day 83 — Reflexion II
  - Implement: Basic self-reflection
  - Practice: Error correction mechanisms
  - Study: Learning from mistakes

- Day 84 — Multi-Agent Collaboration I
  - Read: same file, "Multi-Agent Collaboration"
  - Study: Agent teamwork patterns
  - Do: Define 3 agent roles with handoffs

- Day 85 — Multi-Agent Collaboration II
  - Design: Multi-agent system architecture
  - Practice: Agent coordination mechanisms
  - Plan: Team-based task execution

## Week 18 — Implementation and Deployment (Days 86–90)

- Day 86 — Agent Implementation I
  - Read: `docs/archived/concepts/agentic-ai-patterns.md`, "Design Principles"
  - Study: Modular agent architecture
  - Do: Sketch agent components

- Day 87 — Agent Implementation II
  - Read: same file, "Implementation Strategies"
  - Plan: Incremental development path
  - Build: Minimal viable agent

- Day 88 — Production Considerations
  - Study: Scaling and monitoring strategies
  - Plan: Production deployment architecture
  - Design: Safety and guardrails

- Day 89 — Integration Testing
  - Read: `docs/archived/tutorials/genai-to-agents.md`
  - Practice: End-to-end system testing
  - Validate: Agent behavior verification

- Day 90 — Capstone Project
  - Complete: Full agent system documentation
  - Present: Working agent demonstration
  - Plan: Future development roadmap

---

## Learning Resources by Week

### Weeks 1-2: Foundation

- `docs/archived/concepts/generative-ai-fundamentals.md`
- `docs/archived/day1/01_generative_ai_foundations.ipynb`
- `src/a1/` (basic examples)

### Weeks 3-4: Core Technologies

- `docs/archived/concepts/tokenization-fundamentals.md`
- `docs/archived/concepts/embeddings-fundamentals.md`
- `docs/archived/tutorials/day3-tokenization-workshop.md`
- `docs/archived/tutorials/day4-embeddings-workshop.md`
- `src/a2/` and `src/a3/` (hands-on labs)
- `docs/archived/day4/04_embeddings_discovery_laboratory.ipynb`

### Weeks 5-7: Language Models

- `docs/archived/concepts/language-models.md`
- `docs/archived/reference/tokenization-reference.md`

### Weeks 8-12: AI Agents

- `docs/archived/concepts/ai-agents.md`
- `docs/archived/concepts/agentic-ai-patterns.md`
- `docs/archived/reference/agent-api-reference.md`
- `docs/archived/tutorials/genai-to-agents.md`

## Daily Learning Tips

- **Time Management**: 30 minutes daily = 10 min reading + 15 min coding + 5 min reflection
- **Note Taking**: Keep a running notes file with "3 takeaways/day"
- **Practical Focus**: Prefer small, safe experiments; validate assumptions early
- **Progressive Building**: Each week builds on previous knowledge
- **Project Integration**: Connect daily learning to your capstone project
- **Weekend Usage**: Rest, catch-up, or deeper exploration of interesting topics

## Success Metrics

- **Week 6**: Comfortable with tokenization and embeddings
- **Week 12**: Built first functional AI agent
- **Week 18**: Deployed production-ready agent system
- **Final Goal**: Comprehensive understanding from foundations to deployment

This 90-day journey transforms you from AI beginner to agent developer with deep understanding of the entire stack!
