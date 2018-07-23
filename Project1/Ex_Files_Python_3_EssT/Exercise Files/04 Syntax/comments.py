#!/usr/bin/python3
# comments.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for n in primes(): #generate a list of prime numbers
        if n > 100: break #nadji primes do 100
        print(n, end= " ") #stampa listu, end=" " ne stampa novi red nakon svakog broja

def isprime(n): #proverava da li je n prime
    if n == 1: #1 nije prime po definiciji
        return False
    for x in range(2, n): #proverava brojeve od 2 do n
        if n % x == 0: # ako je n deljiv sa nekim brojem od 2 do n
            return False # vraca False
    else: # ako nije deljiv ni sa jednim osim 1 i n
        return True # vraca True

def primes(n = 1): # postavlja n kao 1 i krece da vrti loop
   while(True):
       if isprime(n): yield n # ako je n prime stampa ga
       n += 1 #ako nije prime doaje +1 na n

if __name__ == "__main__": main()
