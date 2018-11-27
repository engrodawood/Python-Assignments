#from math import sin,cos,sqrt,atan2,radians
from getDistance import hello,getDistance

# variable declearation

hello()
a=30
lat_c1=input("Enter Latitude of City 1 : ")
long_c1=input("Enter Longitude of City 1 : ")
lat_c2=input("Enter Latitude of City 2 : ")
long_c2=input("Enter Longitude of City 1 : ") 
result=getDistance(lat_c1,long_c1,lat_c2,long_c2)
print("Distance between the Cities is:",result,"KM")
b=99
print("b is ",b) # value previously will be overwrite in console
    

#print(__name__)

