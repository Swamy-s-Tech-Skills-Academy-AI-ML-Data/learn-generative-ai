# 12‑Week Generative AI Learning Path (60 days, 5 days/week, ~45 min/day)

This comprehensive plan uses content from this repository's `docs/`, `src/`, and `notebooks/` folders. Study 5 days per week (e.g., Mon–Fri), ~45 minutes per day. Weekends are for rest, catch‑up, or deeper exploration.

Note: Paths below are relative to the repository root.

## Week 1 — Generative AI Foundations (Days 1–5)

- Day 1 — What is Generative AI
  - Read: `docs/concepts/generative-ai-fundamentals.md` (intro + key characteristics)
  - Do: Write 3 concrete outputs you want GenAI to produce in your domain.
  - Explore: `notebooks/day1/01_generative_ai_foundations.ipynb` (introduction cells)

- Day 2 — How GenAI Works (Train → Generate)
  - Read: same file, "How Generative AI Works" + Key Components
  - Do: Sketch the training and generation phases; list 2 quality levers.
  - Code: Run basic text generation example in `src/a1/helloworld.py`

- Day 3 — Mathematical Foundation I: Probability & Loss
  - Read: same file, "Mathematical Foundation" (probability + loss)
  - Do: In 2 sentences, describe what the language modeling loss optimizes.
  - Practice: Work through probability examples in the notebook

- Day 4 — Mathematical Foundation II: Sampling
  - Read: same file, "Sampling Strategies" (greedy, random, top‑k, top‑p)
  - Do: Compare top‑k vs top‑p and when you'd choose each.
  - Experiment: Test different sampling strategies with `src/a1/basic_concepts.py`

- Day 5 — Limitations & Ethics
  - Read: same file, "Current Limitations" + "Ethical Considerations"
  - Do: Pick one limitation and propose a mitigation for your context.
  - Reflect: Document ethical considerations for your planned use cases

## Week 2 — Foundations Wrap + LM Basics (Days 6–10)

- Day 6 — Applications & Future Directions
  - Read: same file, "Practical Applications" + "Future Directions"
  - Do: List 3 practical ideas you could try in your work.
  - Explore: Contact extraction examples in `src/a1/extract_contact_info*.py`

- Day 7 — Language Models Evolution
  - Read: `docs/concepts/language-models.md` (statistical → neural → transformer era)
  - Do: Name 1 transformer advantage over LSTMs and why it matters.
  - Visualize: Study transformer architecture diagrams in Day 1 notebook

- Day 8 — Tokenization Fundamentals
  - Read: `docs/concepts/tokenization-fundamentals.md` + `docs/tutorials/day3-tokenization-workshop.md`
  - Do: Describe how tokenization choices impact downstream behavior.
  - Hands-on: Complete tokenization exercises in `src/a2/`

- Day 9 — Embeddings Fundamentals
  - Read: `docs/concepts/embeddings-fundamentals.md`
  - Do: Explain how embeddings enable semantic similarity.
  - Workshop: Begin `docs/tutorials/day4-embeddings-workshop.md`

- Day 10 — Transformer Blocks
  - Read: `docs/concepts/language-models.md`, "Transformer Blocks"
  - Do: Sketch the block: attention → FFN → residuals → layernorm.
  - Practice: Run transformer visualization code in notebooks

## Week 3 — Tokenization Deep Dive (Days 11–15)

- Day 11 — BPE and Subword Tokenization
  - Read: `docs/reference/tokenization-reference.md`
  - Workshop: Complete `docs/tutorials/day3-tokenization-workshop.md` Experiment 1-2
  - Code: Analyze tokenization with `src/a2/a1_countingtokens.py`

- Day 12 — Encoding Strategies
  - Workshop: Day 3 Experiment 3-4
  - Code: Practice with `src/a2/a2_encodings.py` and `src/a2/a3_tokenencoding.py`
  - Do: Compare different tokenizer outputs for your domain text

- Day 13 — Morphological Analysis
  - Read: `docs/tutorials/bpe-morphological-discovery.md`
  - Code: Explore `src/a2/a2_morphological_bpe.py`
  - Do: Analyze how BPE handles compound words in your language

- Day 14 — Model-Specific Tokenizers
  - Code: Compare tokenizers with `src/a2/a4_model_tokenizer.py` and `src/a2/a5_model_tokenizer.py`
  - Workshop: Day 3 Experiments 5-6
  - Do: Document tokenizer choice impacts for your use case

