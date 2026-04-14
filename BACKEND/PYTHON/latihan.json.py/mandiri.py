import json

print(f"== JSON ==\n")
file_json_path = r"C:\Users\COMPUTER\OneDrive\Desktop\Python\latihan.json.py\data_santri.json"
with open(file_json_path, "r") as file_data_santri:

    data_santri = json.load(file_data_santri)
    print(f"kelas: {data_santri['kelas']}")
    print(f"santri: {data_santri['santri'],{'nama'}}")