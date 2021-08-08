#...TRIUMPHANT

# input statements
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
boi = float(input('What is the value of initial oil formation volume factor'))
ce = float(input('What is the value of effective compressibility'))
p1 = float(input('What is the value of initial reservoir pressure'))
bob = float(input('What is the value of bubble oil formation factor'))
co = float(input('What is the value of initial compressibility'))
pb = float(input('What is the value of bubble point pressure'))
stoiip = float(input('What is the value of stock tank oil intially in place'))
           
# discretizing the reservoir




# calculating the area per block


# initializing output variable
tnp = 0


 # the 'for' loop

for j in range(1,ny+1):
    for i in range(1,nx+1):
        pnow = float(input('What is the value of current reservoir pressure for the reservoir?'))
        block_bo = bob*(1-co*(pnow-pb))
        np = (stoiip*boi*ce*(p1-pnow))/block_bo 
        block_n_order = (nx*(j-1))+i
        print('The current value of the oil formation factor is' ,block_bo)
        tnp = tnp + np
        print('The amount of culmmulative oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_n_order, np))
        
        
        
        

# continuing after the if block
# displaying the results.
print('The total cumulative oil produced is {0:.2f} STB'.format(tnp))                       
