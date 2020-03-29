import re

words = ["eloelo320", "blah@", "192.168.0.1", "asd.asd.20"]
pattern = "^\w+$"    # or (longer): "^([A-Z]|[a-z]|(\d))*$"
id_pattern = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

for word in words:
    match = re.search(pattern, word)
    if match:
        print("matched")
    else:
        print("not matched")

print("*"*80)

for word in words:
    match = re.search(id_pattern, word)
    if match:
        print("matched")
    else:
        print("not matched")
