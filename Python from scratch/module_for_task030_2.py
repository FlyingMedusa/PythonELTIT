import re


def get_sentences(text):
    # characters to split on
    splitters = '.?!;:'
    # where we'll put the sentences
    sentences = []
    # reference to current sentence
    sent = ''
    # go character by character through text
    for character in text:
        # build the sentence
        sent += character
        if character in splitters:
            # append the sentence to list of sentences
            sentences.append(sent)
            # start a new sentence
            sent = ''
    return sentences


def clean_whitespaces(text):
    breaks = '\t\n'
    cleaned_text = ''
    for character in text:
        if character in breaks:
            cleaned_text += ' '
        else:
            cleaned_text += character
    return cleaned_text


def remove_punctuation(text):
    punc = '[\.\?\-!\*,\(\):;\[\]_/~"“”’‘]'
    newtext = ''
    for char in text:
        if re.search(punc, char):
            newtext += ''
        else:
            newtext += char
    return newtext


def remove_words(words):
    newwords = []
    pattern = '\d'
    for w in words:
        if re.search(pattern, w):
            continue
        else:
            newwords.append(w)
    return newwords


def trim_sentences(sentences):
    trimmed_sentences = []
    for sent in sentences:
        trimmed = sent.strip()
        trimmed_new = ' '.join(trimmed.split())
        trimmed_sentences.append(trimmed_new)
    return trimmed_sentences


def get_words_freq(words):
    wordlist = {}
    for w in words:
        if w in wordlist:
            wordlist[w] += 1
        else:
            wordlist[w] = 1
    return wordlist

"""
def get_clusters_freq(words):
    clusters = {}
    for w in words:
        m = re.search('^[^aeiouy]{2,}', w)
        if m:
            onset = w[0:m.end()]
            if onset in clusters:
                clusters[onset] += 1
            else:
                clusters[onset] = 1
    return clusters
"""


def get_clusters_freq(words):
    clusters = {}
    for w in words:
        m = re.search('[^aeiouy]{2,}$', w)
        if m:
            coda = w[m.start():]
            if coda in clusters:
                clusters[coda] += 1
            else:
                clusters[coda] = 1
    return clusters


def get_word_count(sentences):
    count = 1
    for character in sentences:
        if character == " ":
            count += 1
    return count
