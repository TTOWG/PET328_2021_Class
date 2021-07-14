# input statements
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
boi = float(input('What is the value of initial oil FVF?'))
bob = float(input('What is the bubble point oil formation volume factor?'))
pi = float(input('What is the initial reservoir pressure?'))
ce = float(input('What is the effective compressibility?'))
pb = float(input('What is the bubble point pressure?'))
co = float(input('What is the initial compressiblity?'))

# discretizing the reservoir

delta_x = Lx/nx
delta_y = Ly/ny

# calculating the area per block
area = delta_x*delta_y

# initializing output variable

total_np = 0

# the 'for' loop

for j in range(1,ny+1):
    for i in range(1,nx+1):
        block_n_order = (nx*(j-1))+i
        poro = float(input('What is the value of porosity for Block {0}?'.format(block_n_order)))
        sw = float(input('What is the value of water saturation for Block {0}?'.format(block_n_order)))
        pnow = float(input('What is the the value of the current reservoir pressure?'))
        block_bo = float(input('What is the oil formation volume factor?'))
        block_stoiip = (7758*area*h*poro*(1-sw))/boi
        block_np = (block_stoiip*boi*ce*(pi-pnow))/block_bo
        total_block_np = total_np + block_np
        print('The amount of oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_n_order, block_stoiip))
        print('The amount of oil formation volume {0:.0f} is {0:.2f} STB'.format(block_n_order, block_bo))
        print('The cumulative oil  produced in block {0:.0f} is {0:.2f} STB'.format(block_n_order, block_np))
        print('The cumulative oil produced in the entire reservoir  is {0:.2f} STB'.format(total_np))
                    
                    
