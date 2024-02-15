def main_list():
    numbers = ["35","26","81","64"]
    numbers1 = numbers.copy()
    numbers2 = numbers.copy()
    numbers3 = numbers.copy()
    numbers4 = numbers.copy()
    numbers5 = numbers.copy()
    new_numbers = numbers.copy()
    decimal_numbers = ["1.4", "6.8"]
    return [numbers , numbers1 , new_numbers , numbers2 , decimal_numbers , numbers3 , numbers4, numbers5]

def from_big_to_small():
    numbers = main_list()
    numbers.sort(reverse=True)
    print(numbers)
from_big_to_small()

def opposite():
    new_numbers = main_list()
    new_numbers.reverse()
    print(new_numbers)
opposite()


def How_many_do_you_have():
    numbers1 = main_list()
    say=numbers1.count("26")
    print(say)


def deletion():
    numbers2 = main_list()
    numbers2.remove("81")
    print(numbers2)


def alldeletion():
    numbers3 = main_list()
    numbers3.clear()
    print(numbers3)


def finding_index():
    numbers4 = main_list()
    print(numbers4.index(64))


def combining_list():
    numbers5 = main_list()
    decimal_numbers = main_list()
    numbers5.append(decimal_numbers)
    print(numbers5)
combining_list()