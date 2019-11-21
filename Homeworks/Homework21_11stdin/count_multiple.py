import sys

#define vowels
vowels = 'aeiou'

#get the words passed in command line
words = sys.argv[1:]

# iterate through each word
for word in words:
    #create two counters
    counter = 0
    vowelcount = 0
    
    #go through letter by letter
    while counter < len(word):
      #is current letter a vowel?
      if word[counter] in vowels:
        vowelcount += 1
      #keep track of total number of letters
      counter += 1
      #when counter is too big, do this:
    else:
      print('There are', vowelcount, 'vowels in', word)