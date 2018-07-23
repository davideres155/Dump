import random
racun = random.randint(1,1000)
print("racun je:", racun)
while True:
    try:
        novac = int(input())
        break
    except ValueError:
        print("Press a valid key")
kusur = novac - racun
print("Kusur je", kusur)
n500 = kusur // 500
k500 = kusur % 500
n200 = k500 // 200
k200 = k500 % 200
n100 = k200 // 100
k100 = k200 % 100
n50 = k100 // 50
k50 = k100 % 50
n20 = k50 // 20
k20 = k50 % 20
n10 = k20 // 10
k10 = k20 % 10
n5 = k10 // 5
k5 = k10 % 5
n2 = k5 // 2
k2 = k5 % 2
n1 = k2
print(" 500x",n500, "\n" ,"200x", n200, "\n","100x",n100, "\n" ,"50x", n50, "\n","20x",n20, "\n" ,"10x", n10, "\n","5x",n5, "\n" ,"2x", n2, "\n", "1x", n1)

