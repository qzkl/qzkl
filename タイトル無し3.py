# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:14:39 2019

@author: nakahashi
"""

import random

numbers=[]

for i in range(10):
    i=str(i)
    numbers.append(i)
#numbers=['0','1','2','3','4','5','6','7','8','9']
sample4=random.sample(numbers,k=4)
num4=''.join(sample4)

while True:
    print(num4)
    val=input()
    if val==num4:
        print('OK')
        break
    else:
        print(val,':NG')