#TTOWG
#GROUP 2 PROJECT WORK

#INPUTING THE MOLE FRACTION OF GASES IN THE RESERVOIR
yco2 = float(input('What is the value for the mole fraction of co2?'))
yn2 = float(input('What is the value for the mole fraction of n2?'))
yc1 = float(input('What is the value for the mole fraction of c1?'))
yc2 = float(input('What is the value for the mole fraction of c2?'))
yc3 = float(input('What is the value for the mole fraction of c3?'))
yc4 = float(input('What is the value for the mole fraction of c4?'))
ync4 = float(input('What is the value for the mole fraction of nc4?'))

#INPUTING PRESSURE AND TEMPERATURE
p = float(input('What is the value of the pressure of this reservoir?'))
t = float(input('What is the value of the temperature of this reservoir?'))


#THE MOLECULAR WEIGHT OF EACH 
mco2 = 44.01 
mn2 = 28.01
mc1 = 16.04
mc2 = 30.1
mc3 = 44.1
mc4 = 58.1
mnc4 = 58.1

#GAS CONSTANT
R = 10.73

#INPUTING VALUES FOR THE IMPURITIES IN THE RESERVOIR
iyh2s = float(input('What is the value of the mole fraction of h2s impurity?'))
iyco2 = float(input('What is the value of the mole fraction of co2 impurity?'))
iyn2 = float(input('What is the value of the mole fraction of n2 impurity?'))




#CALCULATING FOR APPARENT MOLECULAR WEIGHT AND FOR A and B
A = (iyco2 + iyh2s)
B = iyh2s
E = 120*(A**0.9 - A**1.6) + 15*(B**0.5 - B**4.0) 
apparent_molecular_weight = (yco2*mco2) + (yn2*mn2) + (yc1*mc1) + (yc2*mc2) +(yc3*mc3) + (yc4*mc4) + (ync4*mnc4)

print('The apparent molecualar weight is {0:.2f}'.format(apparent_molecular_weight))


#CALCULATING SPECIFIC GRAVITY 
apparent_molecular_weight_of_air = 28.98
specific_gravity = apparent_molecular_weight/apparent_molecular_weight_of_air
print('The specfic gravity is {0:.2f}'.format(specific_gravity))



#IF conditons
if specific_gravity < 0.75:
    print("Its a Natural Gas System")
    Tpc = 168 + 325*specific_gravity - 12.5*specific_gravity**2
    Ppc = 677 + 15.0*specific_gravity - 37.5*specific_gravity**2
else:
    print("Its a Gas-Condensate System")
    Tpc = 187 + 330*specific_gravity - 71.5*specific_gravity**2
    Ppc = 706 - 51.7*specific_gravity - 11.1*specific_gravity**2

#CONTINUING AFTER THE IF BLOCK
#DISPLAYING RESULTS
print('Psuedo-critical temperature = {0:.2f} deg Rakine '.format(Tpc))
print('Psuedo-critical pressure = {0:.2f} psia'.format(Ppc))


#USING CARR-KOBAYASHI-BURROWS CORRECTION METHOD TO CALCULATE FOR Tpc AND Ppc (NONHYDROCARBON ADJUSTMENNT METHOD)
Carr_T1pc = Tpc - 80*iyco2 + 130*iyh2s - 250*iyn2
Carr_P1pc = Ppc + 440*iyco2 + 600*iyh2s - 170*iyn2
print('Adjusted psuedo-critical temperature using carr-kobayashi-burrows method = {0:.2f} psia'.format(Carr_T1pc))
print('Adjusted psuedo-critical pressure using carr-kobayashi-burrows method  = {0:.2f} deg Rakine'.format(Carr_P1pc))


#CALCULATING FOR THE PSEUDO-REDUCED PROPERTIES
Carr_Ppr = p/Carr_P1pc
Carr_Tpr = t/Carr_T1pc
print('Pseudo-reduced pressure from carr-kobayashi-burrows method 1s {0:.2f} psia'.format(Carr_Ppr))
print('Pseudo-reduced temperature from carr-kobayashi-burrows method is {0:.2f} deg rakine'.format(Carr_Tpr))


#DETERMINING THE COMPRESIBILITY FACTOR {Z}
#IF conditions
if Carr_Ppr < 5 and Carr_Tpr < 2:
    z = 0.85
    print('Compressibility_factor = ',z)
else:
    z = 0.9
    print('Compressibility_factor = ',z)


#CALCULATING DENSITY OF GAS {Pg)
Density_Pg = p*apparent_molecular_weight/z*R*t
print('Density of gas = {0:.2f} pounds/cubic-feet'.format(Density_Pg))




#Determing Wichert-Aziz Corrected Pseudo- critical temperature and pressure
Wiz_T11pc = Tpc - E
Wiz_P11pc = (Ppc * Wiz_T11pc)/(Tpc + B*(1 - B)* E)
print('Corrected psuedo-critical temperature using wichert-aziz method = {0:.2f}'.format(Wiz_T11pc))
print('Corrected psuedo-critical pressure using wichert-aziz method = {0:.2f}'.format(Wiz_P11pc))

#CALCULATING FOR THE PSEUDO-REDUCED PROPERTIES using wichert-aziz method
Wiz_Ppr = p/Wiz_P11pc
Wiz_Tpr = t/Wiz_T11pc
print('Pseudo-reduced pressure using wichert-aziz method = {0:.2f} psia'.format(Wiz_Ppr))
print('Pseudo-reduced temperature using wichert-aziz method = {0:.2f} deg Rakine'.format(Wiz_Tpr))



#DETERMINING THE COMPRESIBILITY FACTOR {Z}
#IF conditions
if Wiz_Ppr > 5 and Wiz_Tpr < 2:
    z = 0.89
    print('Compressibility_factor = ',z)
else:
    z = 0.9
    print('Compressibility_factor = ',z)




#CALCULATING DENSITY OF GAS {Pg)
Density_Pg = p*apparent_molecular_weight/z*R*t
print('Density of gas = {0:.2f} pounds/cubic-feet'.format(Density_Pg))










    
