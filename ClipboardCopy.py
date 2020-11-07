
# Method 1- using pyperclip module
# pip install pyperclip
# pip3 install pyperclip

import pyperclip
pyperclip.copy('data from clipboard.')
print(pyperclip.paste())

# Method 12- using pandas module
# pip install pandas
# pip3 install pandas

import pandas as pd
df = pd.DataFrame(['data from clipboard using pandas'])
df.to_clipboard()
print(pd.read_clipboard())
