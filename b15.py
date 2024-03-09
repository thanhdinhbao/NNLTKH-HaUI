import  math

def sont(n):
    """Ham kiem tra so nguyen to"""
    if n <= 1:
        return False

    for i in  range(2,n):
        if n % i ==0:
            return False
    return True

def sodx(n):
    """Ham kiem tra so doi xung"""
    return str(n) == str(n)[::-1]

def check_valid(n):
    """Ham check valid"""
    return sont(n) and sodx(n)

def main():
    n =  int(input("Nhap n: "))
    if len(str(n)) != 6:
        print("So nhap vao khac 6 chu so!")
    else:
        if check_valid(n) == True:
            print("So n la so hop le")
        else:
            print("So n la so khong hop le")

if __name__ == "__main__":
    main()

