p = int(input('''Lets check if our monkey can climb
a pillar of the height you specify if
it slips 1ft each time it climbs 3ft!
What is the height of pillar you want?'''))
if p ==1 or p ==2: #since minimum step is 3
    print('NO!')
elif p%3 == 2: #effective height after slipping 1ft after climbing 3xft
#i.e. 3x-1, so remainder should be 3-1 = 2
    print ('YES!')
else:
    print('NO!') # any other number
