import os
from QBit import QBit


class QuantumCommunicationWithSpyDetectionDemo:

    

    def __init__(self):
        qbits = self.MakeAndEncodeQBits(10)
        self.ReadQBits(qbits)
        self.DecodeQBits(qbits)

    def MakeAndEncodeQBits(self,length):
        qbits = []
        for _ in range(length):
            qbit = QBit(1)
            qbit.had()
            qbits.append(qbit)
        return qbits

    def ReadQBits(self, qbits):
        for qbit in qbits:
            qbit.read()

    def DecodeQBits(self, qbitsIN):
        qbitsOUT = []
        for qbit in qbitsIN:
            qbit.had()
            qbitsOUT.append(str(qbit.read()))
        return ''.join(qbitsOUT)

    def DoDemo(self):
        demo = 'Initializing and encoding list of 10 qbits, all with initial value 1'
        demo += os.linesep
        qbits = self.MakeAndEncodeQBits(10)
        demo += 'A spy is reading the qbits'
        demo += os.linesep
        self.ReadQBits(qbits)
        demo += 'Decoding the qbits'
        demo += os.linesep
        decoded =  self.DecodeQBits(qbits)
        demo += decoded
        demo += os.linesep
        if ('0' in decoded):
            demo += 'Decoded qbits contain 1 or more zeros, so spy is detected'
        else:
            demo += 'Decoded qbits contain only ones so spy is NOT detected'        
        return demo    


    
            

