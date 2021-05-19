import pytest

from src.date_utils import is_leap_year
from src.date_utils import day_of_week


@pytest.mark.parametrize("year, is_leap", [(1700, False), (1800, False), (1600, True), (2000, True)])
def test_is_leap_year(year, is_leap):

    leap_year = is_leap_year(year)

    assert leap_year == is_leap

@pytest.mark.parametrize("year, month, day, actual_weekday", [(2021, 5, 19, 3), (2000, 1, 1, 6), (1777, 4, 30, 3)])
def test_day_of_week(year, month, day, actual_weekday):

    weekday = day_of_week(year, month, day)

    assert weekday == actual_weekday



