# mukemmel sayi
sayi = int(input("sayi: "))
bolen_toplami = 0

for i in range(1, sayi):
    if sayi % i == 0:
        bolen_toplami += i
if bolen_toplami == sayi:
    print(f"{sayi} mukemmel sayidir.")
else:
    print(f"{sayi} mukemmel sayi degildir.7")
