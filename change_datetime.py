import datetime
import pandas as pd

filename = 'ghost_australia/final'
df = pd.read_csv(filename + '.csv')
goal_format = "%Y-%m-%dT00:00:00.000Z"
major_format = "%Y-%m-%d"
minor_format = "%Y/%m/%d"
df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'].dt.strftime(goal_format))

df.to_csv('final_datefix.csv')
