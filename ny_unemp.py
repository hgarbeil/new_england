
import pandas as pd
import geopandas
import folium
import json
import numpy as np
import webbrowser
import io
import geopandas as gpd
county_geo = r'../us-counties.json'
#with open(county_geo, 'r') as f:
#    get_id = json.load(f)
geo = gpd.read_file(county_geo)
geo.info()
df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample=df_sample[df_sample['State FIPS Code']==36]
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']
df_sample.head()

newdf = geo.merge(df_sample, left_on='id', right_on='FIPS')
newdf.head()
colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
    "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
    "#08519c", "#0b4083", "#08306b"
]
#endpts = list(np.linspace(1, 12, len(colorscale) - 1))
endpts= list(np.linspace(1,10))
fips = df_sample['FIPS'].tolist()
print(fips[0])
values = df_sample['Unemployment Rate (%)'].tolist()
hover =[]

my_map = folium.Map(location=(48,-95),zoom_start=3)
newdf.info()
mydf = newdf.iloc[:,[0,11]]
folium.Choropleth(
    geo_data=mydf, data=mydf,columns=['id','Unemployment Rate (%)'],
    name="choropleth",
    key_on='feature.id'
    #fill_color='BuPu'
).add_to(my_map)
print (newdf)
my_map.save('map.html')
webbrowser.open('map_html')
folium.LayerControl().add_to(my_map)
my_map