#...TTOWG!

# input statements
Lx = float(input('What is the length of the reservoir in x-direction?:'))
Ly = float(input('What is the length of the reservoir in y-direction?:'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?:'))
ny = int(input('How many blocks there are in y-axis?:'))
pi = float(input("Enter the value of the inital reservoir pressure?:"))
ce=float(input("Enter the value of the effective compressiblity factor?:"))
co = float(input("Enter the value of oil compressiblity?:"))
boi= float(input("Enter the value of the inital oil FVF?:"))
bob= float(input("Enter the value of the oil FVF at bubblepoint condition?:"))
pb = float(input("Enter the bubble point pressure value?:"))           
# discretizing the reservoir

delta_x = Lx/nx
delta_y = Ly/ny

# calculating the area per block
area = delta_x*delta_y

# initializing output variable

tnp= 0
 
# the 'for' loop

for j in range(1,ny+1):
    for i in range(1,nx+1):
        block_position = (nx*(j-1))+i
        poro = float(input('What is the value of porosity for Block {0}?:'.format(block_position)))
        sw = float(input('What is the value of water saturation for Block {0}?:'.format(block_position)))
        pnow = float(input('What is the current reservioir pressure of the reservoir?:'))
        bo = float(input('What is the current value of the oil formation for Block {0}?:'.format(block_position)))
        block_stoiip = (7758*area*h*poro*(1-sw))/boi
        bo= bob*(1-co*(pnow-pb))
        np=((block_stoiip*boi*ce)*(pi-pnow))/bo
        tnp = tnp + np
        print('The amount of cummulative oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_position, np))
        print("The current value of the oil formation factor is", bo)

# continuing after the if block
# displaying the results.
print('The total cummulative oil produced from the reservoir is {0:.2f} STB'.format(tnp))                       
