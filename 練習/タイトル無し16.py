# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:22:05 2019

@author: nakahashi
"""

def show_message(num=0):
    
    def decolate(func):
        
        if num==0:
            flag="Rad" 
        else:
            flag="Blue"
            
        print("==== flag:",flag)
        func()
        print("====")
        
        
    def show_selection(num=num):
        if num==0:
            
            print("Selection is",num,"which may be the default")
        else:
            print("Your choise is",num)
            
    return decolate(show_selection)
    decolate(show_selection)
    decolate(show_selection)
#    return decolate
            
        

show_message(0)
show_message(1)