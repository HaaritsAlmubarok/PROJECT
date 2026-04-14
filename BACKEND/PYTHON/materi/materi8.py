print("  MATERI 8 - FUNCTION DASAR")
print("==============================")

#struktur fungsi dasar tanpa parameter
def halo_dunia():
    print("Hello world")
    print("Halo dunia")
    print("Ciao mondo")
    print("Привет, мир")
    print("Salut Lume")

#cara akses function,sertakan nama dan () nya
halo_dunia()

#ungsi dengan parameter (variable di fungsi)
def rumus_luas_segi_tiga(alas,tinggi):
    print("alas:",alas)
    print("tinggi:",tinggi)
    rumus_segitiga = 1/2 * (alas * tinggi)
    print("hasil:",rumus_segitiga)
rumus_luas_segi_tiga(8,12)

def rumus_keliling_persegi_pamjang(panjang,luas,tinggi):
    print("panjang:",panjang)
    print("luas:",luas)
    print("tinggi:",tinggi)
    rumus_persegi_panjang = panjang*luas*tinggi
    print("hasil;",rumus_persegi_panjang)
rumus_keliling_persegi_pamjang(20,10,15)

def filter_teman_toxic(nama,sifat):
    #ciri ciri toxic
    sifat_toxic = [
        "sombong",
        "suka meledek",
        "pamer",
        "manipulatif",
        "baperan",
    ]
    if any(kata in sifat for kata in sifat_toxic):
        print(nama,"itu teman toxic, cabut")
    else:
        print(nama, "itu teman baik,gapapa...")

filter_teman_toxic("haarits","rajin,baik hati,tawadhu")
filter_teman_toxic("doni","sombong,dll")