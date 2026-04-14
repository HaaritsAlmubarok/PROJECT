print("MATERI 7B - PYTHON DATA STRUCTURE")
print("=================================")
# Set --> {} --> tidak berurutan,berubah,tidak dupilikat
game_haarits={"ML","FF"}
game_evan={"Ganshin","GTA","ML"}

#.add = menambahkan item baru
game_haarits.add("Valorant")
game_haarits.add("PUBG")

#.remove = untuk menghapus item
game_evan.remove("GTA")

#.len = untuk menghitung jumlah item
print("haris ada",len(game_haarits),"game",game_haarits)
print("evan ada",len(game_evan),"game",game_evan)

#.union = untuk menggabungkan 2 set yang berbeda
game_berdua=game_haarits.union(game_evan)
total_game=len(game_berdua)
print("semua game ada",total_game,"game",game_berdua)

#.intersection = untuk mencari game yang sama
#.difference = untuk mencari game yang berbeda
game_kembar=game_haarits.intersection(game_evan)
game_beda=game_haarits.difference(game_evan)
total_game_kembar=len(game_kembar)
total_game_beda=len(game_beda)
print("game yang kembar:",total_game_kembar,"game",game_kembar)
print("game yang berbeda:",total_game_beda,"game",game_beda)

koleksi_anime={
    "re_zero": "subaru",
    "one_piece": "usop",
    "waifu": {
        "re_zero": "rem-chan",
        "demon_slayer": "nezuko"
    }
}
print("koleksi anime:",koleksi_anime)
print("MC one piece;",koleksi_anime["one_piece"])
koleksi_anime["naruto"]="boruto"
koleksi_anime["one_piece"]="zoro"
koleksi_anime["waifu"]["re_zero"]="rem kanan"
print("koleksi anime skrg:",koleksi_anime)