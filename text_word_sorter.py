# alfabetik sira
# metin: Hitit Universitesi Bilgisayar Mühendisliği

metin = input("metin girin: ")

kelimeler = metin.split()

for i in range(len(kelimeler)):
    for j in range(i + 1, len(kelimeler)):
        if kelimeler[i] > kelimeler[j]:
            kelimeler[i], kelimeler[j] = kelimeler[j], kelimeler[i]

for kelime in kelimeler:
    print(kelime)
