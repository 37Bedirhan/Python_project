def getdays():
    weekdays = ["Pazartesi" ,"Salı" , "Çarşamba" ,"Perşembe" , "Cuma"]
    return weekdays

def Chosenday():
    weekdays = getdays()
    weekdays.pop(3)
    weekdays.pop(2)
    weekdays.pop(1)
    weekdays.pop(0)
    print(weekdays)
Chosenday()