- Day 15 — Tokenization Best Practices
  - Read: `docs/reference/tokenization-reference.md` (troubleshooting section)
  - Workshop: Complete Day 3 summary and reflection
  - Project: Design tokenization strategy for a custom application

## Week 4 — Embeddings Deep Dive (Days 16–20)

- Day 16 — Embedding Generation and Properties
  - Workshop: `docs/tutorials/day4-embeddings-workshop.md` Experiments 1-2
  - Code: Run `src/a3/a1_embeddings.py` and `src/a3/a2_embeddings.py`
  - Notebook: Complete `notebooks/day4/04_embeddings_discovery_laboratory.ipynb` Experiments 1-2

- Day 17 — Semantic Similarity and Vector Arithmetic
  - Workshop: Day 4 Experiments 3-4
  - Code: Explore similarity with `src/a3/a3_embeddings.py` and `src/a3/a4_embeddings.py`
  - Lab: Use `src/a3/embeddings_discovery_lab.py` for hands-on exploration

- Day 18 — Clustering and Visualization
  - Workshop: Day 4 Experiments 5-6
  - Code: Practice clustering with `src/a3/a5_embeddings.py` and `src/a3/a6_embeddings.py`
  - Notebook: Complete all embedding laboratory experiments

- Day 19 — Advanced Similarity Search
  - Code: Build semantic search with `src/a3/embeddings_discovery_lab.py`
  - Project: Create a custom semantic search for your domain
  - Do: Compare keyword vs semantic search results

- Day 20 — Embeddings in Practice
  - Workshop: Complete Day 4 summary and key discoveries
  - Project: Implement embeddings-based recommendation system
  - Reflect: Document when to use embeddings vs other approaches

## Week 5 — Attention and Context (Days 21–25)

- Day 21 — Attention Mechanism Fundamentals
  - Read: `docs/concepts/language-models.md`, "Attention Mechanism"
  - Do: Summarize self‑attention in your own words.
  - Visualize: Study attention patterns in example texts

- Day 22 — Multi-Head Attention
  - Study: Attention implementations from transformer examples
  - Do: Explain why multiple attention heads are beneficial
  - Code: Implement basic attention scoring from scratch

- Day 23 — Context Window and Efficiency
  - Read: `docs/concepts/language-models.md`, "Context Window"
  - Do: Note 2 tactics you'll use for long inputs.
  - Experiment: Test context window limits with different models

- Day 24 — Positional Encoding
  - Study: How transformers handle sequence order
  - Do: Compare absolute vs relative positional encoding
  - Implement: Basic positional encoding examples

- Day 25 — Attention Patterns Analysis
  - Project: Analyze attention patterns in real texts
  - Do: Identify common attention patterns (local, global, sparse)
  - Reflect: When does attention help vs hurt performance?

## Week 6 — Training and Model Types (Days 26–30)

- Day 26 — Training Process I: Data & Preprocessing
  - Read: `docs/concepts/language-models.md`, "Training Process" (data collection, cleaning, dedup, filtering)
  - Do: List 3 data quality risks and mitigations.
  - Practice: Clean and prepare a small training dataset

- Day 27 — Training Process II: Pretraining Objective
  - Read: same file, "Training Process" (objective/loop)
  - Do: Write a pseudo‑loop of the pretraining step.
  - Code: Implement basic language modeling loss calculation

- Day 28 — Fine‑tuning Strategies
  - Read: same file, "Fine‑tuning" section (SFT, RLHF, Constitutional AI)
  - Do: Map a use case → which fine‑tuning approach and why.
  - Experiment: Compare fine-tuned vs base model outputs

- Day 29 — Model Families: GPT/BERT/Enc‑Dec
  - Read: same file, "Types of Language Models"
  - Do: Map 3 tasks → (GPT|BERT|Enc‑Dec) with justification.
  - Compare: Test different model types on the same task

- Day 30 — Evaluation Metrics
  - Read: same file, "Evaluation Metrics" (Perplexity, BLEU, Human eval)
  - Do: Choose a metric for your next experiment and why.
  - Practice: Calculate evaluation metrics for model outputs

## Week 7 — Prompting and Optimization (Days 31–35)

- Day 31 — Prompt Engineering Basics
  - Read: `docs/concepts/language-models.md`, "Prompt Engineering" (principles)
  - Do: Draft a prompt with clear task, constraints, and format.
  - Practice: Test prompt variations systematically

