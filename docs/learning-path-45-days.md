# 9‑Week Generative AI Learning Path (45 days, 5 days/week, ~30 min/day)

This plan uses only content from this repository’s `docs/` folder. Study 5 days per week (e.g., Mon–Fri), ~30 minutes per day. Weekends are for rest or catch‑up.

Note: Paths below are relative to `docs/`.

## Week 1 — Generative AI Foundations (Days 1–5)

- Day 1 — What is Generative AI
  - Read: `concepts/generative-ai-fundamentals.md` (intro + key characteristics)
  - Do: Write 3 concrete outputs you want GenAI to produce in your domain.

- Day 2 — How GenAI Works (Train → Generate)
  - Read: same file, “How Generative AI Works” + Key Components
  - Do: Sketch the training and generation phases; list 2 quality levers.

- Day 3 — Mathematical Foundation I: Probability & Loss
  - Read: same file, “Mathematical Foundation” (probability + loss)
  - Do: In 2 sentences, describe what the language modeling loss optimizes.

- Day 4 — Mathematical Foundation II: Sampling
  - Read: same file, “Sampling Strategies” (greedy, random, top‑k, top‑p)
  - Do: Compare top‑k vs top‑p and when you’d choose each.

- Day 5 — Limitations & Ethics
  - Read: same file, “Current Limitations” + “Ethical Considerations”
  - Do: Pick one limitation and propose a mitigation for your context.

## Week 2 — Foundations Wrap + LM Basics (Days 6–10)

- Day 6 — Applications & Future Directions
  - Read: same file, “Practical Applications” + “Future Directions”
  - Do: List 3 practical ideas you could try in your work.

- Day 7 — Language Models Evolution
  - Read: `concepts/language-models.md` (statistical → neural → transformer era)
  - Do: Name 1 transformer advantage over LSTMs and why it matters.

- Day 8 — Tokenization
  - Read: same file, “Tokenization”
  - Do: Describe how tokenization choices impact downstream behavior.

- Day 9 — Embeddings
  - Read: same file, “Embedding Layer”
  - Do: Explain how embeddings enable semantic similarity.

- Day 10 — Transformer Blocks
  - Read: same file, “Transformer Blocks”
  - Do: Sketch the block: attention → FFN → residuals → layernorm.

## Week 3 — Attention, Training, Model Types (Days 11–15)

- Day 11 — Attention & Context Window
  - Read: same file, “Attention Mechanism” + “Context Window”
  - Do: Summarize self‑attention in your own words.

- Day 12 — Training Process I: Data & Preprocessing
  - Read: same file, “Training Process” (data collection, cleaning, dedup, filtering)
  - Do: List 3 data quality risks and mitigations.

- Day 13 — Training Process II: Pretraining Objective
  - Read: same file, “Training Process” (objective/loop)
  - Do: Write a pseudo‑loop of the pretraining step.

- Day 14 — Fine‑tuning (SFT, RLHF, Constitutional AI)
  - Read: same file, “Fine‑tuning” section content (SFT, RLHF, constitutional)
  - Do: Map a use case → which fine‑tuning approach and why.

- Day 15 — Model Families: GPT/BERT/Enc‑Dec
  - Read: same file, “Types of Language Models”
  - Do: Map 3 tasks → (GPT|BERT|Enc‑Dec) with justification.

## Week 4 — Evaluation & Prompting (Days 16–20)

- Day 16 — Context Window Tactics & Efficiency
  - Read: same file, “Context Window” (limits and strategies)
  - Do: Note 2 tactics you’ll use for long inputs.

- Day 17 — Evaluation Metrics
  - Read: same file, “Evaluation Metrics” (Perplexity, BLEU, Human eval)
  - Do: Choose a metric for your next experiment and why.

- Day 18 — Prompt Engineering Basics
  - Read: same file, “Prompt Engineering” (principles)
  - Do: Draft a prompt with clear task, constraints, and format.

- Day 19 — Prompting Techniques
  - Read: same file, “Prompt Engineering” (zero/few‑shot, CoT examples)
  - Do: Write a few‑shot prompt for a task you care about.

- Day 20 — Popular Models & Getting Started
  - Read: same file, “Popular Models Comparison” + “Getting Started”
  - Do: Pick a model class and note its trade‑offs for your use case.

## Week 5 — Agents: Concepts to Architectures (Days 21–25)

- Day 21 — AI Agents Overview
  - Read: `concepts/ai-agents.md` (what agents are, relation to GenAI)
  - Do: List 3 differences between a chatbot and an agent.

- Day 22 — Agent Types
  - Read: same file, “Types of AI Agents”
  - Do: Pick a use case and choose a suitable agent type.

- Day 23 — Core Components
  - Read: same file, “Key Components” (perception, reasoning/planning, action, learning)
  - Do: Bullet the signals your agent needs to perceive.

