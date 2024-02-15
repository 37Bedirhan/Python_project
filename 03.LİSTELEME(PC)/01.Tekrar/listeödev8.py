Ders=["B","İ","L","İ","Ş","İ","M"]
alan_listesi= Ders.copy()
yeni_ders= Ders.copy()


Ders.sort()
print(Ders)

Ders.reverse()
print(Ders)

say=yeni_ders.count("İ , İ")
print(say)

yeni_ders.remove(yeni_ders[-2 and-3])
print(yeni_ders)

print("alan_listesi:",alan_listesi)

Ders.clear()
print(Ders)

print(yeni_ders.index("L"))