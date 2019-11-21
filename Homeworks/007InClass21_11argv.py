import sys

arguments = sys.argv[1:]
vowels = "aeiou"

for word in arguments:
    counter = 0
    vowelcount = 0
    while counter < len(word):
        if word[counter] in vowels:
            vowelcount += 1
        counter += 1
    else:
        print("There are", vowelcount, "vowels in", word)
