kg = int(input("Kullanilacak bagaj miktarini giriniz (KG) :"))
if kg <= 20:
    print("UCRET odemenize gerek yok")
else: 
    fazladan_kg = kg - 20
    fazladan_ucret = fazladan_kg *10
    print("EKSTRA'DAN" ,fazladan_ucret, "TL Kadar odemeniz yeterlidir")