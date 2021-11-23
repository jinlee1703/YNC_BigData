import pandas as pd
from pyparsing import col

CB = pd.read_csv('D:/YNC_3_2/BigData/pythonProject/week09/address/CoffeeBean.csv', encoding='CP949', index_col=0, header=0, engine='python')

addr = []
for address in CB.address:
    addr.append(str(address).split())

addr2 = []

for i in range(len(addr)):
    if addr[i][0] == "서울":addr[i][0] = "서울특별시"
    elif addr[i][0] == "서울시":addr[i][0] = "서울특별시"
    elif addr[i][0] == "부산시":addr[i][0] = "부산광역시"
    elif addr[i][0] == "인천":addr[i][0] = "인천광역시"
    elif addr[i][0] == "광주": addr[i][0] = "광주광역시"
    elif addr[i][0] == "대전시": addr[i][0] = "대전광역시"
    elif addr[i][0] == "울산시": addr[i][0] = "울산광역시"
    elif addr[i][0] == "세종시": addr[i][0] = "세종특별자치시"
    elif addr[i][0] == "경기": addr[i][0] = "경기도"
    elif addr[i][0] == "충북": addr[i][0] = "충청북도"
    elif addr[i][0] == "충남": addr[i][0] = "충청남도"
    elif addr[i][0] == "전북": addr[i][0] = "전라북도"
    elif addr[i][0] == "전남": addr[i][0] = "전라남도"
    elif addr[i][0] == "경북": addr[i][0] = "경상북도"
    elif addr[i][0] == "경남": addr[i][0] = "경상남도"
    elif addr[i][0] == "제주": addr[i][0] = "제주특별자치도"
    elif addr[i][0] == "제주도": addr[i][0] = "제주특별자치도"
    elif addr[i][0] == "제주시": addr[i][0] = "제주특별자치도"
    addr2.append(' '.join(addr[i]))

addr2 = pd.DataFrame(addr2, columns=['address2'])
CB2 = pd.concat([CB, addr2], axis=1)
CB2.to_csv('D:/YNC_3_2/BigData/pythonProject/week09/address/CoffeeBean2.csv', encoding='CP949', index=False)

# import folium
# map_osm = folium.Map(location=[37.5599811473406, 126.97530908762165], zoom_start=16)
# map_osm.save('D:/YNC_3_2/BigData/pythonProject/week09/address/map.html')

