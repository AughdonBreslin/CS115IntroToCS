#
# life.py - Game of Life lab
#
# Name:Aughdon Breslin
# Pledge:
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A
def printBoard( A ):
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width, height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
def innerCells(w,h):
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

def randomCells(w,h):
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0,1])
    
    return A
def copy(A):
    cp = createBoard(len(A), len(A[0]))
    for row in range(len(A)):
        for col in range(len(A[0])):
            cp[row][col] = A[row][col]
    return cp
def innerReverse(A):
    B = createBoard(len(A), len(A[0]))
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            B[row][col] = 1 - A[row][col]
    
    return B
def next_life_generation(A):
    output = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            neighbors = \
                A[row-1][col-1] + \
                A[row-1][col] + \
                A[row-1][col+1] + \
                A[row][col-1] + \
                A[row][col+1] + \
                A[row+1][col-1] + \
                A[row+1][col] + \
                A[row+1][col+1]
            if neighbors == 3 and A[row][col] == 0:
                output[row][col] = 1
            elif neighbors < 2:
                output[row][col] = 0
            elif neighbors > 3:
                output[row][col] = 0
    return output

                    









