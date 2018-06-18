#Let the number of natural numbers be n = 100,
#Find squares of each number and sum results to get: 1^2+2^2+...+100^2= say x
#Find sum of each number and square the results to get: 1+2+...+100^2= say y
#Find the difference between the sum of the squares x and the square of the sum y = x-y
a = 0 #sum of squares
p = 0 #square of natural number i
i = 0 #natural number i
q = 0 #sum of all natural numbers in range

#for a in range(1,11):
for i in range (1,101):
    p = i**2
    #print (p)   #return p
    a = a+p
print(a)

for i in range (1,101):
    q = i+q
    #print (q)
print(q**2)

difference = ((q**2)-a)
print(difference)
