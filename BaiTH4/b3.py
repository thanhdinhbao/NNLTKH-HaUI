def readtovariable(filename):
    a = []
    n = m = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        for i in range(n):
            k = f.readline().split()
            for i in range(len(k)):
                k[i] = float(k[i])
            a.append(k)
    return a, n, m



def columnavg(a, n, m, i):
    if i >= m:
        print('Data with ', m, 'columns !')
        return
    else:
        total = 0.0
        for j in range(n):
            total += a[j][i]
        return total/n


a, n, m = readtovariable('D:/iris.txt')
print(n)
print(m)
print(a)

col = int(input("Column = "))
k = columnavg(a, n, m, col)
print("AVG = ", k)
    