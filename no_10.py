def hitung_kembalian(total_pembayaran, total_belanja):
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    kembalian = total_pembayaran - total_belanja

    hasil = {}

    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah_pecahan = kembalian // pecahan
            kembalian -= jumlah_pecahan * pecahan
            hasil[str(pecahan)] = jumlah_pecahan

    return hasil

print(hitung_kembalian(10000, 7500))
print(hitung_kembalian(5000, 1100))
print(hitung_kembalian(178000, 90500))
