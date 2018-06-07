fruit = "banana"
print(fruit[0])
print(len(fruit))

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

count = 0
for c in fruit:
    print(c)


s = "Pirates of the Caribbean"
print(s[0:100])

word = "banana"
if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")


greeting = "Hello, world!"
greeting = "J" + greeting[1:]
print(greeting)


word = input("type something")
if "J" not in word:
    print('J in the house')
else:
    print("Nah Js dead")


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels

test(remove_vowels("compsci") == "cmpsc")
test(remove_vowels("aAbEefIijOopUus") == "bfjps")


def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

test(find("Compsci", "p") == 3)
test(find("Compsci", "C") == 0)
test(find("Compsci", "i") == 6)
test(find("Compsci", "x") == -1)

