
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


def trim_sentences(sentences):
    trimmed_sentences = []
    for sentence in sentences:
        new_sentence = sentence.strip()
        trimmed_sentences.append(new_sentence)
    return trimmed_sentences


def get_word_count(sentence):
    return len(sentence.split())
