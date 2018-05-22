C = int(input("Enter Celsius value:"))
F = int(input("Enter Fahrenheit value:"))

def f_to_c (Celsius):#a parameter - in this case Celsius, keeps the function
#independent of the 'C' outside
    F = (9/5)*Celsius+32
    return F

def c_to_f (Fahrenheit):#a parameter - in this case Celsius, keeps the function
    #independent of the 'F' outside
    C = (5*Fahrenheit/9 - 32)
    return F

x = f_to_c(C)
print ('Your Fahrenheit value is '+ str(x))
y = c_to_f(F)
print ('Your Celcius value is '+ str(y))
