import pandas as pd
import grequests
import math  # Import math module to handle NaN values

# Function to retrieve coordinates for a given place name asynchronously
def get_coordinates_async(place_names):
    urls = [f'http://ghap.tlcmap.org/places?fuzzyname={place_name.strip()}&format=json' for place_name in place_names if isinstance(place_name, str)]
    responses = grequests.map((grequests.get(url) for url in urls))
    print(urls)
    coordinates = []
    for response in responses:
        if response and response.status_code == 200:
            try:
                data = response.json()
                if data and 'features' in data and len(data['features']) > 0:
                    coord = data['features'][0]['geometry']['coordinates']
                    coordinates.append((coord[1], coord[0]))  # Latitude, Longitude
                else:
                    coordinates.append((None, None))
            except:
                coordinates.append((None, None))
        else:
            coordinates.append((None, None))
    return coordinates

# Read CSV file
filename = input("Filename: ")
input_file = filename + '.csv'  # Replace 'input.csv' with your input CSV file name
output_file = filename + '_w_coords_gpt.csv'  # Output CSV file to store coordinates

# Read CSV into pandas DataFrame
df = pd.read_csv(input_file)

# Strip leading/trailing spaces and handle NaN values in placenames, then split placenames into a list and get coordinates asynchronously
placenames_list = df['placenames'].str.strip().apply(lambda x: str(x).split(',') if not pd.isna(x) else [])

# Get coordinates for each list of placenames
coordinates = placenames_list.apply(get_coordinates_async)

# Extract the first successful coordinates from the list
df['Latitude'] = [lat for lat, lon in coordinates.apply(lambda x: next(((lat, lon) for lat, lon in x if lat is not None and lon is not None), (None, None)))]

df['Longitude'] = [lon for lat, lon in coordinates.apply(lambda x: next(((lat, lon) for lat, lon in x if lat is not None and lon is not None), (None, None)))]

# Write updated DataFrame to output CSV
df.to_csv(output_file, index=False)

print("Coordinates retrieved and saved to output.csv.")
