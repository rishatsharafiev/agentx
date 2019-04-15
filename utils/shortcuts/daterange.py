from datetime import timedelta
from math import ceil


def daterange(start_date, end_date):
    """Daterange generator"""
    for n in range(ceil((end_date - start_date).seconds / 60)):
        yield start_date + timedelta(minutes=n)
