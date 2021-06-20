# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 00:21:45 2018

@author: nakahashi
"""
S=[7,4,6,3,2,8,91,18,34,22,57]
def quicksort(seq):
    if len(seq) < 1:
        return seq
    pivot = seq[0]
    left = []
    right = []
    for x in range(1, len(seq)):
        if seq[x] <= pivot:
            left.append(seq[x])
        else:
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right
    

print(quicksort(S))