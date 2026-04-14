#list --> [] --> berurutan,berubah,duplikat
print("===============================================")
daftarBelanja = [
    "es teh desa",#index 0
    "olive",#index 1
    "gorengan",#index 2
    ]
print("daftar belanja:",daftarBelanja)
print(daftarBelanja[0])

#append() menambah item ke akhir list
daftarBelanja.append("gabin")
print("daftar belanja skrg:",daftarBelanja)

#insert() menambahkan item ke spesifik index
daftarBelanja.insert(3,"naspad")
print("daftar belanja:",daftarBelanja)

#remove() menghapus item berdasarkan value
daftarBelanja.remove("olive")
print("daftar belanja akhir:",daftarBelanja)

#[no_Index:no_urut_item]
print("potong list",daftarBelanja[1:3])

#menggabungkan dua list +
jajananHaarits=["pisang kembung","molen"]
jajananZaki=["pentol","macaroni"]
gabunganJajanan=jajananHaarits+jajananZaki
print("gabungan jajanan:",gabunganJajanan)
print("zakiNambah",jajananZaki * 2)

#Tuple --> () --> berurutan,berubah,tidak duplikat
ttl=("Depok",10,"Januari",2002)
print("TTL Hamka:",ttl)
print("Tgl lahir:",ttl[1])

#unpacking tuple ke variable baru
#harus berurutan sesuai value nya
tempatLahir,TglLahir,BlnLahir,ThnLahir=ttl
print("tempat lahir:",tempatLahir)
print("Tgl lahir",TglLahir)

#list multi dimensi
daftarMinuman=[
["kopi","teh","susu jahe"],#baris 0
["jus apel","jus melon","jus mangga"],#baris 1
["es campur","es doger","es teler"],#baris 2
]
print(daftarMinuman)
#cara memmanggilnya yaitu dengan menulis barisnya terlebih dahulu [0] kemudian indexnya [2] maka yang akan keluar adalah "susu jahe"
print("es faforit haarits:",daftarMinuman[0][2])


#================ LEN ================ (untuk menghitung panjang)
data_nama = ["daffa","fawwaz","yanto","ridho"]
print(len(data_nama))

#================ INSERT ================== (untuk menambah (di mana saja))
data_nama.insert(0,"hamka")
print(data_nama)

#================ APPEND ==================== (untuk menambah (di akhir))
data_nama.append("evan")
print(data_nama)

#================ REMOVE =================== (untuk menhapus value yang di masukkan)
data_nama.remove("ridho")
print(data_nama)

#================ POP =================== (untuk menghapus yang paling akhir)
data_nama.pop()
print(data_nama)

#================ EXTEND ================== (untuk menggabung dua data)
data_baru=("jamal","ridwan")
data_nama.extend(data_baru)
print(data_nama)

my_tuple=("daffa","fawwaz","yanto","rodho")
my_tuple.append("hamka")