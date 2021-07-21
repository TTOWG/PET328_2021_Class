#LAMIIACE!

#input statement
Lx=float(input('What is the length of the reservoir in x-direction?'))
Ly=float(input('What is the length of the reservoir in y-direction?'))
h=float(input('What is the thickness of the reservoir?'))
nx=int(input('How many blocks there are in x-axis?'))
ny=int(input('How many blocks there are in y-axis?'))
boi = float(input('What is the value of inital oil formation volume factor?'))
ce = float(input('What is the value of effective compressibility?'))
co = float(input('What is the value of initial compressibility factor?'))
bob= float(input('What is the value of bubble-point oil FVF?'))
pi = float(input('What is the value of inital reservoir pressure?'))
pb = float(input('What is the value of bubble-point pressure?'))

#discretizing the reservoir

delta_x = Lx/nx
delta_y = Ly/ny

#calculating the area per block
area=delta_x*delta_y

#initializing the area per block 

tnp = 0

#the 'for' loop

for j in range(1, ny+1):
    for i in range(1,nx+1):
        block_position=(nx*(j-1))+i
        poro=float(input('What is the value of porosity for this Block{0}?:'.format(block_position)))
        sw=float(input('What is the value of water saturation for this Block{0}?:'.format(block_position)))
        pnow=float(input('What is the value of current reservoir pressure?:'))
        bo=float(input('What is the current value of the oil formation Block{0}?:'.format(block_position)))
        block_stoiip=(7758*area*h*poro*(1-sw))/boi
        bo = bob*(1-co*(pnow - pb))
        np =(block_stoiip*boi*ce*(pi-pnow))/bo
        tnp=tnp+np
        print('The amount of cumulative oil in Block {0:.0f} is {1:.2f} STB'.format(block_position, np))
        print("The current value of the oil formation factor is", bo)
        #continuing after the if block
        #displaying the results.
        print('The total cumulative oil produced from the reservoir is {0:.2f} STB'.format(tnp))

        
