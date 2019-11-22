import moduleForTask008 as mod

choice = mod.user_choice()

if choice == "w":
    n_words = int(input("How many words do you want to give?\t"))
    for i in range(0,n_words):
        word = input("Give me a word: ")
        n_vowels = mod.single_words(word)
        mod.printing_result(n_vowels, word)

elif choice == "l":
    list = input("Give me a word list separated by spaces: ")
    list = list.split()
    for word in list:
        n_vowels, word = mod.lists(word)
        mod.printing_result(n_vowels, word)
