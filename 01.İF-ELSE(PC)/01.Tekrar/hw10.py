hour=int(input("KALDIĞINIZ SAATİ GİRİNİZ :"))

if hour <=1 :
    money= 5
elif hour <=5 :
    money= 4* hour
else:
    money= 3* hour

print("ÖDEMENİZ GEREKEN ÜCRET {}TL".format(money))