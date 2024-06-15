import math
a = int(input("a = "))
isNT = True
#Check so nguyen to
for i in range(2, a):
    if a % i == 0:
        isNT = False

#Check doi xung
isDX = True
n = 6
while a // (10 ** n) == 0: n = n-1

k = int((n + 1) / 2)
for i in range(1, k + 1):
    if a % 10 == a//(10**n):
        a = a % (10**n) // 10
        n = n - 2
    else:
        isDX = False
#In ket qua
if isNT and isDX:
    print("So hop le")
else:
    print("So khong hop le !")