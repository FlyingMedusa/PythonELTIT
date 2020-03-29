"""
Program to translate English sentences to Pig Latin
"""


def eng_sent(input):
    """This function helps to deal with sentences"""
    sent_list = input.split()
    sent_pig_lat = []
    for word in sent_list:
        sent_pig_lat.append(word_polisher(word))
    output = ' '.join(sent_pig_lat)
    output = output.capitalize()
    return output


def eng_pig_lat(input):
    """This functions translates single English words to pig latin"""
    vowels = 'aeiouy'
    cons_clust = ''
    cons_count = 0
    if input[0] in vowels:
        output = input + 'way'
        return output
    else:
        for letter in input:
            if letter not in vowels:
                cons_clust += letter
                cons_count += 1
            else:
                break
        output = input[cons_count:] + cons_clust + 'ay'
        return output


def word_polisher(word):
    """This function 'polishes' the input
    - punctuation removal,
    - lowering"""
    word = word.lower()

    bef_punc = punct_removal(word)
    word = word.replace(bef_punc, '',1)
    aft_punc = ''.join(reversed(punct_removal(''.join(reversed(word)))))
    word = word.replace(aft_punc, '')
    word_pig_lat = eng_pig_lat(word)
    word_pig_lat = bef_punc + word_pig_lat + aft_punc
    return word_pig_lat


def punct_removal(word):
    punct = '.,?!()<>'
    punc_leftovers = ''
    for i in word:
        if i in punct:
            punc_leftovers += i
        else:
            break
    return punc_leftovers


print(__doc__)
print("Example: \nEven now, Mary likes (only her) cats...\n" + eng_sent("Even now, Mary likes (only her) cats..."))
users_word = input("\nPlease provide a word or a sentence (advised language: English)\n")
print(eng_sent(users_word))