import math
def main():
    count = 0
    for a in range(1, 14):
        for b in range(1, 14):
            for c in range(1, 14):
                for d in range(1, 14):
                    if ( a == b and c == d and a != d) or (a == c and b == d and a != d) or (a == d and b == c and a != b):
                        count += 1
    print(int(count*math.factorial(4)/2))
if __name__ == '__main__':
    main()

    # broj mogucih kombinacija 2 para karata