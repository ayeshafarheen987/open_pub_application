import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
from shapely.geometry import Point
from streamlit_folium import folium_static
from scipy.spatial import distance



import io
import streamlit as st
import os
import pandas as pd
import numpy as np
st.markdown("""
    <style>
        body {
            background-image: url("https://cdn.diffords.com/contrib/stock-images/2014/9/36/20148df56607255750373ef80869c2bad48f.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.3);
        }
    </style>
""", unsafe_allow_html=True)













# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "pub_cleaned.csv")
#st.title(":green[Pub Data Info]")

#st.header(':red[DataFrame]')

df = pd.read_csv(DATA_PATH)
st.header(":blue[ basic information and statistics about the dataset]")
df["geometry"] = df.apply(lambda row: Point(row["longitude"], row["latitude"]), axis=1)


data_info = st.radio('Click to view the Details of the Dataset:',
                      ('Shape', 'Info', 'Descriptive Statistics'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number of Rows:  {df.shape[0]}")
    st.write(f"Number of Columns:  {df.shape[1]}")
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())



# Page Title
st.title("Pub Locations")

# Dropdown Widget to Select Search Type
search_type = st.selectbox("Select Search Type", ["Postal Code", "Local Authority"])

if search_type == "Postal Code":
    unique_postcodes = sorted(df["postcode"].unique())
    search_input = st.selectbox("Select Postal Code", unique_postcodes)

    # Filter DataFrame based on Search Input
    filtered_df = df[df["postcode"] == search_input]
    
elif search_type == "Local Authority":
    # Search Input Widget
    unique_local_authority = sorted(df["local_authority"].unique())
    search_input = st.selectbox("Enter Local Authority:",unique_local_authority)

    # Filter DataFrame based on Search Input
    filtered_df = df[df["local_authority"]==search_input]

# Create GeoDataFrame
geo_filtered_df = gpd.GeoDataFrame(filtered_df, geometry=filtered_df["geometry"])

# Create Map
if not geo_filtered_df.empty:
    pub_map = folium.Map(location=[geo_filtered_df["latitude"].mean(), geo_filtered_df["longitude"].mean()], zoom_start=12)
    marker_cluster = MarkerCluster().add_to(pub_map)

    # Add Markers to Map
    for idx, row in geo_filtered_df.iterrows():
        folium.Marker(location=[row["latitude"], row["longitude"]],
                      tooltip=row["name"],
                      popup=row["address"],
                      icon=None).add_to(marker_cluster)

    # Display Map
    folium_static(pub_map)
else:
    st.warning("No pubs found.")
