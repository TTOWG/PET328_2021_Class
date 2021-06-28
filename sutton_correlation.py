co2_comp = input('What is the CO2 composition? ')
n2_comp = input('What is the n2 composition? ')
h2s_comp = input('What is the h2s composition? ')
h2o_comp = input('What is the h2o composition? ')
gas_gravity = input('What is the measured gas gravity? ')

co2_comp = float(co2_comp)
n2_comp = float(n2_comp)
h2s_comp =float(h2s_comp)
h2o_comp = float(h2o_comp)
gas_gravity = float(gas_gravity)

if co2_comp > 12 or n2_comp > 3 or h2s_comp > 0:
    gas_gravity = (gas_gravity - (1.1767 * h2s_comp) - \
                   (0.622 * h2o_comp)) / (1-h2s_comp -co2_comp - n2_comp - h2o_comp)
    print('The corrected gas gravity is', gas_gravity)


pseudo_critical_pressure = 756.8 - (131 * gas_gravity) - (3.6 * gas_gravity **2)
pseudo_critical_temperature = 169.2 + (349.5 * gas_gravity) - (74.0 * gas_gravity **2)
pseudo_pressure = (1 - h2s_comp - co2_comp - n2_comp - h2o_comp)*pseudo_critical_pressure + (1360*h2s_comp) + (1071*co2_comp) + (493.1*n2_comp) + (3200.1*h2o_comp)
pseudo_temperature = (1 - h2s_comp - co2_comp - n2_comp - h2o_comp)*pseudo_critical_temperature + (672.35 * h2s_comp) + (547.58*co2_comp) + (227.16 * n2_comp) + (1164.9 * h2o_comp)


print('The pseudo-critical pressure is {0:2f} psia'.format(pseudo_critical_pressure))
print('The pseudo-critical temperature is {0:.2f} deg Rankine'.format(pseudo_critical_temperature))
print('The pseudo pressure is {0:2f} psia'.format(pseudo_pressure))
print('The pseudo temperature is {0:2f} deg Rankine'.format(pseudo_temperature))
