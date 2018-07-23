def main():
    a = range(0, 26)
    count = 0
    for x1 in a:
        for x2 in a:
            for x3 in a:
                for x4 in a:
                    for x5 in a:
                        if x1+x2+x3+x4+x5 == 25:
                            count+=1
                            print(x1, x2, x3, x4, x5)
    print(count)
if __name__ == '__main__':
    main()