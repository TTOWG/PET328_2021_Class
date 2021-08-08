#...TTOWG!

# input statements
gas_gravity = float(input('What is the value of gas gravity?'))
oil_gravity = float(input('What is the value of oil gravity?'))
tf = float(input('What is the value of reservoir temperature in Fahrenheit?'))
p = float(input('What is the value of current reservoir pressure?'))
rs = float(input('What is the value of solution gas-oil ratio at current reservoir pressure?'))
pb = float(input('What is the value of reservoir bubble point pressure?'))
co = float(input('What is the value of oil compressibility?'))

# importing needed library
import math

# calculating F parameter
F = (rs*((gas_gravity/oil_gravity)**0.5))+(1.25*tf)
 
# the if-then-else statement

if p > pb:
    bob = 0.9759+(0.00012*(F**1.2))
    bo = bob*(math.exp(co*(pb-p)))
else:
    bo = 0.9759+(0.00012*(F**1.2))

# continuing after the if block
# displaying the results.
print('The oil formation volume factor is {0:.2f} RB/STB'.format(bo))
 
