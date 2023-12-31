from collections import Counter

def anak_nakal(nama_anak):
    hitung = Counter(nama_anak)
    urutan = sorted(hitung.items(), key=lambda x: x[1], reverse=True)
    if urutan[0][1] == 1:
        return "Semuanya anak baik"
    paling_nakal = [nama for nama, jumlah in urutan if jumlah == urutan[0][1]]
    return " dan ".join(paling_nakal) + " Nakal"

print(anak_nakal(["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]))
print(anak_nakal(["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]))
print(anak_nakal(["Aisyah" , "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang" , "Hana", "Indra", "Jihan"]))
