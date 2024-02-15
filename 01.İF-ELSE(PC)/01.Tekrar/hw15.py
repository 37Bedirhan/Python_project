vote = input("Sinemayami gitmek istersin (s), Tiyatroyami gitmek istersin (t)  : ")
student = input("Öğrenci misiniz(E/H) : ")
fee = 0

if vote == 's':
    fee = 15 
elif vote == 't':
    fee = 10 


if student =='E' or student =='e':
    fee= fee / 2  

print("Ödemeniz gereken ücret :{}".format(fee))
