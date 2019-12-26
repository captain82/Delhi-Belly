import pandas
import geopy
from geopy.geocoders import Nominatim


df = pandas.read_csv("MagicBricks.csv")
print(df.shape)


nom=Nominatim()
df2 = df.iloc[1150:1250,0:10]
df2["Coordinates"] = df2["Locality"].apply(nom.geocode)
df2["Latitude"] = df2["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df2["Longitude"] = df2["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df2)
df2.to_csv('file29.csv')
