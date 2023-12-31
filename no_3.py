urutan_kedatangan = ["Ningguang", "Hutao", "Xiao", "Childe"]
bersih = []
suspect = urutan_kedatangan
bukti_foto = "Xiao"

for teman in urutan_kedatangan:
    if teman != bukti_foto:
        bersih.append(teman)
    else:
        for hapus in bersih:
            suspect.remove(hapus)
        break

print("Suspect kemungkinan: ")
print(suspect)