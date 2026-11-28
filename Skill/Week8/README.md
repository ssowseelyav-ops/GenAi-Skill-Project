# WEEK 8 – Generative AI Programming Practical

## Aim
Implement Scaled Dot-Product Attention and Multi-Head Attention from scratch using PyTorch.

## Files
- `main.py` – implements scaled dot-product attention, optional causal masking, and a multi-head attention module.
- `requirements.txt` – contains the PyTorch dependency.
- `.gitignore` – excludes virtual environments and Python cache files.

## Run in VS Code (Windows PowerShell)

This project can use the shared virtual environment in the main `GenAI` folder.

1. Open the `GenAI` folder in VS Code, or open a terminal in `GenAI\LAB\Week8`.
2. If the terminal is inside `GenAI\LAB\Week8`, activate the shared environment:
   ```powershell
   ..\..\.venv\Scripts\Activate.ps1
   ```
3. Install the dependency:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Run the program:
   ```powershell
   python main.py
   ```

If you are running from the main `GenAI` folder instead, use:
```powershell
python -m pip install -r LAB/Week8/requirements.txt
python LAB/Week8/main.py
```

## Expected output
The program prints:
- Query, Key and Value tensor shapes: `(1, 3, 4)`
- Scaled dot-product attention weights and output
- Multi-head attention input shape: `(1, 3, 8)`
- Number of attention heads: `2`
- Attention weights shape: `(1, 2, 3, 3)`
- Multi-head attention output shape: `(1, 3, 8)`

Tensor values are randomly initialized, so the numerical values will differ on each run. The tensor shapes should match the practical's expected output.

## Concepts demonstrated
1. Query-Key dot products.
2. Scaling by the square root of the key dimension.
3. Softmax attention weights.
4. Weighted sum of Value vectors.
5. Causal masking to prevent attention to future positions.
6. Splitting and combining multiple attention heads.
