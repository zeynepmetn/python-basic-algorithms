calisanlar = [
{"ad": "Elif", "soyad": "Güneş", "departman": "Yazılım", 'projeler' : {"Proje A": 85,"Proje B": 90,"Proje C": 88}},
{"ad": "Burak", "soyad": "Ak", "departman": "Yazılım", 'projeler' : {"Proje A": 75,"Proje B": 95,"Proje C": 90} },
{"ad": "Zeynep", "soyad": "Mavi", "departman": "Pazarlama", 'projeler' : {"Proje A": 82,"Proje B": 78,"Proje C": 91}},
{"ad": "Kemal", "soyad": "Yeşil", "departman": "Pazarlama", 'projeler' : {"Proje A": 90,"Proje B": 82,"Proje C": 87}}
]
def ortalamanin_ustundekiler(calisanlar):
    proje_a_notlari = [int(calisan['projeler']["Proje A"]) for calisan  in calisanlar]
    proje_b_notlari = [int(calisan['projeler']["Proje B"]) for calisan  in calisanlar]
    proje_c_notlari = [int(calisan['projeler']["Proje C"]) for calisan  in calisanlar]

    a_not_toplam = 0
    b_not_toplam = 0
    c_not_toplam = 0

    proje_a_ortalama_ustu = []
    proje_b_ortalama_ustu = []
    proje_c_ortalama_ustu = []

    #proje A
    for notlar in proje_a_notlari:
        a_not_toplam += notlar
    proje_a_ortalama = a_not_toplam/len(proje_a_notlari)

    for calisan in calisanlar:
        if calisan['projeler']["Proje A"] >= proje_a_ortalama:
            proje_a_ortalama_ustu.append(calisan["ad"]+" "+calisan["soyad"])

    # proje B
    for notlar in proje_b_notlari:
        b_not_toplam += notlar
    proje_b_ortalama = b_not_toplam / len(proje_b_notlari)

    for calisan in calisanlar:
        if calisan['projeler']["Proje B"] >= proje_b_ortalama:
            proje_b_ortalama_ustu.append(calisan["ad"]+" "+calisan["soyad"])

    #proje C
    for notlar in proje_c_notlari:
        c_not_toplam += notlar
    proje_c_ortalama = c_not_toplam / len(proje_c_notlari)

    for calisan in calisanlar:
        if calisan['projeler']["Proje C"] >= proje_c_ortalama:
            proje_c_ortalama_ustu.append(calisan["ad"]+" "+calisan["soyad"])

    print("Proje A'de ortalama performans puanının üstünde puan alan çalışanlar:", ', '.join(proje_a_ortalama_ustu))
    print("Proje B'de ortalama performans puanının üstünde puan alan çalışanlar:", ', '.join(proje_b_ortalama_ustu))
    print("Proje C'de ortalama performans puanının üstünde puan alan çalışanlar:", ', '.join(proje_c_ortalama_ustu))

ortalamanin_ustundekiler(calisanlar)