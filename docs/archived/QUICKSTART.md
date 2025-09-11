<!-- filename: QUICKSTART.md -->
# Quick Start: Begin Your AI Learning Journey

> **📝 Migration Note**: This QUICKSTART content has been superseded by:
>
> - **Main Setup Guide**: [`README.md`](../../README.md#quick-environment-setup)
> - **90-Day Learning Path**: [`docs/learning-path-90-days.md`](../learning-path-90-days.md)
> - **Week 1 Daily Guides**: [`docs/daily-guides/week01/`](../daily-guides/week01/)
>
> This file remains for reference. Please use the current learning materials for active study.

This guide helps you establish your learning environment and start exploring generative AI concepts immediately. Follow these steps to join our systematic discovery workshop.

## Quick Start (TL;DR)

```powershell
# Clone the discovery workspace
git clone https://github.com/your-username/learn-generative-ai.git
cd learn-generative-ai

# Set up your learning environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

# Begin Day 1 exploration
python src/day1/basic_concepts.py

# Start interactive discovery (optional)
jupyter notebook notebooks/day1/01_generative_ai_foundations.ipynb
```

## Prerequisites

- **Windows 10/11** with PowerShell
- **Python 3.12.5** (recommended for optimal compatibility)
- **Git** for version control
- **OpenAI API key** (for advanced examples - free tier available)
- **Curiosity and willingness to experiment!**

## Detailed Setup Instructions

### 1. Environment Configuration

Create your isolated learning environment:

```powershell
# Navigate to your desired directory
cd d:\STSAAIMLDT\

# Clone the discovery workspace
git clone https://github.com/your-username/learn-generative-ai.git
cd learn-generative-ai

# Create virtual environment
python -m venv .venv

# Activate your learning environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip for latest features
python -m pip install --upgrade pip

# Install all learning dependencies
pip install -r requirements.txt
```

### 2. API Configuration (Optional for Advanced Examples)

Set up your OpenAI API access for enhanced exploration:

```powershell
# Create environment file for API credentials
ni .env -ItemType File -Force | Out-Null
```

Edit `.env` and add your API key:

```text
OPENAI_API_KEY=sk-your-api-key-here
```

**Important**: Keep your API key secure and never commit it to version control.

### 3. Verify Your Setup

Test your environment with our discovery verification script:

```powershell
# Run the setup verification
python src/day1/basic_concepts.py

# Expected output: Environment verification and basic AI concepts
```

## Daily Discovery Workflow

### Morning Exploration (15-20 minutes)

1. **Activate Environment**: Start each session with environment activation

   ```powershell
   cd learn-generative-ai
   .\.venv\Scripts\Activate.ps1
   ```

2. **Review Learning Path**: Check your current position in the 45-day journey

   ```powershell
   # View today's focus
   type docs\learning-path-90-days.md | Select-String "Day X"
   ```

3. **Execute Today's Code**: Run the day's exploration script

   ```powershell
   python src\dayX\exploration_script.py
   ```

### Interactive Discovery (Optional 10-15 minutes)

Enhance understanding with Jupyter notebooks:

```powershell
# Launch interactive environment
jupyter notebook notebooks\dayX\

# Or use VS Code with Jupyter extension
code notebooks\dayX\discovery_notebook.ipynb
```

### Evening Reflection (5 minutes)

Document your insights and questions for tomorrow's exploration.

## GPU Considerations

Our discovery workspace is optimized for CPU-only learning:

- **No GPU Required**: All examples run efficiently on standard hardware
- **Cloud-Based Models**: Advanced examples use API calls rather than local model hosting
- **Performance Focus**: Learning-optimized rather than production-optimized implementations

### CPU Optimization Tips

If you encounter performance issues:

```powershell
# Install CPU-optimized PyTorch (if needed)
pip install --upgrade --index-url https://download.pytorch.org/whl/cpu torch

# Force CPU usage for current session
$env:CUDA_VISIBLE_DEVICES = "-1"
```

## Interactive Learning Tools

### GitHub Copilot Integration

Our workspace includes enhanced Copilot configurations:

```powershell
# Explore custom prompt templates
Get-ChildItem .github\prompts\ -Name

# Example: Use code explanation prompts
# See .github\prompts\code-explanation.md for guidance
```

### Jupyter Notebook Exploration

Launch interactive discovery sessions:

```powershell
# Start Jupyter for hands-on experimentation
jupyter notebook

# Navigate to: notebooks/day1/01_generative_ai_foundations.ipynb
```

### VS Code Integration

Optimize your development experience:

```powershell
# Open workspace in VS Code with proper configuration
code .

# Our .copilot/settings.json provides enhanced AI assistance
```

## Create Your Own Discovery Repository

Share your learning journey with the community:

### 1. Fork and Customize

```powershell
# Create your own repository on GitHub
# Then clone your fork instead of the original

git clone https://github.com/your-username/learn-generative-ai.git
cd learn-generative-ai
```

### 2. Initialize Your Learning Journal

```powershell
# Create your personal learning log
ni LEARNING_JOURNAL.md -ItemType File -Force | Out-Null

# Track your daily discoveries
git add LEARNING_JOURNAL.md
git commit -m "Start my 45-day AI discovery journey"
git push origin main
```

### 3. Recommended .gitignore

Add protection for sensitive files:

```gitignore
# Python environment
.venv/
__pycache__/
*.pyc

# Jupyter checkpoints
.ipynb_checkpoints/

# Environment variables
.env
.streamlit/secrets.toml

# Model caches
.cache/
.hf_cache/
models/

# Personal notes (optional)
PRIVATE_NOTES.md
```

## Troubleshooting Your Discovery Environment

### Common Setup Issues

**PowerShell Execution Policy Error**:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**Package Installation Issues**:

```powershell
# Clear pip cache
pip cache purge

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

**Python Version Conflicts**:

```powershell
# Check your Python version
python --version

# Should show Python 3.12.5 or compatible
```

### Learning-Specific Troubleshooting

**API Rate Limiting**:

- Start with CPU-only examples
- Gradually introduce API-dependent features
- Use the free tier responsibly

**Concept Confusion**:

- Revisit prerequisite concepts in docs/concepts/
- Use GitHub Copilot with our custom prompts
- Reference the learning path for concept connections

**Environment Deactivation**:

```powershell
# When finished with your session
deactivate
```

## Daily Learning Milestones

Track your progress through these verification checkpoints:

- **Day 1**: Environment setup and basic AI concepts
- **Day 5**: First successful API integration
- **Day 10**: Understanding tokenization mechanics
- **Day 15**: Building semantic similarity systems
- **Day 30**: Creating functional embedding applications
- **Day 45**: Deploying a complete AI agent

## Ready to Begin?

Your systematic AI discovery journey starts now:

1. **Complete the setup** following this guide
2. **Start Day 1** with [basic concepts](src/day1/basic_concepts.py)
3. **Follow the learning path** in [our 90-day comprehensive curriculum](docs/learning-path-90-days.md)
4. **Engage with the community** by sharing your discoveries

**Welcome to your AI mastery journey!** 🚀

---

*Need help? Check our comprehensive documentation in `docs/` or use GitHub Copilot with our custom prompts in `.github/prompts/`*
