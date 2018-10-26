import folium
import shutil,os

def maper(x,y,text):
    x1 = (sum(x)/len(x))
    y1 = (sum(y)/len(y))

    map1=folium.Map(location=[x1,y1],zoom_start=1,tiles='Stamen Terrain')

    fg = folium.FeatureGroup('Tweets')

    for i in range(len(x)):
        fg.add_child(folium.Marker(loation = [x[i],y[i]],popup = (folium.Popup(text[i]))))

    map1.add_child(fg)

    map1.save(outfile = 'map1.html')
    shutil.copy('map1.html','/templates')