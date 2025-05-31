import json
import yaml
from pathlib import Path

def parse_file(filepath):
    ext = Path(filepath).suffix.lower()
    with open(filepath, 'r') as f:
        content = f.read()
    
    if ext in ('.yml', '.yaml'):
        return yaml.safe_load(content) or {}
    elif ext == '.json':
        return json.loads(content) or {}
    
    raise ValueError(f"Unsupported file format: {ext}")