def user_choice():
    while True:
        choice = input("Do you want to give words separately or in a list?\n\t[l - list, w - single word]\n")
        choice = choice.lower()
        if choice in ('l', 'w'):
            return choice
        print('Invalid input.')


def single_words(word):
    vowels = "aeiouy"
    word = word.lower()
    vowelcount = 0
    counter = 0
    while counter < len(word):
        for letter in word:
            if letter in vowels:
                vowelcount += 1
            counter += 1
    return vowelcount


def lists(word):
    vowels = "aeiouy"
    counter = 0
    vowelcount = 0
    word = word.lower()
    while counter < len(word):
        if word[counter] in vowels:
            vowelcount += 1
        counter += 1
    else:
        return vowelcount, word


def printing_result(number, word):
    if number == 1:
        print("There is", number, "vowel in '" + word + "'\n")
    else:
        print("There are", number, "vowels in '" + word + "'\n")

