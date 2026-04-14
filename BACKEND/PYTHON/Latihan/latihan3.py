print("====== PROFIL DIGITAL ======")
nama= input ("nama mu:")
umur= int (input("umur mu:"))
kelas= input ("kelas:")
hobi=input("hobi mu:")
citaCita=input("cita cita mu:")
waktuBelajar=input("waktu belajar faforit mu (siang/malam):")
if waktuBelajar== "siang":
    print("aku sukanya malam")
else:
    print("sama donk...")
hitungUmur=2025 - umur

print("====== TYPE DIGITAL ======")
print("1. wibu")
print("2. k-popers")
print("3. anak konten")
print("4. anak nongki")
print("5. gamer")
p = (input("gaya digital kamu:"))
if (p == "1"):
    waifuMu=input("sebutkan waifu mu:")
    print("pasti asyik nonton anime,apalagi di anime nya ada karakter",waifuMu)
elif (p == "2"):
    biasMu=input("Siapa bias kamu:")
    print("lumayan juga selera bias mu...")
elif (p == "3"):
    platformMu=input("Platform favorit kamu? TikTok? YouTube?")
    print("kapan kapan ngonten bareng yuk..")
elif (p == "4"):
    NongkrongPalingSering=input("Nongkrong paling sering di mana?")
    print("emangnya di",NongkrongPalingSering,"wort it") 
else :
    gameMu=input("apa game faforit mu :")
    print("Wih, kamu pasti jago main",gameMu,"sambil ngoding. GG gaming!")
teman=input("apakah teman sebelah mu bau:")
print("====== FUN CHECK ======")
if teman=="tidak":
    print("aman berarti...")
else:
    print("Aduh... kasih pewangi darurat dong, darurat nasional ini")


print("====== PROFIL DIGITAL ======")

print ("nama:",nama)
print("umur:",umur)
print("kelas:",kelas)
print("hobi:",hobi)
print("cita cita:",citaCita)
print("waktu faforit untuk belajar:",waktuBelajar)
print(f"lahir tahun: {hitungUmur}\n")

print("====== TYPE DIGITAL ======")
if p =="1":
    print("type:wibu")
    print("waifu:",waifuMu)
    print(f"komentar:pasti asyik nonton anime,apalagi di anime nya ada",waifuMu,"\n")
elif p == "2":
    print("type:k-popers")
    print("bias:",biasMu)
    print(f"komentar:lumayan juga selera bias mu...\n")
elif p == "3":
    print("type:anak konten")
    print("platform:",platformMu)
    print(f"komentar:kapan kapan ngonten bareng yuk..\n")
elif p == "4":
    print("type:anak nongki")
    print("tempat nongkrong:",NongkrongPalingSering)
    print(f"komentar:emangnya di",NongkrongPalingSering,"wort it\n") 
else :
    print("type:gamer")
    print("game:",gameMu)
    print(f"komentar:Wih, kamu pasti jago main",gameMu,"sambil ngoding. GG gaming!\n")
print("====== FUN CHECK ======")
print("teman di sebelah mu:",teman)
print("Aduh... kasih pewangi darurat dong, darurat nasional ini")