from src.date_utils import month_name_map
from src.date_utils import day_name_map
from dominate.tags import *

def create_html_month_block(month, month_block):
    
    month_table = table()
    with month_table:

        with tr(cls='header_row'):
            th(month_name_map[month], colspan="7")

        with tr(cls='header_row'):
            for day in range(7):
                th(day_name_map[day])
        
        for row in month_block:
            with tr():
                for weekday, day in enumerate(row):
                    if day is None:
                        td("_", cls="empty")
                    else:
                        if (weekday == 0) or (weekday == 6):
                            td(day, cls="weekend")
                        else:
                            td(day, cls="full")

    return month_table