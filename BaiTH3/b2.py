def listinput():
    n = int(input("n="))
    a = [0]*n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a

def matrixfromlist(a):
    n = int(input("n="))
    m = int(input("m="))
    b = []
    if n*m > len(a):
        print('Can not create matrix !')
    else:
        for i in range(n): 	#có n dòng trong ma trận
            k = a[i*m:i*m + m]
            b.append(k)	#thêm dòng k vào ma trận b
    return b

#chương trình chính
a = listinput()
print(a)
b = matrixfromlist(a)
print("matrix", b)