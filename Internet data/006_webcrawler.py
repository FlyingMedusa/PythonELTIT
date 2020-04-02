import urllib.request
from bs4 import BeautifulSoup
import urllib.parse


def main():
    print('Getting staff urls...')

    staff_url = 'http://wa.amu.edu.pl/wa/en/staff_list'
    staff_content = get_content(staff_url)

    links = staff_content.find_all('a')

    urls = []

    for link in links:
        if len(link.get_text()) > 1:
            base_url = 'http://wa.amu.edu.pl'
            url = urllib.parse.urljoin(base_url, link['href'])
            urls.append(url)

    print('Staff headers found:')
    for url in urls:
        print(get_details(url))

    print('Urls found:')
    print('\n'.join(urls))


def get_content(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    doc = BeautifulSoup(data, 'html.parser')
    return doc.find(id='tresc_wlasciwa')


def get_details(url):
    try:
        content = get_content(url)
    except:
        print('Error getting details from', url)
        return 'No content'
    header = content.find('h1')
    return header.get_text()


main()
