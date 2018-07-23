#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # David Eres
    # Kusur
    # V.0.0.1.
#----------------------------------------------------------------------------------------

import random

class kusur():

    def __init__(self):

        #----------------------------------------------------------------------------------------
        # Comment 1
        #----------------------------------------------------------------------------------------
        self.done = False
        self.novcanice = [1000, 500, 200, 100, 50, 20, 10,  5,  2,  1]
        # self.kolicina = [2,   3,   1,   3,  4,  5, 10, 10, 20, 20]
        self.racun = random.randint(1, 5000)
        self.a = range(0, 10)

        self.calc()
    
    #----------------------------------------------------------------------------------------
    # Comment 2
    #----------------------------------------------------------------------------------------
    def calc(self):

        while self.done == False:
            kes = int(input("Racun je: " + str(self.racun) + " "))
            kusur = kes - self.racun

            if kusur < 0:
                print ("Nedovoljno para, plati ponovo")

            elif kusur > 0:
                print("Kusur je:", kusur)
                for i in self.a:
                    n = kusur // self.novcanice.__getitem__(i)
                    kusur = kusur - n*self.novcanice.__getitem__(i)
                    if n != 0:
                        print (self.novcanice.__getitem__(i), n)
                        # aktiviraj motor i puta n ?
                    else:
                        pass
                    #print(self.novcanice.__getitem__(i), n)
                    self.done == True
                break
    
            else:
                print ("Tacan iznos")
                self.done == True
                break

if __name__ == '__main__':
    try:
        kusur()
    except  ValueError:
        print("Press a valid key")
        pass
        
