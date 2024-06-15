def readtoscreen(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        n, m = f.readline().split()
        print(n, m)
        n = int(n)
        for i in range(n):
            print(f.readline(), end = '')


def readtovariable(filename):
    a = []
    n = m = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        a = []
        for i in range(n):
            k = f.readline().split()
            for i in range(len(k)):
                k[i] = float(k[i])
            a.append(k)
    return a, n, m


def countzero(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                count += 1
    return count



def columnavg(a, col):
    total = 0.0
    for i in range(len(a)):
        total += a[i][col]
    return total/len(a)


def replace(a):
    for col in range(len(a[0])):
        t = columnavg(a, col)
        for row in range(len(a)):
            if a[row][col] == 0:
                a[row][col] = t
    return a



def create2file(a, filename1, filename2):
    with open(filename1, mode='w', encoding='utf-8') as f1:
        f1.write(str(100) + ' ')
        f1.write(str(len(a[0])) + '\n')
        for i in range(100):
            for j in range(len(a[0])):
                f1.write(str(a[i][j]) + ' ')
            f1.write('\n')
    with open(filename2, mode='w', encoding='utf-8') as f2:
        f2.write(str(len(a)-100) + ' ')
        f2.write(str(len(a[0])) + '\n')
        for i in range(101, len(a)):
            for j in range(len(a[0])):
                f2.write(str(a[i][j]) + ' ')
            f2.write('\n')



readtoscreen('D:/image.data')
a, n, m = readtovariable('D:/image.data')
print(n)
print(m)
print(a)
print('Số phần tử 0: ', countzero(a))
a = replace(a)
print(a)
create2file(a, 'D:/image1.data', 'D:/image2.data')


import os
import shutil
os.mkdir('D:/BAI45')
shutil.copy('D:/image1.data', 'D:/BAI45')
shutil.copy('D:/image2.data', 'D:/BAI45')
os.remove('D:/image1.data')
os.remove('D:/image2.data')