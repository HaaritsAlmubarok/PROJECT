import requests # mengimport module requests
print(f"\n")

url1 =f"https://api.alquran.cloud/v1/ayah/2:255/quran-simple" # texs ayatb kursi
url2 =f"https://api.alquran.cloud/v1/ayah/2:255/en.asad" # teks terjemahan bahasa inggris

response1 = requests.get(url1)
data_json_ayat = response1.json() # .json di gunakan untuk menubah menjadi dectionary python

ayat = data_json_ayat["data"]
print(f"                     ===== AYAT  KURSI =====\n")
print(ayat["text"])
print(f"\n")

response2 = requests.get(url2) 
data_json_terjemah= response2.json()

data_terjemah = data_json_terjemah["data"]
print(f"                    ===== TERJEMAH EN =====\n")
print(data_terjemah["text"])
print(f"\n")