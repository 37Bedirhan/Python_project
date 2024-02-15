def information(): 
    name = str(input("Adinizi Giriniz\n"))
    wage = int(input("Maaşinizi Giriniz\n"))
    work_year = int(input("Çalişma Yilinizi Giriniz\n"))
    if 0 > work_year < 5 : 
        increased_salary = wage * 10 / 100
    elif 6 > work_year < 10 :
        increased_salary = wage * 15 / 100
    elif work_year <= 11  :
        increased_salary = wage * 25 / 100
        print(f"{name},İSİMLİ ÇALIŞANIMIZ ZAMLI MAAŞINIZ {increased_salary} TL")
information()