- Day 32 — Advanced Prompting Techniques
  - Read: same file, "Prompt Engineering" (zero/few‑shot, CoT examples)
  - Do: Write a few‑shot prompt for a task you care about.
  - Experiment: Chain-of-thought vs direct prompting comparison

- Day 33 — Prompt Optimization Strategies
  - Practice: A/B test different prompt formulations
  - Do: Develop prompt templates for common tasks
  - Tools: Create prompt evaluation framework

- Day 34 — Popular Models Comparison
  - Read: same file, "Popular Models Comparison" + "Getting Started"
  - Do: Pick a model class and note its trade‑offs for your use case.
  - Benchmark: Compare models on your specific tasks

- Day 35 — Model Selection and Trade-offs
  - Project: Create model selection framework for your use cases
  - Do: Document cost vs performance trade-offs
  - Plan: Design model deployment strategy

## Week 8 — AI Agents Foundations (Days 36–40)

- Day 36 — AI Agents Overview
  - Read: `docs/concepts/ai-agents.md` (what agents are, relation to GenAI)
  - Do: List 3 differences between a chatbot and an agent.
  - Explore: Study existing agent examples and architectures

- Day 37 — Agent Types and Use Cases
  - Read: same file, "Types of AI Agents"
  - Do: Pick a use case and choose a suitable agent type.
  - Design: Sketch an agent for your specific domain

- Day 38 — Core Agent Components
  - Read: same file, "Key Components" (perception, reasoning/planning, action, learning)
  - Do: Bullet the signals your agent needs to perceive.
  - Plan: Design the key components for your agent

- Day 39 — ReAct Architecture
  - Read: same file (ReAct) + `docs/concepts/agentic-ai-patterns.md` (ReAct pattern)
  - Do: Outline a 4‑loop ReAct cycle for a research goal.
  - Implement: Basic ReAct loop in code

- Day 40 — Plan‑and‑Execute Architecture
  - Read: `docs/concepts/ai-agents.md` + `docs/concepts/agentic-ai-patterns.md`
  - Do: Draft a 5‑step plan for a multi‑step task you face.
  - Code: Implement basic planning and execution logic

## Week 9 — Advanced Agent Architectures (Days 41–45)

- Day 41 — Reflexion and Self-Improvement
  - Read: `docs/concepts/ai-agents.md` + `docs/concepts/agentic-ai-patterns.md`
  - Do: Describe how you'd integrate self‑reflection into a workflow.
  - Implement: Basic self-reflection and error correction

- Day 42 — Multi‑Agent Collaboration
  - Read: `docs/concepts/agentic-ai-patterns.md`, "Multi‑Agent Collaboration Pattern"
  - Do: Define 3 roles for a small team with handoff criteria.
  - Design: Multi-agent system for complex tasks

- Day 43 — Agent Frameworks Overview
  - Read: `docs/concepts/ai-agents.md` + `docs/concepts/agentic-ai-patterns.md` (frameworks)
  - Do: Pick one framework (LangChain/AutoGen/CrewAI/Semantic Kernel/LlamaIndex) and list 2 strengths.
  - Experiment: Build simple agent with chosen framework

- Day 44 — Real‑World Applications
  - Read: `docs/concepts/ai-agents.md` (applications)
  - Do: Choose one application and note success criteria.
  - Study: Analyze successful agent deployments

- Day 45 — Challenges & Best Practices
  - Read: same file (challenges, ethics, best practices)
  - Do: List 3 guardrails you'll enforce before "write" actions.
  - Framework: Design safety and monitoring systems

## Week 10 — Agent Implementation (Days 46–50)

- Day 46 — Design Principles & Architecture
  - Read: `docs/concepts/agentic-ai-patterns.md`, "Design Principles" + "Architecture Components"
  - Do: Sketch your agent's modular blocks and interfaces.
  - Code: Implement basic agent architecture

- Day 47 — Implementation Strategies
  - Read: same file, "Implementation Strategies"
  - Do: Describe a safe incremental path from single‑tool → multi‑tool.
  - Build: Start with minimal viable agent

- Day 48 — LangChain Integration
  - Read: `docs/reference/agent-api-reference.md` (LangChain basic agent setup)
  - Do: Write a minimal agent outline (inputs/outputs).
  - Implement: LangChain-based agent prototype

- Day 49 — Custom Tools & Functions
  - Read: same file (custom tool creation + memory integration)
  - Do: Spec one tool: name, args schema, failure modes.
  - Code: Implement custom tools for your domain

