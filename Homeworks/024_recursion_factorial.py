def fac(x):
    operation_list.append(str(x))
    if x == 1:
        return 1
    else:
        return x * fac(x-1)


operation_list = []
nat = int(input("Please enter a natural number:\t"))
result = fac(nat)
whole_operation = " * ".join(operation_list)
print(str(nat) + "! =", whole_operation, "=", result)

