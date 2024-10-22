import pandas as pd

nas_list = pd.read_excel('./NL.xlsx')

query = 'AAPL'

yes_twit_cnt = nas_list.at[query, 'Mentions Yesterday']

print(yes_twit_cnt)