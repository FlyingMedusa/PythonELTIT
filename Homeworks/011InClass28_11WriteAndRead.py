#Creating a new file and writing in it:

# file = open('testfile.txt', 'w')
# file.write('some text!\n')
# file.write('...and some more text\n')
# file.write('hello!')
#
# file.close()

file = open('test.txt', 'r')
data = file.read()
lines = data.split("\n")
for line in lines:
    print(line)
file.close()
