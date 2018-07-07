l = 0 #loop for entire word = number of rows
nl = 0 #for loop for additional new letter at each step, as per row it goes to
word = str(input("Input:"))
for l in range(0,len(word)):#runs for number of rows defined by length
    for nl in range(0,l+1):#why i+1?
        print(word[nl], end=" ")#print all data for this iteration in loop in same row
        nl = nl + 1 #new letter location to be included in subsequent row
    print(' ')
