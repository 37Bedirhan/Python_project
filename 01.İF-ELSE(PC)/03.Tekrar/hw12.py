def Body_Mass_Index():
    weight = input("Kilonuzu Giriniz\n")
    Lenght = input("Boyunuzu Giriniz(Metre)\n")
    vki = weight / Lenght * Lenght
    return weight,Lenght,vki

def Whats_The_Condition():
    weight,Lenght,vki = Body_Mass_Index()

    if 18 < vki < 25:
        print("Durumunuz Normal")
    elif 25 < vki < 30:
        print("Durumunuz Kilolu")
    elif vki >= 30:
        print("Durumunuz Obez")
    elif vki >= 35:
        print("Durumunuz Ciddi Obez")
Whats_The_Condition()