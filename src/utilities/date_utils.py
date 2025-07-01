"""
Date and time utility functions.
"""

from datetime import datetime, timedelta, date
from typing import Optional, Union, List
import pandas as pd


def today() -> date:
    """
    Get today's date.
    
    Returns:
        date: Today's date
    """
    return date.today()


def now() -> datetime:
    """
    Get current datetime.
    
    Returns:
        datetime: Current datetime
    """
    return datetime.now()


def format_date(dt: Union[date, datetime], fmt: str = "%Y-%m-%d") -> str:
    """
    Format date/datetime as string.
    
    Args:
        dt: Date or datetime to format
        fmt: Format string
        
    Returns:
        str: Formatted date string
    """
    return dt.strftime(fmt)


def parse_date(date_str: str, fmt: str = "%Y-%m-%d") -> date:
    """
    Parse date string to date object.
    
    Args:
        date_str: Date string to parse
        fmt: Format string
        
    Returns:
        date: Parsed date
    """
    return datetime.strptime(date_str, fmt).date()


def parse_datetime(datetime_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parse datetime string to datetime object.
    
    Args:
        datetime_str: Datetime string to parse
        fmt: Format string
        
    Returns:
        datetime: Parsed datetime
    """
    return datetime.strptime(datetime_str, fmt)


def days_ago(days: int) -> date:
    """
    Get date N days ago.
    
    Args:
        days: Number of days ago
        
    Returns:
        date: Date N days ago
    """
    return today() - timedelta(days=days)


def days_from_now(days: int) -> date:
    """
    Get date N days from now.
    
    Args:
        days: Number of days from now
        
    Returns:
        date: Date N days from now
    """
    return today() + timedelta(days=days)


def date_range(start_date: Union[str, date], end_date: Union[str, date], 
               freq: str = 'D') -> List[date]:
    """
    Generate date range between two dates.
    
    Args:
        start_date: Start date
        end_date: End date
        freq: Frequency ('D' for daily, 'W' for weekly, 'M' for monthly)
        
    Returns:
        List[date]: List of dates in range
    """
    if isinstance(start_date, str):
        start_date = parse_date(start_date)
    if isinstance(end_date, str):
        end_date = parse_date(end_date)
    
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    return [d.date() for d in dates]


def quarter_start(dt: Union[date, datetime]) -> date:
    """
    Get start of quarter for given date.
    
    Args:
        dt: Input date
        
    Returns:
        date: Start of quarter
    """
    if isinstance(dt, datetime):
        dt = dt.date()
    
    quarter = (dt.month - 1) // 3 + 1
    month = (quarter - 1) * 3 + 1
    return date(dt.year, month, 1)


def quarter_end(dt: Union[date, datetime]) -> date:
    """
    Get end of quarter for given date.
    
    Args:
        dt: Input date
        
    Returns:
        date: End of quarter
    """
    start = quarter_start(dt)
    # Move to next quarter start, then subtract one day
    next_quarter = start + timedelta(days=93)  # Approximately 3 months
    next_quarter_start = quarter_start(next_quarter)
    return next_quarter_start - timedelta(days=1)


def business_days_between(start_date: Union[str, date], 
                         end_date: Union[str, date]) -> int:
    """
    Calculate number of business days between two dates.
    
    Args:
        start_date: Start date
        end_date: End date
        
    Returns:
        int: Number of business days
    """
    if isinstance(start_date, str):
        start_date = parse_date(start_date)
    if isinstance(end_date, str):
        end_date = parse_date(end_date)
    
    return pd.bdate_range(start=start_date, end=end_date).size