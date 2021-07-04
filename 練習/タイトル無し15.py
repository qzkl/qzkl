# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:47:25 2019

@author: nakahashi
"""

def show_how_it_works(func):
    def my_function(*args,**kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result=func(*args,**kwargs)
        print('Result:', result)
        return result
    return my_function

def add_two_numbers(a,b,c=3):
    return a+b+c

#print(add_two_numbers(1,8))

declataed_func=show_how_it_works(add_two_numbers)
declataed_func(1,8,4)