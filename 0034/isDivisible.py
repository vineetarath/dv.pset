count = 0 #count of integers divisible by 7
n = int(input("Input:")) #get input
for i in range(1,n): #define range
    if i%7 == 0: #check divisibility by 7
        count = count+1 #update count
print ('Output:' + str(count)) #answer
