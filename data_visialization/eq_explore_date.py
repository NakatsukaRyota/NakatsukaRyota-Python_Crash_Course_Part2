import json
from pathlib import Path

import plotly.express as px

path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

all_eq_dics = all_eq_data["features"]

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dics:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    eq_titles.append(eq_dict["properties"]["title"])

title = all_eq_data["metadata"]["title"]
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "マグニチュード"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
