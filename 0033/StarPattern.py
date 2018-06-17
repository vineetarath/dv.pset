p = int(input('Enter number of rows of stars = number of stars in the longest line: '))
for i in range (p,0,-1):#(top value, last value, decrement)
   for q in range(i,0,-1):
       print('*', end=' ') #end with ' ' to print in same line
   print (' ')
