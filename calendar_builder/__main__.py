import sys
import argparse

import dominate
from dominate.tags import *

from .date_utils import create_month_block
from .html_utils import create_html_month_block


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, dest="year", default=2021)
    parser.add_argument("--output_file", type=str, dest="output_file", default="calendar.html")

    parsed_args = parser.parse_args(args)
    base_year = parsed_args.year
    output_file = parsed_args.output_file
    
    doc = dominate.document(title=f'Year {base_year} +-1 calendar')

    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        for year in [base_year -1, base_year, base_year + 1]:
            h1(f'{year}', cls='year')
            with div(cls='grid') as year_div:
                for month in range(1, 13):
                    month_block = create_month_block(year, month)
                    html_month_block = create_html_month_block(month, month_block)
                    year_div.add(html_month_block)

    with open(output_file, "w") as f:
        f.write(str(doc))