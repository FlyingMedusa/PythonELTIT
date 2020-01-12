filename = 'alice_for_019task.txt'

word_list = []
wordlengths = {}

#I had problems so I added encoding='utf-8' and now it works
with open(filename, 'r', encoding='utf-8') as f:
    all_lines = f.readlines()

#starts from index 254 (not 255) because lines in text start with 1, but any list starts with index 0
all_lines = all_lines[254:]
for line in all_lines:
    words = line.split()
    for word in words:
        word_list.append(word)

for single_word in word_list:
    letters_num = 0
    single_word = single_word.lower()
    for character in single_word:
        if character.isalpha():
            letters_num += 1
    if letters_num in wordlengths:
        wordlengths[letters_num] += 1
    else:
        wordlengths[letters_num] = 1

with open('output.txt', 'w', encoding='utf-8') as s:
    for length in wordlengths:
        frequency = str(wordlengths[length])
        result = str(length) +":" + frequency + "\n"
        s.write(result)