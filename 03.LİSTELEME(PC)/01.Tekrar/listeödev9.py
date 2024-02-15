numbers=[35,26,81,64]
numbers2=numbers.copy()
numbers3=numbers.copy()
numbers4=numbers.copy()
ondalikli_sayilar=[1.4 , 6.8]




numbers.sort(reverse=True)
print(numbers)

numbers2.reverse()
print(numbers2)

say=numbers2.count(26)
print(say)

numbers3.remove(81)
print(numbers3)

numbers3.clear()
print(numbers3)

print(numbers4.index(64))

ondalikli_sayilar.extend(numbers)
print(ondalikli_sayilar)





