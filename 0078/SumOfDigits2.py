#n = str(input('Enter any number between 0001 and 9999 to find the sum of its digits: '))
#v = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])
#print (n[0]+ " + " + n[1]+ " + "+ n[2]+ " + "+ n[3] + " = " + str(v))

number = 0
n = str(input('Enter any number to find the sum of its digits: '))
l = len(n)
print (l)
i = 0

def findSumOfDigits(x):
    for i in range (len(n)):
        number += int(n[i])
o = addIndexValFn()
print (number)

#i = 0
#for l in range (0,l):
#    i = int(n[l])+int (n[l+1])
#v = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])
#print (i)
