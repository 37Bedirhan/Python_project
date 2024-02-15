def Time_Spent_In_The_Parking_Lot():
    duration = int(input("Otoparkta kalınan süreyi Giriniz\n"))
    return duration

def Calculating_The_Length_Of_Stay():
    duration = Time_Spent_In_The_Parking_Lot()
    if duration <= 1:
        print("Ödemeniz Gereken Ücret 5TL")
    elif 1 > duration < 5:
        duration += 4
        print(f"Ödemeniz Gereken ücret {duration}TL")
    elif duration > 5 :
        duration +=3
        print(f"Ödemeniz Gereken Ücret {duration}TL")
Calculating_The_Length_Of_Stay()