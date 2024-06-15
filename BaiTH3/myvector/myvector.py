def vecinput():
    n = int(input("n="))
    a = [0]*n
    for i in range(n):
        a[i] = int(input('a[{}] = '.format(i)))
    return a

#cách 2 dùng append
def vecinput():
    n = int(input("n="))
    a = []
    for i in range(n):
        a.append(int(input('a[{}] = '.format(i))))
    return a

#Dùng để nhập nhiều mảng khác nhau: thêm biến name
def vecinput(name):
    n = int(input("Kích thước:"))
    a = [0]*n
    for i in range(n):
        a[i] = int(input('{}[{}] = '.format(name, i)))
    return a
#chú ý lúc gọi, ví dụ: a = vecinput(‘a’),
#b = vecinput(‘b’)

def vecinsert(a, p, v):
    if p < 0 or p > len(a):
        print("Position error !")
    else:
        a.insert(p, v)
    return a

def vecdel(a, v):
    if a.count(v) > 0:
        a.remove(v)  	#chỉ xóa được 1 phần tử
			#chú ý: nếu xóa hết: 	t    return ahay if bằng while




def vecsum(a):
    total = 0.0
    for i in a[:]:
        total += i
    return total

def vecadd(a, b):
    res = []
    if len(a) == len(b):
        for i in range(len(a)):
            res.append(a[i] + b[i])
    return res