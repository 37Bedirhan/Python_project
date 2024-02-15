important_phones = {"Acil Çağrı Merkezi":112 , "Polis İmdat":155 , "Milli Eğitim Bakanlığı İletişim Merkezi":4440632}
important_phones1 = important_phones.copy()
def subtracting_values():
    print(important_phones)
subtracting_values()

def delete_the_list():
    important_phones.clear()
    print(important_phones)
delete_the_list()

def emergency_call_center_delete():
    important_phones.remove("Acil Çağrı Merkezi")
    print(important_phones1)
emergency_call_center_delete()

def find_ministry_of_health_contact_center():
    say = important_phones1.count("Sağlık Bakanlığı İletişim Merkezi")
    print(say)
find_ministry_of_health_contact_center()

def important_informations():
    important_phones1.clear()
    print(important_phones1)
