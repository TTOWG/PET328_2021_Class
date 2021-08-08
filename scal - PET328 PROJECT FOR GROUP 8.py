#TTWOG
#PET328 PROJECT (GROUP 8- Bayode Favour Olayinka,Abasilim Chidimma,Elendu Samuel,Ogunfuwa Teniola,Aichinede Ose)
#Effective permeabilities of water and oil

#input statements
length= float(input("Enter the length(inches):"))
diameter= float(input("Enter the diameter:"))
voi= float(input("Enter the viscosity of oil:"))
vow= float(input("Enter the viscosity of water:"))
n= int(input("Enter the number of blocks:"))

# calculating the area per block
length=length/12
diameter=diameter/12
area=(3.1415926535*(diameter**2))/4

# initializing output variable
total_keo=0
total_kew=0

# the 'for' loop
for x in range(1,n+1):
    position= x
    press= float(input("Enter the pressure for block{0}:".format(position)))
    qo = float(input("Enter the flow-rate of oil for block{0}:".format(position)))
    qw = float(input("Enter the flow-rate of water for block{0}:".format(position)))
    keo = (qo*voi*length)/(area*press*0.001127)
    kew = (qw*vow*length)/(area*press*0.001127)
    print("The Effective Permeablity of oil for block{0}:".format(position),keo)
    print("The Effective Permeability of water block{0}:".format(position), kew)
    print("")
   
               

