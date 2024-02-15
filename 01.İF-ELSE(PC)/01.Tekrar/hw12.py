def guest_information() :
    size = float(input("Boyunuzu Giriniz\n"))
    kg = int(input("Kilonuzu Giriniz\n"))
    VKİ= kg/(size*size)
    if 18 > VKİ < 25 :
        print("Normal Düzeydesiniz")
    elif 25 > VKİ < 30 :
        print("Kilolu Düzeydesiniz")
    elif 30 > VKİ :
        print("Obeziteli Bir Bireysiniz")
    elif 35 > VKİ :
        print("Ciddi Bir Obeziteye Sahipsiniz")
guest_information()