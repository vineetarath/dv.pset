# m is the range within which the randominteger function is used to
#generate a random number a. An input is taken from user called guess
#and matched with a, until they get correct answer,
#c keeps count of number of tries
#match runs while loop until true

import random #import module
print ('''Let's play a guessing game!
Pick a top limit to guess within''') #initiate game
count = 1 #count of inputs
m = int(input("Top limit is:")) #input range
r = 0 #initial value of random number
match = True #condition to run while loop

def ri(r):
    r = (random.randint(1,m))#call function
    return r

for a in range (m):
    a = ri(r)

while match:
    guess = int(input("MY guess is:")) #get guess

    if guess == a: #check if correct
        print ("You've guessed it right in " + str(count) + " attempt/s") #answer
    elif guess > a:
        print ('Your attempt number ' + str(count) + ' is higher') #answer
    elif guess < a:
        print ('Your attempt number ' + str(count) + ' is lower') #answer
    count = count+1 #update count
