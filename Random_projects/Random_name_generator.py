import random, string

while True:
    try:
        lenght = int(input("What random name lenght do you want? "))
        quantity = int(input("How many random names do you want? "))
        break
    except ValueError:
        print("Enter a number")
def Generator():
    name = ''
    for i in range(lenght):
        letter = random.choice(string.ascii_lowercase)
        name = name + letter
    print(name.capitalize())
    return name
for i in range(int(quantity)):
    Generator()
