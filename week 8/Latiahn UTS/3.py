kalimat = 'apel jeruk apel mangga jeruk apel'

kata = kalimat.split()

hasil = {}

for i in kata:
    if i in hasil:
        hasil[i] += 1
    else:
        hasil[i] = 1

print(hasil)