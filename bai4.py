def kiem_tra_so_nguyen(a):
    if a.is_integer():
        print("Integer")
    else:
        print("Not integer")

a = float(input("Nhập một số thực a: "))
kiem_tra_so_nguyen(a)