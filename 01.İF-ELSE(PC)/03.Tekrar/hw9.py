def weather_information():
    temperature = input("Hava Sıcaklığı Giriniz\n")
    return temperature

def learning_air_temperature():
    temperature = weather_information()

    if temperature <= "5":
        print("Soğuk")
    elif temperature == "6" or temperature < "14":
        print("Ilık")
    elif temperature >= "15":
        print("Sıcak")
learning_air_temperature()