import json
# untuk membaca file json
print(f"\n")

print(f"      ===== PEMINJAMAN BUKU =====\n")

file_path=r"C:\Users\COMPUTER\OneDrive\Desktop\Python\Json\pinjaman_buku.json"

with open (file_path,"r") as data_pinjaman:
    #         read (membaca saja)
    data_pinjam_buku=json.load(data_pinjaman)
    # with open(...) agar file otomatis tertutup setelah dibaca.
    yang_belum_balik = 0 # menghitung pinjaman yang belum kembali
    total = 0 # menghitung semua pinjaman

    for i in data_pinjam_buku ["anggota"]:  # untuk mengambil nama setiap anggota
    
        for u in i ["pinjam"]:  # untuk mengambil data setiap buku yang di pinjam

            total += 1
            if u ["kembali"] == False : # (Jika kembali = False) maka tampilkan siapa dan buku apa yang belum dikembalikan
                yang_belum_balik += 1 # untung menghitung buku yang belum kembali dan di masuk kan ke variable (yang_belum_balik)
                print(f"-{i['nama']} : {u['judul']} ({u['tanggal']})")
print(f"\n")
print(f"  total = {total}    |    yang belum kembali = {yang_belum_balik}\n")