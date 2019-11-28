import sys

vowels = "aeiou"

for words in sys.stdin:
    for word in words.split():
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