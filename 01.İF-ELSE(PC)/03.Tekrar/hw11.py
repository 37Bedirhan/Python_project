def Get_Angle(number):
    angle = int(input(str(number)+ ".Açıyı Giriniz\n"))
    return angle

angle1 = Get_Angle(1)
angle2 = Get_Angle(2)
angle3 = Get_Angle(3)

def Triangle_Type():
    if angle1 == angle2 == angle3:
        print("Bu Bir Eşkenar Üçgendir")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Bu Bir İkizkenar Üçgendir")
    else:
        print("Bu Bir Çeşitkenar Üçgendir")
Triangle_Type()