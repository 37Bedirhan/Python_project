product1 = int(input("Enter the price of the first product \n"))
product2 = int(input("Enter the price of the second product \n"))

total = product1 + product2

def product_process() :
    if total <= 200 :
        print(f"Amount of payment {total}TL")
    elif total > 200 :
        next_total = total / 4
        print(f"Amount of payment,after discount{next_total}TL")
product_process()
