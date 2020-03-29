import re

"""
ą -> ɔn, ɔm, ɔw
ę -> ɛn, ɛm, ɛw, ɛ

kąt jako kont, zomb, jak na końcu to ą
ę na końcu to po prostu ę

EXTRA: 

"""


def transcribe(word):
    transdict = str.maketrans("eńłoóśwyźż", "ɛɲwɔuɕvɨʑʐ")
    output = word.translate(transdict)
    transdict = {'sz': 'ʂ', 'ch': 'x', 'cz': 'tʂ', 'rz': 'ʐ'}
    output = transwithdict(output, transdict)
    transdict = {'c': 'ts', 'ć': 'tɕ'}
    output = transwithdict(output, transdict)

    transdict = {'tsi': 'tɕ', 'ni': 'ɲ', 'si': 'ɕ', 'zi': 'ʑ'}
    vowels = 'aɛɔuiɨ'
    for key in transdict.keys():
        regex_with_vowel = '{}([{}])'.format(key, vowels)
        regex_without_vowel = '{}([^{}])'.format(key, vowels)
        output = re.sub(regex_with_vowel, '{}\\1'.format(transdict[key]), output)
        output = re.sub(regex_without_vowel, '{}i\\1'.format(transdict[key]), output)

    return output


def transwithdict(word, transdict):
    for char in transdict.keys():
        word = word.replace(char, transdict[char])
    return word



print(transcribe("zielony"))
print(transcribe("cisza"))
