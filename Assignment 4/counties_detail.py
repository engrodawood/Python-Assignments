# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:27:35 2017

@author: Muhammad
"""

import csv
from getDistance import *


import matplotlib.pyplot as plt
import numpy as np

country_name=[]
capital_name=[]
latitude=[]
longitude=[]
fartest=[]
nearest=[]
closest=[]
equi_cap_dis=38000000.0
equi_cap_name=''

#distDict={}
distance=[]
with open('countries.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        country_name.append(row[0])
        capital_name.append(row[1])
        latitude.append(row[2])
        longitude.append(row[3])
    
    for i in range(0,len(country_name)):
        distDict={}
        distance_sum=0
        equidist = np.array([])
        for j in range(0,len(capital_name)):
            if(i==j):
                continue
            dist=getDistance(latitude[i],longitude[i],latitude[j],longitude[j])
            distance.append(dist)
            distance_sum+=dist
            equidist=np.append(equidist,abs(dist))
            #print(capital_name[i]," TO ",capital_name[j], " Distance is ",dist)
            distDict.update({(capital_name[i],capital_name[j]):dist})
        sortedDict=sorted(distDict.items(), key=lambda x: (x[1])) 
        for l in sortedDict:
            nearest.append(l)
            break
        sortedDict=sorted(distDict.items(), key=lambda x: (-x[1])) 
        for m in sortedDict:
            fartest.append(m)
            break
        closest.append((capital_name[i],distance_sum))
        difference=np.diff(equidist)
        result=np.sum(abs(difference))
        if(result<equi_cap_dis):
            equi_cap_dis=result
            equi_cap_name=capital_name[i]
            
        
plt.hist(distance)
plt.show()

# writing the data to csv file

with open ('distance.csv','w') as csvfile:
    fieldnames = ['CountryName', 'Capital','Fartest','Nearest']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(len(fartest)):
        writer.writerow({'CountryName':country_name[i],'Capital':fartest[i][0][0],'Fartest':fartest[i][0][1],'Nearest':nearest[i][0][1]})              

shortest=min(nearest,key=lambda x:x[1])
apartest=max(fartest,key=lambda x:x[1])
print("\n\n",'*'*10," The Capital Fartest from Each other are : ", 10*'*')
print(apartest[0][0]," And ",apartest[0][1], "Distance is ",apartest[1])

print("\n\n",'*'*10," The Capital Nearest to Each other are : ", 10*'*')
print(shortest[0][0]," And ",shortest[0][1], "Distance is ",shortest[1])

print("\n\n",'*'*10," The Capital Closest to most of the Capital of other Country : ", 10*'*')
closest_capital=min(closest,key=lambda x:x[1])
print(closest_capital[0])

print("\n\n",'*'*10," The Capital Isolated from most of the Capital of other Country : ", 10*'*')
isolated_capital=max(closest,key=lambda x:x[1])
print(isolated_capital[0])

print("\n\n",'*'*10," The Capital Equidistance from most of the Capital of other Country : ", 10*'*')
print(equi_cap_name)
