# mandelbrot.py
# Lab 9

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    result = 0
    for i in range(n):
        result += c
    return result


def update(c,n):
    z = 0
    for i in range(n):
        z = (z**2 + c)
    return z

def inMSet(c,n):
    z = 0
    for i in range(n):
        z = (z**2 + c)
        if abs(z) > 2:
            return False
    return True
    
def weWantThisPixel(col, row):
    if col%10 == 0 or row%10 == 0:return True
    else:return False
def test():
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)
    image.saveFile()
    
def scale(pix, pixMax, floatMin, floatMax):
    return floatMin + (pix/pixMax * (floatMax - floatMin))
def mset():
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2.0, 1)
            y = scale(row, height, -1.0, 1)
            c = x + y*1j
            if inMSet(c,25) == True:
                image.plotPoint(col, row)
    image.saveFile()
    


