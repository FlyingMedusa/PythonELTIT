#Write a program that prints the prime numbers from 1 to 100.
#A prime number is a number that is divisible only by 1 and itself.

not_prime = []
prime = []

for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            not_prime.append(i)
            break

for el in range(1,101):
    if el not in not_prime:
        prime.append(el)

print("\n\tPrime numbers from 1 to 100:")
print(*prime, sep = ", ")


