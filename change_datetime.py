# This is an attempt to change the format of the date
# in a csv file so it can be read in Carto and 
# transformed into a timeseries
import datetime
import pandas as pd

filename = 'ghost_australia/final'
df = pd.read_csv(filename + '.csv')
goal_format = "%Y-%m-%dT00:00:00.000Z"
major_format = "%Y-%m-%d"
minor_format = "%d/%m/%Y"

df['date'] = pd.to_datetime(df['date'])
for index, row in df.iterrows():

df['date'] = pd.to_datetime(df['date'].dt.strftime(goal_format))

df.to_csv('final_datefix.csv')
