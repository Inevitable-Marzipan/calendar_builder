import pytest

from calendar_builder.date_utils import is_leap_year
from calendar_builder.date_utils import day_of_week
from calendar_builder.date_utils import create_month_block


@pytest.mark.parametrize("year, is_leap", [(1700, False), (1800, False), (1600, True), (2000, True)])
def test_is_leap_year(year, is_leap):

    leap_year = is_leap_year(year)

    assert leap_year == is_leap

@pytest.mark.parametrize("year, month, day, actual_weekday", [(2021, 5, 19, 3), (2000, 1, 1, 6), (1777, 4, 30, 3)])
def test_day_of_week(year, month, day, actual_weekday):

    weekday = day_of_week(year, month, day)

    assert weekday == actual_weekday


def test_month_block_one():
    year = 2021
    month = 1
    month_block = create_month_block(year, month)

    actual_month_block = \
        [[None, None, None, None, None, 1, 2],
         [3, 4, 5, 6, 7, 8, 9],
         [10, 11, 12 , 13, 14, 15, 16],
         [17, 18, 19, 20, 21, 22, 23],
         [24, 25, 26, 27, 28, 29, 30],
         [31, None, None, None, None, None, None]]
    
    assert month_block == actual_month_block

def test_month_block_two():
    year = 2020
    month = 2

    month_block = create_month_block(year, month)

    actual_month_block = \
        [[None, None, None, None, None, None, 1],
         [2, 3, 4, 5, 6, 7, 8],
         [9, 10, 11 , 12, 13, 14, 15],
         [16, 17, 18, 19, 20, 21, 22],
         [23, 24, 25, 26, 27, 28, 29],
         [None, None, None, None, None, None, None]]