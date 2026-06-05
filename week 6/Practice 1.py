stack = [] # Buat stack kosong
print('Awal:', stack)
# PUSH — tambah elemen ke atas stack
stack.append('A')
stack.append('B')
stack.append('C')
print('Setelah push:', stack)
# PEEK — lihat elemen teratas tanpa hapus
top = stack[-1]
print('Peek:', top)
# POP — hapus dan ambil elemen teratas
popped = stack.pop()
print('Dipop:', popped)
print('Stack:', stack)
# IS EMPTY & SIZE
print('Kosong?', len(stack)==0)
print('Ukuran:', len(stack))