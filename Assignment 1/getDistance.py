# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 08:45:55 2016

@author: Muhammad
Todo ://Next to be done
"""
from math import sin,cos,sqrt,atan2,radians
a=555
def hello():
    print("Author is Muhammad")
    return
    
def getDistance(lat_c1,long_c1,lat_c2,long_c2):
    
    """
    This Function Will Calculate Distance between Two cities
    
    Parameters: latitude_city1,longitude_city2,latitude_city2,longitude_city2
    
    Return : function will return distance in Kilometers
    """
    lat_c1 = radians(float(lat_c1))
    lat_c2 = radians(float(lat_c2))
    long_c1 = radians(float(long_c1))
    long_c2 = radians(float(long_c2))
    lat_diff = lat_c2 - lat_c1
    long_diff = long_c2 - long_c1
    a = sin(lat_diff/2.0)**2 + cos(lat_c1) * cos(lat_c2) * sin(long_diff/2.0)**2
    b = 2 * atan2(sqrt(a),sqrt(1 - a))
    R=6371
    distance=R*b
    return distance
print ("__name__ in", __file__, "is",__name__)
#if __name__=='__main__': 
    #print("Distance between the Cities is:KM")