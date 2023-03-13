import pandas as pd
import folium

# Load the dataset into a pandas dataframe
df = pd.read_csv('your_dataset.csv')

# Define the boroughs and their colors
boroughs = {
    'MANHATTAN': 'red',
    'BROOKLYN': 'blue',
    'QUEENS': 'green',
    'BRONX': 'orange',
    'STATEN ISLAND': 'purple'
}

# Create a map object centered on NYC
map = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

# Add a layer with the borough boundaries
folium.GeoJson(
    'https://data.cityofnewyork.us/api/geospatial/tqmj-j8zm?method=export&format=GeoJSON',
    name='boroughs'
).add_to(map)

# Add a marker for each collision using the borough and latitude and longitude columns
for index, row in df.iterrows():
    if pd.isna(row['LATITUDE']) or pd.isna(row['LONGITUDE']) or pd.isna(row['BOROUGH']):
        continue
    borough = row['BOROUGH'].upper()
    if borough not in boroughs:
        continue
    popup_text = f"Date: {row['CRASH DATE']}<br>Time: {row['CRASH TIME']}<br>Location: {row['LOCATION']}"
    marker = folium.Marker(
        [row['LATITUDE'], row['LONGITUDE']],
        popup=popup_text,
        icon=folium.Icon(color=boroughs[borough])
    )
    marker.add_to(map)

# Add a layer control to toggle the borough boundaries on and off
folium.LayerControl().add_to(map)

# Save the map as an HTML file and open it in your web browser
map.save('collision_map.html')
