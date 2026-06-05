angka = [34, 7, 23, 5, 62]
 
terbesar = angka[0]
terkecil = angka[0]

for nilai in angka:
    if nilai > terbesar:
        terbesar = nilai
        
    if nilai < terkecil:
        terkecil = nilai
        
print("terbesar :", terbesar)
print("terkecil :", terkecil)