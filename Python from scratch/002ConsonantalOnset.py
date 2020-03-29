# Write a program that prints the consonantal onsets of the words 'smell', 'amoc', 'wrap', 'joyous'.

words_list = ["smell", "amoc", "wrap", "joyous"]
vowels = "aeiou"

el = 0
while el < len(words_list):
    word = words_list[el]
    for i in word:
        if i in vowels:
            print("")
            break
        else:
            print(i, end = "")
    el += 1