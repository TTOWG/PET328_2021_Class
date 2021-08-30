B_comp = float (input('What is the bit cost?'))
CR_comp = float (input('What is the rig cost per hour?'))
t_comp = float (input('What is the drilling time?'))
T_comp = float (input('What is the round trip time?'))
F_comp = float (input('What is the footage drill per bit?'))

# convert inputs to numerals


# the formula for drilling cost per foot

drilling_cost_per_foot =(B_comp + CR_comp * (t_comp + T_comp))/(F_comp)
print('The drilling cost per foot is {0:.2f} $' .format (drilling_cost_per_foot))
