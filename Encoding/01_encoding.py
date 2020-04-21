f = open('r1251.txt', 'rb')
r = f.read()
r = r.decode('1251') # windows-1251 encoding
f.close()
print('Some Russian: ', r)

f = open('cb5.txt', 'rb')
c = f.read()
c = c.decode('big5')
f.close()
print('Some Chinese: ', c)
