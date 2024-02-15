odd_numbers = [5,7,9,11,13,15]
Even_numbers = [6,8,10,12,14,16]
new_odd_numbers = odd_numbers.copy()
new_Even_numbers = Even_numbers.copy()
def number_combining():
    odd_numbers.extend(Even_numbers)
    print(odd_numbers)
number_combining()

def finding_number():
    odd_numbers.remove(5)
    odd_numbers.remove(9)
    odd_numbers.remove(11)
    odd_numbers.remove(13)
    odd_numbers.remove(15)
    Even_numbers.remove(6)
    Even_numbers.remove(8)
    Even_numbers.remove(10)
    Even_numbers.remove(12)
    Even_numbers.remove(16)
print(odd_numbers,Even_numbers)
finding_number()
def finding_numbers_in_two_lists():
    new_odd_numbers.remove(5)
    new_odd_numbers.remove(7)
    new_odd_numbers.remove(9)
    new_odd_numbers.remove(11)
    new_odd_numbers.remove(15)
    new_odd_numbers.remove(6)
    new_odd_numbers.remove(8)
    new_odd_numbers.remove(14)
    new_odd_numbers.remove(16)
print(new_odd_numbers,new_Even_numbers)
finding_numbers_in_two_lists()




