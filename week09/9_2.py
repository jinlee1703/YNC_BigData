import pandas as pd
import folium

CB_geoData = pd.read_csv('D:/YNC_3_2/BigData/pythonProject/week09/address/CB_geo.shp_2.csv', encoding='CP949', engine='python')
map_CB = folium.Map(location=[37.560284, 126.975334], zoom_start=15)

for i, store in CB_geoData.iterrows():
    folium.Marker(location=[store['위도'], store['경도']],
                  popup=store['store'], icon=folium.Icon(color='red', icon='star')).add_to(map_CB)

map_CB.save('D:/YNC_3_2/BigData/pythonProject/week09/address/map_CB.html')