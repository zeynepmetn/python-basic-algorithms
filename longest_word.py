# en uzun kelime
# Metin: hitit üniversitesindeki en zeki öğrenciler bilgisayar mühendisliği bölümündedir

metin = input("metin giriniz: ")

kelimeler = metin.split()

en_uzun_kelime = ""

for kelime in kelimeler:
    if len(kelime) > len(en_uzun_kelime):
        en_uzun_kelime = kelime

print(en_uzun_kelime)
print(len(en_uzun_kelime))