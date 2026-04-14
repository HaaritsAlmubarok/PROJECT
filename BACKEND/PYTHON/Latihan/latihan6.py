# TUGAS KE 1
jadwal_piket=["dani","doni","dono","dino","dunu","deni","danu","dina","dini"]

print("========================")
print("==== PIKET HARI INI ====")
print("========================")
for i in jadwal_piket:
    print(" - ",i)

# TUGAS KE 2
rukun_islam=[
    "syhadat",
    "sholat",
    "zakat",
    "puasa",
    "haji"
    ]

print("=====================")
print("==== RUKUN ISLAM ====")
print("=====================")
for i in range(len(rukun_islam)):
    print(f"{i+1}. {rukun_islam[i]}\n")

rukun_iman=[
    "beriman kepada allah",
    "beriman kepada maklaikat",
    "beriman kepada kitab kitab nya",
    "beriman kepada nabi nya",
    "beriman kepada kodo' dan kodar"
]

print("====================")
print("==== RUKUN IMAN ====")
print("====================")
for i in range(len(rukun_iman)):
    print(f"{i+1}. {rukun_iman[i]}\n")

# TUGAS KE 3
kitab_yang_di_pelajari=[
    "kitab tajwid",
    "kitab fiqih",
    "kitab aqidah"
]
print("================================")
print("==== KITAB YANG DI PELAJARI ====")
print("================================")
for i in range(len(kitab_yang_di_pelajari)):
    print(f"{i+1}. {kitab_yang_di_pelajari[i]}")

# TUGAS KE 4
print("========================")
print("==== BIODATA SANTRI ====")
print("========================")
biodata={
    'nama':'Haarits',
    'kelas':'B-2',
    'hafalan_juz:':'10'
}
for key, value in biodata.items():
    print(f"{key} -> {value}")