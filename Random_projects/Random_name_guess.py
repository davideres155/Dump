import random, string, time
t = time.time()
Name = input("Enter your name ").capitalize()
def Generator():
    name = ''
    for i in range(len(Name)):
        letter = random.choice(string.ascii_lowercase)
        name = name + letter
    return name.capitalize()
Generator()
counter = 0
while Name != Generator():
    counter += 1
    Generator()
    # print(Generator())
    # print(counter) #hash this to stop printng all the numbers
print(counter+1)
print(Name)
print(time.time() - t)