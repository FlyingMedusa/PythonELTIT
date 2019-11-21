import sys

vowels = "aeiou"
line = 1

for words in sys.stdin:
    print("This is line", line)
    line += 1
    for word in words.split():
        counter = 0
        vowelcount = 0
        while counter < len(word):
            if word[counter] in vowels:
                vowelcount += 1
            counter += 1
        else:
            print("There are ", vowelcount, " vowels in '", word,"'", sep='')