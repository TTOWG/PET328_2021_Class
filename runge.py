#TTOWG{}GROUP 3 

# function to be solved
def f(x,y):
    return (3*(x+1))-y
   

# Runge Kutta
def runge(x0,y0,xn,n):
    
  
    
    print('----------------------------------SOLUTION----------------------------------------------')
    print('---------------------------------------------------------------------------------------------')    
    print('x0\tk1\tk2\tk3\tk4\ty0')
    print('----------------------------------------------------------------------------------------------')
    for i in range(step):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t%.4f'% (x0,k1,k2,k3,k4,y0) )
        print('--------------------------------------------------------------------------------------------')
        y0 = yn
        x0 = x0+h
      
    
   
# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter end point of x : ')
xn = float(input('xn = '))
print('enter the range:')
h=float(input('h = '))

step = int(((xn-x0)/h)+1)

#runge - function  call
runge(x0,y0,xn,step)
