import os
from typing import Dict, Any

def heuristic_descriptions(metadata: Dict[str, Any]) -> Dict[str, str]:
    """Simple fallback to produce descriptions without an LLM."""
    descriptions = {}
    pii_keywords = ["email", "name", "phone", "dob", "ssn", "id"]
    for col in metadata["columns"]:
        name = col["name"].lower()
        if any(k in name for k in pii_keywords):
            pii = "Contains PII (likely)"
        else:
            pii = "No obvious PII"
        desc = f"{col['name']} ({col['dtype']}): {pii}. Sample: {col['sample_values'][:3]}"
        descriptions[col["name"]] = desc
    return descriptions

def generate_descriptions(metadata: Dict[str, Any], model_path: str = None) -> Dict[str, str]:
    """
    If a local GPT4All model path is provided and available, use it.
    Otherwise fall back to a deterministic heuristic (so repo demo works without models).
    """
    if model_path and os.path.exists(model_path):
        try:
            from gpt4all import GPT4All
            model = GPT4All(model_path)
            res = {}
            for col in metadata["columns"]:
                prompt = (
                    f"Column name: {col['name']}\n"
                    f"Data type: {col['dtype']}\n"
                    f"Sample values: {col['sample_values'][:5]}\n\n"
                    "Provide a one-sentence business-friendly description and state if it contains PII (Yes/No)."
                )
                # generate returns a string; adjust if API differs
                out = model.generate(prompt, max_tokens=60)
                res[col["name"]] = out.strip()
            return res
        except Exception as e:
            print("Local model failed to load; falling back to heuristic.", e)
            return heuristic_descriptions(metadata)
    else:
        return heuristic_descriptions(metadata)

