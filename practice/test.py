import pandas as pd
data = {'col0': [1, 2, 3], 'col1': [4, 5, 6]}

df = pd.DataFrame(data)

from pretty_html_table import build_table
html_table_blue_light = build_table(df, 'blue_light')

# Save to html file
with open('pretty_table.html', 'w') as f:
    f.write(html_table_blue_light)

# Compare to the pandas .to_html method:
with open('pandas_table.html', 'w') as f:
    f.write(df.to_html())