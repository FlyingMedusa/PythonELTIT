from webhelpers import getlinks

url = input("Please paste the url\t")

a_list = getlinks(url)

for link in a_list:
    print(link.get('href'))