import convert_currency.counter as counter
mile = float(input("Nhập số dặm bay: "))
uint_price = float(input("Số tiền/ dặm: "))
k = mile*uint_price
print("Số tiền phải trả là", k, "VND")
print("=", counter.toUSD(k), "USD")
print("=", counter.toEUR(k), "EUR")
print("=", counter.toRUB(k), "RUB")
print("=", counter.toJPY(k), "JPY")
