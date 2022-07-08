import pandas as pd
from get_info import get

past ={x[1]:x[2] for x in pd.read_csv('save.csv').values.tolist()}
now = {x[0]:x[1] for x in pd.DataFrame.from_dict(get()).values.tolist()}

for user in now:
    if now[user]==past[user]:
        print(user)