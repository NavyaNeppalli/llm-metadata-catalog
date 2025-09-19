# 🗂️ LLM-Powered Metadata Catalog

This project extracts metadata from CSV/Parquet files and uses a local LLM (GPT4All) to generate human-readable descriptions of dataset columns.

## Features
- Extracts column names, data types, row counts
- Uses GPT4All to generate semantic column descriptions
- Saves results as JSON for easy catalog integration

## Tech Stack
- Python (pandas, langchain, gpt4all)
- Local LLM
- GitHub for version control

## Run Locally
```bash
git clone https://github.com/<your-username>/llm-metadata-catalog.git
cd llm-metadata-catalog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py

