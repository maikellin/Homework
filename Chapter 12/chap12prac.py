import random
rng = random.Random()
drng = random.Random(123)

dice_throw = rng.randrange(2,102,2)
delay_in_seconds = rng.random() * 5.0
print(dice_throw)
print(delay_in_seconds)


cards = list(range(52))
rng.shuffle(cards)
print(cards)

import seqtools
s = "A string!"
s = seqtools.remove_at(4, s)
print(s)


import module1
import module2
print(module1.question)
print(module2.question)
print(module1.answer)
print(module2.answer)


def f():
    n = 7
    print("printing n inside of f:", n)
def g():
    n = 42
    print("printing n inside of g:", n)
n = 11
print("printing n before calling f:", n)
f()
print("printing n after calling f:", n)
g()
print("printing n after calling g:", n)