def Angles(number):
    angle = int(input(str(number) + ".Enter The Angle\n"))
    return angle

angle1 = Angles(1)
angle2 = Angles(2)
angle3 = Angles(3)

def process():
    total = angle1 + angle2 + angle3
    if total == 180:
        print("Bu Bir Üçgendir")
    else:
        print("Bu Bir Üçgen Değildir")
process()