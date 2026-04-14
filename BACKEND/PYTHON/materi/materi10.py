import csv

print(f"\n")
print("==== OPEN & EXTRAK CSV ====")
konsumsi_file_path=r"C:\Users\COMPUTER\OneDrive\Desktop\Python\Latihan\materi-file\anime.csv"
data_konsumsi = [] # List Kosong
with open(konsumsi_file_path, "r") as file_konsumsi:
    # Baca Dengan Fungsi Reader () Dari Modul CSV
    baca_file_konsumsi = csv.reader(file_konsumsi)
    # Extrak Tiap Baris Dengan For Loop Ke List
    for konsumsi in baca_file_konsumsi: