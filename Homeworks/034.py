
def givemeleet(text):
    table = str.maketrans("abcdefghijklnostz", "48[)3v6#!¿X1^0572")
    result = text.lower().translate(table)
    return result


output = givemeleet("This is some text I wanna edit")
print(output)