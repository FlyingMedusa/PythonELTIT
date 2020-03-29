filename = 'test.txt'

vowels = 'aeiou'


with open(filename, 'r') as fopen:
    words = fopen.readlines()

for line in words:
    for word in line.split():
        counter = 0
        vowelcount = 0

        while counter < len(word):

            if word[counter] in vowels:
                vowelcount += 1
            counter += 1
        else:
            if vowelcount == 1:
                text = 'There is 1 vowel in: "{}"\n'.format(word)
            else:
                text = 'There are {} vowels in: "{}"\n'.format(vowelcount, word)
            print(text)

