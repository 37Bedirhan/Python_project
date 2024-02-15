Note1 = int(input("Birnci notunuzu giriniz :"))
Note2 = int(input("Ikinci notunuzu giriniz :"))
performance = int(input("performans notunuzu giriniz :"))
ortalamasi= (Note1+Note2+performance)/3
if ortalamasi >= 50:
    print ("Başarili")
else:
    print("Başarisiz")