from math import factorial
from functools import reduce
def dbl(x):
    return 2*x
def inverse(n):
    return 1.0/n
def add(x, y):
    return x + y
def e(n):
    mylist = list(range(n+1))
    return reduce(add, map(inverse,map(factorial, mylist)))
    
