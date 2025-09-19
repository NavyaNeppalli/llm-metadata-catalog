import argparse
import json
import os
from src.metadata_extractor import extract_metadata
from src.llm_generator import generate_descriptions

def main():
    parser = argparse.ArgumentParser(description="Generate metadata + LLM descriptions")
    parser.add_argument("--input", required=True, help="Path to CSV or parquet file (data/...)")
    parser.add_argument("--model", required=False, help="Path to local GPT4All model (optional)")
    parser.add_argument("--output", default="outputs/metadata.json", help="Output JSON path")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    metadata = extract_metadata(args.input)
    descriptions = generate_descriptions(metadata, model_path=args.model)

    output = {"metadata": metadata, "descriptions": descriptions}
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Wrote output to {args.output}")

if __name__ == "__main__":
    main()

