'''
Example.py
'''
import os 


def width():
    "A function to calculate the width"
    return 5
    
def area(length, func):
    return(length * func())
    
area(5, width)


