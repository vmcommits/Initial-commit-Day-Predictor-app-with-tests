---

## **`day_predictor.py`**
```python
#!/usr/bin/env python3
"""
day_predictor.py
A simple Python app that predicts the day of the week for a given date.
"""

import datetime

def get_day_of_week(day: int, month: int, year: int) -> str:
    """
    Returns the day of the week for the given date.
    """
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A")
    except ValueError as e:
        return f"Invalid date: {e}"

def main():
    print("📅 Day Predictor")
    try:
        day = int(input("Enter day (1-31): "))
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (e.g., 2025): "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return
    
    result = get_day_of_week(day, month, year)
    print(f"The day for {day:02d}-{month:02d}-{year} is: {result}")

if __name__ == "__main__":
    main()
