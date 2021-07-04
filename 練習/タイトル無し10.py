# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:35:18 2019

@author: nakahashi
"""

num=[194,223,516,2,-12,5,7,1,9,8,10,14,33,51,0,99,1000]

i=int(len(num))

for n in range(i):
    for m in range(n+1,i):
        if num[n]>num[m]:
            a=num[n]
            b=num[m]
            num[n]=b
            num[m]=a
            
            
print(num)