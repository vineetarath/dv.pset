A = [2,4,5,7,8,9]
found=0
x = int(input("Enter a single digit number to check if it is part of our set: "))
for j in range (0,len(A)):
    if x == A[j]:
        found=1
print (found)
