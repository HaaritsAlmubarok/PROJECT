import json

print(f"== JSON ==\n")
file_json_path = r"C:\Users\COMPUTER\OneDrive\Desktop\Python\Materi\materi_Json.json"
with open(file_json_path, "r") as file_rukun_islam:
    # Baca Dengan Fungsi Load () Dari Module Json
    data_rukun_islam = json.load(file_rukun_islam)
    print(f"judul: {data_rukun_islam['judul']}")
    print(f"jumlah: {data_rukun_islam['jumlah']}")
    print(f"info hal: {data_rukun_islam['info']['halaman']}")
    print(f"info reting: {data_rukun_islam['info']['reting']}")