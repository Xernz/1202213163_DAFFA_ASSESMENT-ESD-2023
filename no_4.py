def cek_duplikat(data):
    # Membuat set untuk melacak angka yang sudah ditemukan
    angka_terlihat = set()

    # Iterasi melalui setiap angka dalam data
    for angka in data:
        # Jika angka sudah terlihat sebelumnya, maka ada duplikat
        if angka in angka_terlihat:
            return True
        # Menambahkan angka ke set jika belum terlihat
        else:
            angka_terlihat.add(angka)

    # Jika loop selesai tanpa menemukan duplikat
    return False

# Meminta input dari pengguna dan mengonversinya menjadi list angka
input_data_str = input("Masukkan angka-angka (pisahkan dengan spasi): ")
input_data = [int(angka) for angka in input_data_str.split()]

# Contoh penggunaan fungsi dengan input yang diberikan
hasil = cek_duplikat(input_data)
print(hasil)
