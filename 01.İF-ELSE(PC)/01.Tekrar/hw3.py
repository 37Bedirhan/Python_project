kilo = int(input("Bagajinizi girin (kg):"))

if kilo <=20:
    print("Herhangi bir ücret ödemeniz gerekmiyor")
else:
    ek_kilo  = kilo - 20
    ek_ucret = ek_kilo * 10
    print("Fazla bagaj için {} TL ödemelisiniz.".format(ek_ucret)) 
