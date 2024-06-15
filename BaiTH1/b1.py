n = int(input('Nhap mot so nguyen: '))
while n < 0 or n >= 10000:
	print('n thuoc [0, 9999]. Moi nhap lai: ')
	n = int(input('Nhap mot so nguyen: '))
N = n//1000
T = (n % 1000)//100
C = (n % 100)//10
D = n % 10
print("{} nghin {} tram {} chuc {} don vi".format(N, T, C, D))
