print("----------------------------------")
print("=== MATERI 9 PYTHON 3 FUNCTION ===")
print("----------------------------------")

#======== LAMDA ========
def hello_world(name):
    print("hello Mr.",name)
    print(f"how are you doing {name}?")

hello_world("azka")
hello_world("ali")
hello_world("haarits")

#FUNGSI ANONIM DENGAN 'LAMBDA'
print("------- LAMDA -------")
greeting = lambda name:print(f"hello {name} with lambda")
greeting("azmi")
greeting("zaky")
greeting("karim")

print("----- KONFERSI TYPE DATA -----")
nilai_string = "1000"#type data string
nilai_integer = int(nilai_string)# int (ubah jadi integer)
kalikan_dua_salah = nilai_string * 2
kalikan_dua_benar = nilai_integer * 2
print("yang salah:",kalikan_dua_salah)
print("yang benar:",kalikan_dua_benar)

# MAP : UNTUK MENTRANSFORMASI DATA

nilai_mentah = [100,95.5,90,88.3,81.9]
nilai_dibulatan = map(lambda nilai: round(nilai), nilai_mentah)
list_nilai_dibulatkan = list (nilai_dibulatan)
print(f"nilai mentahan:: {nilai_mentah}")
print(f"nilai di bulatkan: {list_nilai_dibulatkan}")

# SORTED : MENGURUTKAN DATA
daftar_siswa=[
    {"nama": "haarits", "angka": 8},
    {"nama": "dzaky", "angka": 77},
    {"nama": "abdul", "angka": 25},
    {"nama": "hanif", "angka": 26},
]
print("DAFTAR ANGKA ASLI",daftar_siswa)
daftar_siswa_terurut= sorted(daftar_siswa, key=lambda siswa:siswa ['angka'])
for siswa in daftar_siswa_terurut:
    print(siswa)