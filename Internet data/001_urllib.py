import urllib.request

url = 'http://wa.amu.edu.pl/wa/'

file = urllib.request.urlopen(url)

content = file.read()

print(content.decode('UTF-8'))