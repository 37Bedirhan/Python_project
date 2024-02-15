def user_plate():
    number_plate_code = input("Plaka Kodunu Giriniz\n")
    return number_plate_code

def where_is_the_city():
    number_plate_code = user_plate()

    if number_plate_code == "6" or "06":
        print("Ankara")
    elif number_plate_code == "7" or "07":
        print("Antalya")
    elif number_plate_code == "8" or "08":
        print("Artvin")
    else:
        print("Türkiye")
where_is_the_city()