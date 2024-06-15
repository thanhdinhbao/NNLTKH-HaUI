def isPrim(n):
    if n > 1:
        for i in range(2, n): # có thể cho chạy tới sqrt(n)
            if n % i == 0:
                return False
        return True
    return False


def isSymmetry(n):
    k = 8  # tìm k là số chữ số của n
    while n//(10 ** k) == 0: k = k - 1

    t = (k+1)//2
    for j in range(t):
        if n % 10 == n // (10 ** k):
            n = n % (10 ** k) // 10
            k = k - 2
        else:
            return False
    return True


S = int(input("Start number: "))
E = int(input("End number  : "))
while E <= S:
    print("E > S please !")
    E = int(input("End number  : "))
TOTAL = 0
for i in range(S, E+1):
    if isPrim(i) and isSymmetry(i):
        TOTAL += i
print("TOTAL: ", TOTAL)