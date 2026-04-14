import requests

print("== MATERI 13 - JSON API ==")
print("-" * 40)
# Swt Target Url Ke API Al-Adhan
url = "https://api.aladhan.com/v1/timingsByCity/28-08-2025?city=Jakarta&country=Indonesia&method=5"
respone = requests.get(url) # Http Get (Ambil Data)
data_json = respone.json() # Ambil Data Sebagai Format Json
print("Jadwal Sholat:", data_json)
print(data_json)
jadwal_sholat = data_json["data"]["timings"]
print(f"-> Shubuh = {jadwal_sholat["Fajr"]}")
print(f"-> Maghrib = {jadwal_sholat["Maghrib"]}")
print(f"-> Isya = {jadwal_sholat["Isha"]}")