import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import seaborn as sns

df = pd.read_csv = ("shopping_centers.csv")

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry )


dc_boundary = gpd.read_file("/Users/amiratlemsani/Documents/infochallenge data/Washington_DC_Boundary/Washington_DC_Boundary.shp")

fig, ax = plt.subplots(figsize =(10,10))
dc_boundary.plot(ax=ax, color = 'lightgrey') 

gdf.plot(ax=ax, marker = 'o', color = 'red', markersize = 5 )

plt.title("Shopping Center Locations in Washington, D.C.", fontsize = 14 )
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()