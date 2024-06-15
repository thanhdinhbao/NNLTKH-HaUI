def listinput():
    n = int(input("n="))
    a = [0]*n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a

def mergelist(a, b):
    c = []
    if len(a) <= len(b):
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        for t in range(i+1, len(b)):
            c.append(b[t])
    else:
        for i in range(len(b)):
            c.append(a[i])
            c.append(b[i])
        for t in range(i+1, len(a)):
            c.append(a[t])
    return c
#Chú ý: Sinh viên có thể cải tiến hàm mergelist


a = listinput()
b = listinput()
c = mergelist(a, b)
print(c)
