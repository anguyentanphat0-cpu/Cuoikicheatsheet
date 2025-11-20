# spam_confidence.py

# Nhập tên file
filename = input("Enter the file name: ")

try:
    fhand = open(filename)
except:
    print("File không tồn tại:", filename)
    quit()

count = 0
total = 0.0

for line in fhand:
    line = line.strip()
    # Chỉ xử lý dòng bắt đầu bằng 'X-DSPAM-Confidence:'
    if not line.startswith('X-DSPAM-Confidence:'):
        continue

    # Tìm vị trí dấu ':' và lấy phần số phía sau
    colon_pos = line.find(':')
    number_str = line[colon_pos + 1:].strip()
    value = float(number_str)

    count += 1
    total += value

# Tính trung bình và in kết quả
if count > 0:
    print("Average spam confidence:", total / count)
else:
    print("Không tìm thấy dòng X-DSPAM-Confidence trong file.")
