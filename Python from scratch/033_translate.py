
table = str.maketrans("aeiouy", "AEIOUY")

s1 = "This is my sample string"

print(s1)
print(s1.translate(table))