import folium

import pandas as pd  

#map=folium.Map(location=[15.3764,78.9251],zoom_start=10)


data=pd.read_csv("volcanoes.txt")

print(data)

latitude=list(data["LAT"])

longitude=list(data['LON'])

elevation=list(data['ELEV'])


map=folium.Map(location=[48.7,-121.8],zoom_start=6,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

def color_coding(el):
    if el<1000:
        return "green"
    elif el>1000 and el<2000:
        return "orange"
    else:
        return "red"

for lt,ln,el in zip(latitude,longitude,elevation):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+"m",fill_color=color_coding(el),color="black",radius=8,opacity=0.7))


fgp=folium.FeatureGroup("Population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),

style_function=lambda  x: {'fillColor':'green' if x['properties']['POP2005']<1000000 

else "orange"  if 1000000<x['properties']['POP2005']<2000000 else "red"  }
))



#print(elevation)

map.add_child(fgv)


map.add_child(fgp)

map.add_child(folium.LayerControl())




map.save("loc1.html")