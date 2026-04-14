print(f"\n")
print(f"==== HITUNG UANG ====\n")
def tambah_bonus(uang_list):
    uang_tambah = list(map(lambda uang: uang + 5000,uang_list))

    return uang_tambah

def filter_boros(uang_list):
    uang_boros = list(filter(lambda uang_gede: uang_gede >= 50000,uang_list))

    return uang_boros