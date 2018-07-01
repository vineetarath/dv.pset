n1 = str(input('Enter any number 1 to find the sum of its digits: '))
n2 = str(input('Enter any number 2 to find the sum of its digits: '))
def findSumOfDigits(n1):
    number1 = 0
    for i in range (len(n1)):
        number1 += int(n1[i])
    return(number1)
print (findSumOfDigits(n1))

def findSumOfDigits1(n2):
    number2 = 0
    for i in range (len(n2)):
        number2 += int(n2[i])
    return(number2)
print (findSumOfDigits(n2))

def compareN():
    if findSumOfDigits(n1) == findSumOfDigits(n2):
        print(1)
    else:
        print (0)
compareN()
