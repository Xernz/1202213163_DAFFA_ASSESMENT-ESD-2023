produk = [
    {"nama": "TV", "kategori": "elektronik", "harga": 1000},
    {"nama": "headphone", "kategori": "elektronik", "harga": 200},
    {"nama": "baju", "kategori": "fashion", "harga": 50},
    {"nama": "gitar", "kategori": "musik", "harga": 300},
    {"nama": "sepatu", "kategori": "olahraga", "harga": 80},
    {"nama": "kamera", "kategori": "elektronik", "harga": 600}
]
pelanggan = [
    {"nama": "Rina", "minat": ["elektronik", "musik"], "beli": ["TV", "headphone"]},
    {"nama": "Budi", "minat": ["fashion", "musik"], "beli": ["baju", "gitar"]},
    {"nama": "Hartono", "minat": ["olahraga", "elektronik"], "beli": ["sepatu", "kamera"]}
]
produk_rekomendasi = []
def rekomendasi(minat):
    for search in minat:
        for record in produk:
            if record["kategori"] == search:
                produk_rekomendasi.append(record["nama"])

while True:
    nama = input("Masukkan nama pelanggan: ")
    for p in pelanggan:
        if p["nama"] == nama:
            global minat;
            minat = p["minat"]
            
    rekomendasi(minat)
    print(produk_rekomendasi) 
    break
