# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:41:58 2019

@author: nakahashi
"""

s_coordi_list=["1.1,2.2,3.5","2.1,3.2,5.5","1.2,1.3,2.2","2.1,3.1,4.5"]

s_coordi="1.0,2.5,2.3"
reslut=s_coordi.split(",")

print(reslut)
print(s_coordi.split(","))

num_list=list(range(1,8))

def double(x):
    return x*2

reslut_1=list(map(double,num_list))

#for e in map(double,num_list):
#    print(e,end=" ")