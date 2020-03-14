import urllib.request
from bs4 import BeautifulSoup


def getlinks(url):
    file = urllib.request.urlopen(url)
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    list_of_a = soup.find_all('a')
    return list_of_a
