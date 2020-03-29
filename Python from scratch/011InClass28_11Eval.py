front = "aeiy"
back = "ou"

words = input("Give me words with spaces").split()
u_input = input('front or back?')
vowels = eval(u_input)

for word in words:
        counter = 0
        vowelcount = 0
        while counter < len(word):
            if word[counter] in vowels:
                vowelcount += 1
            counter += 1
        else:
            if vowelcount == 1:
                print('-\tThere is', vowelcount, 'vowel in: "' + word + '"\n')
            else:
                print('-\tThere are', vowelcount, 'vowels in: "' + word + '"\n')

# print(eval("'whatever'.upper()"))
#
# text = "'whenever'.upper()"
# result = eval(text)
# print(result)
#
# x = "Tom"
# y = "Dick"
# z = "Harry"
#
# result = input("Type x, y or z: ")
# print(eval(result))