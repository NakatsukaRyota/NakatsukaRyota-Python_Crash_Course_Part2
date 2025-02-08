import csv
from pathlib import Path

import plotly.express as px

path = Path("eq_data/world_fires_7_day.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

lats, lons, brights = [], [], []
lat_index = header_row.index("latitude")
lon_index = header_row.index("longitude")
brights_index = header_row.index("brightness")

for row in reader:
    lats.append(float(row[lat_index]))
    lons.append(float(row[lon_index]))
    brights.append(float(row[brights_index]))

title = "世界の火災"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brights,
    title=title,
    color=brights,
    color_continuous_scale="Viridis",
    labels={"color": "放射温度"},
    projection="natural earth",
)
fig.show()
