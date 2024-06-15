import counter
import point

print("Nhập tọa độ điểm A:")
x1, y1 = point.getPoint()
print("Nhập tọa độ điểm B:")
x2, y2 = point.getPoint()
print("Nhập tọa độ điểm C:")
x3, y3 = point.getPoint()

k = counter.checkMin(x1, y1, x2, y2, x3, y3)
print(k)
q = counter.checkMax(x1, y1, x2, y2, x3, y3)
print(q)
print("Diện tích tam giác ABC: ", counter.arcage(x1, y1, x2, y2, x3, y3))