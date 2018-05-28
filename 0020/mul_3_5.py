n = 0 #set initial value
for i in range(1,1000): #define range
    if i%3 == 0 or i%5 == 0: #check divisibility
        n = n+i #update value
    print n #answer
