def mainlist():
    dictionary = ["Biliminsanı:Aziz Sancar", "Şair:Mehmet Akif Ersoy", "Astronom:Ali Kuşçu"]
    dictionary1 = dictionary.copy()
    dictionary2 = dictionary.copy()
    jobs = dictionary.copy()
    add_list = ["Matematikçi: Cahit Arf"]
    return [dictionary , jobs , add_list , dictionary1 , dictionary2]

def print_values():
    jobs = mainlist()
    print("meslekler =",jobs)
    print(jobs)
print_values()

def clear_values():
    jobs = mainlist()
    jobs.clear()
    print(jobs)
clear_values()

def add_value():
    dictionary , add_list= mainlist()
    dictionary.extend(add_list)
    print(dictionary)
add_value()
def Is_there_any_artist():
    dictionary1 = mainlist()
    say = dictionary1.count("sanatcı")
    print(say)
Is_there_any_artist()
def value_change():
    dictionary1 = mainlist()
    dictionary1.pop(0)
    dictionary1.extend("Biliminsanı:Canan Dağdeviren")
value_change()
def print_the_value_in_the_poet():
    dictionary2 = mainlist()
    dictionary2.pop(0)
    dictionary2.pop(2)
    print(dictionary2)
print_the_value_in_the_poet()
