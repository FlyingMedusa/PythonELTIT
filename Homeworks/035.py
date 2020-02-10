import re

s1 = "First sentence. Second sentence."

strings = re.split("e.", s1)

s2 = "".join(strings)
print(s2)