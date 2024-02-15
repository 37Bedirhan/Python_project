def values():
    value1 = ["3","1","2"]
    return value1

def new_values():
    value1 = values()
    value1.pop(0)

    value1.insert(0,"1")
    print(value1)
new_values()