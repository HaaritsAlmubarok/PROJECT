import doa_sehari_hari

print("doa bangun tidur : ",doa_sehari_hari.doa_bangun_tidur())
print("doa sebelum tidur : ",doa_sehari_hari.doa_sebelum_tidur())
print("doa sebelum makan : ",doa_sehari_hari.doa_sebelum_makan())
print("doa sesudah makan : ",doa_sehari_hari.doa_sesudah_makan())

import hitung_uang
jajan = [50000, 30000, 15000, 70000, 10000]

print(hitung_uang.tambah_bonus(jajan))

uang_lebih_besar = hitung_uang.filter_boros(jajan)
print(uang_lebih_besar)