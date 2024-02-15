name = input("Enter The Name \n")
wage = float(input("Enter The Wage \n"))
working_year = float(input("Enter The Working Year \n"))
increased_salary = 0

def İnterest() :
    if working_year == 0 or  working_year == 5 :
        increased_salary = wage * 10 / 100
    elif working_year == 6 or working_year == 11 :
        increased_salary = wage *15 / 100
    elif working_year >= 11 :
        increased_salary = wage * 25 / 100
    total = increased_salary + wage
    print(f"Dear {name} your increased salary {total} TL ")
İnterest()