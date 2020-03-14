import urllib.request
from bs4 import BeautifulSoup

url = 'http://wa.amu.edu.pl/wa/'

file = urllib.request.urlopen(url)

content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# print(soup.get_text())
# print(soup.prettify())

# go through all the hyperlinks and print them
for link in soup.find_all('a'):
    print(link.get('href'))