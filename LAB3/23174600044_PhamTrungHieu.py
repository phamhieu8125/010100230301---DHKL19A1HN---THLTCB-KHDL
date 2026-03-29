#Bai1
#a
tong_a = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong_a += i
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 là:", tong_a)

#b
tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 là:", tong_b)

#Bai2
for j in range(1, 11):
    for i in range(1, 10):
        print(f"{i} x {j:2} = {i*j:2}", end="\t")
    print()

#Bai3
h = int(input("Nhập số hàng: "))
for i in range(h):
    for j in range(i + 1):
        if j == 0 or j == i or i == h - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Bai4
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Yêu cầu nhập lại số nguyên dương!")
    n = int(input("Nhập lại n: "))
S = 0
for i in range(1, n + 1):
    S += 1 / i
print(f"Tổng S = {S:.3f}")

#Bai5
for i in range(1, 1001):
    if (i**0.5) == int(i**0.5):
        print(i, end=" ")

#Bai6
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Giá trị nhập vào phải là số nguyên dương!")
    n = int(input("Vui lòng nhập lại n: "))
S1 = 0
for i in range(1, n + 1):
    S1 += i
print(f"Tổng S1 = 1 + 2 + ... + {n} là: {S1}")

#Bai7
n = int(input("Nhập số nguyên dương n: "))
dem = 0
for i in range(1, n + 1):
    s = str(i)
    tong_chu_so = 0
    for ky_tu in s:
        tong_chu_so += int(ky_tu)
    if tong_chu_so % 2 == 0:
        dem += 1
print(f"Số lượng các số trong khoảng [1, {n}] có tổng chữ số chẵn là: {dem}")

#Bai8
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
max_tong = -1
so_tim_duoc = 0
for i in range(1, n + 1):
    s = str(i) 
    tong_hien_tai = 0
    for ky_tu in s:
        tong_hien_tai += int(ky_tu) 
    if tong_hien_tai > max_tong:
        max_tong = tong_hien_tai
        so_tim_duoc = i
print(f"Số có tổng chữ số lớn nhất trong khoảng từ 1 đến {n} là: {so_tim_duoc}")
print(f"Tổng các chữ số của nó là: {max_tong}")

#Bai9
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))
max_uoc = 0
so_tim_duoc = 0
for i in range(1, n + 1):
    count_uoc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count_uoc += 1
    if count_uoc > max_uoc:
        max_uoc = count_uoc
        so_tim_duoc = i
print(f"Số có nhiều ước nhất trong khoảng từ 1 đến {n} là: {so_tim_duoc}")
print(f"Số lượng ước của nó là: {max_uoc}")

#Bai11
n = int(input("Nhập n số Fibonacci cần in: "))

if n <= 0:
    print("Vui lòng nhập n > 0")
else:
    f1, f2 = 1, 1
    print(f"{n} số Fibonacci đầu tiên là:", end=" ")
    for i in range(1, n + 1):
        if i == 1:
            print(f1, end=" ")
        elif i == 2:
            print(f2, end=" ")
        else:
            f_next = f1 + f2
            print(f_next, end=" ")
            f1 = f2
            f2 = f_next

#Bai12
mapping = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
container = input("Nhập mã container (10 ký tự): ").upper()
if len(container) != 10:
    print("Mã container phải có đúng 10 ký tự!")
else:
    tong_trong_so = 0
    for i in range(10):
        ky_tu = container[i]
        if ky_tu.isdigit():
            gia_tri = int(ky_tu)
        else:
            gia_tri = mapping.get(ky_tu, 0) 
        trong_so = gia_tri * (2**i)
        tong_trong_so += trong_so
        print(f"w{i} = {gia_tri} * 2^{i} = {trong_so}")
    so_du = tong_trong_so % 11
    if so_du == 10:
        so_kiem_tra = 0
    else:
        so_kiem_tra = so_du
    print("-" * 20)
    print(f"Tổng các trọng số: {tong_trong_so}")
    print(f"Số kiểm tra của container {container} là: {so_kiem_tra}")