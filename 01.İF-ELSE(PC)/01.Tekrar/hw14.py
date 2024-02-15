number1 = int(input("1. Sayiyi Giriniz\n"))
number2 = int(input("2. Sayiyi Giriniz\n"))
number3 = int(input("3. Sayiyi Giriniz\n"))
if number1 > number2 and number3 :
    print("EN BÜYÜK SAYI" , number1)
elif number2 > number1 and number3 :
    print("EN BÜYÜK SAYI " ,number2)
elif number3 > number1 and number2 :
    print("EN BÜYÜK SAYI " ,number3)
else:
    print("TÜM SAYILAR BİRBİRİNE EŞİT")