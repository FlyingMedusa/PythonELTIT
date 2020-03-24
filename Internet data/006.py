"""
A student usually seeks class cancelations for the whole week
For BONUS task: best on 12.11.2019 (date present also as 12 November 2019)
from http://wa.amu.edu.pl/wa/Nieobecnosci_WA?page=8
"""


import urllib.request
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta, date
import re

print('Checking for potential class cancellations...')

url = 'http://wa.amu.edu.pl/wa/Nieobecnosci_WA?page=8'
response = urllib.request.urlopen(url)
data = response.read()

doc = BeautifulSoup(data, 'html.parser')
content = doc.find(id='tresc_wlasciwa')
links = content.find_all('a')

today = datetime.date.today()
today = date.strftime(today, "%Y-%m-%d")
# today_regex = today.strftime('%d.(%m|%B)')
print(today)

#--------------------------------------------------
"""
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2015, 12, 20)
end_dt = date(2016, 1, 11)
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d"))

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
"""
