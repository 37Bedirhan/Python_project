Toplam = 0
saymak = 0

while True:
    sayi = int(input("Bir sayi giriniz: "))
    if sayi == 1:
        break
    Toplam += sayi
    saymak += 1

if saymak > 0:
    ortalama = Toplam / saymak
    print("Girilen sayilarin ortalamasi:", ortalama)
else:
    print("Hiç sayi girilmedi.")
