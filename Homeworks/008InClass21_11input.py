def single_words(word):
    vowelcount = 0
    counter = 0
    while counter < len(word):
        for letter in word:
            if letter in vowels:
                vowelcount += 1
            counter += 1
    return vowelcount

# def lists(list):
#     for word in list.split():
#         counter = 0
#         vowelcount = 0
#         while counter < len(word):
#             if word[counter] in vowels:
#                 vowelcount += 1
#             counter += 1
#         else:
#             return vowelcount, word


vowels = "aeiou"
choice = input("Do you want to give a word or a list? [l - list, w - single word]\n")

if choice.lower() == "w":
    while True:
        word = input("Give me a word: ")
        vowels = single_words(word)
        print("There are", vowels, "vowels in '" + word + "'")

# elif choice.lower() == "l":
#     list = input("Give me a word list separated by spaces: ")
#     vowels, word = lists(list)
#     print("There are", vowels, "vowels in '" + word + "'")



