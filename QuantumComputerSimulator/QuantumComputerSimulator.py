from QBit import QBit


def MakeAndEncodeQBits(length):
    qbits = []
    for _ in range(length):
        qbit = QBit(1)
        qbit.had()
        qbits.append(qbit)
    return qbits


def ReadQBits(qbits):
    for qbit in qbits:
        qbit.read()

def DecodeAndShowQBits(qbits):
    for qbit in qbits:
        qbit.had()
        print(qbit.read(), end='')
    print('')

qbits= MakeAndEncodeQBits(10)
#ReadQBits(qbits)
DecodeAndShowQBits(qbits)







