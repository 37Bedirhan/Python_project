kg = int(input("Gereken bagaj hakkinizi giriniz (kg cinsinde) :"))

if kg <=20:
    print("Fazladan ucret odemenize gerek yok")
else:
    additional_kg = kg - 20
    additional_fee = additional_kg *10
    print("Ekstra kargo ucreti", additional_fee, "TL'dir.")
