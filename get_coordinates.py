import pandas as pd
import re
import json
import requests
from urllib.request import urlopen

filename = input("filename: ")
df = pd.read_csv(filename + '.csv')

latitudes = []
longitudes = []
counter = 0
      

def get_coords(url):
    
    try:
        coord_data = requests.get(url).json()
    except:
        print("JSON Decode Error")
        return ['Empty','Empty']
    #coord_data = json.loads(urlopen(url).read().decode('utf-8'))
    if coord_data['features'] == []:
        return ['Empty','Empty']
    else:
        latitude = coord_data['features'][0]['properties']['latitude']
        longitude = coord_data['features'][0]['properties']['longitude']
        print(latitude + ', ' + longitude)
        return [latitude, longitude]

for index, row in df.iterrows():
    placenames = df.iloc[index]['placenames']
    if placenames != "Empty" and not pd.isnull(placenames) and placenames != "" and placenames != "None":
        for placename in re.split(', ', placenames):
            if placename != "Empty" and placename != "" and placename != "None":
                url = "http://tlcmap.org/ghap/search?fuzzyname=" + placename + "&format=json"
                print(str(df.iloc[index]['line_num']) + ': ' + url)
                coords = get_coords(url)
                if coords == []:
                    continue
                else:

                    latitudes.append(coords[0])
                    longitudes.append(coords[1])
                    break

coords_d = d = {'latitude': latitudes, 'longitude': longitudes}
coords_df = pd.DataFrame(data=coords_d)
final_df = pd.concat([df, coords_df], axis=1)
final_df.to_csv(filename + '_w_coords.csv', index=False)

        

