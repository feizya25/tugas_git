data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {
            "padi": 1200,
            "jagung": 800,
            "kedelai": 500
        }
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {
            "padi": 1500,
            "jagung": 900,
            "kedelai": 450
        }
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {
            "padi": 1100,
            "jagung": 750,
            "kedelai": 600
        }
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {
            "padi": 1300,
            "jagung": 850,
            "kedelai": 550
        }
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {
            "padi": 1400,
            "jagung": 950,
            "kedelai": 480
        }
    }
}

#1
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for komoditas, jumlah in data['hasil_panen'].items():
        print(f"  {komoditas.capitalize()}: {jumlah} kg")
    print()

#2
hasil_jagung_lok2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"\nJumlah panen jagung dari lokasi2 (Kebun B): {hasil_jagung_lok2}")

#3
nama_lok3 = data_panen["lokasi3"]["nama_lokasi"]
print(f"Nama lokasi dari lokasi3: {nama_lok3}")

#4
hasil_padi = {}
hasil_kedelai = {}
for lokasi, data in data_panen.items():
    hasil_padi[lokasi] = data['hasil_panen']['padi']
    hasil_kedelai[lokasi] = data['hasil_panen']['kedelai']

print("\nHasil panen padi per lokasi:", hasil_padi)
print("Hasil panen kedelai per lokasi:", hasil_kedelai)

#5
hasil_padi_lok1 = data_panen["lokasi1"]["hasil_panen"]["padi"]
hasil_kedelai_lok1 = data_panen["lokasi1"]["hasil_panen"]["kedelai"]

hasil_padi_lok2 = data_panen["lokasi2"]["hasil_panen"]["padi"]
hasil_kedelai_lok2 = data_panen["lokasi2"]["hasil_panen"]["kedelai"]

hasil_padi_lok3 = data_panen["lokasi3"]["hasil_panen"]["padi"]
hasil_kedelai_lok3 = data_panen["lokasi3"]["hasil_panen"]["kedelai"]

hasil_padi_lok4 = data_panen["lokasi4"]["hasil_panen"]["padi"]
hasil_kedelai_lok4 = data_panen["lokasi4"]["hasil_panen"]["kedelai"]

hasil_padi_lok5 = data_panen["lokasi5"]["hasil_panen"]["padi"]
hasil_kedelai_lok5 = data_panen["lokasi5"]["hasil_panen"]["kedelai"]

print(f"\nHasil panen padi lokasi1: {hasil_padi_lok1}, kedelai: {hasil_kedelai_lok1}")
print(f"\nHasil panen padi lokasi2: {hasil_padi_lok2}, kedelai: {hasil_kedelai_lok2}")
print(f"\nHasil panen padi lokasi3: {hasil_padi_lok3}, kedelai: {hasil_kedelai_lok3}")
print(f"\nHasil panen padi lokasi4: {hasil_padi_lok4}, kedelai: {hasil_kedelai_lok4}")
print(f"\nHasil panen padi lokasi5: {hasil_padi_lok5}, kedelai: {hasil_kedelai_lok5}")

#6
print("\nStatus dari Lokasi:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")

#banch baru