#TTOWG

#Inputing parameters
Ca = float(input('Enter the weight fraction of acid:'))
va = float(input('Enter the stoichiometry number of acid:'))
vm = float(input('Enter the stoichiometry number of mineral:'))
MWm = float(input('Enter the molecular weight of mineral:'))
MWa = float(input('Enter the molecular weight of acid:'))
Cm = float(input('Enter the mineral content:'))
ϼa = float(input('Enter the density of acid:'))
ϼm = float(input('Enter the density of mineral:'))
rw = float(input('Enter the radius of wellbore:'))
ra = float(input('Enter the radius of acid treatment:'))
ø =  float(input('Enter the porosity:'))
k = float(input('Enter the permeability of undamaged formation:'))
h = float(input('Enter the thickness of pay zone to be treated:'))
Pbd = float(input('What is the given formation breakdown pressure:'))
P = float(input('Enter the reservoir pressure:'))
Psf = float(input('Enter the safety margin,200 to 500 psi:'))
µ = float(input('Enter the viscosity of the fluid:'))
re = float(input('Enter the drianage radius:'))
S = float(input('Enter the skin factor:'))
L = float(input('Enter the tubing length:'))
pi = float(input('Enter the formation gradient:'))
D = float(input('Enter the tubing diameter:'))
g = float(input('Enter the specific gravity given:'))


import math

# solving for dissolving power of acid and acid volume requirement

def graviβ(Ca):
    gravimetric=Ca*((vm*MWm)/(va*MWa))
    return gravimetric

ϼa_total= ϼa*62.4
X = graviβ(Ca)*(ϼa_total/ϼm)
Vm = math.pi*(ra**2-rw**2)*(1-ø)*(Cm)
Vp = math.pi*(ra**2-rw**2)*(ø)
Va =((Vm/X)+Vp+Vm)*(7.48)


print('The volumetric dissolving power of acid solution is {0:.3f}'\
      .format(X),'ft3/mineral ft3 solution')
print('The volume of minerals to be removed is {0:.2f}'.format(Vm),'ft3')
print('The initial pore volume is {0:.2f}'.format(Vp),'ft3')

# result for gravimetric dissolving power of acid solution

print('The gravimetric dissolving power of acid solution is {0:.2f}'\
      .format(graviβ(Ca)),'lbm mineral/lbm solution')

# result for the required minimum acid volume 

print('The required minimum acid volume is {0:.0f}'.format(Va),'gal')

# solving for injection rate

pbd = pi*L
print(pbd)

qi_max = (((4.917*10**-6)*k*h)*(pbd-P-Psf))\
         /((µ)*(math.log((0.472*re)/rw)+S))

# result for injection rate

print('The Acid Injection Rate is {0:.2f}'.format(qi_max),'bbl/min')

# solving for injection pressure

Pwf= (pi*L)-Psf
Ph = 0.433*g*L
Pf = ((518*(g**0.79)*(qi_max**1.79)*(µ**0.207))\
      /(1000*(D**4.79)))*L

Psi = Pwf-Ph+Pf

print('The frictional pressure drop is {0:.0f}'.format(Pf),'psi')
print('The hydrostatic pressure drop is {0:.0f}'.format(Ph),'psi')
print('The flowing bottom hole pressure is {0:.0f}'.format(Pwf),'psia')

# result for maximum expected surface injection pressuré

print('The maximum expected surface injection pressure is {0:.0f}'.format(Psi),'psia')


# closing remarks




