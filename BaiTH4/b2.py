def readtoscreen(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        n, m = f.readline().split()
        print(n, m)
        n = int(n)
        for i in range(n):
            print(f.readline(), end='')


def readtovariable(filename):
    a = []
    n = m = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        for i in range(n):
            k = list(map(float, f.readline().split()))
            a.append(k)
    return a, n, m


readtoscreen('D:/MATRIX.txt')
a, n, m = readtovariable('D:/MATRIX.txt')

print(a)