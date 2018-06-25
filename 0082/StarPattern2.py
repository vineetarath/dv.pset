t = int(input('Enter the number of stars you want in the longest row: '))
for i in range (t,0,-1):
    for j in range (i,t+1):
        print ('*', end=' ')
    print (' ')
for i in range (t,0,-1):
    for k in range (i,0,-1):
        print ('*', end=' ')
    print (' ')
