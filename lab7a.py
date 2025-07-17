#!/usr/bin/env python3
# Student ID: rbhandari17@myseneca.ca

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum, ensuring proper carry over of minutes and seconds."""
    sum = Time(0, 0, 0)
    
    # Add hours, minutes, and seconds separately
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # Handle seconds overflow (if seconds exceed or equal to 60)
    while sum.second >= 60:
        sum.second -= 60  # Subtract 60 seconds
        sum.minute += 1   # Add 1 minute

    # Handle minutes overflow (if minutes exceed or equal to 60)
    while sum.minute >= 60:
        sum.minute -= 60  # Subtract 60 minutes
        sum.hour += 1     # Add 1 hour
    
    return sum  # Return the resulting Time object

def valid_time(t):
    """Check for the validity of the time object attributes:
    24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
python3 ./CheckLab7.py -f -v lab7i
python3 ./CheckLab7.py -f -v lab7i
