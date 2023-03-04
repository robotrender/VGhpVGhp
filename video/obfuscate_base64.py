import os
import hashlib
import base64

# Lấy đường dẫn thư mục hiện tại
current_dir = os.getcwd()

# Lặp lại các tệp trong thư mục hiện tại
for filename in os.listdir(current_dir):
    if not filename.endswith(".py"):  # Không đổi tên các tệp có đuôi .py
        # Lấy đường dẫn đầy đủ của tệp
        filepath = os.path.join(current_dir, filename)

        # Tạo mã băm MD5 của tên tệp
        hash_object = hashlib.md5(filename.encode())
        new_filename = hash_object.hexdigest()

        # Đổi tên tệp thành mã băm MD5
        os.rename(filepath, os.path.join(current_dir, new_filename) + '.' +filename.split('.')[-1])

# Tạo danh sách tên tệp mới
new_filenames = [f for f in os.listdir(current_dir) if not f.endswith(".py")]
new_filenames_b64 = [base64.b64encode(f.encode()).decode().replace('==', '/',).replace('"', '') for f in new_filenames]
# Tạo biến chứa mã bash64 của các tên tệp mới nối nhau bởi "JCR5Jl55eXl5JCR5JT8jQCEh"
b64_names = base64.b64encode("JCR5Jl55eXl5JCR5JT8jQCEh".join(new_filenames_b64).encode()).decode()
print(b64_names)
open('../output.txt', 'w').write(b64_names)
