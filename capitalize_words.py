# bas harfleri buyut
# Metin: hitit universitesi bilgisayar mühendisliği
metin = input("metin giriniz: ")
yeni_cumle = ""
kelimeler = metin.split()

for kelime in kelimeler:
    kelime = kelime.capitalize()
    yeni_cumle += kelime + " "

print(yeni_cumle)