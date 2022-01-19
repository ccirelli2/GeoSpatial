"""Ref = https://gis.stackexchange.com/questions/130963/write-geojson-into-a-geojson-file-with-python
"""

from geojson import Point, Feature, FeatureCollection, dump

point = Point((-115.81, 37.24))

features = []
features.append(Feature(geometry=point, properties={"country": "Spain"}))

# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
   dump(feature_collection, f)






