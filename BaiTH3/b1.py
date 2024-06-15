from BaiTH3.myvector.myvector import *
from myvector import *
a = vecinput('a')
print(vecsum(a))
a = vecinsert(a, 2, 100)
print(a)
a = vecdel(a, 3)
print(a)
b = vecinput('b')
c = vecadd(a, b)
print(c)