#CODE MASTER

#input statement
Boi = float(input('Enter the value of initial oil formation volume factor?'))
Ce = float(input('Enter the value of effective compressiblity?'))
Pi = float(input('Enter the value of initial reservoir pressure?'))
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
Pb = float(input('Enter the bubble point pressure?'))
Co = float(input('Enter the initial compressibility?'))
Bob = float(input('Enter the bubble point oil FVF?'))

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
        poro = float(input('What is the value of porosity for this block?'))
        sw = float(input('What is the value of water saturation for this block?'))
        Pnow = float(input('What is the current reservoir pressure?'))
        block_stoiip = (7758*area*h*poro*(1-sw))/Boi
        block_Bo = Bob*(1-Co*(Pnow-Pb))
        block_np = (block_stoiip*Boi*Ce*(Pi-Pnow))/block_Bo
        block_n_order = (nx*(j-1))+i
        total_block_np = total_np + block_np
        print('The amount oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_n_order, block_stoiip))
        print('The amount of oil formation volume {0:.0f} is {1:.2f} STB'.format(block_n_order, block_Bo))
        print('The cumulative oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_n_order, block_np))

# continuing after the if block
# displaying the results
print('The cumulative oil produced in the entire reservoir is {0:.2f}STB'.format(total_np))
        
