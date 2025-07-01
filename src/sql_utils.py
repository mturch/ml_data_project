"""
SQL utility functions for database connections and query execution.
"""

import pandas as pd
from sqlalchemy import create_engine, text
from typing import Optional, Dict, Any
import os


class DatabaseConnection:
    """Handle database connections and query execution."""
    
    def __init__(self, connection_string: str):
        """
        Initialize database connection.
        
        Args:
            connection_string (str): SQLAlchemy connection string
        """
        self.engine = create_engine(connection_string)
    
    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """
        Execute SQL query and return results as DataFrame.
        
        Args:
            query (str): SQL query to execute
            params (dict, optional): Query parameters
            
        Returns:
            pd.DataFrame: Query results
        """
        with self.engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            return pd.DataFrame(result.fetchall(), columns=result.keys())
    
    def execute_file(self, filepath: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        """
        Execute SQL query from file.
        
        Args:
            filepath (str): Path to SQL file
            params (dict, optional): Query parameters
            
        Returns:
            pd.DataFrame: Query results
        """
        with open(filepath, 'r') as f:
            query = f.read()
        return self.execute_query(query, params)
    
    def to_sql(self, df: pd.DataFrame, table_name: str, if_exists: str = 'replace') -> None:
        """
        Write DataFrame to SQL table.
        
        Args:
            df (pd.DataFrame): DataFrame to write
            table_name (str): Target table name
            if_exists (str): What to do if table exists ('replace', 'append', 'fail')
        """
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)


def get_connection_from_env() -> DatabaseConnection:
    """
    Create database connection from environment variables.
    
    Returns:
        DatabaseConnection: Configured database connection
    """
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        raise ValueError("DATABASE_URL environment variable not set")
    
    return DatabaseConnection(db_url)


def load_sql_file(filepath: str) -> str:
    """
    Load SQL query from file.
    
    Args:
        filepath (str): Path to SQL file
        
    Returns:
        str: SQL query content
    """
    with open(filepath, 'r') as f:
        return f.read()