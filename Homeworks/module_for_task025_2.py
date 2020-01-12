
def clean_whitespaces(text):
    breaks = '\n\t'
    cleaned_text = ''
    for character in text:
        if character in breaks:
            cleaned_text += ' '
        else:
            cleaned_text += character
    return cleaned_text


def get_sentences(text):
    markers = ".:;!?"
    final_text = []
    elem = ""
    for character in text:
        if character not in markers:
            elem += character
        else:
            final_text.append(elem)
            elem = ""
    return final_text
