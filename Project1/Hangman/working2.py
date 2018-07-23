import random
novci = [1000, 500, 200, 100, 50, 20, 10,  5,  2,  1]
kolicina = [2,   3,   1,   3,  4,  5, 10, 10, 20, 20]
racun = random.randint(1, 5000)
a = range(0, 10)
kes = int(input("Racun je " + str(racun)))
if kes < racun:
    while kes < racun:
        racun = racun - kes
        kes = int(input("Unesite jos"+ str(racun)))
elif kes == racun:
    print("kusur je 0")

# if kes < racun:
#     racun = racun - kes
#     print("unesite jos " + str(racun))
#     kes = int(input())
# elif kes == racun:
#     print("kusur je 0 dinara")
# kusur = kes - racun
# print(kusur)
