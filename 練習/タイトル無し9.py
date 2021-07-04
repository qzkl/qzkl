# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:13:46 2019

@author: nakahashi
"""

vote_num=0

def vote(vote_n):
    print("投票します")
    vote_n +=1
    return vote_n

def reset_box(vote_n):
    print("空にします")
    vote_n=0
    return vote_n

def check_box(vote_n):
#    vote_n=str(vote_n)
    print("投票数は{}です".format(vote_n))
    return


vote_num=vote(vote_num)

for i in range(3):
    vote_num=vote(vote_num)
check_box(vote_num)
vote_num=reset_box(vote_num)
check_box(vote_num)   

n=sum([1,2,3,4])
print(n)

n=sum(range(10))
print(n)

add_all=sum
print(add_all([1,2,3,4]))