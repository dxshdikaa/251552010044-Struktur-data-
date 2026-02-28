# Membuat dictionary
user = {
"name": "Fadhli",
"age": 27,
"role": "DevOps"
}

# Mengakses value berdasarkan key
print("Nama:", user["name"])
print("Usia:", user["age"])
print("Peran:", user["role"])

# Menambah key-value baru
user["email"]= "abc@example.com"

# Mengubah value
user["age"] = 28

# Hasil akhir
print(user)