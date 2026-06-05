from collections import deque
d = deque([1, 2, 3]) # deque([1, 2, 3])
# Tambah ke kanan (seperti Queue enqueue)
d.append(4) # deque([1,2,3,4])
# Tambah ke kiri (seperti Stack push dari bawah)
d.appendleft(0) # deque([0,1,2,3,4])
# Hapus dari kanan (seperti Stack pop)
print(d.pop()) # 4 — deque([0,1,2,3])
# Hapus dari kiri (seperti Queue dequeue)
print(d.popleft()) # 0 — deque([1,2,3])
# ROTATE — geser semua elemen
d2 = deque([1,2,3,4,5])
d2.rotate(2) # geser 2 ke kanan
print(d2) # deque([4,5,1,2,3])
d2.rotate(-1) # geser 1 ke kiri
print(d2) # deque([5,1,2,3,4])