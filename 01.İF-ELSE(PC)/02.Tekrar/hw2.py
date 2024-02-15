def angles () :
    angle = int(input("1. Açiyi Giriniz \n"))
    angle2 = int(input("2. Açiyi Giriniz \n"))
    angle3 = int(input("3. Açiyi Giriniz \n"))
    total = angle + angle2 + angle3
    return total
angles()


def process(total) :
    if total == 180 :
        print("BU BİR ÜÇGENDİR")
    else :
        print("BU BİR ÜÇGEN DEĞİLDİR")
process()