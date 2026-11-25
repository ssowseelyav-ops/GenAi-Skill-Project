# WEEK 6 — Generative AI Programming Practical

This practical creates a 30-question golden set and runs a first baseline evaluation with the local Ollama `llama3.2` model. Results are saved to `baseline_results.csv` as Release `v0.1`.

## Files
- `golden_set.json`: 30 questions with expected answers, keywords and sources.
- `main.py`: calls Ollama, calculates keyword coverage and writes a CSV report.
- `requirements.txt`: Python dependency.
- `.gitignore`: excludes virtual environments and caches.

## Run in VS Code (Windows PowerShell)

1. Install Ollama and open/run Ollama Desktop.
2. Check Ollama:
   ```powershell
   ollama --version
   ```
3. Download the model:
   ```powershell
   ollama pull llama3.2
   ```
4. From this WEEK6 folder, create and activate an environment if needed:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   If you already use a shared `.venv` in the parent GenAI folder, activate that environment from the parent folder instead.
5. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
6. Run the baseline:
   ```powershell
   python main.py
   ```

Make sure the terminal's current directory is the folder containing `main.py`. Ollama must be running locally. The script sends all 30 questions to `http://localhost:11434/api/generate`, using temperature 0.

## Output
The terminal prints each question, Llama response, expected answer, matched/missing keywords, score and status. Keyword coverage of 60% or more is labelled `PASS`; below 60% is `REVIEW`. Request failures are labelled `ERROR`.

The program creates `baseline_results.csv` in the WEEK6 folder. Open it in VS Code or Excel. It includes the model response, keyword score, status, source and release version.

This is a simple keyword-coverage baseline, not a semantic evaluation. Record actual scores from your run; results depend on the local model response.

## Troubleshooting
- Connection refused: start Ollama Desktop/service and retry.
- Model not found: run `ollama pull llama3.2`.
- `ollama` not recognized: install Ollama and reopen the terminal.
- `golden_set.json` not found: change directory to WEEK6 before running `python main.py`.
