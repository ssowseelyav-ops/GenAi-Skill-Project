# WEEK5 — Token Economics

## Cost and Rate-Limit Budgeting Before Building an LLM Feature

### Aim
Build a reusable Python budget planner that estimates input/output token consumption, daily and monthly hosted API cost, checks expected traffic against configured RPM/TPM limits, applies a safety margin, and gives a planning recommendation.

### Concepts
- **Input tokens:** system instructions, user prompt, conversation history, retrieved context and tool descriptions sent to the model.
- **Output tokens:** tokens generated in the response.
- **Total tokens:** input tokens plus output tokens.
- **RPM:** requests per minute.
- **TPM:** tokens per minute.
- **Safety margin:** reserved capacity for spikes, estimation error, retries and other workloads.

### Files
```text
WEEK5/
├── budget.py
├── test_budget.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Setup in VS Code
Open the `WEEK5` folder in VS Code and open **Terminal → New Terminal**.

Create a virtual environment if you do not already have one:
```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependency:
```powershell
python -m pip install -r requirements.txt
```

Create your local configuration file by copying the example:
```powershell
Copy-Item .env.example .env
```

The `.env.example` contains the illustrative assumptions from the practical. You can edit `.env` for your what-if scenarios. The `.env` file is excluded from Git by `.gitignore`.

### Run the budget planner
```powershell
python budget.py
```

### Run the automated tests
```powershell
python -m unittest -v test_budget.py
```

The tests check the cost calculation, passing capacity checks, RPM failure and monthly-budget failure. They do not call an LLM API.

### Sample assumptions and expected planning figures
The practical's illustrative assumptions are:
- 2,000 requests/day
- 1,200 average input tokens/request
- 300 average output tokens/request
- 30 peak requests/minute
- $0.30 per million input tokens
- $1.20 per million output tokens
- RPM limit 60; TPM limit 100,000
- Daily budget $2; monthly budget $50
- Safety margin 20%

Expected results with these values:
| Metric | Expected value |
|---|---:|
| Input tokens/day | 2,400,000 |
| Output tokens/day | 600,000 |
| Total tokens/day | 3,000,000 |
| Estimated daily cost | $1.4400 |
| Estimated monthly cost (30 days) | $43.20 |
| Peak RPM with 20% margin | 36 |
| Peak total TPM with 20% margin | 54,000 |

The example should report PASS for RPM capacity, TPM capacity, daily budget and monthly budget, and recommend that the feature is within the configured planning limits.

### What-if analysis
Change one assumption at a time in `.env`, then run `python budget.py` again:
1. Double `REQUESTS_PER_DAY` and compare daily/monthly cost.
2. Increase `PEAK_REQUESTS_PER_MINUTE` until an RPM or TPM check fails.
3. Increase `AVG_INPUT_TOKENS` to model a larger retrieved context.
4. Reduce `AVG_OUTPUT_TOKENS` and explain the effect on cost.
5. Increase token prices and observe the cost change.

### Important notes
- Prices and provider limits in the practical are illustrative. Verify the current price and quota for the exact model, account and service tier before using the estimate for a real feature.
- The lab uses total TPM as a simplified planning check. Providers may enforce separate input/output limits or other quota dimensions.
- A cost estimate is not a billing guarantee. Retries can increase actual usage and cost.
- `.env` contains local planning values and must not be uploaded. Do not add API keys or other secrets to a public repository.
