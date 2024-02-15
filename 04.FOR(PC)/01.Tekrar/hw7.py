def value():
    nm=int(input("SAYIYI GİRİNİZ :"))
    value=1
    for factorial in range(nm):
        value= value * (factorial+1)

    print("SAYININ FAKTORİYELİ ", value)
value()
