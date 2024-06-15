from point import distance
def checkMax(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, 0, 0)
    d2 = distance(x2, y2, 0, 0)
    d3 = distance(x3, y3, 0, 0)
    m = d1
    if d2 > m:  m = d2
    if d3 > m:  m = d3
    if m == d1: return "Điểm xa O nhất: A"
    if m == d2: return "Điểm xa O nhất: B"
    return "Điểm xa O nhất: C"

def checkMin(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, 0, 0)
    d2 = distance(x2, y2, 0, 0)
    d3 = distance(x3, y3, 0, 0)
    m = d1
    if d2 < m:  m = d2
    if d3 < m:  m = d3
    if m == d1: return "Điểm gần O nhất: A"
    if m == d2: return "Điểm gần O nhất: B"
    return "Điểm gần O nhất: C"

def arcage(x1, y1, x2, y2, x3, y3):
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x2, y2, x3, y3)
    d3 = distance(x3, y3, x1, y1)
    if d1 + d2 > d3 and d2 + d3 > d1 and d3 + d1 > d2:
         return d1 + d2 + d3
    return 0