# Jupyter Book — C-S-H Manual

## Publish via GitHub Actions
1) Upload all files at the **repo root**.
2) Settings → Pages → Source = **GitHub Actions**.
3) Push to main; Actions builds and publishes to `gh-pages`.

## Local build (optional)
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter-book build .
open _build/html/index.html
