import json

print(f"== JSON ==\n")
# Buka file JSON
with open("data_santri.json", "r", encoding="utf-8") as f:
    #encoding = Menerjemahkan teks dari byte di file ke bentuk string Python.
    #
    data = json.load(f)

# Tampilkan data
print("Kelas:", data["kelas"])
print("Daftar Santri:")

for s in data["santri"]:
    print(f"- {s['nama']} | Hafalan: {s['hafalan']}")
