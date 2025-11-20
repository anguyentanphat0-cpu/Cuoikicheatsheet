# Nhập tên file từ người dùng
filename = input("Enter a file name: ")

# Mở file để đọc
try:
    fhand = open(filename)
except:
    print("File không tồn tại:", filename)
    quit()

# Đọc từng dòng và in ra chữ in hoa
for line in fhand:
    line = line.rstrip()      # bỏ ký tự xuống dòng
    print(line.upper())       # in ra bằng chữ hoa
