import csv

# Baca Semua Data Dari CSV                f Di Bawah Ini Berarti Variable
with open("Keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

print("\n")
# 1. Tampilkan Semua Data
print("📌 Semua Data")
print("\n")
print("  Tanggal    | Keterangan  | Kategori     | Jumlah")
print("------------------------------------------------")
for row in data:
    print (f"- {row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | {row['Jumlah']}")

# 2. Hitung Semua Pengeluaran
total = sum(int(row['Jumlah']) for row in data)
print("-------------------------------")
print(f"💰 Total Pengeluaran: Rp.{total}")
print("-------------------------------")
print("\n")

# 3. Kategori Total Per Kategori
kategori_total = {}
for row in data:
    kategori = row["Kategori"]
    jumlah = int(row["Jumlah"])
    if kategori not in kategori_total:
        kategori_total[kategori] = 0
    kategori_total[kategori] += jumlah

print("📊 Pengeluaran Per Kategori :")
print("\n")
print("  Kategori     | Jumlah")
print("-----------------------------")
for kategori, jumlah in kategori_total.items():
    print(f"- {kategori} | Rp.{jumlah}")
print("\n")