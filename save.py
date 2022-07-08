from get_info import get
import pandas as pd

df = pd.DataFrame.from_dict(get(user_list))
df.to_csv('save.csv')