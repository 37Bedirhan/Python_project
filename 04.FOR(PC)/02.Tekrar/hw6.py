number1 = int(input("1. Sayiyi Giriniz \n"))
number2 = int(input("2. Sayiyi Giriniz \n"))
total = 0
for n in range(number1,number2+1) :
    total+= n 
    ort = total /(number1 + number2 +1)

print(f"Girdiğiniz İki Sayinin Arasindaki Sayilarin Ortalamasi {ort}")
