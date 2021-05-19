import pytest

from src.date_utils import is_leap_year


@pytest.mark.parametrize("year, is_leap", [(1700, False), (1800, False), (1600, True), (2000, True)])
def test_is_leap_year(year, is_leap):


    leap_year = is_leap_year(year)

    assert leap_year == is_leap

