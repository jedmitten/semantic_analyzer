import csv
import json
import tomli
from typing import Literal, Union
from pathlib import Path

InputType = Literal["words", "texts"]

def read_input_file(file_path: Union[str, Path], required_type: InputType) -> list[str]:
    """
    Read input from a file in CSV, JSON, or TOML format.
    
    Args:
        file_path: Path to the input file
        required_type: Required input type (words/texts)
        
    Returns:
        List of strings from the file
        
    Raises:
        ValueError: If file format is not supported or required type is not found
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Determine file type from extension
    file_type = file_path.suffix.lower()
    
    try:
        if file_type == '.csv':
            return _read_csv(file_path, required_type)
        elif file_type == '.json':
            return _read_json(file_path, required_type)
        elif file_type == '.toml':
            return _read_toml(file_path, required_type)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    except Exception as e:
        raise ValueError(f"Error reading file {file_path}: {str(e)}")

def _read_csv(file_path: Path, required_type: InputType) -> list[str]:
    """Read input from a CSV file"""
    with open(file_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no headers")
        
        if required_type not in reader.fieldnames:
            raise ValueError(f"CSV file must contain a column named '{required_type}'")
        
        values = [row[required_type] for row in reader if row[required_type].strip()]
        return values

def _read_json(file_path: Path, required_type: InputType) -> list[str]:
    """Read input from a JSON file"""
    with open(file_path, 'r') as f:
        data = json.load(f)
        
        if not isinstance(data, dict):
            raise ValueError(f"JSON file must contain an object with a '{required_type}' key")
        
        if required_type not in data:
            raise ValueError(f"JSON file must contain a key named '{required_type}'")
        
        values = data[required_type]
        if not isinstance(values, list):
            raise ValueError(f"JSON value for '{required_type}' must be an array")
        
        return values

def _read_toml(file_path: Path, required_type: InputType) -> list[str]:
    """Read input from a TOML file"""
    with open(file_path, 'rb') as f:
        data = tomli.load(f)
        
        if not isinstance(data, dict):
            raise ValueError(f"TOML file must contain a table with a '{required_type}' key")
        
        if required_type not in data:
            raise ValueError(f"TOML file must contain a key named '{required_type}'")
        
        values = data[required_type]
        if not isinstance(values, list):
            raise ValueError(f"TOML value for '{required_type}' must be an array")
        
        return values 