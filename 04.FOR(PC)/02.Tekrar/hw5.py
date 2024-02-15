number1 = int(input("1. Sayiyi Giriniz \n"))
number2 = int(input("2. Sayiyi Giriniz \n"))
total=0

for n in range (number1,number2 +1) :
    total+= n

print(f"İki Sayinin Arasindaki Sayilarin Toplami {total}")