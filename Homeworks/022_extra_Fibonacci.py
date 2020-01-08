def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


while True:
    n = int(input("Give me a number:\t"))
    if n >= 0:
        print(fib(n))
        break
    else:
        print("Remember to give a natural number! (Negative numbers aren't welcomed!)")