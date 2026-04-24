# Local LLM Resume Agent (Ollama-Based)

## Overview
This project is a Python-based AI agent that improves resume content using a **local LLM (Large Language Model)** instead of a paid API.

It takes rough work experience text and rewrites it into **professional, structured resume bullet points**.

---

## Features
- Uses a **local LLM (Llama 3.2 via Ollama)**
- Improves resume text into strong professional bullet points
- Maintains **truthful and realistic wording**
- Stores last output using simple memory
- Works entirely offline (after model download)

---

## Why I Built This
After building rule-based agents (Day 1–3), this project introduces:

- Real AI (LLM-based rewriting)
- Prompt engineering
- Local model usage without API cost

This helps bridge the gap between:
**rule-based automation → real AI-powered systems**

---

## Tech Stack
- Python
- Ollama (local LLM runtime)
- Llama 3.2 model (1B)

---

## How It Works
1. User provides input using the `improve:` command
2. The agent:
   - Sends a structured prompt to the local LLM
   - Rewrites the text into professional bullet points
   - Stores the last output in memory
3. Output is returned in structured format

---

## Setup Instructions (IMPORTANT)

### 1. Install Ollama
Download and install from: https://ollama.com

---

### 2. Start Ollama server
Run in terminal:

```bash
ollama serve
```

---

### 3. Download model
Run in terminal:

```bash
ollama pull llama3.2:1b
```

---

### 4. Run the agent
Run in terminal:

```bash
python3 day4_agent.py
```

---

## Usage
Type your resume text after `improve:` to get professional bullet points.

Example:
```
improve: worked on dashboards and helped team with weekly reports
```

Type `last output` to see the previous result.

---

## Common Issues & Fixes

### Issue 1: Python version conflict
If you have multiple Python versions (e.g., Anaconda + system Python):
- `python3` may point to the wrong version
- Some packages may break due to version mismatch

**Fix:** Use the correct Python version explicitly:
```bash
which python3
python3 --version
```
If needed, use full path to working Python (e.g., `/usr/local/bin/python3`).

---

### Issue 2: typing_extensions error
If you see errors related to `typing_extensions`:

**Fix:**
```bash
pip install --upgrade typing_extensions
```

---

### Issue 3: Ollama not responding
If you get connection errors:

**Fix:** Make sure Ollama is running:
```bash
ollama serve
```

---

### Issue 4: Model not found
If you see model-related errors:

**Fix:**
```bash
ollama pull llama3.2:1b
```

---

### Issue 5: Earlier projects worked but this failed
Day 1–3 projects used only built-in Python features.

This project uses:
- External library (ollama)
- Local model server

So additional setup is required.
