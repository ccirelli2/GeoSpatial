"""
	Tutorial:
		https://geopandas.org/getting_started/introduction.html
   
	Get Distance between two points
		https://stackoverflow.com/questions/63722124/get-distance-between-two-points-in-geopandas
    	https://gis.stackexchange.com/questions/293310/how-to-use-geoseries-distance-to-get-the-right-answer
		https://protect-us.mimecast.com/s/EjvHCG626LilVl4cKfZHv?domain=kodu.ut.ee
"""

# Import Library
import geopandas as gpd
from shapely.geometry import Point
import geopy.distance

LAT1=40.748441
LNG1=-73.985664

LAT2= 40.740179500000004
LNG2= -73.985313700000006

pnt1 = Point(LAT1, LNG1)
pnt2 = Point(LAT2, LNG2)
points_df = gpd.GeoDataFrame({'geometry': [pnt1, pnt2]}, crs='EPSG:4326')
print(points_df)

#dist=points_df.distance(points_df.shift()) 
#print(dist)


