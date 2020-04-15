from googletrans import Translator


def translation(user_input):
    splitted_input = user_input.split("-")

    translator = Translator()
    try:
        print(translator.translate(splitted_input[0], src=splitted_input[2], dest=splitted_input[1]).text)
    except IndexError:
        print(translator.translate(splitted_input[0], dest=splitted_input[1]).text)


def main():
    print("The pattern of translation is as follows:\n"
          "  text to translate-target language-source language(optional)\n"
          "  e.g.\n"
          "  input: Hi, how are you?-de-en\n"
          "  output: Hallo, wie geht es dir?")
    to_translate = input("Please enter your request:\t")
    translation(to_translate)


main()