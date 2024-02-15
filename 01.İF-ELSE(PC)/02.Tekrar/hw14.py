def getNumber(number) :
    numbers = int(input(str(number) +". sayıyı girin \n"))
    return numbers

number1 = getNumber(1)
number2 = getNumber(2)
number3 = getNumber(3)


def getBigNumber():
    if number1 > number2  and number1 > number3 :
        print(number1)
    elif number2 > number1 and  number2 > number3 :
        print(number2)
    elif number3 > number1 and number3 > number2 :
        print(number3)
    else :
        print("all equal")
getBigNumber()
