antrian = ['Laporan', 'Foto', 'Tugas']

print("Antrian :", antrian)

while antrian:
    cetak = antrian.pop(0)
    print("Cetak :", cetak, "| Sisa :", antrian)