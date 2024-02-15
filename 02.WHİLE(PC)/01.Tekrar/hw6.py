başlangiç = int(input("Başlangiç sayisini giriniz: "))
son = int(input("Bitiş sayisini giriniz: "))

toplam = 0
ilk = başlangiç

while ilk <= son:
    toplam += ilk
    ilk += 1

print("Toplam:", toplam)