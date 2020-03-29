def get_text(filename,offset=0):
    file = open(filename,'r' ,encoding ='utf8')
    text = file.read()
    file.close()
    return text[offset:]