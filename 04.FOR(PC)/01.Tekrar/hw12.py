def account():
    password = input("8 KARAKTERLİK bir şifre giriniz :")

    for p in range(1,8):
        if len(password) < 8 or len(password) > 8 :
            print("8 KARAKTERLİK BİR ŞİFRE GİRMENİZ GEREKMEKTEDİR")
    
        else :
            print("ŞİFRENİZ KAYDEDİLDİ  ŞİFRENİZ:", password)
        break
account() 