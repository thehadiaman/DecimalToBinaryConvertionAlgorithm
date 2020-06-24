def toBinary(num):
    binaryNumber = []
    b = 0
    while num != 0:
        a = num % 2
        num = int(num/2)
        binaryNumber.insert(b, a)
        b += 1
    binaryNumber.reverse()
    
    binaryNum: str = ''
    for a in binaryNumber:
        a = str(a)
        binaryNum += a
    return binaryNum


decimal = int(input('Enter Number: '))
binary = toBinary(decimal)
print(binary)
