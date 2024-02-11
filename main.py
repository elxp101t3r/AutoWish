import datetime as dt
import pandas as pd
from random import choice

templates = ['template1.txt', 'template2.txt', 'template3.txt']
data = pd.read_csv('birthdays.csv', index_col=False)

now = dt.datetime.now()

todays_birthdays = data[(data['year'] == now.year) & (data['month'] == now.month) & (data['day'] == now.day)]

today_name = todays_birthdays['name'].values[0]

r_choice = choice(templates)


with open(f'./templates/{r_choice}', 'r') as f:
        txt_tmp = f.readlines()

for i in range(len(txt_tmp)):
    if '[Name]' in txt_tmp[i]:
            txt_tmp[i] = today_name
    elif '[Your Name]' in txt_tmp[i]:
            txt_tmp[i] = 'Kostas'

print(''.join(txt_tmp))
