# kelime sıralama
# Metin: yüz yüz elma elma yüz armut cilek cilek cilek
metin = input("metin girin: ")

kelimeler = metin.split()

frekans = {}
for kelime in kelimeler:
    if kelime not in frekans:
        frekans[kelime] = 1
    else:
        frekans[kelime] += 1

for kelime, sayi in frekans.items():
    print(f"{kelime} kelimesi metinde {sayi} kez geçiyor.")

