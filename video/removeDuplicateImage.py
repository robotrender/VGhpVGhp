import hashlib
import os

# Tạo một dict để lưu trữ hash của các file
hashes = {}

# Duyệt qua tất cả các file trong thư mục hiện tại và các thư mục con
count = 0
for root, dirs, files in os.walk("."):
    for filename in files:
        # Tính toán hash của file và lưu vào dict
        full_path = os.path.join(root, filename)
        with open(full_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
            if file_hash in hashes:
                # Xóa file trùng lặp
                os.remove(full_path)
                print('(+) Đã xóa: ', full_path)
                count += 1
            else:
                hashes[file_hash] = full_path

# Hiển thị kết quả
duplicates = {k: v for k, v in hashes.items() if isinstance(v, list)}
print(f'(+) Đã xóa: {count} tệp')
if not duplicates:
    print("Không có file trùng nhau trong thư mục hiện tại")
else:
    print("Các file trùng nhau:")
    for file_hash, filenames in duplicates.items():
        print(f"Hash: {file_hash}")
        for filename in filenames:
            print(f"\t{filename}")
