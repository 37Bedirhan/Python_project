def user_information():
    nickname = input("Kullanıcı Adınızı Giriniz :\n")
    password = input("Şifrenizi Giriniz :\n")
    return nickname , password

def account_login():
    nickname,password = user_information()
    if nickname == "türkiye" and password == "1923":
        print("Giriş Başarılı")
    else:
        print("Kullanıcı Adı Veya Şifre Yanlış")
account_login()