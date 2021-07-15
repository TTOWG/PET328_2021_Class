#...TTOWG!

# input statements
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
boi = float(input('What is the value of initial oil FVF?'))
ce = float(input('What is the value of effective compressibility'))
p1 = float(input('What is the value of initial reservoir pressure'))
bob = float(input('What is the value of bubble point oil formation factor'))
co = float(input('What is the value of initial compressibility'))
pb = float(input('What is the value of bubble point pressure'))
           
# discretizing the reservoir

delta_x = Lx/nx
delta_y = Ly/ny

# calculating the area per block
area = delta_x*delta_y

# initializing output variable
tnp = 0


 # the 'for' loop

for j in range(1,ny+1):
    for i in range(1,nx+1):
        poro = float(input('What is the value of porosity for this block?'))
        sw = float(input('What is the value of water saturation for this block?'))
        pnow = float(input('What is the value of current reservoir pressure for the reservoir?'))
        block_bo = float(input('What is the value of oil formation for this block?'))
        block_stoiip = (7758*area*h*poro*(1-sw))/boi
        np = (block_stoiip*boi*ce*(p1-pnow))/block_bo 
        block_n_order = (nx*(j-1))+i
        bo = bob*(1-co*(pnow-pb))
        tnp = tnp + np
        print('The amount of culmulative oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_n_order, np))
        print('The current value of the oil formation factor is' ,bo)
        
        
    
# displaying the results
print('The total cumulative oil produced is {0:.2f} STB'.format(tnp))                       
