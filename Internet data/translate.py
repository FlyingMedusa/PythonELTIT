from googletrans import Translator


def main():
    translator = Translator()
    result = translator.translate('Jak się masz?', dest='fr')
    print(result.text)


main()