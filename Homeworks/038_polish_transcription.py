import re


def transcribe(word):
    transdict = str.maketrans('eńłoóśwyźż', 'ɛɲwɔuɕvɨʑʐ')
    output = word.translate(transdict)

    transdict = {'ch': 'x', 'cz': 'tʂ', 'rz': 'ʐ', 'sz': 'ʂ'}
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

    b4_bilab = {'ą': 'ɔm', 'ę': 'ɛm'}
    b4_alv = {'ą': 'ɔn', 'ę': 'ɛn'}
    b4_velar = {'ą': 'ɔŋ', 'ę': 'ɛŋ'}
    b4_alv_fric = {'ą': 'ɔw', 'ę': 'ɛw'}

    dicts = [b4_bilab, b4_alv, b4_velar, b4_alv_fric]
    cons = ['pb', 'td', 'kg', 'sz']

    for i in range(len(dicts)):
        output = extra_trans(dicts[i], cons[i], output)

    if output[-1] == 'ą':
        output = output.replace('ą', 'ɔw')
    elif output[-1] == 'ę':
        output = output.replace('ę', 'ɛ')

    return output


def extra_trans(transdict, cons, output):
    for key in transdict.keys():
        regex = '{}([{}])'.format(key, cons)
        output = re.sub(regex, '{}\\1'.format(transdict[key]), output)
    return output


def transwithdict(word, transdict):
    for char in transdict.keys():
        word = word.replace(char, transdict[char])
    return word


print(transcribe("kąt"))
print(transcribe("dąsać"))
print(transcribe("kęs"))
print(transcribe("męka"))
print(transcribe("gęba"))
print(transcribe("trę"))