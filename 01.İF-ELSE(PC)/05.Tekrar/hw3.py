kilogram=int(input("Kaç tane bagaj hakki istersiniz (KG cinsinden) :"))

if kilogram <= 20 :
    print ("Fazladan ucret odemenize gerek yok.")
else:    
    fazladan_kilogram= kilogram - 20
    fazladan_ucret= fazladan_kilogram *10
    print("Ek olarak {}TL odemeniz gerekmektedir".format(fazladan_ucret))
