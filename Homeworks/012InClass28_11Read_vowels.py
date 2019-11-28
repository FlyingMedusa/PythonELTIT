
vowels = "aeiou"

file = open('test.txt', 'r')
data = file.read()
for word in data.split():
    counter = 0
    vowelcount = 0
    while counter < len(word):
        if word[counter] in vowels:
            vowelcount += 1
        counter += 1
    else:
        if vowelcount == 1:
            text = 'There is 1 word in: "{}"\n'.format(word)
        else:
            text = 'There are {} words in: "{}"\n'.format(vowelcount, word)
        print(text)

file.close()