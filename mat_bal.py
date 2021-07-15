# input statements

Lx = float(input('What is the length of the reservoir in x-direction?:'))
Ly = float(input('What is the length of the reservoir in y-direction?:'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
Boi = float(input('What is the inital volume factor?'))
bob= float(input('Enter the value of the oil formation volume factor at bubblepoint condition?:'))
Ce = float(input('What is the effective compressibility?'))
co = float(input('Enter the value of inital oil compressiblity?:'))
Pi = float(input('What is the initial reservoir pressure?'))
pb = float(input('Enter the bubble point pressure value?'))

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
        poro = float(input('What is the value of porosity for this block?'))
        sw = float(input('What is the value of water saturation for this block?'))
        Bo = float(input('What is the current value of the Oil formation volume factor'))
        Pnow = float(input('What is the current effective compressibility?'))
        block_stoiip =(7758*area*h*poro*(1-sw))/Boi
        np=((block_stoiip*Boi*Ce)*(Pi-Pnow))/Bo
        bo= bob*(1-co*(Pnow-pb))
        block_position =(nx*(j-1))+i
        tnp = tnp + np
        print('The amount of cumulative oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_position, np))
        print("The current value of the oil formation factor is", Bo)

       
# displaying the results.
print('The total cumulative oil produced from the reservoir is {0:.2f} STB'.format(tnp))                       

        
        
        
   
    
