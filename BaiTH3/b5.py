def strlistinput():
    n = int(input("n="))
    a = ['0']*n
    for i in range(n):
        a[i] = input('a[{}] = '.format(i))
    return a

def tuplefromlist(a):
    b = tuple(a)
    return b

def numcount(a):
    d = 0
    for x in a[:]:
        if x.isnumeric():
            d += 1
    return d


a = strlistinput()
b = tuplefromlist(a)
print(b)
print(type(b))
print("Numerical form = ", numcount(b))

