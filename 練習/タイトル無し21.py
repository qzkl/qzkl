# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:09:43 2019

@author: nakahashi
"""

from collections import deque

queue=deque([1,2])
queue.append(3)
queue.append(4)
print("queue:", queue)
print("popleft from queue 1st value:", queue.popleft())
print("popleft from queue 1st value:", queue.popleft())
print("queue:", queue)