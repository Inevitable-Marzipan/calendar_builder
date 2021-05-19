def is_leap_year(year):
    
    return ((year % 4) == 0) and \
            (((year % 100) != 0) or \
              (year % 400 == 0))


def day_of_week(year, month, day):
    """
    Follows ISO 8601 in that 
    Sunday = 0
    Monday = 1
    ...
    """

    if is_leap_year(year):
        offsets = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    else:
        offsets = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    months = [x for x in range(1, 13)]
    month_offset = dict(zip(months, offsets))
    
    m = month_offset[month]
    return (day + 
            m + 
            5 * ((year - 1) % 4) +
            4 * ((year -1) % 100) +
            6 * ((year -1) % 400)) % 7