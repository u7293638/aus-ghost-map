"""
This program takes in a csv file and extracts the 
coordinates from the first hit on the placenames in 
that row when searched on TLC Map.org. It then adds 
two new columns to the csv file with the extracted 
longitude and latitude.
"""
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
        print("GET query error")
        return []
    #coord_data = json.loads(urlopen(url).read().decode('utf-8'))
    if coord_data['features'] == []:
        print("Features empty")
        return []
    else:
        try:
            latitude = coord_data['features'][0]['properties']['latitude']
            longitude = coord_data['features'][0]['properties']['longitude']
            return [latitude, longitude]
        except:
            print("No longitude/latitude field")
            return []

# iterate through rows
for index, row in df.iterrows():
    # isolate placenames column
    placenames = df.iloc[index]['placenames']
    # if the placenames column is empty, go to next row
    if placenames == "Empty" or pd.isnull(placenames) or placenames == "" or placenames == "None":
        print(str(index) + "empty")
        counter += 1
        latitudes.append('Empty')
        longitudes.append('Empty')
    else:
        # split the placenames column into a list
        # placenames_list = re.split(', ', placenames)
        # iterate through places
        #for place in placenames_list:
        if placenames != "":
            url = "http://ghap.tlcmap.org/places?fuzzyname=" + placenames + "&format=json"
            print(str(index) + url)
            #print(str(df.iloc[index]['line_num']) + ': ' + url)
            coords = get_coords(url)
            if coords == []:
                continue
            else:
                counter +=1
                latitudes.append(coords[0])
                longitudes.append(coords[1])
                print(coords)
                # break
    # if loop iterates through all places and finds no coordinates
    if len(latitudes) == index:
        counter += 1
        latitudes.append('Empty')
        longitudes.append('Empty')
        print("Empty", "Empty")

coords_d = d = {'latitude': latitudes, 'longitude': longitudes}
coords_df = pd.DataFrame(data=coords_d)
final_df = pd.concat([df, coords_df], axis=1)
final_df.to_csv(filename + '_w_coords.csv', index=False)

        

