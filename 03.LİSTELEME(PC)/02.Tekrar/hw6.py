def before_sentence():
    sentence = ["sanat" ,"sanat" , "içindir"]
    return sentence

def after_sentence():
    sentence = before_sentence()
    sentence.pop(1)

    sentence.insert(1,"toplum")
    print(sentence)
after_sentence()
