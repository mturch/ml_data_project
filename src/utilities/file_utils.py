"""
File utility functions for handling various file operations.
"""

import os
import json
import pickle
import yaml
from pathlib import Path
from typing import Any, Dict, List, Union


def ensure_dir(directory: Union[str, Path]) -> Path:
    """
    Ensure directory exists, create if it doesn't.
    
    Args:
        directory: Directory path
        
    Returns:
        Path: Directory path as Path object
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_json(data: Any, filepath: Union[str, Path]) -> None:
    """
    Save data to JSON file.
    
    Args:
        data: Data to save
        filepath: Output file path
    """
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def load_json(filepath: Union[str, Path]) -> Any:
    """
    Load data from JSON file.
    
    Args:
        filepath: Input file path
        
    Returns:
        Any: Loaded data
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def save_yaml(data: Any, filepath: Union[str, Path]) -> None:
    """
    Save data to YAML file.
    
    Args:
        data: Data to save
        filepath: Output file path
    """
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def load_yaml(filepath: Union[str, Path]) -> Any:
    """
    Load data from YAML file.
    
    Args:
        filepath: Input file path
        
    Returns:
        Any: Loaded data
    """
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def save_pickle(data: Any, filepath: Union[str, Path]) -> None:
    """
    Save data to pickle file.
    
    Args:
        data: Data to save
        filepath: Output file path
    """
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)


def load_pickle(filepath: Union[str, Path]) -> Any:
    """
    Load data from pickle file.
    
    Args:
        filepath: Input file path
        
    Returns:
        Any: Loaded data
    """
    with open(filepath, 'rb') as f:
        return pickle.load(f)


def get_file_size(filepath: Union[str, Path]) -> int:
    """
    Get file size in bytes.
    
    Args:
        filepath: File path
        
    Returns:
        int: File size in bytes
    """
    return os.path.getsize(filepath)


def list_files(directory: Union[str, Path], pattern: str = "*") -> List[Path]:
    """
    List files in directory matching pattern.
    
    Args:
        directory: Directory to search
        pattern: File pattern (e.g., "*.csv", "*.json")
        
    Returns:
        List[Path]: List of matching file paths
    """
    path = Path(directory)
    return list(path.glob(pattern))