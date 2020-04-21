import urllib.parse

# %20 -> space
text = "Cześć, mam na imię Michał!"
encoded = urllib.parse.quote(text)
print(encoded)