import folium
import pandas

data = pandas.read_csv("UpdatedPrices.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
price = list(data["Price"])

def color_producer(price):
    if price<1000000:
        return 'green'
    elif 1000000<=price < 3000000:
        return 'orange'
    elif 3000000<=price < 5000000:
        return 'blue'
    elif 5000000<=price < 6000000:
        return 'black'
    elif 7000000<=price < 8000000:
        return 'pink'
    elif 10000000<=price < 30000000:
        return 'purple'
    elif 3000000<=price < 50000000:
        return 'grey'
    elif 5000000<=price < 80000000:
        return 'yellow'
    else:
        return 'red'

map = folium.Map(location=[22.4809646,88.4113023],zoom_start=15)
tile = folium.TileLayer('Mapbox Bright').add_to(map)

fg=folium.FeatureGroup(name="Delhi Belly")

for lt,ln,pr in zip(lat,lon,price):
    fg.add_child(folium.CircleMarker(location=[lt,ln] , radius=10,popup=str(pr)+" m",fill_color = color_producer(pr),color = 'grey',fill_opacity=1))


map.add_child(fg)

map.save("DelhiBelly.html")
