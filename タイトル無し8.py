# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:05:08 2019

@author: nakahashi
"""

vote_num=0

def vote():
    print("投票します")
    global vote_num
    vote_num +=1
    
def reset_box():
    print("箱を空にします")
    global vote_num
    vote_num=0
    
def check_box():
    print("中身を確認します")
    global vote_num
    print("投票数は{}です".format(vote_num))
    
vote()
vote()
check_box()
reset_box()
for i in range(4):
    vote()
check_box()