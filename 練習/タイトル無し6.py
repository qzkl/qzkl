# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:00:36 2019

@author: nakahashi
"""

def number_to_day(num=0):
    if num==0:
        day='今日'
    elif num==1:
        day='明日'
    elif num==-1:
        day='昨日'
    else:
        day='今日より1日を超えて離れた日'
    return day

num=input('入力して')
num=int(num)
n=number_to_day(num)

print(n)