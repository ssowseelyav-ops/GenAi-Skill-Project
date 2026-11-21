# WEEK4 — Tokenizer Lab

## Comparison of BPE, WordPiece and SentencePiece Tokenizers
**Languages:** English, Telugu and Hindi

### Aim
Implement and compare three pretrained subword tokenizers—BPE, WordPiece and SentencePiece—and observe how each tokenizer splits text and how many tokens are produced.

### Tokenizers used
| Approach | Pretrained model |
|---|---|
| BPE (Byte Pair Encoding) | `gpt2` |
| WordPiece | `bert-base-multilingual-cased` |
| SentencePiece | `xlm-roberta-base` |

**Comparison note:** These are real pretrained tokenizers, not three algorithms trained on the same dataset with the same vocabulary size. Token-count differences reflect both tokenizer method and each model's vocabulary and training data. XLM-R uses SentencePiece with a BPE model; SentencePiece is a framework, not one single algorithm.

### Files
```text
WEEK4/
├── requirements.txt
├── tokenizer_comparison.py
├── README.md
└── .gitignore
```

### Requirements
- Python 3.10 or later
- Visual Studio Code
- An active virtual environment
- Internet access on the first run to download pretrained tokenizer files

### Setup
Open a terminal in the `WEEK4` folder. Activate your existing virtual environment. If it is in the parent LAB folder and the terminal is currently in WEEK4, use:

```powershell
..\.MyEnv\Scripts\Activate.ps1
```

If your environment is stored elsewhere, use its actual path.

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Execute

```powershell
python tokenizer_comparison.py
```

The program loads the three pretrained tokenizers and compares the same English, Telugu and Hindi sentences. For each language and tokenizer, it prints token pieces, token IDs and token count.

The first run needs internet access to download pretrained tokenizer files. Exact token pieces, IDs and counts depend on the tokenizer files; run the program to obtain actual output.

### Viva / practice questions
1. What is tokenization, and why do language models need it?
2. What is the difference between a word and a subword token?
3. Explain the basic idea of Byte Pair Encoding (BPE).
4. How does WordPiece split an unknown or rare word?
5. What is SentencePiece? Does SentencePiece always mean the Unigram algorithm?
6. Why might GPT-2 split Telugu or Hindi text into more tokens than a multilingual tokenizer?
7. Does a lower token count always mean that a tokenizer is better? Give a reason.
8. What are token IDs, and where are they used?
9. Why should we compare tokenizers using the same input sentences?
10. What is the difference between token count and the number of characters in a sentence?
