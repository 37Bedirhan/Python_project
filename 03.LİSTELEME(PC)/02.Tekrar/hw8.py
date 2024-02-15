def letters():
    lesson = ["B","İ","L","İ","Ş","İ","M"]
    lesson2 = lesson.copy()
    lesson3 = lesson.copy()
    area = lesson.copy()
    return lesson , lesson2 , lesson3 , area
def arrangementletters():
     lesson , lesson2 , lesson3 , area = letters()

     lesson.sort()
     print(lesson)

     lesson2.reverse()
     print(lesson2)

     say =lesson.count("İ")
     print(say)

     lesson3.pop(4)
     lesson3.pop(3)
     print(lesson3)

     print("alan listesi =",area)

     lesson.clear()
     print(lesson)

     print(area.index("L"))


arrangementletters()