def is_prime(num):
    for i in range(3, num):
        if num % i == 0:
            return False
    return True


def main():
    primes = []

    for num in range(1, 101):
        if is_prime(num):
            primes.append(num)
    print(primes)


if __name__ == '__main__':
    main()
