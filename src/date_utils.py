month_name_map = \
    {1: "January",
     2: "February",
     3: "March",
     4: "April",
     5: "May",
     6: "June",
     7: "July",
     8: "August",
     9: "September",
     10: "October",
     11: "November",
     12: "December"}

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

def days_in_month(year, month):
    number_of_days = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31, 
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11:30,
                      12: 31}
    if is_leap_year(year):
        number_of_days[2] = 29
    
    return number_of_days[month]

def create_month_block(year, month):
    number_of_days = days_in_month(year, month)
    first_day = day_of_week(year, month, 1)

    month_block = [[None for _ in range(7)] for _ in range(6)]

    row = 0
    for day_offset, day in enumerate(range(1, number_of_days + 1)):
        weekday = (first_day + day_offset) % 7
        month_block[row][weekday] = day
        
        if weekday == 6:
            row += 1

    return month_block
