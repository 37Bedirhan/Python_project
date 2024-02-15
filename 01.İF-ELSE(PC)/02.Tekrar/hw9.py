temperature = int(input("Enter The temperature(°C):"))

def Temperature_İnformation():
    if temperature <= 5 :
        print("Cold")
    elif temperature == 6 or temperature == 14 :
        print("Warm")
    if temperature >= 15 :
        print("HOT")
Temperature_İnformation()
