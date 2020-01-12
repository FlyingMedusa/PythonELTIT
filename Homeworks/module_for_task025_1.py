
def get_text(filename, offset=0):
    f = open(filename, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    text = text[offset:]
    return text
