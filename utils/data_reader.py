import json
from pathlib import Path

def read_json_file(file_path):
    path  = Path(file_path)
    
    with path.open("r", encoding="utf-8")as f:
        data = json.load(f)
    return data
