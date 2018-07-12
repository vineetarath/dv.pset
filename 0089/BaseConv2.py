remainderlist = [] #list of remainders whose reverse order will give the binary number
n = int(input("Input:")) #get denary number input
#while (remainder/2 != 0 or remainder/2 != 1):
q = 0
r = 0
for i in range (n):
        q = n//2
        r = n%2
        q = q//2
print (q,r)
remainderlist.append(r)
print (remainderlist)
#    for i in range(0,bten): #define range
#        for j in range (0,i):
#            quotient = bten//2
#            remainder = bten%2
#        print (remainder)
#print (remainderlist.append(rem))
#new = list.reverse(remainderlist)
#print ("binary is: "+ new)
