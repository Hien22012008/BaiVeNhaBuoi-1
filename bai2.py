def tim_so_lon_thu_hai(arr):
    # Loại bỏ các phần tử trùng lặp
    arr_unique = list(set(arr))
    # Sắp xếp mảng theo thứ tự giảm dần
    arr_sorted = sorted(arr_unique, reverse=True)
    # In ra "Not found" nếu không tìm thấy
    if len(arr_sorted) < 2:
        return "Not found"
    else:
        # Trả về phần tử thứ hai
        return arr_sorted[1]

# Yêu cầu người dùng nhập số lượng phần tử và các phần tử của danh sách
n = int(input("Nhập số lượng phần tử n: "))
arr = []
print(f"Nhập {n} số nguyên:")
for i in range(n):
    arr.append(int(input()))

# Gọi hàm và in kết quả
result = tim_so_lon_thu_hai(arr)
print(f"Số lớn thứ hai là: {result}")
