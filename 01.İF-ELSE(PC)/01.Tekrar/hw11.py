def lenght():
    uzunluk1=int(input("1. UZUNLUĞU GİRİNİZ :"))
    uzunluk2=int(input("2. UZUNLUĞU GİRİNİZ :"))
    uzunluk3=int(input("3. UZUNLUĞU GİRİNİZ :"))

    if uzunluk1 == 60 and  uzunluk2 == 60 and uzunluk3 == 60 :
        print("Bu Bir Eşkenar Üçgendir")
    elif uzunluk1 == uzunluk2 or uzunluk1 == uzunluk3 or uzunluk2 == uzunluk3 :
        print("Bu Bir İkizkenar Üçgendir")
    else :
        print ("Bu Bir Çeşitkenar üçgendir")
lenght()