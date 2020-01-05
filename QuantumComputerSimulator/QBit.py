from random import seed
from random import randint

class QBit:
    _zeroprobability= 50
    _oneprobability = 50
    
    def __init__(self, initvalue):
        if (initvalue == 0):
            self._zeroprobability = 100
            self._oneprobability = 0
        elif (initvalue == 1):
            self._zeroprobability = 0
            self._oneprobability = 100

    def read(self):
       if (self._zeroprobability == 100):
            return 0
       elif(self._oneprobability == 100):
            return 1
       else:
            seed()
            random = randint(0, 1)
            if (random == 0):
                self._zeroprobability = 100
                self._oneprobability = 0
            elif (random == 1):
                self._zeroprobability = 0
                self._oneprobability = 100

    def had(self):
        self._zeroprobability = 50
        self._oneprobability = 50