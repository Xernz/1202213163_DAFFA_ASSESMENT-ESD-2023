list_menu = [{"menu": "ayam goreng krispi", "tipe": "makanan", "harga": 15000},
        {"menu": "ayam puk puk", "tipe": "makanan", "harga": 13000},
        {"menu": "ayam bakar", "tipe": "makanan", "harga": 20000},
        {"menu": "es teh", "tipe": "minuman", "harga": 5000},
        {"menu": "es jeruk", "tipe": "minuman", "harga": 7000}
        ]
pesanan = []
found = False
def cari_menu(nama_menu, qty):
    for record in list_menu:
        if record["menu"] == nama_menu:
            global found; found = True
            if record["tipe"] == "minuman":
                total = record["harga"]*qty
                pajak = total*0.3
                bersih = total+pajak
                detail_pesanan = {"menu": nama_menu,"qty": qty,"harga": record["harga"], "pajak": pajak, "bersih": bersih}
                pesanan.append(detail_pesanan)
                print("pesanan ditambahkan")
            elif record["tipe"] == "makanan":
                total = record["harga"]*qty
                pajak = total*0.5
                bersih = total+pajak
                detail_pesanan = {"menu": nama_menu,"qty": qty,"harga": record["harga"], "pajak": pajak, "bersih": bersih}
                pesanan.append(detail_pesanan)
                print("Pesanan Ditambahkan")

while True :
    req = input("Masukkan menu: ")
    qty = int(input("Masukkan jumlah: "))
    cari_menu(req, qty)
    if found == False :
        print("Menu tidak tersedia")
    tambah = input("Pesan lagi? y/n: ")
    if tambah == "y":
        continue
    else: 
        for record in pesanan:
            print(record)
        break


