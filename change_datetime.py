import datetime
import pandas as pd

filename = 'records2_w_placenames_50_w_coords'
df = pd.read_csv(filename + '.csv')
goal_format = "%Y-%m-%dT00:00:00.000Z"
major_format = "%Y-%m-%d"
minor_format = "%Y/%m/%d"
df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'].dt.strftime(goal_format))

df.to_csv('records2_50_datefix.csv')
