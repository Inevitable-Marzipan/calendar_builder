from src.html_utils import create_html_month_block

def test_create_html_month_block():

    month_block = [[None, 1, 2, 3, 4, 5, 6]]
    month = 1

    html_month_block = create_html_month_block(month, month_block)

    expected_html_block = \
"""<table>
  <tr class="header_row">
    <th colspan="7">January</th>
  </tr>
  <tr class="header_row">
    <th>Sun</th>
    <th>Mon</th>
    <th>Tue</th>
    <th>Wed</th>
    <th>Thu</th>
    <th>Fri</th>
    <th>Sat</th>
  </tr>
  <tr>
    <td class="empty">_</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
  </tr>
</table>"""

    assert str(html_month_block) == expected_html_block