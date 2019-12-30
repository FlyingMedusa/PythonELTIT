def fac(x):
    if x == 1:
        return 1
    else:
        return x * fac(x-1)


nat = int(input("Please enter a natural number:\t"))
print(str(nat) + "! =", fac(nat))
