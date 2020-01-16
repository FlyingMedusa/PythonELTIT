import filehelpers
import stringhelpers
import re

fulltext = filehelpers.get_text('alice_text.txt',750)
cleantext = stringhelpers.clean_whitespaces(fulltext)

# get words in cleantext
words = cleantext.split()

pattern = "^(A|a)[a-z]{6,}"

# iterate over words
for word in words:
    match = re.search(pattern, word)

    if match:
        print(match.start())
        print(match.end())
        print(match.span())
        print(match.group())
        print(word)

# use regular expressions to match patterns passed to script