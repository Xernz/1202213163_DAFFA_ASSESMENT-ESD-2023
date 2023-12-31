import itertools

def hitung_kombinasi_username(nama_lengkap, panjang_max):
    # Menggabungkan karakter lowercase dari nama lengkap
    karakter = [char.lower() for char in nama_lengkap.replace(" ", "")]

    # Menghitung kombinasi untuk setiap panjang username hingga panjang_max
    total_kombinasi = 0
    for panjang in range(1, panjang_max + 1):
        kombinasi = list(itertools.product(karakter, repeat=panjang))
        total_kombinasi += len(kombinasi)

    return total_kombinasi

# Nama lengkap
nama_lengkap = "Naip Lovyu"

# Panjang username maksimal
panjang_max = 6

# Menghitung jumlah kombinasi username
jumlah_kombinasi = hitung_kombinasi_username(nama_lengkap, panjang_max)

print(f"Jumlah kombinasi username yang mungkin: {jumlah_kombinasi}")
