print (('''Select number for operation:
1: To add\n 2: To subtract\n 3: To multiply\n 4: To divide'''))

def add(x,y):
    '''
    Returns the sum of x and y
    '''
    return x+y

def subtract(x,y):
    '''
    Returns the x difference y
    '''
    return x-y

def multiply(x,y):
    '''
    Returns the product of x and y
    '''
    return x*y

def divide(x,y):
    '''
    Returns the value of x divided by y
    '''
    return x/y

o = input("Enter operation:")
x = int(input("Enter x value:"))
y = int(input("Enter y value:"))

if o == 1:
    print ('Answer is '+ str(add(x,y)))
elif o == 2:
    print ('Answer is '+ str(subtract(x,y)))
elif o == 3:
    print ('Answer is '+ str(multiply(x,y)))
elif o == 4:
    print ('Answer is '+ str(divide(x,y)))
