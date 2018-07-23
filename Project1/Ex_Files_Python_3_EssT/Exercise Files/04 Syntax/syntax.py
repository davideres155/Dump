#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    function(1)
    function()
    function(5)
    fried = Egg()
    scrambled = Egg("scrambled")
    print(scrambled.whatKind())

def function(a=7):
    for i in range(a, 10):
        print(i, end= " ")
    print()

if __name__ == "__main__": main()
