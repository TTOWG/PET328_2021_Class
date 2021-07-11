#...TTOWG!

# input statements
pi = float(input("Enter the value of the inital reservoir pressure?:"))
ce=float(input("Enter the value of the effective compressiblity factor?:"))
co = float(input("Enter the value of co?:"))
boi= float(input("Enter the value of the inital oil formation volume factor?:"))
np = float(input("Enter the value of the cummulative oil produced from the given block?:"))
bob= float(input("Enter the value of the oil formation volume factor at bubblepoint condition?:"))
pb = float(input("Enter the bubble point pressure value?:"))
n= float(input("Enter the value of the initial oil in place(N)?:"))
n_1 = int(input('How many blocks are there?:'))


           
# initializing output variable

tnp=0


for i in range(1,n_1+1):
    pnow = float(input('What is the current reservoir pressure of the reservoir?:'))
    bo = float(input('What is the current value of the oil formation for this block?:'))
    np=((n*boi*ce)*(pi-pnow))/bo
    block_position = (i)
    bo= bob*(1-co*(pnow-pb))
    tnp = tnp + np
    print('The amount of cumulative oil produced in Block {0:.0f} is {1:.2f} STB'.format(block_position, np))
    print("The current value of the oil formation factor is", bo)

# continuing after the if block
# displaying the results.
print('The total cumulative oil produced from the reservoir is {0:.2f} STB'.format(tnp))                       
