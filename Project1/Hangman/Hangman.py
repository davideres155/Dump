# noinspection PyUnresolvedReferences
from randomnumber import number
list1 = range(1, 1000)
fh = open('words.txt', "r").read()
list1 = fh.split("\n")
word = (list1.__getitem__((number))).upper()
length = len(word)
def level():
    while True:
        try:
            lvl = int(input("Select dificulty level: \n1: Easy \n2: Medium \n3:Hard     "))
            break
        except ValueError:
            print("Press a valid key")
    if int(lvl) == 1:
        a = 15
        print("Sellected dificulty level is Easy")
        return a
    elif int(lvl) == 2:
        a = 12
        print("Sellected dificulty level is Medium")
        return a
    elif int(lvl) == 3:
        a = 9
        print("Sellected dificulty level is Hard")
        return a
    else:
        level()
a = level()
print(a)
print("Your word has", str(length), "letters")

# Get a word from the list and transform it into all caps
# list1 - list of words
# number - random number 0-999 given from randomnumber.py
# word - randomly selected word from list
#print(word)
dashes = ""
for i in word:
    dashes = dashes + "_ "
print(dashes)

def get_ulaz():
    ulaz = ""
    ulaz = input("Your guess: ").upper()
    return ulaz

def proveri_ulaz(dashes):
    if len(ulaz) > 1:
        if ulaz == word:
            print("Correct!")
            dashes = word
            #print(dashes)
        else:
            print("no")
        return dashes
    else:
        if ulaz in word:
            count = 0
            tempd = ""
            for i in word:
                if i == ulaz:
                    tempd = tempd + i + " "
                else:
                    tempd = tempd + dashes[count * 2] + " "
                count = count + 1
            return tempd
        else:
            print("Guess again")
            return dashes
tries = 0
while dashes != word:
    while tries != a:

        ulaz = get_ulaz()

        dashes = proveri_ulaz(dashes)

        print(dashes)

        tries = tries + 1

        print("Current number of tries:", tries)

        if not "_" in dashes:
            print("You've guessed the word in", tries, "guesses")
            exit(0)
    print("You lost")
    print(word)
    exit(0)