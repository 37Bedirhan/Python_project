size = float(input("Enter The Size \n"))
weight = float(input("Enter The Weight \n"))
vki = size*size / weight  

def User_Kilo() :
    if  vki == 18 or vki == 25 :
        print("Normal")
    elif vki == 25 or vki == 30 :
        print("Kilolu")
    elif vki == 30 or vki == 35 :
        print("Obez")
    elif vki > 35 :
        print("Ciddi Obez")
User_Kilo()