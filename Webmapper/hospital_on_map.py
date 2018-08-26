import folium
import pandas

data = pandas.read_csv("hospital_data.csv",low_memory=False)
lat = list(data["Latitude"])
lon = list(data["Longitude"].dropna())
name = list(data["Name"])

def color_producer(latitude):
    if latitude < 15:
        return 'green'
    elif 15 <= latitude < 25:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[23.26, 77.41], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="geocode_health_centre")

for lt, ln, nm in zip(lat, lon, name):
    fgv.add_child(folium.Marker(location=[float(lt),float(ln)],popup=str(nm), icon=folium.Icon(color=color_producer(lt))))

map.add_child(fgv)

map.save("hospital_places_map.html")
