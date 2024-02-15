def user_computer_information():
    processor = input("İşlemci Bilgisini Giriniz\n")
    ram = input("Ram Bilgisini Giriniz(Gb)cinsinde\n")
    return processor,ram

def computer_proficiency():
    processor,ram = user_computer_information()
    if processor == "i7" or "İ7" and ram == "8":
        print("Kurulum Uygun")
    else:
        print("Kurulum Uygun Değil")
computer_proficiency()