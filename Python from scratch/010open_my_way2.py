filename = 'test.txt'
vowels = 'aeiou'

with open(filename, 'r') as fopen:
    words = fopen.readlines()

for line in words:
    for word in line.split():
        num_vowels = 0
        for i in range(0,len(word)):
            if word[i] in vowels:
                num_vowels = num_vowels + 1
        print("{} vowels in {}".format(num_vowels, word.upper()))
