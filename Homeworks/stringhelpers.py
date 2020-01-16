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
        else :
            cleaned_text += character
    return cleaned_text

def trim_sentences(sentences):
    trimmed_sentences = []
    for sent in sentences:
        trimmed = sent.strip()
        trimmed_new = ' '.join(trimmed.split())
        trimmed_sentences.append(trimmed_new)
    return trimmed_sentences
        
        
def get_word_count(sentences):
    count =1
    for character in sentences:
        if character == " ":
          count +=1
    return count
        