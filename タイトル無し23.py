# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:46:56 2019

@author: nakahashi
"""

#mat=[
#     [1,2,3,4],
#     [5,6,7,8]
#]

I=4
J=5
mat=[[i*J+j+1 for j in range(J)] for i in range(I)]

print(mat)

