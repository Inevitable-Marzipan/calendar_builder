from src.html_utils2 import create_html_month_block

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
    <th>Sunday</th>
    <th>Monday</th>
    <th>Tuesday</th>
    <th>Wednesday</th>
    <th>Thursday</th>
    <th>Friday</th>
    <th>Saturday</th>
  </tr>
  <tr>
    <td> </td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
  </tr>
</table>"""

    assert str(html_month_block) == expected_html_block