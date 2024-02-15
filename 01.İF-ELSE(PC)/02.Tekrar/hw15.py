def request():
    preference = input("Cinema(c) or Theatre(t) \n")
    return preference
def take():
    information = input("Student(s) or Not(n) \n")
    return information
def price():
    preference = request()
    information = take()
    total = 0
    if preference == "c" :
         total = 15
    elif preference == "t":
        total = 10

    if information == "s" or information == "S":
        total = total / 2

    print("ödemeniz gereken ücret{}TL".format(total))
price()