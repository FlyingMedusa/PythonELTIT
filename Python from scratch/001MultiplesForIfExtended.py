#program zawiera trochę ulepszeń ale [w zależności od podanych danych] można uzyskać ten sam wynik
# For multiples of three print “Boo” instead of the number and for the multiples of five print “Hoo”.
# For numbers which are multiples of both three and five print “BooHoo”.


def printing_range(r_from, r_to):
    print("Numbers included:", end = " ")
    for i in range(r_from, r_to + 1):
        print(i, end = " ")


def multiplying(r_from, r_to):
    for i in range(r_from, r_to + 1):
        if i % 3 == 0  and i % 5 == 0:
            print(i,"\t multiple of 3 and 5 - BooHoo!")
        elif i % 5 == 0:
            print(i,"\t multiple of 5 - Hoo!")
        elif i % 3 == 0:
            print(i,"\t multiple of 3 - Boo!")
        # else:
        #     print(i,"\t- ---")


def run_again():
    while True:
        ans = input('Do you want to run again? (y/n): ')
        if ans in ('y', 'n'):
            break
        print('Invalid input.')

    return ans


print("*" * 61)
print("You will be asked to give a range of numbers".center(61))
print("which will be later used to check multiplicity".center(61))
print("*" * 61)


while True:

    while True:
        try:
            range_from = int(input("\nPlease give FIRST integer number\n(the range will START at this point): \n\t"))
            break
        except ValueError as v:
            print("We need an integer!", v)

    while True:
        try:
            range_to = int(input("\nPlease give SECOND integer number\n(the range will END at this point): \n\t"))
            break
        except ValueError as v:
            print("We need an integer!", v)



    printing_range(range_from, range_to)
    print("\n", "*" * 25)
    multiplying(range_from, range_to)

    answer = run_again()
    if answer == 'y':
        continue
    else:
        print('Goodbye!')
        break

