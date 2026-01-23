import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# 1. Load World Shapefile (Natural Earth Admin 0 – Countries)
# ----------------------------------------------------------
world = gpd.read_file(
    "ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
)

# Column used for matching country names
name_col = "NAME"   # some shapefiles use NAME_EN; change if needed


# ----------------------------------------------------------
# 2. Aerocene Countries List (as real names)
# ----------------------------------------------------------
aerocene_countries = [
    "Albania",
    "United Arab Emirates",
    "Argentina",
    "Antarctica",                     # territory (will match if shapefile includes it)
    "Australia",
    "Austria",
    "Belgium",
    "Bulgaria",
    "Bolivia",
    "Brazil",
    "Canada",
    "Switzerland",
    "China",
    "Cameroon",
    "Colombia",
    "Cuba",
    "Germany",
    "Denmark",
    "Egypt",
    "Spain",
    "Finland",
    "France",
    "United Kingdom",
    "Greece",
    "Israel",
    "Italy",
    "Japan",
    "South Korea",
    "Netherlands",
    "Norway",
    "New Zealand",
    "Pakistan",
    "Peru",
    "Palestine",
    "Poland",
    "Russia",
    "Singapore",
    "Solomon Islands",
    "Slovenia",
    "Thailand",
    "Turkey",
    "Taiwan",
    "United States of America",
    "Kosovo",
]


# ----------------------------------------------------------
# 3. Match by name ("NAME" column)
# ----------------------------------------------------------
highlight = world[world[name_col].isin(aerocene_countries)]
others = world[~world[name_col].isin(aerocene_countries)]


# ----------------------------------------------------------
# 4. Load Aerocene City Points
# ----------------------------------------------------------
cities = pd.read_csv("aerocene_cities.csv")


# ----------------------------------------------------------
# 5. Plot the Map
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9))  # 16:9 aspect ratio

# Other countries in light gray
others.plot(
    ax=ax,
    color="#e6e6e6",
    edgecolor="white",
    linewidth=0.6,
    zorder=1,
)

# Highlighted Aerocene countries in light blue
highlight.plot(
    ax=ax,
    color="#8ecae6",
    edgecolor="white",
    linewidth=0.7,
    zorder=2,
)

# Cities (black dots, no labels)
ax.scatter(
    cities["lon"],
    cities["lat"],
    s=12,
    color="black",
    zorder=3,
)

# Country labels (using their NAME field)
for _, row in highlight.iterrows():
    rep = row.geometry.representative_point()
    ax.text(
        rep.x, rep.y,
        row[name_col],
        fontsize=8,
        ha="center",
        va="center",
        zorder=4,
    )

ax.set_axis_off()   # No axes, no title

plt.tight_layout()
plt.savefig("aerocene_world_map.png", dpi=300, bbox_inches="tight")
plt.close()