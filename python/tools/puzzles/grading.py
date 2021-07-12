"""
Grading Students
HackerLand University has the following grading policy:

    Every student receives a grade in the inclusive range from 0 to 100 .
    Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

    If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
    If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""

from unittest import TestCase


def is_passing(grade):
    return False if grade < 40 else True


def round_grade(grade):
    delta = 5 - grade % 5
    rounded = grade + delta
    roundable = is_passing(rounded) and delta < 3
    print(grade, delta, rounded, roundable)
    return grade + delta if roundable else grade


class TestGrades(TestCase):
    tests = [
        {'arg': 84, 'want': 85},
        {'arg': 29, 'want': 29},
        {'arg': 57, 'want': 57},
        {'arg': 73, 'want': 75},
        {'arg': 67, 'want': 67},
        {'arg': 38, 'want': 40},
        {'arg': 33, 'want': 33}
    ]

    def test_round(self):
        for t in self.tests:
            print(f'Testing {t}')
            assert round_grade(t['arg']) == t['want']
            print('--- PASS ---')
