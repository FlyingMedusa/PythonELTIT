import re

links1 = ["http://www.wp.pl", "https://google.com", "https://www.wa.amu.edu.pl",
          "www.wp.pl", "https://google.com.", "httpss://www.wa.amu.edu.pl"]
pattern = "http(s)?:\/\/\w+((\.\w+)?)+"

print("\nUsed expression:", pattern)
for link in links1:
    match = re.match(pattern, link)
    if match and match.group() == link:
        print("MATCHED\t", link)
    else:
        print("not matched\t", link)