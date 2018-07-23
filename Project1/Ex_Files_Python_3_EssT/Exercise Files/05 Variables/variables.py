#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    num = round(42 / 9, 2)
    num2 = round(42 / 9, 4)
    print(type(num), num)
    print(type(num2), num2)
    s = "broj {} na 2 decimale".format(num)
    print(s)

if __name__ == "__main__": main()
