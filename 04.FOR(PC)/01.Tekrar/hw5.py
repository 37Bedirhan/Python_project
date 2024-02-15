

number1 = int(input('Lütfen ilk sayiyi giriniz :'))
number2 = int(input('Lütfen ikinci sayiyi giriniz :'))
toplam= 0

def n() :
    for numbers in range (number1,number2 +1):
        toplam += numbers
n()

print(f"Sayilarin Toplami: {toplam}")