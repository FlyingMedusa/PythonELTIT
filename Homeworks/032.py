import re

def substitute(source):

    f_pattern = "-\w+/(\w+)"
    masc = re.sub(f_pattern, r"a", source)
    fem = re.sub(f_pattern, r"ka", source)
    output = ("\nmasculine form: ", masc, "\nfeminine form: ", fem)
    return output


s1 = "fundamentalist-a/ka"
output = substitute(s1)
print(output)