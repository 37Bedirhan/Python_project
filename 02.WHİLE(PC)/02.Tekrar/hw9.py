total= 0 
desired= 0
number= 123



while number != 1 : 
    number= int(input("SAYI GİRİNİZ :"))
    desired += 1
    total += number

ort= total / (desired -1)
print("sayilarin ortalamasi: {}".format(desired))
