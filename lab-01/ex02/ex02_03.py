#Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
#Kiểm tra xem số đo scos phải số chẵn hay không 
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, " không phải là số chẵn.")