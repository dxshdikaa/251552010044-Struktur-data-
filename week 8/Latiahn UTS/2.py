data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

hasil = []

for i in data:
    if i not in hasil:
        hasil.append(i)

print(hasil)