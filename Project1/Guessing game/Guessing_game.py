import random
import webbrowser
url = "https://www.youtube.com/watch?v=0tJGk4ofc18"
numbr = int(random.randint(1, 10))
print(numbr)
name = input("Hello, please enter your name: ")
tries = 1
print("Hello", name + "!", "\nDo you want to play a game? [Y/N]")
def game():
    global question
    tries = 1
    question = input().lower()
    if question == "n":
        webbrowser.open(url); return (0)
    if question == "y":
        print("Great!\nI'm thinking of a number from 1 to 10..\nTry to guess it")
        while True:
            try:
                broj = int(input())
                break
            except ValueError:
                print("Press a valid key")
        if broj > numbr:
            print("Guess lower")
        if broj < numbr:
            print("Guess higher")
        if broj == numbr:
            print("You've guessed correct the first time")
        while broj != numbr:
            tries += 1
            while True:
                try:
                    broj = int(input())
                    break
                except ValueError:
                    print("Press a valid key")
            if broj > numbr:
                print("Guess lower")
            if broj < numbr:
                print("Guess higher")
            if broj == numbr:
                print("You've guessed correct in", tries, "tries." )
    else:
        print("Please enter a valid key"); game()
game()



