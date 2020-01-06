from random import seed
from random import randint

class QBit:
    _zeroprobability= 50
    _oneprobability = 50
    _phasesequal = True
    
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
                return 0
            elif (random == 1):
                self._zeroprobability = 0
                self._oneprobability = 100
                return 1

    def had(self):
        if (self._zeroprobability == 100) and (self._oneprobability == 0):
            self._zeroprobability = 50
            self._oneprobability = 50
            self._phasesequal = True
        elif (self._zeroprobability == 0) and (self._oneprobability == 100):
             self._zeroprobability = 50
             self._oneprobability = 50
             self._phasesequal = False
        elif (self._zeroprobability == 50) and (self._oneprobability == 50):
            if (self._phasesequal):
                self._zeroprobability = 100
                self._oneprobability = 0
                self._phasesequal = True
            elif not (self._phasesequal):
                self._zeroprobability = 0
                self._oneprobability = 100
                self._phasesequal = True

            
            