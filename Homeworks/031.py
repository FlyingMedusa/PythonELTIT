import re

s1 = "This iS a rather long string"

pattern = "(\w)s( )"

# replace with 'WOW'
s2 = re.sub(pattern, r"\1z\1\2\1", s1, flags=re.IGNORECASE, count=1)

print(s1, "\n", s2)
