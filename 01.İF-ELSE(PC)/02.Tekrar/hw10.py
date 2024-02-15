remaining_time = float(input("Enter The Remaining Time: \n"))
money = 0 

def Auto_Park_time():
    if remaining_time<=1:
        print("Ödemeniz gereken ücret:",+5)
    if remaining_time>1 <=5:                                                                                            
        print("Ödemeniz gereken ücret:",remaining_time*4)
    elif remaining_time>5:
        print("Ödemeniz gereken ücret:",remaining_time*3)
Auto_Park_time()