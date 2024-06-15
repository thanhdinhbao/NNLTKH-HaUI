from math import sqrt
def getPoint():
    x = float(input('Nhập tọa độ x: '))
    y = float(input('Nhập tọa độ y: '))
    return x, y

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)