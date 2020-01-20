import re

links1 = ["http://www.wp.pl", "https://google.com", "https://www.wa.amu.edu.pl",
          "www.wp.pl", "https://google.com.", "httpss://www.wa.amu.edu.pl"]
pattern = ["https{0,1}://\w+\.\w+((\.\w+)?)+", "https{0,1}://\w+\.\w+((\.\w+)?)+[a-z]$"]
comment = ["No '$' used but matches the 5th link", "Works well but I had to use '$'"]

i = 0
while i < len(pattern):
    print("\nUsed expression:", pattern[i])
    print("Comment:", comment[i])
    for link in links1:
        match = re.search(pattern[i], link)
        if match and match.group() == link:
            print("MATCHED\t", link)
        else:
            print("not matched\t", link)
    i += 1