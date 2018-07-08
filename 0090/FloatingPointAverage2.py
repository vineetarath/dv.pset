b = float(0)
a = float(input("Enter 10 floats separated by enter after each input:"))
for i in range (0,10):
    b = float(a)+float(b)
    print (b)
avg = b/10
print (avg)
