#...TTOWG!

# input statements
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
Boi = float(input('What is the value of initial oil FVF?'))
Ce = float(input("What is the effective compressibility"))
Pi = float(input("What is the Initial reservoir pressure"))
Pb = float(input("what is bubble point pressure"))
Co = float(input("what is the oil compressibility"))
Bob = float(input("what is the Bob?"))
h = float(input('what is the thickness of the reservoir'))
delta_x= Lx/nx
delta_y=Ly/ny

area = delta_x*delta_y



# initializing output variable

total_stoiip = 0
 
# the 'for' loop

for j in range(1,ny+1):
    for i in range(1,nx+1):
        block_n_order = (nx*(j-1))+i
        Pnow = float(input('What is the current reservoir pressure for Block {0}?'.format(block_n_order)))
        poro = float(input('What is the porosity for Block{0}'.format(block_n_order)))
        sw = float(input('what is the water saturation for Block{0}'.format(block_n_order)))
        Bo =  Bob*((1-Co)*(Pnow-Pb))
        block_stoiip = (7758*area*h*poro*(1-sw))/Boi
        Np = (block_stoiip*Boi*Ce*(Pi-Pnow))/Bo
        total_stoiip = total_stoiip + block_stoiip
        print('The amount of oil in Block {0} is {1:.2f} STB'.format(block_n_order, block_stoiip))
        print('The cumulative oil produced in Block {0} is {1:.2f} STB'.format(block_n_order, Np))

# continuing after the 'for' loop
# displaying the results.
print('The amount of oil in the entire reservoir is {0:.2f} STB'.format(total_stoiip))                       
