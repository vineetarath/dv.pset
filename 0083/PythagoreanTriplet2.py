lhs = 0
rhs = 0
a = int(input('''A Pythagorean triplet is a set of three natural numbers, a<b<c,
for which,a^2+b^2=c^2. For example, 3^2+4^2 = 5^2
To find out if your set is a Pythagoream Triplet, enter a: '''))
b = int(input('Enter b (ensure that a<b<c): '))
c = int(input('Enter c: '))
def a2b2fn():
    lhs=(a**2)+(b**2)
    return lhs
def c2fn():
    rhs=(c**2)
    return rhs
lhs = a2b2fn()
rhs = c2fn()

if lhs == rhs:
    print ('True')
else:
    print ('Your chosen set is not a Pythagoran Triplet, try again!')
