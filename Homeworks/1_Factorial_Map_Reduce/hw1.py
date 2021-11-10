'''
Aughdon Breslin
Homework 1
'''

from functools import reduce

def add(a, b):
    return a+b

def mul(a, b):
    return a*b

def factorial(n):
    return reduce(mul,range(1,n+1))

def mean (l):
    return reduce(add,l)/len(l)
