# fibonacci
fibonacci = [1, 1]

sayi = int(input("sayi: "))
yeni_eleman = 0

while yeni_eleman < sayi:
    yeni_eleman = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(yeni_eleman)

if sayi in fibonacci:
    print(f"{sayi} bir fibonacci sayisidir.")
else:
    print(f"{sayi} bir fibonacci sayisi degildir.")
