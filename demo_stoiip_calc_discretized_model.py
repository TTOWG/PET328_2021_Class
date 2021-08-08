#...TTOWG!

# input statements
Lx = float(input('What is the length of the reservoir in x-direction?'))
Ly = float(input('What is the length of the reservoir in y-direction?'))
h = float(input('What is the thickness of the reservoir?'))
nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
boi = float(input('What is the value of initial oil FVF?'))
           
# discretizing the reservoir to get the reservoirs into blocks(having same properties)

delta_x = Lx/nx
delta_y = Ly/ny

# calculating the area per block
area = delta_x*delta_y

# initializing output variable

total_stoiip = 0 # 0 is used as a dummy value
 
# the 'for' loop note i is usued for clounm and j is for rows, also note the block is named colunm,row e.g 2 column,3row
# in a 3D way i,j,k, note k indicates layering (all b4 is known as engineering ordering)

for j in range(1,ny+1):  # jump from rows to rows (jumping loop occurs after looping has occur through all the colunms in a row) THIS IS THE OUTER LOOP
    for i in range(1,nx+1): # moves from columns to cloumns (moving loop) THIS IS THE INNER LOOP
        poro = float(input('What is the value of porosity for this block?'))
        sw = float(input('What is the value of water saturation for this block?'))
        block_stoiip = (7758*area*h*poro*(1-sw))/boi
        block_n_order = (nx*(j-1))+i
        total_stoiip = total_stoiip + block_stoiip
        print('The amount of oil in Block {0:.0f} is {1:.2f} STB'.format(block_n_order, block_stoiip))

# continuing after the if block
# displaying the results.
print('The amount of oil in the entire reservoir is {0:.2f} STB'.format(total_stoiip))                       
