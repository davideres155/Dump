import random
novcanice = [1000, 500, 200, 100, 50, 20, 10,  5,  2,  1]
# kolicina = [2,   3,   1,   3,  4,  5, 10, 10, 20, 20]
racun = random.randint(1, 5000)
a = range(0, 10)
kes = int(input("Racun je: " + str(racun) + " "))
kusur = kes - racun
print("Kusur je:", kusur)
for i in a:
    n = kusur // novcanice.__getitem__(i)
    kusur = kusur - n*novcanice.__getitem__(i)
    print(novcanice.__getitem__(i), n)