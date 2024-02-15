def getAngle(number):
    angle = int(input(str(number) + ". Enter The Angel  \n"))
    return angle


angle1 = getAngle(1)
angle2 = getAngle(2)
angle3 = getAngle(3)


def process_Angles() :
    if angle1 == angle2 == angle3 :
        print("This is an equilateral triangle .")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle1 :
        print("This is an isosceles triangle .")
    else :
        print("This is a scalene triangle .")
process_Angles()