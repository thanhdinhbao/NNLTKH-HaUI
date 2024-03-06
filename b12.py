import math

print("Nhap toa do diem A:")
x1 = float(input("Nhap x1: "))
y1 = float(input("Nhap y1: "))

print("Nhap toa do diem B:")
x2 = float(input("Nhap x2: "))
y2= float(input("Nhap y2: "))

def Euclidean(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def Manhattan(x1,x2,y1,y2):
    return math.fabs(x2-x1) + math.fabs(y2-y1)

def Cosin(x1,x2,y1,y2):
    return 1 - ((x1*x2+y1*y2)/(math.sqrt(x1**2+y1**2)*math.sqrt(x2**2+y2**2)))

print("Khoang cach Euclidean giua 2 diem A va B la: ",Euclidean(x1,x2,y1,y2))
print("Khoang cach Manhattan giua 2 diem A va B la: ",Manhattan(x1,x2,y1,y2))
print("Khoang cach Cosin giua 2 diem A va B la: ",Cosin(x1,x2,y1,y2))
