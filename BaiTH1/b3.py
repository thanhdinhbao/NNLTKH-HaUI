import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a==0:
    if b==0 and c==0:
        print("Pt bac 1 - vo so nghiem")
    elif b==0 and c !=0:
        print("PT bac 1 - Vo nghiem")
    else:
        print("Pt bac 1 co nghiem: X = ", -c/b)
else:
    delta = b*b - 4*a*c
    if delta<0:
        print("Vo nghiem")
    elif delta==0:
        print("Nghiem kep: ", -b/(2*a))
    else:
        print("X1 = ", (-b + math.sqrt(delta))/(2*a))
        print("X2 = ", (-b - math.sqrt(delta))/(2*a))