- Day 24 — Architectures: ReAct
  - Read: same file (ReAct) + `concepts/agentic-ai-patterns.md` (ReAct pattern)
  - Do: Outline a 4‑loop ReAct cycle for a research goal.

- Day 25 — Architectures: Plan‑and‑Execute
  - Read: `concepts/ai-agents.md` + `concepts/agentic-ai-patterns.md`
  - Do: Draft a 5‑step plan for a multi‑step task you face.

## Week 6 — Architectures, Frameworks, Patterns (Days 26–30)

- Day 26 — Architectures: Reflexion
  - Read: `concepts/ai-agents.md` + `concepts/agentic-ai-patterns.md`
  - Do: Describe how you’d integrate self‑reflection into a workflow.

- Day 27 — Frameworks Overview
  - Read: `concepts/ai-agents.md` + `concepts/agentic-ai-patterns.md` (frameworks)
  - Do: Pick one framework (LangChain/AutoGen/CrewAI/Semantic Kernel/LlamaIndex) and list 2 strengths.

- Day 28 — Real‑World Applications
  - Read: `concepts/ai-agents.md` (applications)
  - Do: Choose one application and note success criteria.

- Day 29 — Challenges & Best Practices
  - Read: same file (challenges, ethics, best practices)
  - Do: List 3 guardrails you’ll enforce before “write” actions.

- Day 30 — Agentic Patterns: ReAct Deep Dive
  - Read: `concepts/agentic-ai-patterns.md` (ReAct structure + example)
  - Do: Translate the example to your domain with specific tools.

## Week 7 — Patterns & Design (Days 31–35)

- Day 31 — Plan‑and‑Execute Pattern Deep Dive
  - Read: `concepts/agentic-ai-patterns.md` (plan → execute → monitor)
  - Do: Add monitoring/rollback to your Day 25 plan.

- Day 32 — Multi‑Agent Collaboration
  - Read: same file, “Multi‑Agent Collaboration Pattern”
  - Do: Define 3 roles for a small team with handoff criteria.

- Day 33 — Design Principles & Architecture Components
  - Read: same file, “Design Principles” + “Architecture Components”
  - Do: Sketch your agent’s modular blocks and interfaces.

- Day 34 — Implementation Strategies
  - Read: same file, “Implementation Strategies”
  - Do: Describe a safe incremental path from single‑tool → multi‑tool.

- Day 35 — Challenges & Solutions
  - Read: same file, “Challenges and Solutions”
  - Do: Design a check for one challenge (hallucination/error propagation/context).

## Week 8 — API Reference, Tools, Function Calling (Days 36–40)

- Day 36 — LangChain Basics
  - Read: `reference/agent-api-reference.md` (LangChain basic agent setup)
  - Do: Write a minimal agent outline (inputs/outputs).

- Day 37 — Custom Tools & Memory (LangChain)
  - Read: same file (custom tool creation + memory integration)
  - Do: Spec one tool: name, args schema, failure modes.

- Day 38 — Function Calling I: Definitions & Schemas
  - Read: same file (function definitions, parameters)
  - Do: Define a function schema and validation notes.

- Day 39 — Function Calling II: Execution Loop
  - Read: same file (execute function call, error handling, final response)
  - Do: Describe your function execution safeguards.

- Day 40 — Custom Agent Implementation
  - Read: same file (BaseAgent, ReActAgent examples)
  - Do: Describe your BaseAgent contract (inputs/outputs/errors).

## Week 9 — Memory, Deployment, Tutorial & Capstone (Days 41–45)

- Day 41 — Memory Systems I: Hierarchical Memory
  - Read: `reference/agent-api-reference.md` (Hierarchical memory)
  - Do: Decide what goes to short/long/episodic memory in your app.

- Day 42 — Memory Systems II: Vector Memory Store
  - Read: same file (Vector memory store)
  - Do: Note your embedding model choice and retrieval threshold.

- Day 43 — Deployment I: FastAPI
  - Read: same file (FastAPI deployment)
  - Do: List your minimal API endpoints and dependencies.

- Day 44 — Deployment II: Docker & Kubernetes
  - Read: same file (Dockerfile + K8s manifests)
  - Do: Capture constraints (CPU/RAM), health checks, readiness.

- Day 45 — From GenAI to Agents + Capstone Plan
  - Read: `tutorials/genai-to-agents.md` (evolution, first agent, advanced patterns, pitfalls)
  - Do: Draft a one‑pager:
    - Goal, success criteria, constraints
    - Architecture (ReAct/Plan‑and‑Execute/Reflexion)
    - Tools (schemas), memory plan, guardrails
    - Evaluation plan (metrics + manual checks)

---

Tips

- Keep a running notes file with “3 takeaways/day.”
- Prefer small, safe experiments; validate assumptions early.
- When ready, connect this plan to hands‑on code in `notebooks/` and `src/`.
