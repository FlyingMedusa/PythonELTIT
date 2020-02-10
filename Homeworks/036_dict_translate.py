import re

def mytranslate(text, dict):
    for el in dict.keys():
        text = re.sub(el, dict[el], text)
    return text


dict1 = {'a': '4', 'b': '8'}
word1 = mytranslate('banana', dict1)
print(word1)  # prints "84n4n4"

dict2 = {'a': '@'}
word2 = mytranslate('banana', dict2)
print(word2)  # prints "b@n@n@"
