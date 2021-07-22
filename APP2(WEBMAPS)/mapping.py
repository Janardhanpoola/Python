#Buidling webmaps
#1.Add points
#2.Add multiple points
#3.popup windows on map
#4.color points


import folium
import pandas as pd
#map= folium.Map(location=[80,-100])# geographic coordinates latitudes(-90 to 90) and longitudes(-180 to 180)
#map= folium.Map(location=[38.58,-99.09],zoom_start=6)

def color_point(elevation): #function for color points based on elevation
    if elevation<1000:
        return "green"
    elif elevation>1000 and elevation<2000:
        return "orange"
    else:
        return "red"


data=pd.read_csv("volcanoes.txt")

lat=list(data["LAT"]) #latitudes

lon=list(data["LON"]) #logitudes

elev=list(data["ELEV"]) # elevation points of the map

map= folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")#tiles changes the map to green(terrain)

fgv=folium.FeatureGroup(name="Volcanoes")   

#fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi im a marker",icon=folium.Icon(color="red"))) #adding points(marker)  ##for one loc

#for coordinates in [[38.2,-99.1],[39.1,-99.0]]:
#    fg.add_child(folium.Marker(location=coordinates,popup="Hi im a marker",icon=folium.Icon(color='blue'))) #adding points(marker) ##for two locs


#for lt,ln,el in zip(lat,lon,elev):
#       fg.add_child(folium.Marker(location=[lt,ln],popup=str(el),icon=folium.Icon(color=color_point(el)))) #popup element elevation is float,but add_child will support str.so, str(el) 

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+"m",fill_color=color_point(el), color="grey" , radius=8, fill_opacity=0.7)) # radius is pixel size,fill_color is inner area of the circle, color(grey) is surrounding area of circle

fgp=folium.FeatureGroup("Population")


#############to add Geojson layer/borders/polygons to the map
#step 1:loading world.json data to fill polygons to each country
#step 2:style function gets the color of the country depending on population



fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':"green" if x['properties']['POP2005']< 10000000 
else "orange" if 10000000 <= x['properties']['POP2005'] <= 20000000 else "red"} ))



map.add_child(fgv) #adding feature group volcanoes to map
map.add_child(fgp)#adding feature group population to map

map.add_child(folium.LayerControl()) #option at top right

map.save("loc.html")#save map object to a file loc.html


#######Adding popup window on map

