from PIL import Image
import numpy as np
import streamlit as st
import numpy as np
import folium
import geopandas as gpd
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_folium import st_folium
from utils import popupTable
import branca
import cv2
import pandas as pd
import rasterio
# from PIL import Image
import os
import geojson




import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, shape,Polygon
from shapely import geometry
import geojson
import csv
# datastring = 'map_ls.geojson'
# with open(datastring) as f:
#     gj = geojson.load(f)

# geo = gj['features'][0]['geometry']['coordinates']
# print(len(geo))
# df = pd.read_csv('./static/WTGL-RK.csv')
# lon = list(df['longitude'])
# lat = list(df['latitude'])


# ets =[]
# for i in zip(lon,lat):
#     ets.append(tuple(i))
# ls = LineString(ets)

# offset = .000370
# ret_left = ls.parallel_offset(offset, 'left')
# ret_right = ls.parallel_offset(offset, 'right')


# lons = []
# lats = []
# for i in list(ret_left.coords):
#     lons.append(i[0])
#     lats.append(i[1])

# ll = pd.DataFrame({'Longitude':lons,'Latitude':lats})
# ll.to_csv('./static/ll1.csv',index = False)


# lons = []
# lats = []
# for i in list(ret_right.coords):
#     lons.append('['+str(i[0])+',')
#     lats.append(str(i[1])+']'+',')

# rl= pd.DataFrame({'Longitude':lons[::-1],'Latitude':lats[::-1]})
# print(rl)
# rl.to_csv('./static/rl2.csv',index = False)

#print(list(ret_left.coords))
# ll= pd.DataFrame({'left' :list(ret_left.coords)})
# rl = pd.DataFrame({'right':list(ret_right.coords)})
# rl.to_csv('./static/rl.csv',index = False)
# ll.to_csv('./static/ll.csv',index = False)
# all = list(ret_left.coords)+list(ret_right.coords)
# p = Polygon([ *list(ret_right.coords)[::-1],*list(ret_left.coords)])

df = pd.read_csv('./static/adani_report.csv')
#df = df.dropna(thresh=4)
#df = pd.read_csv('./static/GeneratedReport - GeneratedReport.csv')
insights = ["Temperature"]
#insights = [ "Vegetation encroachment","Land Subsidence","Potential Fouling","Corrosion"]
for i in insights:
    df_temp = df[['latitude', 'longitude','name', i]]
    df_temp = df_temp.dropna(thresh=3)
    #df_temp = df_temp.loc[df_temp[i] == ]

    df_temp.to_csv('./static/{}.csv'.format(''.join(i)),index = False)
# print(df['Temperature'].unique())
# insights = ["Temperature", "Vegetation encroachment","Land Subsidence","Potential Fouling","Corrosion"]
# for i in insights:
#     df_temp = df[['latitude', 'longitude', i]]
#     df_temp = df_temp.loc[df_temp[i] == 1]


# im = Image.open('./static/2_corr.tif')
# im.save('./static/2_corr.png')
# print(im)


# img = Image.open('./static/2_corr.png')
# img = img.convert("RGBA")
# datas = img.getdata()
# newData = []
# for item in datas:
#     if item[0] == 0 and item[1] == 0 and item[2] == 0:
#         newData.append((0, 0, 0, 0))
#     else:
#         newData.append(item)
 
# img.putdata(newData)
# img.save('./static/1_corr.png', "PNG")
# datastring = './static/map_row.geojson'
# with open(datastring) as f:
#     gj = geojson.load(f)

# geo = gj['features'][0]['geometry']['coordinates'][0]
# #print(geo)
# print(len(geo))
# print(geo[:10])

# imgs = ['1_corr.tif','2_corr.tif','3_corr.tif']
# for im in imgs:
#     file_  = np.array(rasterio.open('./static/'+im).read())
#     with rasterio.open('./static/'+im, 'r') as src:
#         # Access the CRS of the raster
#         crs = src.crs
#         transform = src.transform
#     print(crs)   
#         # Print the CRS inf
#     for i in range(file_[0].shape[0]):
#         for j in range(file_[0].shape[1]):
#             if np.isnan(file_[0][i][j]):
#                 file_[0][i][j] = 1.0


#     with rasterio.open(
#         './static/'+im.split('.')[0]+'mod.tif',
#         'w',
#         driver='GTiff',
#         height=file_.shape[1],
#         width=file_.shape[2],
#         count=1,
#         transform=transform,
#         dtype=file_.dtype,
#         crs=crs,

#     ) as dst:
#         dst.write(file_)
im = Image.open('./static/HOTSPOT.tif')
im.save('./static/HOTSPOT.png')
print(im)


img = Image.open('./static/HOTSPOT.png')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)
 
img.putdata(newData)
img.save('./static/HOTSPOT.png', "PNG")
# from rasterio.merge import merge
# import rasterio as rio


# output_path = 'C:/Users/tanya/Desktop/Live_adani/tif_files_adani/mosaic_py.tif'

# files = os.listdir('C:/Users/tanya/Desktop/Live_adani/tif_files_adani/inSAR/')

# raster_to_mosiac =[]
# for p in files:
#     raster = rio.open('C:/Users/tanya/Desktop/Live_adani/tif_files_adani/inSAR/'+p)
#     raster_to_mosiac.append(raster)

# mosaic, output = merge(raster_to_mosiac, method='max')

# output_meta = raster.meta.copy()
# output_meta.update(
#     {"driver": "GTiff",
#         "height": mosaic.shape[1],
#         "width": mosaic.shape[2],
#         "transform": output
#     }
# )

# with rio.open(output_path, "w", **output_meta) as m:
#     m.write(mosaic)