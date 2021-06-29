#...TTOWG!

# function definition
def stoiip_calc(area, thickness, poro, sw, boi):
    STOIIP = (7758*area*thickness*poro*(1-sw))/boi
    return STOIIP

# function call for Reservoir TTOWG_1 (re-use)
oil_inplace_TTOWG_1 = stoiip_calc(40, 15, 0.3, 0.28, 1.2)
print('The amount of oil in place in Reservoir TTOWG_1 is', oil_inplace_TTOWG_1, 'STB')


# function call for Reservoir TTOWG_2 (re-use)
oil_inplace_TTOWG_2 = stoiip_calc(80, 10, 0.23, 0.35, 1.1)
print('The amount of oil in place in Reservoir TTOWG_2 is {0:.2f} STB'.format(oil_inplace_TTOWG_2))
