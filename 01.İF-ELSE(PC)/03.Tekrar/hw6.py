def user_number():
    number = int(input("Sayıyı Giriniz\n"))
    return number

def full_partition():
    number = user_number()
    if number  %3 == 0 and number %5 == 0:
        print("15'e tam bölünür")
    else:
        print("15'e tam bölünmez")
full_partition()
