import requests
# pip --version
# pip install requests
target_url = "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
print(f"Target URL: {target_url}")

# HTTP GET (Ambil Data)
response = requests.get(target_url)
# Konversi Data ke JSON
data_json = response.json()
# print(f"Response Data: {data_json}")
print("   JADWAL SHOLAT")
print("=" * 20)
jadwal = data_json['data']['timings']
shubuh = jadwal['Fajr']
dzuhur = jadwal['Dhuhr']
ashar = jadwal['Asr']
maghrib = jadwal['Maghrib']
isya = jadwal['Isha']
print(f"- Shubuh  : {shubuh}")
print(f"- Dzuhur  : {dzuhur}")
print(f"- Ashar   : {ashar}")
print(f"- Maghrib : {maghrib}")
print(f"- Isya'   : {isya}")
