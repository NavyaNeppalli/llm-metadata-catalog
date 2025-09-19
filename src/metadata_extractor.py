import pandas as pd
from typing import Dict, Any

def extract_metadata(file_path: str, sample_n: int = 5) -> Dict[str, Any]:
    """
    Read CSV/Parquet and return lightweight metadata:
    - columns: name, dtype, null_count, sample_values (up to sample_n)
    - row_count
    """
    if file_path.endswith(".parquet"):
        df = pd.read_parquet(file_path)
    else:
        df = pd.read_csv(file_path)

    cols = []
    for col in df.columns:
        series = df[col]
        sample_vals = series.dropna().unique()[:sample_n].tolist()
        cols.append({
            "name": col,
            "dtype": str(series.dtype),
            "null_count": int(series.isnull().sum()),
            "sample_values": sample_vals
        })

    return {"row_count": len(df), "columns": cols}

