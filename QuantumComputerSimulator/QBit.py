from random import seed
from random import randint

class QBit:
    zeroprobability= 50
    oneprobability = 50
    
#comment
    def __init__(self, initvalue):
        if (initvalue == 0):
            self.zeroprobability = 100
            self.oneprobability = 0
        elif (initvalue == 1):
            self.zeroprobability = 0
            self.oneprobability = 100

    def read(self):
       if (self.zeroprobability == 100):
            return 0
       elif(self.oneprobability == 100):
            return 1
       else:
            seed()
            random = randint(0, 1)
            if (random == 0):
                self.zeroprobability = 100
                self.oneprobability = 0
            elif (random == 1):
                self.zeroprobability = 0
                self.oneprobability = 100

    def had(self):
        self.zeroprobability = 50
        self.oneprobability = 50