- Day 50 — Function Calling Implementation
  - Read: same file (function definitions, parameters, execution loop)
  - Do: Define function schemas and execution safeguards.
  - Build: Complete function calling system

## Week 11 — Memory and Advanced Features (Days 51–55)

- Day 51 — Memory Systems Design
  - Read: `docs/reference/agent-api-reference.md` (Hierarchical memory)
  - Do: Decide what goes to short/long/episodic memory in your app.
  - Implement: Basic memory architecture

- Day 52 — Vector Memory Store
  - Read: same file (Vector memory store)
  - Do: Note your embedding model choice and retrieval threshold.
  - Build: Vector-based memory system with embeddings

- Day 53 — Advanced Memory Patterns
  - Study: Memory consolidation and retrieval strategies
  - Implement: Sophisticated memory management
  - Test: Memory system performance and accuracy

- Day 54 — Error Handling and Recovery
  - Read: `docs/concepts/agentic-ai-patterns.md`, "Challenges and Solutions"
  - Do: Design checks for hallucination/error propagation/context issues.
  - Implement: Robust error handling and recovery

- Day 55 — Agent Testing and Validation
  - Design: Comprehensive testing strategy for agents
  - Build: Automated testing framework
  - Validate: Agent behavior across edge cases

## Week 12 — Deployment and Capstone (Days 56–60)

- Day 56 — Deployment Architecture
  - Read: `docs/reference/agent-api-reference.md` (FastAPI deployment)
  - Do: List your minimal API endpoints and dependencies.
  - Build: FastAPI-based agent service

- Day 57 — Containerization and Orchestration
  - Read: same file (Dockerfile + K8s manifests)
  - Do: Capture constraints (CPU/RAM), health checks, readiness.
  - Deploy: Docker-based agent deployment

- Day 58 — Production Considerations
  - Study: Scaling, monitoring, and maintenance strategies
  - Implement: Production-ready agent features
  - Plan: Long-term maintenance and updates

- Day 59 — Integration and Testing
  - Read: `docs/tutorials/genai-to-agents.md` (evolution, patterns, pitfalls)
  - Integration: Connect all components into complete system
  - Test: End-to-end system validation

- Day 60 — Capstone Project
  - Do: Complete your agent project with full documentation:
    - Goal, success criteria, constraints
    - Architecture (ReAct/Plan‑and‑Execute/Reflexion)
    - Tools (schemas), memory plan, guardrails
    - Evaluation plan (metrics + manual checks)
    - Deployment and monitoring strategy
  - Present: Demonstrate your working agent system

---

## Learning Resources by Week

### Weeks 1-2: Foundation

- `docs/concepts/generative-ai-fundamentals.md`
- `notebooks/day1/01_generative_ai_foundations.ipynb`
- `src/a1/` (basic examples)

### Weeks 3-4: Core Technologies

- `docs/concepts/tokenization-fundamentals.md`
- `docs/concepts/embeddings-fundamentals.md`
- `docs/tutorials/day3-tokenization-workshop.md`
- `docs/tutorials/day4-embeddings-workshop.md`
- `src/a2/` and `src/a3/` (hands-on labs)
- `notebooks/day4/04_embeddings_discovery_laboratory.ipynb`

### Weeks 5-7: Language Models

- `docs/concepts/language-models.md`
- `docs/reference/tokenization-reference.md`

### Weeks 8-12: AI Agents

- `docs/concepts/ai-agents.md`
- `docs/concepts/agentic-ai-patterns.md`
- `docs/reference/agent-api-reference.md`
- `docs/tutorials/genai-to-agents.md`

## Daily Learning Tips

- **Time Management**: 45 minutes daily = 15 min reading + 20 min coding + 10 min reflection
- **Note Taking**: Keep a running notes file with "3 takeaways/day"
- **Practical Focus**: Prefer small, safe experiments; validate assumptions early
- **Progressive Building**: Each week builds on previous knowledge
- **Project Integration**: Connect daily learning to your capstone project
- **Weekend Usage**: Rest, catch-up, or deeper exploration of interesting topics

## Success Metrics

- **Week 4**: Comfortable with tokenization and embeddings
- **Week 8**: Built first functional AI agent
- **Week 12**: Deployed production-ready agent system
- **Final Goal**: Comprehensive understanding from foundations to deployment

This 60-day journey transforms you from AI beginner to agent developer with deep understanding of the entire stack!
