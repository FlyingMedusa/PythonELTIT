import urllib.request
from bs4 import BeautifulSoup
# https://flyingmedusa.github.io/simple_page/index.html


def extract_ol(url):
    page = urllib.request.urlopen(url)
    html = BeautifulSoup(page.read(), 'html.parser')
    ol_nodes = html.find_all('ol')
    children = []
    for ol in ol_nodes:
        children.append(ol.findChildren())
    return children


def main():
    url = input("Please paste the url\t")

    ols_children = extract_ol(url)

    for li_list in ols_children:
        print()
        for nr, li in enumerate(li_list, 1):
            print(f"{nr}. {li.text}")


if __name__ == "__main__":
    main()
