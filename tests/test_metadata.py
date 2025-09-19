import tempfile
import os
from src.metadata_extractor import extract_metadata

def test_extract_basic_csv():
    csv = "id,name\n1,A\n2,B\n"
    fd, path = tempfile.mkstemp(suffix=".csv")
    with open(path, "w") as f:
        f.write(csv)
    meta = extract_metadata(path)
    assert meta["row_count"] == 2
    assert any(c["name"] == "id" for c in meta["columns"])
    os.remove(path)

