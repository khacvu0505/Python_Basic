# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# (Bộ sưu tập sắp xếp có thứ tự và k thể thay đổi chúng. Cho phép giá trị lặp lại)
# Không thể xóa hay thay đổi từng item bên trong tuple nhưng có thể xóa tuple


# Simple tuple
fruit_tuple=('Appple','Orange','Mango')

# Using constructor
# fruit_tuple=tuple(('Appple','Orange','Mango'))

# Get single value 
# print(fruit_tuple[0])

# Can not change value ==> Error
# fruit_tuple[0]='Banana'

# Tuples with value should value tralling command
# (Tuples nếu chỉ có 1 giá trị thì nên có dấu , ngoài sau nếu k nó chỉ là 1 chuỗi)
fruit_tuple_2=('Apple',)

# Delete Tuples
del fruit_tuple_2

# Get length of tuple
# print(len(fruit_tuple_2))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# (Bộ sưu tập không có thứ tự và không được lặp chỉ mục(index) và không có item(thành viên) trùng lặp)

# Create Set
fruit_set={'Apple','Orange','Mango'}

# Check if in set(Kiểm tra apple có tồn tại trong fruit_set )
print('Apple' in fruit_set) # => Boolean

# Add to set
fruit_set.add('Vũ')

# Remove from set
fruit_set.remove('Apple') 

# Clear set(Clear rỗng)
fruit_set.clear()

# Delete set(Xóa luôn)
del fruit_set

print(fruit_set)