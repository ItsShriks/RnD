import geopandas as gpd
import open3d as o3d
import numpy as np
import pydeck as pdk

# Load the GPKG file (vegetation and stump data)
gpkg = gpd.read_file("/home/shrikar/RnD/dataset/STUMP.gpkg")
#print(gpkg.geom_type.value_counts())

# Convert MultiPolygon to Centroid
gpkg["geometry"] = gpkg["geometry"].centroid

# Extract latitude and longitude
gpkg["latitude"] = gpkg.geometry.y
gpkg["longitude"] = gpkg.geometry.x

# Define 3D visualization layer
layer = pdk.Layer(
    "ScatterplotLayer",
    gpkg,
    get_position=["longitude", "latitude"],
    get_elevation=100,  # Modify if needed
    get_radius=50,
    get_fill_color=[255, 0, 0, 160],
    pickable=True,
    extruded=True,
)

# Define viewport
view_state = pdk.ViewState(
    latitude=gpkg["latitude"].mean(),
    longitude=gpkg["longitude"].mean(),
    zoom=12,
    pitch=50,
)

# Render
pdk.Deck(layers=[layer], initial_view_state=view_state).show()
