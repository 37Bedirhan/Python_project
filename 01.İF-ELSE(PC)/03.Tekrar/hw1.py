def information():
    note1 = int(input("Enter The  note1\n"))
    note2 = int(input("Enter The  note2\n"))
    performance = int(input("Enter The Performance note\n"))

    average = note1 + note2 + performance
    return average

def situation():
    average = information()
    if average >= 50:
        print("Başarılı")
    else:
        print("Başarısız")
situation()
