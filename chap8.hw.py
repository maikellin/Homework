#name="maikel"
#newname=name.capitalize()
#print(newname)


#"Python"[1]
#"Strings are sequences of characters."[5]
#len("wonderful")
#"Mystery"[:4]
#"p" in "Pineapple"
#"apple" in "Pineapple"
#"pear" not in "Pineapple"
#"apple" > "pineapple"
#"pineapple" < "Peach"
#nothing happens when i run it


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter =="O" or letter == "Q":
        print(letter +"u" + suffix)
    else:
        print (letter + suffix)
#for letter in prefixes:
    #while letter == prefixes [5] or letter == prefixes[7]:
        #print(letter + "u" + suffix)
