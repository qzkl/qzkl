# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:32:37 2019

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

#while True:
#    print('4桁の数字を入力してください')
#    val=input()
#    if val==num4:
#        print('OK')
#        break
#    if len(val)!=4:
#        print('4桁の数字を入力しなさい')
#        continue
#    answer=''
#    for i in range(4):
#        if num4[i]==val[i]:
#            answer +=num4[i]
#        else:
#            answer+='X'
#    print('->'+answer)
    