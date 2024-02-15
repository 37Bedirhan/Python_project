kilo = int(input("Kac (kg) bagaj hakki istersiniz :"))

if kilo <= 20:
    print("Ucret odemeniz gerekmemektedir")
else:    
    additional_kilo = kilo -20
    additional_fee = additional_kilo *10
    print("Fazla bagaj icin {} TL odemelisiniz.".format(additional_fee))
    

