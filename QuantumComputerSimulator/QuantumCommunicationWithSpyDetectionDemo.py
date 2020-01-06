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
        qbits = self.MakeAndEncodeQBits(10)
        self.ReadQBits(qbits)
        return self.DecodeQBits(qbits)    


    
            

