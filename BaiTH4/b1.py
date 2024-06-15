def matrixinput():
    n = int(input("n="))
    m = int(input("m="))
    a = []
    for i in range(n):
        k = [0]*m
        for j in range(m):
            k[j] = float(input('a[{}][{}] = '.format(i, j)))
        a.append(k)
    return a


def writefile(a):
    f = open('D:/MATRIX.txt', mode='w')
    f.write(str(len(a)) + ' ')      #ghi số dòng
    f.write(str(len(a[0])) + '\n')  #ghi số cột

    for i in range(len(a)):
        for j in range(len(a[0])):
            f.write(str(a[i][j]) + ' ')
        f.write('\n')
    f.close()



a = matrixinput()
print(a)
writefile(a)
