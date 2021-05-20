import dominate
from dominate.tags import *

from src.date_utils import create_month_block
from src.html_utils import create_html_month_block


if __name__ == "__main__":

    base_year = 1995
    
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

    output_file = "test.html"
    with open(output_file, "w") as f:
        f.write(str(doc))
