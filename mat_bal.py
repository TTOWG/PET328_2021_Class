#...TTOWG!

# input statements
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
nx = int(input('How many blocks there are in x-axis:'))
ny = int(input('How many blocks there are in y-axis:'))
pi = float(input("Enter the value of the inital reservoir pressure:"))
ce=float(input("Enter the value of the effective compressiblity factor:"))
co = float(input("Enter the value of oil compressiblity:"))
boi= float(input("Enter the value of the inital oil FVF:"))
bob= float(input("Enter the value of the oil FVF at bubblepoint condition:"))
pb = float(input("Enter the value bubble point pressure:"))
N = float(input("Enter the value of initial oil in place, STOIIP:"))

# discretizing the reservoir

delta_x = Lx/nx
delta_y = Ly/ny

# calculating the area per block
area = delta_x*delta_y

# initializing output variable

total_Np= 0

# the 'for' loop

for j in range(1,ny+1):
    for i in range(1,nx+1):
        block_n_order = (nx*(j-1))+i
        pnow = float(input('What is the current reservioir pressure of the reservoir for Block {0}?'.format(block_n_order)))
        block_bo = bob*(1-co*(pnow-pb))
        block_Np = (N*boi*ce*(pi-pnow))/block_bo
        total_Np = total_Np + block_Np
        print('The amount of oil in Block {0} is {1:.2f} STB'.format(block_n_order, block_Np))


    # continuing after the 'for' loop
# displaying the results.
print('The cummulative amount of oil in the entire reservoir is {0:.2f} STB'.format(total_Np))
