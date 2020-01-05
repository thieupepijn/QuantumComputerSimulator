from QBit import QBit


bit = QBit(1)
bit.had()
for _ in range(25):
    print(bit.read())
