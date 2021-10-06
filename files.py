# Python has functions for creating, reading, updating, and deleting files.

# Open a file
# w:write- ghi đè file(đã có) or thêm mới file(chưa có)
# a:append - Nếu chưa có thì thêm file mới. Còn nếu file đã có thì concat nội dung
my_file = open('myfile.txt', 'w')

# Get some info
print('Name', my_file.name)
print('Is Closed', my_file.closed)
print('Openninh Mode', my_file.mode)

# Write to file
my_file.write('Em Fish oi')
my_file.write(' I love Quyen')
my_file.close()

# Append to file
my_file = open('myfile.txt', 'a')
my_file.write(' I also like em Quyen Ca')
my_file.close()

# Read from file
my_file = open('myfile.txt', 'r+')
text = my_file.read(10)  # chỗ này là đọc file từ đầu => ký tự thứ 10
print(text)