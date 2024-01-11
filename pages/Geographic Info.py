import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster

def load_data():
    df = pd.read_csv('migrants.csv')
    return df

st.title('Geographic Information')
st.subheader('Map of where the incidents occured')

df = load_data()
# Assume your dataset has a column 'Coordinates' with values like "Lat, Lon"
df[['Lat', 'Lon']] = df['Coordinates'].str.split(',', expand=True)
df[['Lat', 'Lon']] = df[['Lat', 'Lon']].astype(float)

# Drop rows with NaN values in 'Lat' or 'Lon'
df = df.dropna(subset=['Lat', 'Lon'])

# Create an interactive map centered around the mean latitude and longitude
mymap = folium.Map(location=[df['Lat'].mean(), df['Lon'].mean()], zoom_start=3)

# Use MarkerCluster for better performance with a large number of markers
marker_cluster = MarkerCluster().add_to(mymap)

# Add markers for each missing migrant incident
for index, row in df.iterrows():
    folium.Marker([row['Lat'], row['Lon']], popup=row['Location of death']).add_to(marker_cluster)

# Save the map to an HTML file
map_html = 'map.html'
mymap.save(map_html)

# Display the HTML file in Streamlit
st.components.v1.html(open(map_html, 'r').read(), width=1000, height=800, scrolling=True)

st.divider()


