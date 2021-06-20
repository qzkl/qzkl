# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:33:45 2019

@author: nakahashi
"""

class Data:
    def __init__(self):
        self.nums=[1,2,3,4,5]
        
    def change_data(self,index,n):
        self.nums[index]=n
        
data_one=Data()
data_one.nums[0]=100

print(data_one.nums)

data_two=Data()
data_two.change_data(0,100)
print(data_two.nums)