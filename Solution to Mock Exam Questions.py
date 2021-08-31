# ... to the only wise God

##### Question 1:

# a.    GitHub Workflow: Fork the repository -------> Clone the forked repository. [2 marks]

# b.    If a user did not specify value for Argument pb, then pb remain defaulted to None.
#        Based on Line 39 - 40; If pb is None, the function call Function bubbpe_pressure which then return a value for pb.

# c.    The while loop
while p > pb:
    Bo = Bob*(math.exp(co*(Pb - P)
    print('The value of oil FVF at {0:.2f} psi is {1:.4f}').format(P, Bo)
    p = p - pressure_step

# d.

# i. If Line 8 is not included, then Function gas_density would have no return value specified, and therefore would return None

# ii. If a user specified a value for pb; then pb is no more defaulted to None. Since Line 40 is only executed if pb is None.
#     Since pb is no more None, then Line 40 would not be executed.

# iii. In Line 49, Module math, which contain Function exp, is imported. Without this, Function exp would not be available for call.

# iv. The bug is caused by the fact that pb - pressure is not enclosed in parenthesis. The parenthesis is neccessary to force the intended order
#       of operation which is pb - pressure before multipling with co. Presently, pb is wrongly get multiplied with co before pressure is subtracted.

# v. Sample call
my_data = {'area': 40, 'thickness': 10, 'poro': 0.19, 'swi': 0.3, 'boi': 1.12}
stoiip_2(my_data)


##### Question 2:

# a.    A line that assigns value to Variable current_pressure should have preceded the given code snippet; else, an error would occur.
current_pressure = 3500

# b.    Line 75 is written to create and initialize total_stoiip, which is to hold the sum of block_stoiip value that would be generated in the 'for' loop.
#       If Line 75 is not written to create stoiip_total, an error would be thrown at the first run of the loop; becuase, the total_stoiip at the LHS
#       would be non-existent.

# c.    Function archie_sw
def archie_sw(n, a, rw, poro, m, rt):
    sw = ((a*rw)/((poro**m)*rt))**(1/n)
    return round(sw, 4)

# d.    Function average_poro
def average_poro(pay_list, poro_list):
    numerator_sum = 0
    denominator_sum = 0
    for i in range(len(pay_list)):
        numerator = poro_list[i] * pay_list[i]
        numerator_sum = numerator_sum + numerator
        denominator = pay_list[i]
        denominator_sum = denominator_sum + denominator
    avg_poro = numerator_sum/denominator_sum
    return avg_poro


##### Question 3:

# a.    The natural orderings of gridblocks are of the type int. To concatenate an int value to a string, the int value must be converted to a string using function str
block_n_order = 1
'Block' + str(block_n_order)

# b.    The logical statement is thus:
counter <= num_of_blocks and block_status == 'active'

# c.

# i.  Importing only Functions sol_gor and bubble_pressure

from peteng import sol_gor, bubble_pressure

# ii.  Importing all functions; not needing prefixes afterwards

from peteng import *

# iii.  Importing all functions; needing prefixes afterwards

import peteng


#d.     The script:

# Making Function stoiip_discretized available
from peteng import stoiip_discretized

# Defining Function trimmed_sum
def trimmed_sum(inp_list, threshold_val):
    the_sum = 0
    for value in inp_list:
        if value > threshold_val:
            the_sum = the_sum + value
    return the_sum

# Calling Function stoiip_discretized
(stoiip_value, the_list) = stoiip_discretized(100, 100, 40, 2, 1, 1.12, [0.25, 0.31], [0.28, 0.30])

# Passing the stoiip_list component to trimmed_sum
trimmed_sum(the_list, the_threshold)


# Final Declaration
print('TTOWG!!!!!!!!!!!!!!!!!!')



        

        

          

                       
