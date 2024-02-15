def infortmation() :
    total= 0
    number1=int(input("1. SAYIYI GİRİNİZ :"))
    number2=int(input("2. SAYIYI GİRİNİZ :"))
    
    for numbers in range(number1, number2 +1):
            total += numbers
            ort= total / (number2 - number1 +1)
            print("SAYILARIN ORTALAMASI :{}".format(ort))
infortmation()