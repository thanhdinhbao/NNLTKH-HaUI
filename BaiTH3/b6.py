a = ('123', '456', '789', '012')
b = tuple(float(x) for x in a[:])
print(b)
TOTAL = 0
for x in b[:]:
    TOTAL += x
print("AVERAGE: ", TOTAL/len(b))