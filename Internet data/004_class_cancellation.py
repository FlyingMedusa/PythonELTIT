"""
Aim of this program:
Get info about class cancellations for the current day [best on 10.03.2020]
from http://wa.amu.edu.pl/wa/Nieobecnosci_WA
"""

import urllib.request
from bs4 import BeautifulSoup
import datetime
import re

print('Checking for potential class cancellations...')

url = 'http://wa.amu.edu.pl/wa/Nieobecnosci_WA'
response = urllib.request.urlopen(url)
data = response.read()

doc = BeautifulSoup(data, 'html.parser')
content = doc.find(id='tresc_wlasciwa')
links = content.find_all('a')

today = datetime.date.today()
today_regex = today.strftime('%d.%m')

records = []
for link in links:
    text = link.get_text()
    if re.search(today_regex, text):
        records.append(text)

if len(records) > 0:
    print('Records found:')
    print('\n'.join(records))
else:
    print('No records found. Sorry!')
