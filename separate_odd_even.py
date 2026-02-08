ciftSayiList = []
tekSayiList = []
dizi = []

eleman = 0
n = int(input("n adet sayı giriniz: "))

while eleman != n:
    x = int(input("dizi elemalarını giriniz: (virgülle ayırınız) "))
    dizi.append(x)
    eleman += 1

for sayi in dizi:
    if sayi % 2 == 0:
        ciftSayiList.append(sayi)
    else:
        tekSayiList.append(sayi)

print(ciftSayiList)
print(tekSayiList)