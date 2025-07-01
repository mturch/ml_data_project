"""
Configuration utilities for managing project settings.
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional, Union
from .file_utils import load_json, load_yaml


class Config:
    """Configuration manager for the project."""
    
    def __init__(self, config_file: Optional[Union[str, Path]] = None):
        """
        Initialize configuration.
        
        Args:
            config_file: Optional path to configuration file
        """
        self._config = {}
        
        if config_file:
            self.load_from_file(config_file)
        
        # Load from environment variables
        self.load_from_env()
    
    def load_from_file(self, filepath: Union[str, Path]) -> None:
        """
        Load configuration from file.
        
        Args:
            filepath: Configuration file path
        """
        filepath = Path(filepath)
        
        if filepath.suffix.lower() == '.json':
            self._config.update(load_json(filepath))
        elif filepath.suffix.lower() in ['.yml', '.yaml']:
            self._config.update(load_yaml(filepath))
        else:
            raise ValueError(f"Unsupported config file format: {filepath.suffix}")
    
    def load_from_env(self, prefix: str = "ML_") -> None:
        """
        Load configuration from environment variables.
        
        Args:
            prefix: Environment variable prefix
        """
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            default: Default value if key not found
            
        Returns:
            Any: Configuration value
        """
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value.
        
        Args:
            key: Configuration key (supports dot notation)
            value: Configuration value
        """
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Get all configuration as dictionary.
        
        Returns:
            Dict[str, Any]: Configuration dictionary
        """
        return self._config.copy()


# Global configuration instance
config = Config()


def get_database_url() -> str:
    """
    Get database URL from configuration or environment.
    
    Returns:
        str: Database URL
    """
    db_url = config.get('database_url') or os.getenv('DATABASE_URL')
    if not db_url:
        raise ValueError("Database URL not configured")
    return db_url


def get_data_dir() -> Path:
    """
    Get data directory path.
    
    Returns:
        Path: Data directory path
    """
    data_dir = config.get('data_dir', 'data')
    return Path(data_dir)


def get_output_dir() -> Path:
    """
    Get output directory path.
    
    Returns:
        Path: Output directory path
    """
    output_dir = config.get('output_dir', 'output')
    return Path(output_dir)