import  math

x = float(input("Nhap so thuc x: "))
n = int(input("Nhap vao so nguyen n: "))

S = 0

if n%2 ==0:
    S = 2016*x
    for i in range(2,n+1):
        S+= (x**i)/(3**(i-1))
else:
    S = 0

print("Tong S la: ", S)