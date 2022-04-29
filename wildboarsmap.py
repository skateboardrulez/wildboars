import folium
import pandas


red = ("#EB2408")
blue = ("#068EE1")
green = ("#02B929")
cian = ("#08EBDD")
orange = ("#EE9114")
white = ("#FFFFFF")
yellow = ("#F2F516")

# koca1 yearly localization points, data sow1 yearly
datas1y = pandas.read_csv("map_koca1/koca1_all_lokpont_clean.csv")
lats1y = list(datas1y["LATITUDE"])
lons1y = list(datas1y["LONGITUDE"])

# koca1 spring localization points, data sow1 spring
datas1spr = pandas.read_csv("map_koca1/2015_spring.csv")
lats1spr = list(datas1spr["LATITUDE"])
lons1spr = list(datas1spr["LONGITUDE"])

# koca1 summer localization points, data sow1 summer
datas1sum = pandas.read_csv("map_koca1/2015_summer.csv")
lats1sum = list(datas1sum["LATITUDE"])
lons1sum = list(datas1sum["LONGITUDE"])

# koca1 2014 autumn localization points, data sow1 autumn 2014
datas1a2014 = pandas.read_csv("map_koca1/2014_autumn.csv")
lats1a2014 = list(datas1a2014["LATITUDE"])
lons1a2014 = list(datas1a2014["LONGITUDE"])

# koca1 2015 autumn localization points, data sow1 autumn 2015
datas1a2015 = pandas.read_csv("map_koca1/2015_autumn.csv")
lats1a2015 = list(datas1a2015["LATITUDE"])
lons1a2015 = list(datas1a2015["LONGITUDE"])

# koca1 2014 winter localization points, data sow1 winter 2014
datas1w2014 = pandas.read_csv("map_koca1/2014_2015_winter.csv")
lats1w2014 = list(datas1w2014["LATITUDE"])
lons1w2014 = list(datas1w2014["LONGITUDE"])

# koca1 2015 winter localization points, data sow1 autumn 2015
datas1w2015 = pandas.read_csv("map_koca1/2015_winter.csv")
lats1w2015 = list(datas1w2015["LATITUDE"])
lons1w2015 = list(datas1w2015["LONGITUDE"])

map = folium.Map(location=[47.51, 18.98], zoom_start=14, tiles="Stamen Terrain")

# koca1 yearly localization points feature group
fgs1y = folium.FeatureGroup(name="Sow1 yearly localization points")

for lt, ln in zip(lats1y, lons1y):
    fgs1y.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(red), color=(red), fill_opacity=1))

# koca1 spring localization points feature group
fgs1spr = folium.FeatureGroup(name="Sow1 spring localization points")

for lt, ln in zip(lats1spr, lons1spr):
    fgs1spr.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(cian), color=(cian), fill_opacity=1))

# koca1 summer localization points feature group
fgs1sum = folium.FeatureGroup(name="Sow1 summer localization points")

for lt, ln in zip(lats1sum, lons1sum):
    fgs1sum.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(yellow), color=(yellow), fill_opacity=1))

# koca1 autumn 2014 localization points feature group
fgs1a2014 = folium.FeatureGroup(name="Sow1 2014 autumn localization points")

for lt, ln in zip(lats1a2014, lons1a2014):
    fgs1a2014.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(orange), color=(orange), fill_opacity=1))

# koca1 autumn 2015 localization points feature group
fgs1a2015 = folium.FeatureGroup(name="Sow1 2015 autumn localization points")

for lt, ln in zip(lats1a2015, lons1a2015):
    fgs1a2015.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(green), color=(green), fill_opacity=1))

# koca1 winter 2014 localization points feature group
fgs1w2014 = folium.FeatureGroup(name="Sow1 2014 winter localization points")

for lt, ln in zip(lats1w2014, lons1w2014):
    fgs1w2014.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(white), color=(white), fill_opacity=1))

# koca1 winter 2015 localization points feature group
fgs1w2015 = folium.FeatureGroup(name="Sow1 2015 winter localization points")

for lt, ln in zip(lats1w2015, lons1w2015):
    fgs1w2015.add_child(folium.CircleMarker(location=[lt, ln], radius=1, fill_color=(blue), color=(blue), fill_opacity=1))

map.add_child(fgs1y)
map.add_child(fgs1spr)
map.add_child(fgs1sum)
map.add_child(fgs1a2014)
map.add_child(fgs1a2015)
map.add_child(fgs1w2014)
map.add_child(fgs1w2015)
map.add_child(folium.LayerControl())

map.save("wildboars.html")
