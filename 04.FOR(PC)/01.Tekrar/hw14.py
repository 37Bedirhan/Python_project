import random
def numbers() :
    i_chose_number= random.randint(1,20)

    while True:
        guess_number= int(input("SAYIYI TAHMİN EDİNİZ :\n"))
        if i_chose_number < guess_number :
            print ("SAYINIZI AZALTARAK TEKRAR GİRİNİZ ")
        if i_chose_number > guess_number :
            print ("SAYINIZI ARTIRARAK TEKRAR GİRİNİZ ")
        if i_chose_number == guess_number :
            print("TEBRİKLER DOĞRU SONUCA ULAŞTINIZ")
        break
numbers()

