# GitHub Copilot Instructions for this Repo

These guidelines help ## Learning-specific guidance

- This is an educational repository following a 45-day structured learning path (`docs/learning-path-45-days.md`).
- When generating examples, prioritize educational clarity over production optimization.
- Include step-by-step explanations in code comments for learning purposes.
- For AI/ML concepts, provide intuitive explanations alongside technical implementations.
- Use meaningful variable names that teach concepts (e.g., `attention_weights` not `aw`).

## Generative AI development patterns

- For tokenization examples: explain vocabulary choices, special tokens, and encoding strategies.
- For embeddings: include similarity calculations, dimensionality considerations, and visualization hints.
- For model implementations: break down forward passes, loss calculations, and training loops.
- For agent patterns: document reasoning steps, state management, and failure handling.

## Prompt engineering guidelines

- Check `.github/prompts/` for curated prompt templates before asking general questions.
- Use structured prompts for code explanation, debugging, and concept exploration.
- Include relevant context about learning objectives when requesting assistance.

## Examples of "good Copilot tasks" here

- Improve a script's CLI ergonomics (e.g., add `--model` and `--file` flags).
- Refactor a demo to share a tokenizer/helper across examples.
- Add short markdown explanations above code cells in notebooks.
- Update docs/QUICKSTART.md when moving learning materials.
- Create educational examples that demonstrate specific AI concepts clearly.
- Generate step-by-step breakdowns of complex generative AI algorithms.
- Design progressive exercises that build from basic concepts to advanced implementations.

Thanks for keeping `src/` production‑grade and `notebooks/` learner‑friendly.(and contributors) generate changes that fit the project’s structure and standards.

## Project quick facts

- Language/runtime: Python 3.12.5
- OS focus: Windows; default shell is PowerShell (pwsh)
- Folders:
  - `src/` — production code and scripts (keep clean and runnable)
  - `notebooks/` — learning materials and interactive demos (e.g., `notebooks/day1/...`)
  - `docs/` — documentation, quickstarts, concepts, tutorials
- Dependencies: pinned in `requirements.txt` (keep minimal; add only when needed)

## When generating or editing code

- Prefer small, focused changes that keep the repo building and runnable.
- Use standard Python practices:
  - Type hints where helpful; clean function boundaries; avoid global state.
  - Use `pathlib` for paths, `os.environ` for secrets.
  - Don’t hardcode API keys; load from env (e.g., `OPENAI_API_KEY`). Optional `.env` via `python-dotenv` is OK for local dev.
  - Keep outputs deterministic; avoid unnecessary network calls in examples.
- If you add a dependency:
  - Update `requirements.txt` with a pinned version.
  - Briefly justify in code comments or PR description.
- For scripts that print guidance to users, prefer Windows‑friendly commands (PowerShell) and relative repo paths.

## Notebooks guidance

- Place notebooks under `notebooks/` (not in `src/`).
- When programmatically updating `.ipynb`:
  - Keep cells as valid JSON objects with `metadata.language` set (e.g., `markdown`, `python`).
  - Preserve existing `metadata.id` on existing cells.
  - New cells do not need an `id`.
  - Don’t reference cell IDs in messages or docs; refer by cell number.
- Prefer explanations (markdown) above the code cells they describe.
- Keep demos lightweight; avoid downloading large datasets in notebooks.

## Documentation

- If you move or rename files that are linked from docs, update `docs/QUICKSTART.md` and any in‑repo references.
- Add brief “how to run” notes when introducing new scripts or notebooks.

## Commits and PRs

- Use clear, action‑oriented commit messages (e.g., `notebooks: move day1 foundation notebook`, `feat: add clean_tokenize and sklearn‑style IDF`).
- Open PRs from a feature branch; target `main`.
- PR description should include:
  - What changed and why
  - Any new dependencies
  - How to run/validate (commands or steps)

## Validation checklist

- Build/lint: no syntax errors; code runs on Python 3.12.5.
- If you edited notebooks, open and run the modified cells to sanity check outputs.
- If public behavior changed, add/update a short example or test where feasible.

## Security & secrets

- Never commit secrets. Use environment variables and `.env` (locally) with `python-dotenv`.
- Avoid embedding long outputs or large data files; prefer small samples.

## Style preferences (Python)

- Imports: stdlib, third‑party, local — grouped and sorted.
- Logging/prints: concise, user‑friendly; avoid noisy debug output by default.
- Error handling: fail fast with helpful messages; provide graceful fallbacks where reasonable.

## Examples of “good Copilot tasks” here

- Improve a script’s CLI ergonomics (e.g., add `--model` and `--file` flags).
- Refactor a demo to share a tokenizer/helper across examples.
- Add short markdown explanations above code cells in notebooks.
- Update docs/QUICKSTART.md when moving learning materials.

Thanks for keeping `src/` production‑grade and `notebooks/` learner‑friendly.
