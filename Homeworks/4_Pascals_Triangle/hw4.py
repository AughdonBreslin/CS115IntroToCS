#!/usr/bin/env python
# coding: utf-8

# In[33]:


#erisa 
#October 6
def calculate_helper(L):
    if L == [1]:
        return []
    else:
        return [L[0] + L[1]] + calculate_helper(L[1:])
def pascal_row(n):
    if n == 0:
        return [1]
    else:
        return [1] + calculate_helper(pascal_row(n-1)) + [1]
def pascal_triangle(n):
    if n == 0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]
def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(10) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

# Test cases for pascal_triangle(), based on the hw doc and one that desires the value at "row" 10
def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(10) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]


