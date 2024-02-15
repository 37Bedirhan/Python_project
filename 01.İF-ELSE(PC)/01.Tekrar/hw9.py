weather=int(input("HAVA SİCAKLİĞİNİ GİRİNİZ(°C) :"))

if weather <= 5 :
    print("Soğuk")
elif weather == 6 or weather < 14:
    print("ILIK")
elif weather >= 15 :
    print("Sicak")