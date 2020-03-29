
def receiver(first, second):
    return first * 3, second * 3, (first+second) *3

f = input("Give me 1st word")
s = input("Give me 2nd word")
w_1, w_2, w_3 = receiver(f, s)
print(w_1, w_2 , w_3)