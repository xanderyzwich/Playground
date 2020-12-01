"""
How Many Days Between Two Dates
Create a function that takes two dates and returns the number of days between the first and second date.
Examples
"""
from unittest import TestCase
from datetime import date
import re
import calendar

# https://stackoverflow.com/questions/3418050/month-name-to-month-number-and-vice-versa-in-python
months = {v: k for k, v in enumerate(calendar.month_name)}


def format_date(input_string):
    month, day, year = re.split(r'[^A-Za-z0-9]+', input_string)
    elements = int(year), months[month], int(day)
    return date(*elements)


def get_days(first, second):
    one, two = format_date(first), format_date(second)
    return int((two - one).days)


class TestGetDays(TestCase):

    def test_one(self):
        assert get_days("June 14, 2019", "June 20, 2019") == 6

    def test_two(self):
        assert get_days("December 29, 2018", "January 1, 2019") == 3

    def test_three(self):
        assert get_days("July 20, 2019", "July 30, 2019") == 10


