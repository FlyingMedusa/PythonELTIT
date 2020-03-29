import filehelpers
import stringhelpers
import re


fulltext = filehelpers.get_text('alice.txt',750)
cleantext = stringhelpers.clean_whitespaces(fulltext)

# get words in cleantext
cleantext = cleantext.lower()
words = cleantext.split()

clusters = {}
regex = "^[^aeiou\d\W]{2,}"


for word in words:
  match = re.search(regex, word)
  if match:
    cluster = match.group()
    if cluster in clusters:
      clusters[cluster] += 1
    else:
      clusters[cluster] = 1

for key in clusters.keys():
  text = "Cluster {} appeared {} times."
  print(text.format(key, clusters[key]))