def listinput():
    n = int(input("n="))
    a = [0]*n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a

def mergesortedlist(a, b):
    c = []
    i = 0               #i chạy trên a
    j = 0               #j chạy trên b
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    if i < len(a):
        for t in range(i, len(a)):
            c.append(a[t])
    if j < len(b):
        for t in range(j, len(b)):
            c.append(b[t])
    return c

a = listinput()		#chú ý: a cần được sắp tăng
b = listinput()		#chú ý: b cần được sắp tăng
c = mergesortedlist(a, b)
print(c)