import cdtg


def main():
    dam = float(input("Nhập số dặm bay: "))
    tien = float(input("Nhập số tiền VND/1 dặm bay: "))
    tongtien = dam * tien

    print("Tổng số tiền phải trả bằng VNĐ:", tongtien)

    usd = cdtg.vnd_to_usd(tongtien)
    eur = cdtg.vnd_to_eur(tongtien)
    jpy = cdtg.vnd_to_jpy(tongtien)

    print("Số tiền đổi ra USD:", usd)
    print("Số tiền đổi ra EUR:", eur)
    print("Số tiền đổi ra JPY:", jpy)


if __name__ == "__main__":
    main()
